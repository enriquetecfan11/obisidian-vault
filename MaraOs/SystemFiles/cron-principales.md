# Cron principales MaraOS

#mara-os #cron #automatizaciones

Actualizado: 06-05-2026

Configurados en OpenClaw con zona horaria `Europe/Madrid` y entrega anunciada a Kike por Telegram.

| Nombre | Cron | Descripción | Job ID |
|---|---:|---|---|
| Atlas resumen diario | `0 7 * * *` | Resumen automático de eventos y tareas del día usando calendario + tasks por MCP. | `5874c37b-bd74-4ceb-96f9-bed70af3f441` |
| Mara changelog diario Obsidian | `0 20 * * *` | Genera/actualiza el changelog diario en Obsidian. | `a54851c9-9679-4181-bd98-278896c0807e` |
| Crear archivo diario Obsidian | `5 0 * * *` | Crea el archivo diario del día en Obsidian si no existe. | `448e9b39-9c3c-4bde-9a2f-a15a36e01bcd` |
| Resumen semanal diario | `0 20 * * 0` | Genera resumen semanal del diario los domingos. | `d1f91f6b-124e-4cc3-924d-ef7df5bf4333` |
| Warren análisis diario · España | `0 9 * * 1-5` | Bloque diario de mercado España. | `d718cf8b-f6df-42c5-b6f8-e1f8065fff3b` |
| Warren análisis diario · Crypto | `30 13 * * 1-5` | Bloque diario crypto. | `0a767aae-4a21-410c-a84a-dc260fa75b78` |
| Warren análisis diario · EEUU | `30 15 * * 1-5` | Bloque diario EEUU + crypto. | `07e57292-69a6-4a15-9f5f-43dd545c307a` |
| Resumen diario Warren | `30 22 * * 1-5` | Resumen final corto diario de Warren. | `b5b2b20a-4ae5-47bf-ae70-a5e7cb52b457` |
| Mara estadísticas diarias Ubuntu Desktop | `30 19 * * *` | Informe diario de salud del Ubuntu Desktop donde vive Mara. | `f7b5e2c0-0645-49a7-90cc-ff1c9e7a9662` |

## Reglas operativas incluidas

- Fuente de verdad: `/home/enriquetecfan/Documents/obisidian-vault`.
- Mantener literalmente `obisidian-vault`.
- Usar rutas canónicas dentro de `MaraOs/diario/...`.
- MCPs indicados:
  - Tareas: `https://core-n8n.832gky.easypanel.host/mcp/agents-notes`
  - Calendario: `https://core-n8n.832gky.easypanel.host/mcp/calendar`
  - Linear: `https://core-n8n.832gky.easypanel.host/mcp/agents-linear`
- Si un MCP/fuente falla o no está disponible, decirlo claro y no inventar estado.
