---
title: configuracion
type: nota
tags:
  - openclaw
  - backup
project: none
status: active
date_created: 2026-08-13
date_modified: 2026-08-23
---
# Configuracion de Mara

> Archivo legado. La version viva y canonica esta en `MaraOs/Documentacion Operativa/configuracion.md`.

> Este archivo se conserva solo como referencia historica.

## Skills

Skills disponibles en el contexto de OpenClaw de esta sesion:

- `browser-automation`: control de paginas web con herramienta de navegador.
- `canvas`: presentar HTML en canvases de nodos OpenClaw.
- `diagram-maker`: crear diagramas SVG/HTML o Excalidraw.
- `gh-issues`: flujo de issues de GitHub y PRs.
- `github`: GitHub CLI para issues, PRs, CI, releases y consultas.
- `graphify`: grafo de conocimiento de codigo, docs, papers o imagenes.
- `healthcheck`: auditoria y hardening de hosts OpenClaw.
- `meme-maker`: busqueda y generacion de memes.
- `node-connect`: diagnostico de pairing de nodos OpenClaw.
- `node-inspect-debugger`: debugging Node.js.
- `python-debugpy`: debugging Python.
- `skill-creator`: crear, editar, auditar y validar AgentSkills.
- `spike`: prototipos rapidos para validar viabilidad.
- `taskflow`: coordinar tareas detached durables.
- `taskflow-inbox-triage`: patron de triage de inbox.
- `weather`: tiempo y prevision con `wttr.in`.

Skills adicionales documentadas en el entorno Codex:

- `imagegen`.
- `openai-docs`.
- `plugin-creator`.
- `skill-installer`.

## Subagentes / roles

- Mara: agente principal y orquestadora.
- Atlas: calendario, tareas, notas, organizacion diaria y resumenes Atlas.
- Arvis: creatividad, comunicacion, contenido, storytelling y vigilancia IA/tech.
- Warren: analisis financiero, mercados Espana/EEUU, crypto y senales accionables.
- Scout: rol legacy de research; no vivo salvo reactivacion explicita.

## MCP conectados

Documentados:

- Calendar MCP:
  - Uso: crear, consultar, editar y borrar eventos.
  - MCP configurado: `calendar-mara` cuando este disponible.
  - Endpoint operativo usado en la practica: `https://core-n8n.832gky.easypanel.host/mcp/calendar`.
  - Endpoint historico/documentado: `https://core-n8n.832gky.easypanel.host/mcp/agents-calendar`.
- Notes MCP:
  - Uso: gestion de tareas/notas.
  - Endpoint: `https://core-n8n.832gky.easypanel.host/mcp/agents-notes`.
- Linear MCP:
  - Endpoint documentado en cron: `https://core-n8n.832gky.easypanel.host/mcp/agents-linear`.
  - Estado actual: No especificado.

Reglas:

- Tareas y calendario siempre por MCP cuando Kike las dicte o pida gestionarlas.
- Tareas dictadas por Kike solo en `agents-notes`.
- Eventos por calendario configurado y verificados por respuesta/listado del MCP.
- Viajes no van al calendario; se registran en Obsidian bajo diario/viajes.

## Cronjobs / automatizaciones

Cronjobs activos documentados en OpenClaw:

| Nombre | Cron | Zona | Estado |
|---|---|---|---|
| Atlas resumen diario breve | `0 7 * * *` | Europe/Madrid | Activo |
| Crear archivo diario Obsidian | `5 0 * * *` | Europe/Madrid | Activo |
| Mara changelog diario Obsidian | `0 20 * * *` | Europe/Madrid | Activo |
| Resumen semanal diario | `0 20 * * 0` | Europe/Madrid | Activo |
| WatchDog Warren alertas | `0 9,11,13,15,17,19,21 * * 1-5` | Europe/Madrid | Activo |
| Warren resumen diario unico | `30 22 * * 1-5` | Europe/Madrid | Activo |
| Ubuntu Ops breve | `30 8,14,20 * * *` | Europe/Madrid | Activo |

Cronjobs desactivados documentados:

| Nombre | Cron | Zona | Estado |
|---|---|---|---|
| Warren analisis diario Crypto | `30 13 * * 1-5` | Europe/Madrid | Desactivado |
| Warren analisis diario EEUU | `30 15 * * 1-5` | Europe/Madrid | Desactivado |
| Mara estadisticas Ubuntu Desktop | `0 11,16,21 * * *` | Europe/Madrid | Desactivado |

## Variables de entorno

- Variables requeridas exactas: No especificado.
- Tokens/API keys: no documentar en claro.
- Usar placeholders:
  - `<OPENCLAW_TOKEN>`
  - `<GITHUB_TOKEN>`
  - `<MCP_AUTH_TOKEN>`
  - `<TELEGRAM_TOKEN>`
  - `<N8N_SECRET>`

## Rutas importantes

- Workspace de Mara: `/home/enriquetecfan/.openclaw/workspace`.
- Vault Obsidian canonico: `/home/enriquetecfan/Documents/obisidian-vault`.
- Area operativa principal: `/home/enriquetecfan/Documents/obisidian-vault/MaraOs/`.
- Archivos canonicos del sistema: `/home/enriquetecfan/Documents/obisidian-vault/MaraOs/SystemFiles/`.
- Diarios canonicos: `/home/enriquetecfan/Documents/obisidian-vault/MaraOs/diario/diario/`.
- Formato de diario: `diario-DD-MM-YYYY.md`.
- Resumenes Atlas, changelogs y resumenes semanales: `MaraOs/diario/...`.
- `MaraOs/daily/`: historico/legacy.
- Cronjobs OpenClaw: `/home/enriquetecfan/.openclaw/cron/jobs.json`.
- Estado de cronjobs: `/home/enriquetecfan/.openclaw/cron/jobs-state.json`.
- Runs de cronjobs: `/home/enriquetecfan/.openclaw/cron/runs/`.
- Snapshot Ubuntu Ops: `/home/enriquetecfan/Documents/obisidian-vault/MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`.

## Repositorios

- Vault canonico remoto esperado: `https://github.com/enriquetecfan11/obisidian-vault.git`.
- `mara-os`: panel/mission-control y capa operativa cuando aplique.
- Ruta exacta local de `mara-os`: No especificado.

## Servicios necesarios

- OpenClaw.
- Telegram provider conectado a Kike.
- Obsidian vault local.
- Git y acceso a GitHub para sincronizar el vault.
- n8n / endpoints MCP en `core-n8n.832gky.easypanel.host`.
- Cron/Gateway de OpenClaw.
- Docker: usado por Ubuntu Ops; servicios concretos no especificados.
- Tailscale: comprobado por Ubuntu Ops si existe; configuracion no especificada.
