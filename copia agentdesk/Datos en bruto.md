---
title: Datos en bruto de Agent Desk
tags:
  - agentdesk
  - copia-seguridad
  - backup
date_created: 2026-10-24
date_modified: 2026-10-27
---

# Datos en bruto de Agent Desk

Respuestas JSON tal cual devolvió Agent Desk el 27/10/2026 a las 09:12 (hora de Madrid), para no perder nada. Índice: [[Copia Agent Desk]].

## whoami

```json
{
  "agent": {
    "id": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
    "name": "Notis",
    "status": "active",
    "capabilities": [
      "proyectos",
      "notas",
      "utilidades"
    ]
  },
  "scopes": [
    "tasks:read",
    "tasks:write",
    "delegations:read",
    "delegations:write",
    "runs:read",
    "runs:write",
    "notes:read",
    "notes:write",
    "projects:read",
    "projects:write",
    "activity:read"
  ],
  "queue": {
    "delegations": 0,
    "tasks": 1
  },
  "serverTime": "2026-10-27T08:12:17.331Z"
}
```

## list_projects

```json
{
  "projects": [
    {
      "id": "b308d5fc-1ddd-45b5-bc05-c8feb20dadf3",
      "name": "MaraOs",
      "identifier": "MAOS",
      "status": "active",
      "taskTotal": 0,
      "taskDone": 0
    },
    {
      "id": "c7525703-c2c9-4681-bd02-1154b92f25ae",
      "name": "Biavent",
      "identifier": "BIA",
      "status": "active",
      "taskTotal": 5,
      "taskDone": 4
    },
    {
      "id": "70b16875-640f-49d6-88b9-467019761ae4",
      "name": "Tareas personales",
      "identifier": "TAP",
      "status": "active",
      "taskTotal": 0,
      "taskDone": 0
    }
  ]
}
```

## list_tasks (status=backlog,todo,in_progress,review,done,cancelled; limit=200)

```json
{
  "count": 5,
  "tasks": [
    {
      "id": "266cc328-4cf8-47f3-89ec-848614b15200",
      "title": "Mostrar en el panel del organizador el número de chats con conversación",
      "description": "Hay que arreglar que en el panel del organizador del evento se refleje el número de chats en los que se está hablando (chats con conversación activa).",
      "status": "done",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "0ad3aebc-bf64-44ad-96e0-244576f5511f",
      "title": "Poner en el panel de organizador los encuentros que se han hecho",
      "description": null,
      "status": "done",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "7fc9e10e-a2b3-48f9-bcfe-b61dc22dfec6",
      "title": "Poner Perfil como última opción del menú inferior",
      "description": "Mover la opción de Perfil para que aparezca en último lugar del menú de navegación de abajo.",
      "status": "done",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "b02f5889-c6f2-4d3e-854f-cd9fa19eb738",
      "title": "Revisar el tamaño del chat y por qué se cierra el teclado al enviar un mensaje",
      "description": "Revisar el tamaño de la ventana del chat y averiguar por qué el teclado se cierra al enviar un mensaje.",
      "status": "done",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "f818728e-4eaf-4c8d-accd-7deaa25ea043",
      "title": "Probar la app en un dispositivo sin instalarla (Android e iOS)",
      "description": "Conseguir probar la aplicación en un dispositivo real sin tener que instalarla, tanto en Android como en iOS.",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    }
  ]
}
```

## list_tasks (sin filtro; limit=200)

```json
{
  "count": 5,
  "tasks": [
    {
      "id": "266cc328-4cf8-47f3-89ec-848614b15200",
      "title": "Mostrar en el panel del organizador el número de chats con conversación",
      "description": "Hay que arreglar que en el panel del organizador del evento se refleje el número de chats en los que se está hablando (chats con conversación activa).",
      "status": "done",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "0ad3aebc-bf64-44ad-96e0-244576f5511f",
      "title": "Poner en el panel de organizador los encuentros que se han hecho",
      "description": null,
      "status": "done",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "7fc9e10e-a2b3-48f9-bcfe-b61dc22dfec6",
      "title": "Poner Perfil como última opción del menú inferior",
      "description": "Mover la opción de Perfil para que aparezca en último lugar del menú de navegación de abajo.",
      "status": "done",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "b02f5889-c6f2-4d3e-854f-cd9fa19eb738",
      "title": "Revisar el tamaño del chat y por qué se cierra el teclado al enviar un mensaje",
      "description": "Revisar el tamaño de la ventana del chat y averiguar por qué el teclado se cierra al enviar un mensaje.",
      "status": "done",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "f818728e-4eaf-4c8d-accd-7deaa25ea043",
      "title": "Probar la app en un dispositivo sin instalarla (Android e iOS)",
      "description": "Conseguir probar la aplicación en un dispositivo real sin tener que instalarla, tanto en Android como en iOS.",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    }
  ]
}
```

