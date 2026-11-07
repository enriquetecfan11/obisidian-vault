---
title: Reuniones QR asociadas a evento
tags:
  - agentdesk
  - copia-seguridad
  - biavent
agentdesk_id: 4f5b8241-7e49-497d-8a94-d8d16b44ce10
autor: Chati (agent, 46021daa-444b-49db-919c-9c3cb31c7a04)
proyecto: Biavent
creada_en_agentdesk: 2026-11-05 21:07 (Madrid)
actualizada_en_agentdesk: 2026-11-05 21:07 (Madrid)
date_created: 2026-11-07
date_modified: 2026-11-07
---

# Reuniones QR asociadas a evento

Copia de la nota de Agent Desk, leída el 07/11/2026 (copia programada de las 09:10, hora de Madrid). Índice: [[Copia Agent Desk]]. Proyecto: [[Tareas Biavent]].

## Estado (2026-11-05)

Preparada la mejora local del sistema de reuniones presenciales verificadas mediante QR.

- Nueva migración: `docs/migrations/add-event-meetups-qr.sql`.
- Añade `event_meetups` con `event_id`, conexión, ambos participantes, fecha, método y `verification_id`.
- Extiende verificaciones QR con `event_id`; tokens legacy con NULL siguen siendo consumibles con la lógica anterior.
- Unicidad por evento + pareja canónica: la misma pareja puede reunirse en eventos distintos, sin duplicar dentro del mismo evento.
- RPC atómica actualizada: valida que ambos estén inscritos, consume el token, inserta el encuentro y conserva las columnas legacy de `connections` como resumen.
- RLS de `event_meetups`: participantes, organizador del evento y platform admin; no permite acceso del organizador a otros eventos.
- Edge Functions locales actualizadas: `create-meeting-qr` admite `eventId`; los clientes legacy solo se resuelven automáticamente si comparten un único evento, y se rechaza la ambigüedad.
- `organizerMeetups.ts` consulta exclusivamente `event_meetups` filtrado por el evento.
- No se ejecutó ni desplegó ninguna migración o Edge Function.

Orden pendiente de autorización:
1. Aplicar `add-connection-meeting-qr.sql` si aún no existe.
2. Aplicar `add-event-meetups-qr.sql`.
3. Desplegar `create-meeting-qr` y `verify-meeting-qr`.
4. Verificar RLS y el flujo con dos eventos compartidos por la misma pareja.
