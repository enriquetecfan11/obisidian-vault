---
title: Calendario de rutinas
tags:
  - automatizacion
  - rutinas
  - calendario
date_created: 2026-11-03
date_modified: 2026-11-03
status: active
---

# Calendario de rutinas

Vista rápida en formato calendario de las rutinas y cronjobs conocidos. Horarios en hora de Madrid.

## OpenBot

| Día | Hora | Agente · Rutina | Qué hace | Estado |
|---|---|---|---|---|
| Todos los días | 03:00 | Scribe · Sincronizar vault → Hindsight | `git pull` + `sync_vault.sh` (homelab) → Hindsight. | Activa |
| Todos los días | 09:02 | Dixi · Resumen diario de agenda | Consulta el calendario vía `openbot_browser` y resume eventos de hoy. | Activa |
| Todos los días | 23:00 | Scribe · Actualizar Obsidian Vault | `git pull` + resolver conflictos + reportar commit/archivos/error. | Activa |
| Jueves | 19:00 | Dixi · Recordatorio: Revisar Supabase Biavent | Avisa que debe revisar Supabase de Biavent. | Activa |
| Días 1 y 15 | 19:00 | Dixi · Recordatorio: Revisar Stripe Nundu | Avisa que debe revisar Stripe de Nundu. | Activa |

## Grok Bot

| Día | Hora | Agente · Rutina | Qué hace | Estado |
|---|---|---|---|---|
| Diario | 07:30 | Nexo · Resumen de noticias (7:30 h) | Resumen matinal de IA y tecnología. | Activa |
| Diario | 09:00, 14:00, 17:00 y 21:00 | Nexo · Resumen de noticias (más) | Mismos temas; la de 21:00 añade «Lo más destacado de hoy». | Activa |
| Diario | 09:02 | Darío · Resumen diario de agenda | Resumen de la agenda del día. | Activa |
| Jueves | 19:00 | Darío · Recordatorio: Revisar Supabase Biavent | Recordatorio. | Activa |
| Días 1 y 15 | 19:00 | Darío · Recordatorio: Revisar Stripe Nundu | Recordatorio. | Activa |
| Entre semana | 15:15 y 22:15 | Warren · Mercados | Precios y comentario al estilo Buffett. | Activa |
| Sábado y domingo | 12:00 | Warren · Cripto fin de semana | Bitcoin y Ethereum. | Activa |

## Próximo vistazo rápido

- **Hoy/ahora:** Scribe sincroniza vault (03:00) y Dixi resume agenda (09:02).
- **Próxima ventana activa:** hoy a las 23:00 Scribe actualiza el vault.

## Relacionado

- [[Rutinas y cronjobs]]
- [[OpenBot]]
- [[Grok Bot]]
