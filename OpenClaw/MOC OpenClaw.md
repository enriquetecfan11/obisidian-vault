---
title: MOC OpenClaw
type: moc
tags:
  - agentes-ia
  - documentacion
  - mara-os
  - openclaw
  - pkm
project: MaraOS
date_created: 2026-10-05
date_modified: 2026-10-05
status: active
---
# MOC OpenClaw

Mapa de la capa de agentes OpenClaw (Mara, Atlas, Arvis, Warren) y su documentación operativa.

> Distinto de [[Mara OS]]: OpenClaw es la capa de agentes; Mara OS es el software autoalojado (bot, UI, device).

## Documentación operativa (fuente de verdad)

- [[openclaw/Documentacion Operativa/README|Documentación Operativa — README]]
- [[openclaw/Documentacion Operativa/agentes|Agentes OpenClaw]] — roles, reparto y definición funcional
- [[openclaw/Documentacion Operativa/prompts|prompts]] — prompts base
- [[openclaw/Documentacion Operativa/configuracion|configuracion]] — rutas, MCPs, sync
- [[openclaw/Documentacion Operativa/identidad|identidad]]
- [[openclaw/Documentacion Operativa/usuario|usuario]]
- [[openclaw/Documentacion Operativa/memoria|memoria]]
- [[openclaw/Documentacion Operativa/migracion|migracion]]
- [[openclaw/Documentacion Operativa/AGENTS-ARCHITECTURE|AGENTS-ARCHITECTURE]] — espejo
- [[openclaw/Documentacion Operativa/IDENTITY|IDENTITY]] — espejo

## Agentes

### Mara (orquestadora)
- [[Mara]]
- [[openclaw/Agents/Mara/system-prompt|system-prompt (Mara)]]
- [[github-workflow-rule]]

### Atlas (organización)
- [[Atlas]]
- [[openclaw/Agents/Atlas/system-prompt|system-prompt (Atlas)]]

### Arvis (noticias / LinkedIn)
- [[Arvis]]
- [[flujo-ia-tech-news]]
- [[feeds-ia-tech-news]]
- [[openclaw/Agents/Arvis/system-prompt|system-prompt (Arvis)]]

### Warren (finanzas)
- [[Warren]]
- [[Analisis Empresas]]
- [[Crypto]]
- [[Empresas]]
- [[Template Analisis Diario]]
- [[Prompt Analizador Noticias]] — prompt para procesar lotes de noticias empresariales
- [[openclaw/Agents/Warren/system-prompt|system-prompt (Warren)]]

## Backup legacy

Carpeta histórica; la doc viva está en Documentación Operativa.

- [[openclaw/Backup/README|Backup — README]]
- [[openclaw/Backup/configuracion|Backup configuracion]]
- [[openclaw/Backup/identidad|Backup identidad]]
- [[openclaw/Backup/usuario|Backup usuario]]
- [[openclaw/Backup/migracion|Backup migracion]]

## Scripts

- [[analyze]] — script Python que automatiza frontmatter y tags de las notas

## Scrum / Linear

- [[MARA_SCRUM_v3]]
- [[MARA_SCRUM_PROMPT]]
- [[Documentación MCP Linear — ClawdBot]]

## Ver también

- [[Mara OS]]
- [[ejercito-empleados-digitales]]
- [[MOC Inteligencia Artificial]]
- [[MOC LinkedIn]]
