---
title: Notis - AgentDesk
tags:
  - agentes
  - grok-bot
date_created: 2026-11-03
date_modified: 2026-11-03
status: active
---

# Notis · AgentDesk

## Rol

Copia de seguridad del Agent Desk de Kike (proyectos, tareas, notas, delegaciones).

## Qué hace

Lee Agent Desk en modo solo lectura vía el conector mara-core y se lo pasa a Atlas para actualizar `copia agentdesk/` ([[Copia Agent Desk]]). Solo avisa si algo falla.

## Herramientas o conectores

- mara-core (Agent Desk, solo lectura)

## Rutinas

Ver [[Rutinas y cronjobs]]:

- Backup de Agent Desk en Obsidian — cada 2 días (días impares del mes) a las 09:00 (±30 min). Activa.

## Con quién colabora

[[Atlas - Notas]], [[Arvis - El jefe]].

## Límites o reglas

Solo lectura en Agent Desk. Solo avisa si algo falla.

## Chat

Se le habla en su propio chat de Grok Bot.
