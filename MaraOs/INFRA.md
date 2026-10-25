# INFRA.md — Mapa de la infraestructura

> Documento vivo mantenido por **Orion**. Solo lectura de facto: no contiene secretos.
> Última actualización: 2026-10-25 (recon inicial, sin cambios en el sistema).

## Host — `homelab` (CHUWI HeroBox)
- **SO:** Ubuntu 26.04.1 LTS (Resolute Raccoon)
- **Kernel:** Linux 7.0.0-38
- **CPU:** Intel Celeron J4125 @2.0 GHz · 4 núcleos / 4 hilos
- **RAM:** 7.1 GiB (+4 GiB swap)
- **Disco:** 98 GB raíz ext4 (`/dev/mapper/ubuntu--vg-ubuntu--lv`), ~23% usado
- **Particiones:** `/boot` (sda2), `/boot/efi` (sda1, ESP)
- **Tailscale:** nodo `mara-core` · 100.121.31.69 · funnel `https://mara-core.bombay-pomano.ts.net`
- **SSH:** puerto 22

## Servicios AI (Docker)
| Servicio | Contenedor | Imagen | Puerto | Estado |
|---|---|---|---|---|
| Mara OS | `mara-os` | mara-os (custom) | `9001` | running |
| Hindsight | `mara-hindsight` | ghcr.io/vectorize-io/hindsight:latest | `8888`, `9999` | running |
| AgentDesk (app) | `agentdesk-app-1` | agentdesk:latest (Next.js) | `3000` | running (healthy) |
| AgentDesk (DB) | `agentdesk-db-1` | postgres:16-alpine | `5432` (interno) | running (healthy) |

Otros procesos:
- **Orion / Hermes gateway:** `127.0.0.1:37371`
- **systemd:** `docker.service`, `containerd.service`, `tailscaled.service` activos

## Estructura de directorios
- Base de trabajo: `~/mara/`
  - `mara-os/` — código fuente Mara OS (Node/TS)
  - `AgentDesk/` — app Next.js + Drizzle + MCP (repo git)
  - `hindsight/` — `compose.yml`
  - `backups/` — copias de seguridad
  - `obisidian-vault/` — bóveda Obsidian (daily, notas, IA, automatizaciones…)
- Orion: `~/.hermes/`

## Nodos Tailscale conocidos
- `mara-core` (este host, linux)
- `kikes-mac-mini` (macOS, activo)
- `pve` (linux — probable Proxmox)
- `enriques-macbook-air`, varios iPhone/iPad y equipos Windows (variado offline)

## Memoria: Hindsight + Obsidian (integración Orion)
- **Hindsight API:** `http://192.168.1.196:8888` · **Panel:** `http://192.168.1.196:9999`
- **Acceso de Orion:** vía **REST** (Hindsight no expone MCP; solo openapi/REST). Sin auth en LAN. Verificado.
- **Bancos:**
  - `obsidian` — segundo cerebro (653 hechos, 231 docs, ~233 notas). Fuente de conocimiento.
  - `mara-os` — memoria compartida con Mara OS (8 hechos). Evitar duplicados.
  - `mara-os-diagnostico` — diagnóstico (4 hechos).
- **Consulta:** `~/mara/scripts/hindsight_recall.sh "pregunta" [bank]` (solo lectura).
  - Endpoint: `POST /v1/default/banks/{bank}/memories/recall`
- **Obsidian vault:** dir `~/mara/obisidian-vault` (repo git, 233 `.md`). Bank Hindsight = `obsidian`.
- **sync_vault.sh:** `git pull` → importa chunks vault→banco `obsidian` (modo sin LLM, dentro de la imagen mara-os) → verifica. Automatización: **cron usuario, diario 03:00** (`0 3 * * *`), log en `~/mara/sync_vault.log`. Tiene lock (flock), `--dry-run/--force/--no-delete/--allow-mass-delete`. Estado en `mara-os/data/obsidian-import.json`.

## AgentDesk — centro de gestión de agentes (integración Orion)
- **URL:** http://192.168.1.196:3000 · MCP: `POST /api/mcp` (transport streamable-http, vía funnel `https://mara-core.bombay-pomano.ts.net/api/mcp`)
- **Conexión de Orion:** MCP en `~/.hermes/config.yaml` (`mcp_servers.agentdesk`), token de agente con scopes amplios. Identidad en AgentDesk = agente **Orion** (id `50e2f9b3…`), capacidades `homelab, cve, memoria`.
- **Scopes:** tasks r/w, delegations r/w, runs r/w, notes r/w, projects r/w, activity:read.
- **33 herramientas MCP** (solo lectura salvo marcado):
  - Identidad/estado: `whoami`, `get_queue`.
  - Tareas: `list_tasks`, `get_task`, `create_task`, `update_task`, `create_subtask`, `get_next_task`/`claim_task` (lease), `update_task_status`, `complete_task`, `fail_task`, `comment_task`/`add_comment`.
  - Notas (MD, [[wikilinks]]): `list_notes`, `get_note`, `get_note_by_title`, `create_note`, `update_note`, `append_note`, `upsert_note`, `delete_note`(destructivo).
  - Proyectos: `list_projects` (+ scope projects:write).
  - Delegaciones/aprobaciones: `list_delegations`, `update_delegation`, `propose_delegation`, `request_approval`.
  - Runs: `start_run`, `log_run`/`append_log`, `finish_run`, `add_artifact`/`attach_artifact`.
- **Modelo:** un agente no hace nada irreversible — delegaciones y acciones externas van a **Aprobaciones** hasta que el humano decide. Autonomía por tarea: `suggest_only` / `do_with_approval` / `autonomous_low_risk`.
- **API REST v1** (`/api/v1`, 15 endpoints, Bearer por agente) y OpenAPI en `GET /api/openapi.json`. Docs en `~/mara/AgentDesk/docs/`.
- Orion = coordinador: usa AgentDesk como inventario único de agentes/tareas; NO mantiene listados duplicados.

## Notas operativas
- Recursos ajustados: 7 GB RAM para 4 contenedores + PostgreSQL. Vigilar memoria.
- Secretos en `~/mara/**/.env` — tratar como sensibles, no exponer ni versionar.
- Todos los contenedores arrancan juntos (~mismo instante) → `docker compose up` único o arranque del equipo.

## Comandos útiles (solo lectura)
- Estado contenedores: `docker ps -a`
- Logs: `docker logs -f <container>`
- Recursos: `docker stats`
- Red: `ss -tulpn` · Tailscale: `tailscale status`
