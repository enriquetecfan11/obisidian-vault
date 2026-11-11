---
title: Copia Agent Desk
tags:
  - agentdesk
  - copia-seguridad
  - backup
  - indice
date_created: 2026-10-24
date_modified: 2026-11-11
---

# Copia Agent Desk

Copia de seguridad de todo el contenido de Agent Desk. La primera copia se hizo el 24/10/2026, antes de mover Agent Desk de sitio, y esta versión está actualizada con la instancia nueva. Es una exportación de solo lectura: no se cambió nada en Agent Desk. El historial de git conserva la versión anterior.

- **Última actualización:** 11/11/2026, 08:59 (hora de Madrid), copia programada de Notis (documento completo de origen).
- **Cuenta usada:** agente Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc), estado active, capacidades: proyectos, notas, utilidades
- **Permisos del acceso:** tasks:read, tasks:write, delegations:read, delegations:write, runs:read, runs:write, notes:read, notes:write, projects:read, projects:write, activity:read
- **Cola en ese momento:** no incluida en el documento de origen.

## Resumen

| Elemento | Cantidad |
|---|---|
| Proyectos | 3 |
| Tareas (total) | 22 |
| Tareas en backlog | 0 |
| Tareas en todo | 5 |
| Tareas en in_progress | 0 |
| Tareas en review | 1 |
| Tareas en done | 16 |
| Tareas en cancelled | 0 |
| Notas | 3 |
| Delegaciones | 0 |

## Cambios respecto al 09/11

- **Revisar el nuevo manual de seguros** (`3f4b63c7…`): pasa de todo a **done**. Tareas personales queda en 6 tareas, 5 hechas.
- **Sincronizar vault Obsidian → Hindsight:** la fecha límite pasa del 07/11 al **12/11/2026**. Se registra una aprobación caducada (`complete_task`, rejected) del 08/11.
- Comentarios nuevos de Chati (05/11) en dos tareas de Biavent: «Registrar recomendaciones mostradas y clics en abrir chat» y «Mostrar en el panel del organizador el número de chats con conversación». En la primera, las reclamaciones pasan de 0 a 1.
- Recuento global: 22 tareas (16 done, 5 todo, 1 review). Notas Hermes, INFRA (texto idéntico al del 25/10) y Reuniones QR sin cambios. Sin tareas ni notas nuevas ni eliminadas. 0 delegaciones.


## Cambios entre la copia del 05/11 y la del 07/11

- Biavent pasa de 5 a 15 tareas (10 done, 4 todo, 1 review): 11 tareas nuevas. Ver [[Tareas Biavent]].
- Eliminada (ya no existe en origen): «Probar la app en un dispositivo sin instalarla (Android e iOS)» (`f818728e-4eaf-4c8d-accd-7deaa25ea043`).
- Tareas personales: la fecha límite de «Sincronizar vault Obsidian → Hindsight» pasa del 05/11 al 07/11/2026.
- Nota nueva: [[Reuniones QR asociadas a evento]] (Chati, Biavent, 05/11/2026).
- Hermes e INFRA sin cambios.

## Cambios entre la copia del 03/11 y la del 05/11

- **Mejorar dashboard:** pasa de backlog a **done** (sigue asignada a Orion). Sigue en [[Tareas sin proyecto]].
- **Sincronizar vault Obsidian → Hindsight (diario 23:00):** deja de estar sin proyecto y pasa al proyecto **Tareas personales**. Sigue en todo; fecha límite 05/11/2026; autonomía `suggest_only`.
- Proyecto **Tareas personales** (TAP): ahora tiene 6 tareas (4 done, 2 todo). Ver [[Tareas personales]].
- Tareas nuevas en Tareas personales: Recordar Vera correo Jorge (done), Recordar Vera comida (done), Revisar el nuevo manual de seguros (todo), Revisar lo que se guarda en el panel de Biavent (done), Mi nueva tarea (done).
- Biavent sin cambios de contenido (5 tareas, 4 done).
- Notas Hermes e INFRA sin cambios de contenido. La nota INFRA se mantiene completa (versión del 25/10).

## Cambios desde la copia del 01/11

- **Sincronizar vault Obsidian → Hindsight (diario 23:00):** la fecha límite pasa del 31/10/2026 al 02/11/2026 y ahora figura como recurrente. Sigue en todo.
- No ha cambiado ni desaparecido nada más. La nota INFRA volvió a llegar cortada («NO mantiene lis…»), pero lo recibido coincide con la copia completa del 25/10, así que se conserva.

