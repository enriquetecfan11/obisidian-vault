---
type: config
tags:
  - maraos
  - cron
  - automations
  - schedule
status: active
---
# Cron principales MaraOS

#mara-os #cron #automatizaciones

Actualizado: 09-06-2026

Configurados en OpenClaw con zona horaria `Europe/Madrid` y entrega anunciada a Kike por Telegram.

## Activos principales

| Nombre | Cron | Descripción | Estado |
|---|---:|---|---|
| Atlas resumen diario | `0 7 * * *` | 3-5 bullets con tareas, eventos y slots clave. | Activo |
| Crear archivo diario Obsidian | `5 0 * * *` | Crea el diario canónico en `MaraOs/diario/diario/`. | Activo |
| Mara changelog diario Obsidian | `0 20 * * *` | Actualiza changelog en Obsidian; Telegram corto. | Activo |
| Resumen semanal diario | `0 20 * * 0` | Genera resumen semanal bajo `MaraOs/diario/...`. | Activo |
| WatchDog Warren | `0 9,11,13,15,17,19,21 * * 1-5` | Solo alertas de mercado relevantes. | Activo |
| Resumen diario Warren | `30 22 * * 1-5` | Brief único España + EEUU + Crypto. | Activo |
| Ubuntu Ops | `30 8,14,20 * * *` | Salud del Ubuntu Desktop; si OK, una línea. | Activo |

## Consolidados/desactivados

| Nombre anterior | Motivo |
|---|---|
| Warren análisis diario · Crypto 13:30 | Desactivado por consolidación en Warren 22:30 y WatchDog. |
| Warren análisis diario · EEUU 15:30 | Desactivado por consolidación en Warren 22:30 y WatchDog. |
| Ubuntu Ops 11:00/16:00/21:00 | Desactivado por consolidación en 08:30/14:30/20:30. |

## Reglas operativas incluidas

- Fuente de verdad: `/home/enriquetecfan/Documents/obisidian-vault`.
- Mantener literalmente `obisidian-vault`.
- Usar diarios canónicos en `MaraOs/diario/diario/diario-DD-MM-YYYY.md`.
- `MaraOs/daily/` es histórico/legacy, no destino principal para diarios nuevos.
- MCPs indicados:
  - Tareas: `https://core-n8n.832gky.easypanel.host/mcp/agents-notes`
  - Calendario: `https://core-n8n.832gky.easypanel.host/mcp/calendar`
  - Linear: `https://core-n8n.832gky.easypanel.host/mcp/agents-linear`
- Si un MCP/fuente falla o no está disponible, decirlo claro y no inventar estado.
- Política de estilo vigente: [[cron-politica-brief-radio-2026-06-08]].
- WatchDog Warren debe etiquetar activos USA con horario calculado cada día: convertir `09:30-16:00 America/New_York` a `Europe/Madrid`; antes de apertura usar `premarket EEUU`, durante apertura usar `mercado regular EEUU`, y nunca aplicar `premarket` a crypto, petróleo, futuros ni commodities.
