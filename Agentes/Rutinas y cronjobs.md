---
title: Rutinas y cronjobs
tags:
  - automatizacion
  - agentes
  - rutinas
  - infraestructura
date_created: 2026-11-03
date_modified: 2026-11-03
status: active
---

# Rutinas y cronjobs

Índice general de las rutinas programadas de todos los agentes y de los cronjobs conocidos. Se mantiene actualizado en esta nota; no se crean notas nuevas con fecha. Última actualización: 04/11/2026. Lo recopiló Arvis a petición de Kike. Todos los horarios están en hora de Madrid.

## Timeline

### Diario
- **03:00** — Scribe · Sincronizar vault a Hindsight
- **07:30** — Nexo · Resumen de noticias
- **09:00** — Notis · Backup Agent Desk (días impares)
- **09:00** — Booki · bookmark-digest (mar y vie, en pausa)
- **09:02** — Dixi · Resumen diario de agenda
- **09:02** — Darío · Resumen diario de agenda
- **09:00 · 14:00 · 17:00 · 21:00** — Nexo · Resumen de noticias
- **15:15 / 22:15** — Warren · Mercados (entre semana)
- **19:00** — Dixi · Recordatorio Supabase Biavent (jueves)
- **19:00** — Dixi · Recordatorio Stripe Nundu (días 1 y 15)
- **19:00** — Darío · Recordatorios Supabase y Stripe
- **12:00** — Warren · Cripto Bitcoin y Ethereum (sáb y dom)
- **23:00** — Scribe · Actualizar Obsidian Vault

## Grok Bot

Índice de agentes: [[Grok Bot]].

### Nexo · Noticias — [[Nexo - Noticias]]

| Nombre | Horario | Qué hace | Estado | Última actualización |
|---|---|---|---|---|
| Resumen de noticias (7:30 h) | Todos los días, 07:30 | Resumen matinal de IA (prioridad) y tecnología, incluidos desarrollo de software y automatización. Solo novedades, como máximo 3 por sección, con titular, «por qué importa» y fuente. Si no hay nada, no envía. | Activa | 03/11/2026 |
| Resumen de noticias (9, 14, 17 y 21 h) | Todos los días, 09:00, 14:00, 17:00 y 21:00 | Mismos temas y reglas, sin repetir noticias; las actualizaciones van marcadas con 🔄. La de las 21:00 añade «Lo más destacado de hoy» (hasta 5). | Activa | 03/11/2026 |

Las dos comparten el historial `/workspace/nexo/news-history.md`.

### Darío · Mi diario personal — [[Darío - Diario personal]]

| Nombre | Horario | Qué hace | Estado | Última actualización |
|---|---|---|---|---|
| Resumen diario de agenda | Todos los días, 09:02 | Resumen de la agenda del día. | Activa | 03/11/2026 |
| Recordatorio: Revisar Supabase Biavent | Jueves, 19:00 | Recordatorio para revisar Supabase de Biavent. | Activa | 03/11/2026 |
| Recordatorio: Revisar Stripe Nundu | Días 1 y 15 de cada mes, hacia las 19:00 (±15 min) | Recordatorio para revisar Stripe de Nundu. | Activa | 03/11/2026 |

### Warren · Inversor en valor — [[Warren - Inversor en valor]]

| Nombre | Horario | Qué hace | Estado | Última actualización |
|---|---|---|---|---|
| Mercados: 7 Magníficas + cripto + Brent (entre semana) | De lunes a viernes, hacia las 15:15 y las 22:15 (±10 min) | Precio, % del día y % en el año de AAPL, MSFT, GOOGL, AMZN, NVDA, META, TSLA, BTC, ETH y Brent, con un comentario al estilo Buffett. | Activa | 03/11/2026 |
| Cripto fin de semana: Bitcoin y Ethereum | Sábados y domingos, hacia las 12:00 (±15 min) | Precio y % en 24 h, 7 días y en el año. | Activa (todavía no se ha ejecutado) | 03/11/2026 |

