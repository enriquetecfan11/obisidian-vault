---
title: Tareas Biavent
tags:
  - agentdesk
  - copia-seguridad
  - backup
  - biavent
date_created: 2026-10-24
date_modified: 2026-11-13
---

# Tareas Biavent

Copia de las tareas del proyecto **Biavent** (BIA, id `c7525703-c2c9-4681-bd02-1154b92f25ae`) de Agent Desk, actualizada con la copia programada del 13/11/2026 a las 08:50 (hora de Madrid). Índice: [[Copia Agent Desk]].

## Mostrar en el panel del organizador el número de chats con conversación

| Campo | Valor |
|---|---|
| ID | 266cc328-4cf8-47f3-89ec-848614b15200 |
| Estado | done |
| Prioridad | none |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** Hay que arreglar que en el panel del organizador del evento se refleje el número de chats en los que se está hablando (chats con conversación activa).

**Subtareas:** ninguna

**Comentarios:**

1. **Chati** (agente) — 05/11/2026, 20:55:59 (hora de Madrid): La métrica de chats iniciados queda visible en el panel de networking como conversaciones DM con al menos un mensaje. También se mantiene el embudo: Registrados → Perfil completo → Solicitudes enviadas → Conexiones aceptadas → Chats iniciados. No se ejecutaron migraciones ni despliegues.

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Poner en el panel de organizador los encuentros que se han hecho

| Campo | Valor |
|---|---|
| ID | 0ad3aebc-bf64-44ad-96e0-244576f5511f |
| Estado | done |
| Prioridad | none |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** —

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Poner Perfil como última opción del menú inferior

| Campo | Valor |
|---|---|
| ID | 7fc9e10e-a2b3-48f9-bcfe-b61dc22dfec6 |
| Estado | done |
| Prioridad | none |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** Mover la opción de Perfil para que aparezca en último lugar del menú de navegación de abajo.

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Revisar el tamaño del chat y por qué se cierra el teclado al enviar un mensaje

| Campo | Valor |
|---|---|
| ID | b02f5889-c6f2-4d3e-854f-cd9fa19eb738 |
| Estado | done |
| Prioridad | none |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** Revisar el tamaño de la ventana del chat y averiguar por qué el teclado se cierra al enviar un mensaje.

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Añadir reuniones verificadas al embudo del organizador

| Campo | Valor |
|---|---|
| ID | b5aab8fb-59af-467f-9b02-6d8b6224a971 |
| Estado | todo |
| Prioridad | high |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** Ampliar los cinco pasos actuales.

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Registrar recomendaciones mostradas y clics en abrir chat

| Campo | Valor |
|---|---|
| ID | 88b2927f-c734-4fa1-8905-fcdcbeaadaf4 |
| Estado | done |
| Prioridad | high |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Chati (46021daa-444b-49db-919c-9c3cb31c7a04) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 1 |

**Descripción:** Necesario para medir la efectividad de las recomendaciones.

**Subtareas:** ninguna

**Comentarios:**

1. **Chati** (agente) — 05/11/2026, 20:53:48 (hora de Madrid): Completado en el código: se mantiene `recommendation_shown` con su deduplicación y se sustituye `recommendation_profile_opened` por `recommendation_chat_clicked` al pulsar «Abrir chat». Las métricas del organizador ahora exponen `recommendationChatsClicked` / `recommendation_chats_clicked`. `chatsInitiated` sigue midiendo conversaciones DM reales por separado. No se ejecutaron migraciones ni despliegues.
2. **Chati** (agente) — 05/11/2026, 20:53:53 (hora de Madrid): Implementado y verificado en el repositorio; no se aplicó la migración ni se desplegó.
3. **Chati** (agente) — 05/11/2026, 20:55:59 (hora de Madrid): Implementación reflejada en el panel de administración/analítica compartida: se muestran «Recomendaciones mostradas» y «Clics en Abrir chat», con tasa de interacción condicionada a métricas comparables. Se añadieron traducciones en los 8 locales. No se ejecutaron migraciones ni despliegues.

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Asociar cada reunión QR a un evento concreto

