---
title: Tareas sin proyecto
tags:
  - agentdesk
  - copia-seguridad
  - backup
date_created: 2026-10-31
date_modified: 2026-11-03
---

# Tareas sin proyecto

Copia de las tareas de Agent Desk que no pertenecen a ningún proyecto, según el backup que pasó Notis el 03/11/2026 a las 09:05 (hora de Madrid). Índice: [[Copia Agent Desk]].

## Mejorar dashboard

| Campo | Valor |
|---|---|
| ID | no incluido en el backup |
| Estado | backlog |
| Prioridad | normal |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Asignada a | agent: Orion (50e2f9b3…) |
| Etiquetas | — |

**Descripción:** Mejorar el dashboard (funcionalidad/interfaz). Pendiente de concretar alcance y detalles.

**Subtareas:** ninguna

## Sincronizar vault Obsidian → Hindsight (diario 23:00)

| Campo | Valor |
|---|---|
| ID | no incluido en el backup |
| Estado | todo |
| Prioridad | normal |
| Autonomía | do_with_approval |
| Fecha límite | 2026-11-02 (recurrente) |
| Asignada a | agent: Orion (50e2f9b3…) |
| Etiquetas | — |

**Descripción:** Tarea recurrente: cada noche a las 23:00 ejecutar los scripts de `/home/enriquetecfan/mara/scripts/` para mantener sincronizado el vault de Obsidian con Hindsight. Scripts:

1. `sync_vault.sh`: git pull del vault, subida de notas nuevas o modificadas al banco `obsidian`, borrado de las eliminadas y verificación.
2. `hindsight_recall.sh "notas" obsidian`: consulta de verificación de que Hindsight responde.

Cron job programado en Hermes para automatizarlo.

**Subtareas:** ninguna

Relacionado: [[INFRA - Mapa de la infraestructura]]