## list_notes (limit=100, offset=0)

```json
{
  "notes": [
    {
      "id": "07977151-7486-43d0-8809-c631141c35a4",
      "title": "INFRA.md — Mapa de la infraestructura",
      "excerpt": "Documento vivo mantenido por Orion. Solo lectura de facto: no contiene secretos. Última actualización: 2026-10-25 (recon inicial, sin cambio…",
      "authorType": "agent",
      "authorId": "50e2f9b3-b6a4-4fc3-8d76-6ef9a3459907",
      "authorName": "Orion",
      "projectId": null,
      "project": null,
      "updatedAt": "2026-10-25T10:27:27.372Z",
      "createdAt": "2026-10-25T10:27:27.372Z",
      "outgoingCount": 0,
      "backlinkCount": 0
    }
  ],
  "total": 1,
  "limit": 100,
  "offset": 0,
  "nextOffset": null
}
```

## get_note 07977151-7486-43d0-8809-c631141c35a4

```json
{
  "note": {
    "id": "07977151-7486-43d0-8809-c631141c35a4",
    "title": "INFRA.md — Mapa de la infraestructura",
    "contentMd": "# INFRA.md — Mapa de la infraestructura\n\n> Documento vivo mantenido por **Orion**. Solo lectura de facto: no contiene secretos.\n> Última actualización: 2026-10-25 (recon inicial, sin cambios en el sistema).\n\n## Host — `homelab` (CHUWI HeroBox)\n- **SO:** Ubuntu 26.04.1 LTS (Resolute Raccoon)\n- **Kernel:** Linux 7.0.0-38\n- **CPU:** Intel Celeron J4125 @2.0 GHz · 4 núcleos / 4 hilos\n- **RAM:** 7.1 GiB (+4 GiB swap)\n- **Disco:** 98 GB raíz ext4 (`/dev/mapper/ubuntu--vg-ubuntu--lv`), ~23% usado\n- **Particiones:** `/boot` (sda2), `/boot/efi` (sda1, ESP)\n- **Tailscale:** nodo `mara-core` · 100.121.31.69 · funnel `https://mara-core.bombay-pomano.ts.net`\n- **SSH:** puerto 22\n\n## Servicios AI (Docker)\n| Servicio | Contenedor | Imagen | Puerto | Estado |\n|---|---|---|---|---|\n| Mara OS | `mara-os` | mara-os (custom) | `9001` | running |\n| Hindsight | `mara-hindsight` | ghcr.io/vectorize-io/hindsight:latest | `8888`, `9999` | running |\n| AgentDesk (app) | `agentdesk-app-1` | agentdesk:latest (Next.js) | `3000` | running (healthy) |\n| AgentDesk (DB) | `agentdesk-db-1` | postgres:16-alpine | `5432` (interno) | running (healthy) |\n\nOtros procesos:\n- **Orion / Hermes gateway:** `127.0.0.1:37371`\n- **systemd:** `docker.service`, `containerd.service`, `tailscaled.service` activos\n\n## Estructura de directorios\n- Base de trabajo: `~/mara/`\n  - `mara-os/` — código fuente Mara OS (Node/TS)\n  - `AgentDesk/` — app Next.js + Drizzle + MCP (repo git)\n  - `hindsight/` — `compose.yml`\n  - `backups/` — copias de seguridad\n  - `obisidian-vault/` — bóveda Obsidian (daily, notas, IA, automatizaciones…)\n- Orion: `~/.hermes/`\n\n## Nodos Tailscale conocidos\n- `mara-core` (este host, linux)\n- `kikes-mac-mini` (macOS, activo)\n- `pve` (linux — probable Proxmox)\n- `enriques-macbook-air`, varios iPhone/iPad y equipos Windows (variado offline)\n\n## Memoria: Hindsight + Obsidian (integración Orion)\n- **Hindsight API:** `http://192.168.1.196:8888` · **Panel:** `http://192.168.1.196:9999`\n- **Acceso de Orion:** vía **REST** (Hindsight no expone MCP; solo openapi/REST). Sin auth en LAN. Verificado.\n- **Bancos:**\n  - `obsidian` — segundo cerebro (653 hechos, 231 docs, ~233 notas). Fuente de conocimiento.\n  - `mara-os` — memoria compartida con Mara OS (8 hechos). Evitar duplicados.\n  - `mara-os-diagnostico` — diagnóstico (4 hechos).\n- **Consulta:** `~/mara/scripts/hindsight_recall.sh \"pregunta\" [bank]` (solo lectura).\n  - Endpoint: `POST /v1/default/banks/{bank}/memories/recall`\n- **Obsidian vault:** dir `~/mara/obisidian-vault` (repo git, 233 `.md`). Bank Hindsight = `obsidian`.\n- **sync_vault.sh:** `git pull` → importa chunks vault→banco `obsidian` (modo sin LLM, dentro de la imagen mara-os) → verifica. Automatización: **cron usuario, diario 03:00** (`0 3 * * *`), log en `~/mara/sync_vault.log`. Tiene lock (flock), `--dry-run/--force/--no-delete/--allow-mass-delete`. Estado en `mara-os/data/obsidian-import.json`.\n\n## AgentDesk — centro de gestión de agentes (integración Orion)\n- **URL:** http://192.168.1.196:3000 · MCP: `POST /api/mcp` (transport streamable-http, vía funnel `https://mara-core.bombay-pomano.ts.net/api/mcp`)\n- **Conexión de Orion:** MCP en `~/.hermes/config.yaml` (`mcp_servers.agentdesk`), token de agente con scopes amplios. Identidad en AgentDesk = agente **Orion** (id `50e2f9b3…`), capacidades `homelab, cve, memoria`.\n- **Scopes:** tasks r/w, delegations r/w, runs r/w, notes r/w, projects r/w, activity:read.\n- **33 herramientas MCP** (solo lectura salvo marcado):\n  - Identidad/estado: `whoami`, `get_queue`.\n  - Tareas: `list_tasks`, `get_task`, `create_task`, `update_task`, `create_subtask`, `get_next_task`/`claim_task` (lease), `update_task_status`, `complete_task`, `fail_task`, `comment_task`/`add_comment`.\n  - Notas (MD, [[wikilinks]]): `list_notes`, `get_note`, `get_note_by_title`, `create_note`, `update_note`, `append_note`, `upsert_note`, `delete_note`(destructivo).\n  - Proyectos: `list_projects` (+ scope projects:write).\n  - Delegaciones/aprobaciones: `list_delegations`, `update_delegation`, `propose_delegation`, `request_approval`.\n  - Runs: `start_run`, `log_run`/`append_log`, `finish_run`, `add_artifact`/`attach_artifact`.\n- **Modelo:** un agente no hace nada irreversible — delegaciones y acciones externas van a **Aprobaciones** hasta que el humano decide. Autonomía por tarea: `suggest_only` / `do_with_approval` / `autonomous_low_risk`.\n- **API REST v1** (`/api/v1`, 15 endpoints, Bearer por agente) y OpenAPI en `GET /api/openapi.json`. Docs en `~/mara/AgentDesk/docs/`.\n- Orion = coordinador: usa AgentDesk como inventario único de agentes/tareas; NO mantiene listados duplicados.\n\n## Notas operativas\n- Recursos ajustados: 7 GB RAM para 4 contenedores + PostgreSQL. Vigilar memoria.\n- Secretos en `~/mara/**/.env` — tratar como sensibles, no exponer ni versionar.\n- Todos los contenedores arrancan juntos (~mismo instante) → `docker compose up` único o arranque del equipo.\n\n## Comandos útiles (solo lectura)\n- Estado contenedores: `docker ps -a`\n- Logs: `docker logs -f <container>`\n- Recursos: `docker stats`\n- Red: `ss -tulpn` · Tailscale: `tailscale status`\n",
    "source": "app",
    "authorType": "agent",
    "authorId": "50e2f9b3-b6a4-4fc3-8d76-6ef9a3459907",
    "authorName": "Orion",
    "projectId": null,
    "taskId": null,
    "createdAt": "2026-10-25T10:27:27.372Z",
    "updatedAt": "2026-10-25T10:27:27.372Z"
  },
  "project": null,
  "backlinks": [],
  "outgoing": [
    {
      "title": "wikilinks",
      "note": null
    }
  ],
  "related": []
}
```

## list_delegations (sin filtro)

```json
{
  "delegations": []
}
```

## list_delegations (todos los estados)

```json
{
  "delegations": []
}
```

## get_queue

```json
{
  "delegations": [],
  "tasks": [
    {
      "id": "f818728e-4eaf-4c8d-accd-7deaa25ea043",
      "title": "Probar la app en un dispositivo sin instalarla (Android e iOS)",
      "description": "Conseguir probar la aplicación en un dispositivo real sin tener que instalarla, tanto en Android como en iOS.",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    }
  ]
}
```

## get_task 266cc328-4cf8-47f3-89ec-848614b15200

```json
{
  "task": {
    "id": "266cc328-4cf8-47f3-89ec-848614b15200",
    "title": "Mostrar en el panel del organizador el número de chats con conversación",
    "description": "Hay que arreglar que en el panel del organizador del evento se refleje el número de chats en los que se está hablando (chats con conversación activa).",
    "status": "done",
    "priority": "none",
    "autonomy": "do_with_approval",
    "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
    "project": "Biavent",
    "parentTaskId": null,
    "labels": [],
    "dueDate": null,
    "dueTime": null,
    "assigneeType": "agent",
    "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
    "claimedByAgentId": null,
    "leaseExpiresAt": null,
    "leaseSecondsLeft": null,
    "claimCount": 0,
    "subtaskTotal": 0,
    "subtaskDone": 0
  },
  "subtasks": [],
  "comments": [],
  "approvals": [],
  "openRun": null
}
```

## get_task 0ad3aebc-bf64-44ad-96e0-244576f5511f

```json
{
  "task": {
    "id": "0ad3aebc-bf64-44ad-96e0-244576f5511f",
    "title": "Poner en el panel de organizador los encuentros que se han hecho",
    "description": null,
    "status": "done",
    "priority": "none",
    "autonomy": "do_with_approval",
    "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
    "project": "Biavent",
    "parentTaskId": null,
    "labels": [],
    "dueDate": null,
    "dueTime": null,
    "assigneeType": "agent",
    "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
    "claimedByAgentId": null,
    "leaseExpiresAt": null,
    "leaseSecondsLeft": null,
    "claimCount": 0,
    "subtaskTotal": 0,
    "subtaskDone": 0
  },
  "subtasks": [],
  "comments": [],
  "approvals": [],
  "openRun": null
}
```

## get_task 7fc9e10e-a2b3-48f9-bcfe-b61dc22dfec6

```json
{
  "task": {
    "id": "7fc9e10e-a2b3-48f9-bcfe-b61dc22dfec6",
    "title": "Poner Perfil como última opción del menú inferior",
    "description": "Mover la opción de Perfil para que aparezca en último lugar del menú de navegación de abajo.",
    "status": "done",
    "priority": "none",
    "autonomy": "do_with_approval",
    "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
    "project": "Biavent",
    "parentTaskId": null,
    "labels": [],
    "dueDate": null,
    "dueTime": null,
    "assigneeType": "agent",
    "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
    "claimedByAgentId": null,
    "leaseExpiresAt": null,
    "leaseSecondsLeft": null,
    "claimCount": 0,
    "subtaskTotal": 0,
    "subtaskDone": 0
  },
  "subtasks": [],
  "comments": [],
  "approvals": [],
  "openRun": null
}
```

## get_task b02f5889-c6f2-4d3e-854f-cd9fa19eb738

```json
{
  "task": {
    "id": "b02f5889-c6f2-4d3e-854f-cd9fa19eb738",
    "title": "Revisar el tamaño del chat y por qué se cierra el teclado al enviar un mensaje",
    "description": "Revisar el tamaño de la ventana del chat y averiguar por qué el teclado se cierra al enviar un mensaje.",
    "status": "done",
    "priority": "none",
    "autonomy": "do_with_approval",
    "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
    "project": "Biavent",
    "parentTaskId": null,
    "labels": [],
    "dueDate": null,
    "dueTime": null,
    "assigneeType": "agent",
    "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
    "claimedByAgentId": null,
    "leaseExpiresAt": null,
    "leaseSecondsLeft": null,
    "claimCount": 0,
    "subtaskTotal": 0,
    "subtaskDone": 0
  },
  "subtasks": [],
  "comments": [],
  "approvals": [],
  "openRun": null
}
```

## get_task f818728e-4eaf-4c8d-accd-7deaa25ea043

```json
{
  "task": {
    "id": "f818728e-4eaf-4c8d-accd-7deaa25ea043",
    "title": "Probar la app en un dispositivo sin instalarla (Android e iOS)",
    "description": "Conseguir probar la aplicación en un dispositivo real sin tener que instalarla, tanto en Android como en iOS.",
    "status": "todo",
    "priority": "none",
    "autonomy": "do_with_approval",
    "projectId": "c7525703-c2c9-4681-bd02-1154b92f25ae",
    "project": "Biavent",
    "parentTaskId": null,
    "labels": [],
    "dueDate": null,
    "dueTime": null,
    "assigneeType": "agent",
    "assigneeId": "eecefdf7-cd56-460c-99a0-ac4c382a1adc",
    "claimedByAgentId": null,
    "leaseExpiresAt": null,
    "leaseSecondsLeft": null,
    "claimCount": 0,
    "subtaskTotal": 0,
    "subtaskDone": 0
  },
  "subtasks": [],
  "comments": [],
  "approvals": [],
  "openRun": null
}
```