## Cambios entre la copia del 31/10 y la del 01/11

- Tarea nueva sin proyecto: **Sincronizar vault Obsidian → Hindsight (diario 23:00)** (todo, prioridad normal, asignada a Orion, fecha límite 31/10/2026). Ver [[Tareas sin proyecto]].
- Aviso: en [[INFRA - Mapa de la infraestructura]] figura un cron diario a las 03:00 para `sync_vault.sh`, y la tarea nueva habla de las 23:00 con un cron en Hermes.
- No ha desaparecido nada. La nota INFRA llegó cortada en el backup («Notas operativas», a mitad de línea), así que se conserva la copia completa anterior, sin cambios desde el 25/10.

## Cambios entre la copia del 29/10 y la del 31/10

- Tarea nueva sin proyecto: **Mejorar dashboard** (backlog, prioridad normal, asignada a Orion). Ver [[Tareas sin proyecto]].
- Nota nueva: [[Hermes Homelab Api]], de Enrique Rodriguez Vela, creada el 30/10/2026. La clave de la API no está en la copia.
- No ha desaparecido nada: siguen los 3 proyectos, las 5 tareas de Biavent, la nota INFRA y ninguna delegación.

## Cambios entre la copia del 27/10 y la del 29/10

Ninguno.

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
| Biavent | BIA | c7525703-c2c9-4681-bd02-1154b92f25ae | active | 15 | 10 | [[Tareas Biavent]] |
| Tareas personales | TAP | 70b16875-640f-49d6-88b9-467019761ae4 | active | 6 | 5 | [[Tareas personales]] |

## Tareas

### [[Tareas Biavent]]

- Mostrar en el panel del organizador el número de chats con conversación (done)
- Poner en el panel de organizador los encuentros que se han hecho (done)
- Poner Perfil como última opción del menú inferior (done)
- Revisar el tamaño del chat y por qué se cierra el teclado al enviar un mensaje (done)
- Añadir reuniones verificadas al embudo del organizador (todo)
- Registrar recomendaciones mostradas y clics en abrir chat (done)
- Asociar cada reunión QR a un evento concreto (done)
- Crear la encuesta posterior a cada reunión (done)
- Permitir múltiples reuniones verificadas entre dos usuarios (done)
- Añadir conversión de conexiones a reuniones (done)
- Corregir el cálculo de actividad en las últimas 24 horas (todo)
- Ampliar estadísticas de objetivos profesionales (todo)
- Incorporar resultados de las encuestas al dashboard (done)
- Ampliar informes automáticos con métricas de impacto (todo)
- Probar QR y analíticas con dos usuarios reales (review)

### [[Tareas personales]]

- Sincronizar vault Obsidian → Hindsight (diario 23:00) (todo, Orion, fecha límite 12/11/2026)
- Recordar Vera correo Jorge (done, fecha límite 05/11/2026)
- Recordar Vera comida (done, fecha límite 05/11/2026)
- Revisar el nuevo manual de seguros (done)
- Revisar lo que se guarda en el panel de Biavent (done)
- Mi nueva tarea (done)

### [[Tareas sin proyecto]]

- Mejorar dashboard (done, asignada a Orion)

Ninguna tarea tiene subtareas, comentarios, runs ni aprobaciones.

## Notas

| Nota | Autor | Proyecto | Creada | Actualizada |
|---|---|---|---|---|
| [[INFRA - Mapa de la infraestructura]] | Orion (agente) | ninguno | 25/10/2026 | 25/10/2026 |
| [[Hermes Homelab Api]] | Enrique Rodriguez Vela (humano) | ninguno | 30/10/2026 | 30/10/2026 |
| [[Reuniones QR asociadas a evento]] | Chati (agente) | Biavent | 05/11/2026 | 05/11/2026 |

## Delegaciones

No hay delegaciones en ningún estado.

## Cola (get_queue)

No incluida en el documento de origen del 11/11.


## Datos en bruto

- [[Datos en bruto]]: todas las respuestas JSON originales (snapshot del 27/10; las copias posteriores actualizan las notas humanas de esta carpeta).

## Relacionado

- [[Biavent - Brand Core]]
- [[MOC Automatizaciones]]
