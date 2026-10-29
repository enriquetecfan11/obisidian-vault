---
title: Copia Agent Desk
tags:
  - agentdesk
  - copia-seguridad
  - backup
  - indice
date_created: 2026-10-24
date_modified: 2026-10-29
---

# Copia Agent Desk

Copia de seguridad de todo el contenido de Agent Desk. La primera copia se hizo el 24/10/2026, antes de mover Agent Desk de sitio, y esta versión está actualizada con la instancia nueva. Es una exportación de solo lectura: no se cambió nada en Agent Desk. El historial de git conserva la versión anterior.

- **Última actualización:** 29/10/2026, 09:00 (hora de Madrid), con la copia programada que pasó Notis. La lectura anterior en directo desde el conector fue el 27/10/2026 a las 09:12.
- **Cuenta usada:** agente Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc), estado active, capacidades: proyectos, notas, utilidades
- **Permisos del acceso:** tasks:read, tasks:write, delegations:read, delegations:write, runs:read, runs:write, notes:read, notes:write, projects:read, projects:write, activity:read
- **Cola en ese momento:** 1 tarea y 0 delegaciones

## Resumen

| Elemento | Cantidad |
|---|---|
| Proyectos | 3 |
| Tareas (total) | 5 |
| Tareas en backlog | 0 |
| Tareas en todo | 1 |
| Tareas en in_progress | 0 |
| Tareas en review | 0 |
| Tareas en done | 4 |
| Tareas en cancelled | 0 |
| Notas | 1 |
| Delegaciones | 0 |

## Cambios desde la copia del 27/10

Ninguno. La copia del 29/10/2026 a las 09:00 coincide con la anterior: los mismos 3 proyectos, las mismas 5 tareas (4 hechas y 1 en todo), la misma nota de Orion y ninguna delegación.

## Cambios entre la copia del 24/10 y la del 27/10

- Agent Desk se ha movido a una instancia nueva: han cambiado todos los IDs (proyectos, tareas y el agente Notis, que antes era `59d74399-…` y ahora es `eecefdf7-…`, con capacidades proyectos, notas y utilidades).
- Proyecto nuevo: **Tareas personales** (TAP), sin tareas.
- Biavent: 4 de las 5 tareas han pasado de todo a **done**. Solo sigue en todo «Probar la app en un dispositivo sin instalarla (Android e iOS)».
- «Poner en el panel de organizador los encuentros que se han hecho» antes no tenía a nadie asignado y ahora está asignada a Notis, como las demás.
- Nota nueva: [[INFRA - Mapa de la infraestructura]] («INFRA.md — Mapa de la infraestructura»), de Orion, creada el 25/10/2026.
- La cola de Notis ha bajado de 4 tareas a 1. Siguen sin existir delegaciones.

## Proyectos

| Proyecto | Identificador | ID | Estado | Tareas | Hechas | Copia |
|---|---|---|---|---|---|---|
| MaraOs | MAOS | b308d5fc-1ddd-45b5-bc05-c8feb20dadf3 | active | 0 | 0 | sin tareas |
| Biavent | BIA | c7525703-c2c9-4681-bd02-1154b92f25ae | active | 5 | 4 | [[Tareas Biavent]] |
| Tareas personales | TAP | 70b16875-640f-49d6-88b9-467019761ae4 | active | 0 | 0 | sin tareas |

## Tareas

### [[Tareas Biavent]]

- Mostrar en el panel del organizador el número de chats con conversación (done)
- Poner en el panel de organizador los encuentros que se han hecho (done)
- Poner Perfil como última opción del menú inferior (done)
- Revisar el tamaño del chat y por qué se cierra el teclado al enviar un mensaje (done)
- Probar la app en un dispositivo sin instalarla (Android e iOS) (todo)

Ninguna tarea tiene subtareas, comentarios, runs ni aprobaciones.

## Notas

| Nota | Autor | Proyecto | Creada | Actualizada |
|---|---|---|---|---|
| [[INFRA - Mapa de la infraestructura]] | Orion (agente) | ninguno | 25/10/2026 | 25/10/2026 |

## Delegaciones

No hay delegaciones en ningún estado.

## Cola (get_queue)

0 delegaciones y 1 tarea asignada a Notis abierta: «Probar la app en un dispositivo sin instalarla (Android e iOS)».

## Datos en bruto

- [[Datos en bruto]]: todas las respuestas JSON originales.

## Relacionado

- [[Biavent - Brand Core]]
- [[MOC Automatizaciones]]
