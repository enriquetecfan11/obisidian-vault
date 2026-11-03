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

Índice general de las rutinas programadas de todos los agentes y de los cronjobs conocidos. Se mantiene actualizado en esta nota; no se crean notas nuevas con fecha. Última actualización: 03/11/2026. Lo recopiló Arvis a petición de Kike. Todos los horarios están en hora de Madrid.

## Sistemas

- [[Grok Bot]] — agentes de Grok Bot (Arvis, Nexo, Pixel, Atlas, Darío, Warren, Notis, Booki)
- [[Mara OS]] / [[INFRA]] — MaraOS en el homelab
- [[HermesAgent]] — Hermes en el homelab
- [[OpenBot]] — sin notas todavía

## Nexo · Noticias

| Nombre | Horario | Qué hace | Estado |
|---|---|---|---|
| Resumen de noticias (7:30 h) | Todos los días, 07:30 | Resumen matinal de IA (prioridad) y tecnología, incluidos desarrollo de software y automatización. Solo novedades, como máximo 3 por sección, con titular, «por qué importa» y fuente. Si no hay nada, no envía. | Activa |
| Resumen de noticias (9, 14, 17 y 21 h) | Todos los días, 09:00, 14:00, 17:00 y 21:00 | Mismos temas y reglas, sin repetir noticias; las actualizaciones van marcadas con 🔄. La de las 21:00 añade «Lo más destacado de hoy» (hasta 5). | Activa |

Las dos comparten el historial `/workspace/nexo/news-history.md`.

Agente: [[Nexo - Noticias]]

## Darío · Diario personal

| Nombre | Horario | Qué hace | Estado |
|---|---|---|---|
| Resumen diario de agenda | Todos los días, 09:02 | Resumen de la agenda del día. | Activa |
| Recordatorio: Revisar Supabase Biavent | Jueves, 19:00 | Recordatorio para revisar Supabase de Biavent. | Activa |
| Recordatorio: Revisar Stripe Nundu | Días 1 y 15 de cada mes, hacia las 19:00 (±15 min) | Recordatorio para revisar Stripe de Nundu. | Activa |

Agente: [[Darío - Diario personal]]

## Warren · Inversor en valor

| Nombre | Horario | Qué hace | Estado |
|---|---|---|---|
| Mercados: 7 Magníficas + cripto + Brent (entre semana) | De lunes a viernes, hacia las 15:15 y las 22:15 (±10 min) | Precio, % del día y % en el año de AAPL, MSFT, GOOGL, AMZN, NVDA, META, TSLA, BTC, ETH y Brent, con un comentario al estilo Buffett. | Activa |
| Cripto fin de semana: Bitcoin y Ethereum | Sábados y domingos, hacia las 12:00 (±15 min) | Precio y % en 24 h, 7 días y en el año. | Activa (todavía no se ha ejecutado) |

Agente: [[Warren - Inversor en valor]]

## Notis · AgentDesk

| Nombre | Horario | Qué hace | Estado |
|---|---|---|---|
| Backup de Agent Desk en Obsidian | Cada 2 días (días impares del mes), 09:00 (±30 min) | Lee Agent Desk en modo solo lectura a través de mara-core y se lo pasa a Atlas para actualizar [[Copia Agent Desk]]. Solo avisa si falla. | Activa (última ejecución: 03/11, 09:04, correcta) |

Agente: [[Notis - AgentDesk]]

## Booki

| Nombre | Horario | Qué hace | Estado |
|---|---|---|---|
| bookmark-digest | Martes y viernes, hacia las 09:00 (±15 min) | Lee los bookmarks de X y sus carpetas, guarda el estado, manda un resumen priorizado por IA, growth y producto, y le pasa a Atlas los nuevos para [[Bookmarks de X]]. | **En pausa** (nunca se ha ejecutado; espera la confirmación de Kike) |

Agente: [[Booki - Bookmarks de X]]

## Agentes sin rutinas

- [[Arvis - El jefe]]: ninguna.
- [[Atlas - Notas]]: ninguna. Trabaja bajo demanda, cuando se lo piden Kike, Booki, Notis o Pixel.
- [[Pixel - Experto en Redes]]: ninguna. Borró las rutinas de una sola vez de los posts del 27/10 y del 29/10.

## Cronjobs fuera de los agentes

| Nombre | Dónde | Horario | Qué hace | Estado |
|---|---|---|---|---|
| Sincronizar vault Obsidian → Hindsight (`sync_vault.sh`) | Homelab (`mara-core`), mantenido por Orion | **Pendiente de confirmar con Orion:** la nota [[INFRA]] dice que es diario a las 03:00 (`0 3 * * *`, cron de usuario); la tarea de Agent Desk habla de un cron en Hermes a las 23:00 | `git pull` del vault, sube las notas nuevas o modificadas al banco `obsidian` de Hindsight, borra las eliminadas y verifica con `hindsight_recall.sh`. | Activo según INFRA; horario sin confirmar |

## Relacionado

- [[Grok Bot]]
- [[INFRA]]
- [[INFRA - Mapa de la infraestructura]]
- [[Mara OS]]
- [[HermesAgent]]
- [[OpenBot]]
- [[Copia Agent Desk]]
- [[MOC Automatizaciones]]
