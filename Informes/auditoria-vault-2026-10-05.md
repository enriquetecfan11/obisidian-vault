---
title: "Auditoría del vault — 2026-10-05"
type: auditoria
tags:
  - pkm
  - documentacion
  - mantenimiento
project: none
date_created: 2026-10-05
date_modified: 2026-10-05
status: active
---
# Auditoría del vault - 2026-10-05

Estado tras el refactor `2040d7d`. 195 archivos `.md`, 186 notas con nombre único.

## 1. Enlaces rotos - 22 destinos, 43 apariciones

Casi todos vienen de un solo archivo: `OpenClaw/MOC OpenClaw.md`.

| Destino roto | Apariciones | Causa |
| --- | --- | --- |
| `openclaw/Documentacion Operativa/*` (agentes, identidad, migracion, configuracion, usuario, memoria, prompts, README, AGENTS-ARCHITECTURE) | 26 | ruta en minúscula `openclaw/` vs carpeta real `OpenClaw/` |
| `openclaw/Backup/*` (identidad, usuario, migracion, configuracion, README) | 9 | idem |
| `openclaw/Agents/*/system-prompt` (Mara, Atlas, Arvis, Warren) | 8 | idem |
| `inteligencia-artificial/Custom GPTS/Linkedin Agents/Thumbnail Builder` | 2 | la nota vive en `Custom GPTS/`, no en `Custom GPTS/Linkedin Agents/` |
| `[["$STATUS" != "running"]]` | 2 | falso positivo: es shell dentro de bloque de código en `Wazuh - Server API (operación)` |
| `Pasted image 20250117085739.png` | 1 | el archivo de imagen no está en el vault |

**Fix**: cambiar `openclaw/` por `OpenClaw/` en `MOC OpenClaw.md`. Obsidian resuelve por basename, pero respeta las mayúsculas en las rutas, así que el enlace queda roto aunque la nota exista.

## 2. Nombres duplicados - 7 basenames

Obsidian desambigua con `[[carpeta/nota]]`, pero cualquier enlace corto `[[configuracion]]` es ambiguo:

| Basename | Ocurrencias |
| --- | --- |
| `README.md` | `OpenClaw/Backup/`, `OpenClaw/Documentacion Operativa/` |
| `Thumbnail Builder.md` | `Custom GPTS/`, `Custom GPTS/Linkedin Agents/` |
| `configuracion.md`, `identidad.md`, `migracion.md`, `usuario.md` | `OpenClaw/Backup/`, `OpenClaw/Documentacion Operativa/` |
| `system-prompt.md` | `OpenClaw/Agents/{Arvis,Atlas,Mara,Warren}/` |

**Fix**: renombrar con prefijo de contexto: `Backup - configuracion.md`, `Arvis - system-prompt.md`, etc.

## 3. Tags inconsistentes - 25 grupos de variantes

El caso más grave: `ia` (107 notas) convive con `IA` (18). Lo mismo con acentos y mayúsculas.

| Canónico | Variantes |
| --- | --- |
| `ia` | IA |
| `automatizacion` | Automatización |
| `configuracion` | Configuración |
| `openclaw` | OpenClaw |
| `pkm` | PKM |
| `finanzas` | Finanzas |
| `llm` | LLM |
| `desarrollo` | Desarrollo |
| `openai` | OpenAI |
| `apple` | Apple |
| `google` | Google |
| `codex` | Codex |
| `ghostty` | Ghostty |
| `yabai` | Yabai |
| `networking` | Networking |
| `eventos` | Eventos |
| `startup` | Startup |
| `hackathon` | Hackathon |
| `perplexity` | Perplexity |
| `productividad` | Productividad |
| `biavent` | Biavent |
| `googleai` | GoogleAI |
| `agentesia` | AgentesIA |
| `innovacion` | Innovación, Innovacion |
| `tecnologia` | Tecnología, Tecnologia, tecnología |

Tags inline en el cuerpo: 85 distintos, 3 archivos. Se mezclan con los de frontmatter.

**Fix**: minúsculas sin acentos en todos los tags, y consolidar los inline al frontmatter.

## 4. Frontmatter incompleto - 10 notas

| Nota | Faltan |
| --- | --- |
| `notas-personales/infraestructura/01 - Dispositivos Apple.md` | title, type, project, date_created, date_modified |
| `notas-personales/infraestructura/02 - PCs.md` | ídem |
| `notas-personales/infraestructura/03 - Red, acceso remoto y pendientes.md` | ídem |
| `notas-personales/infraestructura/05 - Topología de red.md` | ídem |
| `inteligencia-artificial/Todo de IA - Comunidad.md` | project, date_created, date_modified |
| `inteligencia-artificial/_enlaces-moc-2026-10-05.md` | project |
| `inteligencia-artificial/_pasada-final-tags-enlaces-2026-10-05.md` | project |
| `inteligencia-artificial/_tag-migración-2026-10-05.md` | project |
| `OpenClaw/diario/analyze.md` | project |
| `redes-sociales/linkedin_posts_full_analytics.md` | project |

## 5. Claves de frontmatter redundantes

El vault mezcla dos esquemas de fechas y estado:

| Clave | Notas | Problema |
| --- | --- | --- |
| `date_created` / `date_modified` | 190 / 190 | esquema estándar, usar este |
| `created` | 56 | duplica `date_created` |
| `updated` | 122 | duplica `date_modified` |
| `status` | 182 | sin normalizar ni documentar |
| `source`, `linkedin_hashtags`, `pipeline`, `promotes_to` | 53 / 32 / 7 / — | específicas, mantener |

**Fix**: migrar `created` → `date_created`, `updated` → `date_modified`, y documentar los valores de `status`.

## 6. Huérfanas - 26 notas sin ningún enlace entrante

- 20 de `OpenClaw/` — consecuencia de los enlaces rotos del punto 1; se resuelven solos al arreglarlos
- `redes-sociales/linkedin_posts_full_analytics.md`
- `daily/2026-08-23.md`
- `Work/Empresas/Prompt Analizador Noticias.md`
- `programacion/Code/Guía Esencial de Spring Boot para Principiantes.md`
- `templates/nota-base 1.md`
- `inteligencia-artificial/_pasada-final-tags-enlaces-2026-10-05.md`

## 7. Ruido menor

- `templates/nota-base 1.md` es copia de `nota-base.md` con campos distintos. Archivar o borrar.
- Las notas de auditoría `_enlaces-moc-*`, `_pasada-final-*` y `_tag-migración-*` del 2026-10-05 son informes de una pasada puntual. Conviene moverlas a una carpeta `_auditorias/` o borrarlas cuando ya no sirvan.
- `[["$STATUS" != "running"]]` en `Wazuh - Server API (operación)` se leerá como enlace en el editor. Ponerlo como código inline.

## Orden de ejecución sugerido

1. Arreglar `OpenClaw/MOC OpenClaw.md` (22 enlaces, de golpe)
2. Consolidar los 25 grupos de tags a minúsculas sin acentos
3. Completar frontmatter de las 10 notas
4. Migrar `created`/`updated` a `date_created`/`date_modified`
5. Renombrar los 7 basenames duplicados
6. Limpiar notas de auditoría y `nota-base 1.md`
7. Re-enlazar las huérfanas que sobrevivan al punto 1