### Notis · AgentDesk — [[Notis - AgentDesk]]

| Nombre | Horario | Qué hace | Estado | Última actualización |
|---|---|---|---|---|
| Backup de Agent Desk en Obsidian | Cada 2 días (días impares del mes), 09:00 (±30 min) | Lee Agent Desk en modo solo lectura a través de mara-core y se lo pasa a Atlas para actualizar [[Copia Agent Desk]]. Solo avisa si falla. | Activa (última ejecución: 03/11, 09:04, correcta) | 03/11/2026 |

### Booki — [[Booki - Bookmarks de X]]

| Nombre | Horario | Qué hace | Estado | Última actualización |
|---|---|---|---|---|
| bookmark-digest | Martes y viernes, hacia las 09:00 (±15 min) | Lee los bookmarks de X y sus carpetas, guarda el estado, manda un resumen priorizado por IA, growth y producto, y le pasa a Atlas los nuevos para [[Bookmarks de X]]. | **En pausa** (nunca se ha ejecutado; espera la confirmación de Kike) | 03/11/2026 |

### Agentes sin rutinas

- [[Arvis - El jefe]]: ninguna.
- [[Atlas - Notas]]: ninguna. Trabaja bajo demanda.
- [[Pixel - Experto en Redes]]: ninguna fija. Crea programaciones de una sola vez y las borra al publicar.

## MaraOS

- [[Mara OS]] — software MaraOS
- [[INFRA]] — mapa de la infraestructura del homelab

| Nombre | Dónde | Horario | Qué hace | Estado | Última actualización |
|---|---|---|---|---|---|
| Sincronizar vault Obsidian → Hindsight (`sync_vault.sh`) | Homelab (`mara-core`), mantenido por Orion | **Pendiente de confirmar con Orion:** diario a las 03:00 (`0 3 * * *`, cron de usuario, según [[INFRA]]); o cron en Hermes a las 23:00 (según la tarea de Agent Desk) | `git pull` del vault, sube las notas nuevas o modificadas al banco `obsidian` de Hindsight, borra las eliminadas y verifica con `hindsight_recall.sh`. | Activo según INFRA; horario sin confirmar | 03/11/2026 |

## HermesAgent

Índice: [[HermesAgent]].

No hay rutinas conocidas.

## OpenBot

Índice: [[OpenBot]].

### Scribe · Notas — [[Scribe - Notas]]

| Nombre | Horario | Qué hace | Estado | Última actualización |
|---|---|---|---|---|
| Actualizar Obsidian Vault | Diario, 23:00 | `git pull` en `/Users/enriquetecfan/Documents/obisidian-vault`, resuelve conflictos conservando ambas versiones, reporta commit/archivos/error. | Activa | 03/11/2026 |
| Sincronizar vault → Hindsight | Diario, 03:00 | Sincroniza el vault con Hindsight vía `sync_vault.sh` (homelab). | Activa | 03/11/2026 |

### Dixi · Mi diario personal — [[Dixi - Diario personal]]

| Nombre | Horario | Qué hace | Estado | Última actualización |
|---|---|---|---|---|
| Resumen diario de agenda | Diario, 09:02 | Consulta el calendario vía `openbot_browser` y resume eventos de hoy. | Activa | 03/11/2026 |
| Recordatorio: Revisar Supabase Biavent | Jueves, 19:00 | Recordatorio para revisar Supabase de Biavent. | Activa | 03/11/2026 |
| Recordatorio: Revisar Stripe Nundu | Días 1 y 15, 19:00 | Recordatorio para revisar Stripe de Nundu. | Activa | 03/11/2026 |

### Agentes sin rutinas

- [[Altair - El jefe]]: ninguna propia.

## Relacionado

- [[Grok Bot]]
- [[INFRA]]
- [[INFRA - Mapa de la infraestructura]]
- [[Mara OS]]
- [[HermesAgent]]
- [[OpenBot]]
- [[Copia Agent Desk]]
- [[MOC Automatizaciones]]
- [[Calendario de rutinas]]