| Campo | Valor |
|---|---|
| ID | d20dda99-8bb1-4057-be09-4ec161c84dc4 |
| Estado | done |
| Prioridad | high |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** Actualmente se guarda en la conexión, no en el evento.

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Crear la encuesta posterior a cada reunión

| Campo | Valor |
|---|---|
| ID | 9c95941e-6fe6-4766-b7b5-b973108131af |
| Estado | done |
| Prioridad | high |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** Preguntar por utilidad y si se habrían conocido sin Biavent.

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Permitir múltiples reuniones verificadas entre dos usuarios

| Campo | Valor |
|---|---|
| ID | 661e6e35-5d1d-45b0-8c19-a71122b0532d |
| Estado | done |
| Prioridad | high |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** El modelo actual marca una reunión confirmada por conexión.

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Añadir conversión de conexiones a reuniones

| Campo | Valor |
|---|---|
| ID | 00172b03-0ef8-42ae-b404-7216ac49c591 |
| Estado | done |
| Prioridad | high |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** Porcentaje y usuarios únicos con al menos una reunión.

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Corregir el cálculo de actividad en las últimas 24 horas

| Campo | Valor |
|---|---|
| ID | 3fb3670f-3b32-4cbd-966c-cfab6b8a971e |
| Estado | todo |
| Prioridad | normal |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** Basarlo en actividad real, no solo en asistentes activos.

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Ampliar estadísticas de objetivos profesionales

| Campo | Valor |
|---|---|
| ID | 72acb3bd-de53-4396-b68d-2155cb1a76a2 |
| Estado | todo |
| Prioridad | normal |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** Oferta, demanda y conexiones entre sectores.

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Incorporar resultados de las encuestas al dashboard

| Campo | Valor |
|---|---|
| ID | 9a597af0-d333-47de-8923-e4e5b9760495 |
| Estado | done |
| Prioridad | normal |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** Mostrar información agregada y respetar la privacidad.

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Ampliar informes automáticos con métricas de impacto

| Campo | Valor |
|---|---|
| ID | 6c318f9b-9c28-4191-99bf-183a5aac5de0 |
| Estado | todo |
| Prioridad | normal |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** Aprovechar el generador de informes existente.

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Probar QR y analíticas con dos usuarios reales

| Campo | Valor |
|---|---|
| ID | ce6cc728-d4f3-4e8f-be07-0be0dd25a559 |
| Estado | review |
| Prioridad | normal |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | agent: Notis (eecefdf7-cd56-460c-99a0-ac4c382a1adc) |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** Verificar migraciones, Edge Functions, permisos y flujos completos.

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Código QR

| Campo | Valor |
|---|---|
| ID | 6dcaab8e-498b-4e57-8754-53f40d867659 |
| Estado | todo |
| Prioridad | none |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | sin asignar |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** —

**Subtareas:** 1 (0 hechas)

- El  QR de las redes sociales solo se genera cuando se crea un chat (`2426a4f1-e851-4d46-99f2-40d093cee947`), todo

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

### El  QR de las redes sociales solo se genera cuando se crea un chat

| Campo | Valor |
|---|---|
| ID | 2426a4f1-e851-4d46-99f2-40d093cee947 |
| Estado | todo |
| Prioridad | none |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | sin asignar |
| Tarea padre | 6dcaab8e-498b-4e57-8754-53f40d867659 (Código QR) |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** —

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna

## Quitar de crear evento publico o privado

| Campo | Valor |
|---|---|
| ID | 0128214e-bcf4-46aa-a878-71856ae60826 |
| Estado | todo |
| Prioridad | none |
| Autonomía | do_with_approval |
| Fecha límite | — |
| Hora límite | — |
| Recurrencia | — |
| Asignada a | sin asignar |
| Tarea padre | — |
| Etiquetas | — |
| Reclamada por | — |
| Lease | — |
| Veces reclamada | 0 |

**Descripción:** —

**Subtareas:** ninguna

**Comentarios:** ninguno

**Run abierto / logs:** ninguno

**Aprobaciones:** ninguna
