---
title: hermes-estado-de-proyectos
type: "document"
tags:
  - resumen
  - hermes
  - proyecto
  - inteligencia-artificial
project: "none"
status: "activo"
date_created: "2026-08-11"
date_modified: "2026-08-11"
---

# Hermes — Estado de Proyectos (Resumen del Vault Obsidian)

> **Fecha de análisis:** 11 de agosto de 2026
> **Fuente:** Vault de Obsidian (`C:\Users\erodriguez\Documents\obisidian-vault`)
> **Nota:** Este resumen fue generado automáticamente por Hermes. No modificar ni eliminar las notas originales.

---

## 1. ¿Qué estás construyendo?

### Proyecto principal: **MaraOS + OpenClaw**
Un sistema de agentes de IA personal basado en **OpenClaw** (plataforma de agentes en Linux), documentado y gestionado desde Obsidian. Es un "segundo cerebro" digital que orquesta múltiples agentes especializados.

### Proyectos secundarios documentados:
- **N8N Automation** — Automatizaciones con N8N (workflows de chatbots, integraciones WhatsApp, chatbots Angular)
- **Raspberry Pi Gateway** — Servidor Raspberry Pi con Tailscale, WireGuard y Pi-hole
- **CAI Framework** — Inteligencia artificial para auditoría web de seguridad (ciberseguridad)
- **Chatbot N8N + Angular** — Frontend de chatbot con integración Webhook
- **BuilderBot WhatsApp** — API para envío de mensajes multimedia
- **Linux Agents (OpenClaw)** — Infraestructura de agentes en Linux con Node.js v22.22.1

---

## 2. Componentes existentes

### MaraOS (Estructura del sistema)

| Componente | Descripción |
|---|---|
| **Mara** | Agente principal y orquestador. Triage, delegación, validación final. |
| **Atlas** | Calendario, tareas, notas, estructura diaria, resúmenes. |
| **Arvis** | Creatividad, comunicación, storytelling, LinkedIn, contenido. |
| **Warren** | Análisis financiero: mercados, crypto, valuations, señales. |
| **Documentación Operativa** | Carpeta canónica: `MaraOs/Documentacion Operativa/` con 7 archivos |
| **Backup** | Copias de seguridad: configuración, identidad, usuario, migración |
| **Git** | Versionado del vault: `https://github.com/enriquetecfan11/obisidian-vault.git` |
| **MCPs** | Calendario, Tareas/Notas, Linear (vía N8N self-hosted) |
| **Telegram** | Canal de chat directo con Mara |

### N8N Automation
- **influencer-ia-n8n.md** — Workflow de influencer con IA
- **chatbot-n8n-angular.md** — Chatbot con frontend Angular
- **builderbot-whatsapp-n8n.md** — API BuilderBot para WhatsApp (API key configurada)
- **n8n-api-endpoints.md** — Documentación completa de la API de N8N (v1)

### Raspberry Pi Gateway
- Tailscale para red privada
- WireGuard para VPN
- Pi-hole para DNS y bloqueo de publicidad
- Guía completa documentada (14,472 chars)

### CAI Framework
- Instalación con Python 3.12
- Modelo: Qwen3:latest (vía Ollama)
- Uso: Auditoría web de seguridad (Kali Linux + herramientas pentest)

---

## 3. Tecnologías utilizadas

| Categoría | Tecnología |
|---|---|
| **Agentes** | OpenClaw (plataforma), Node.js v22.22.1 |
| **LLMs locales** | Ollama (Docker), Qwen3:latest, Qwen2.5 72B/14B |
| **Cerebro** | Obsidian (vault local, Git-synced) |
| **Automatización** | N8N (self-hosted), cronjobs |
| **Comunicación** | Telegram, BuilderBot (WhatsApp API) |
| **Red** | Tailscale, WireGuard, Pi-hole |
| **Infraestructura** | Raspberry Pi, Docker, Linux (Ubuntu) |
| **Git** | GitHub (remote del vault) |
| **Desarrollo** | Python 3.12, Angular (frontend), cURL, bash |
| **Seguridad** | CAI Framework, auditoría web |
| **Análisis** | Warren (mercados, crypto, valuations) |

---

## 4. Decisiones importantes tomadas

1. **Mara es el punto de entrada único.** Todo lo multi-dominio o ambiguo pasa por Mara antes de delegar a especialistas.

2. **Obsidian como fuente persistente de verdad.** El vault es el "segundo cerebro" donde todo se documenta antes de ejecutarse.

3. **Documentar primero, sincronizar después.** Flujo: escribir en vault → versionar con Git → sincronizar.

4. **MCPs centralizados en N8N.** Los MCPs de calendario, tareas y Linear están en un N8N self-hosted (no directamente en OpenClaw).

5. **Cronjobs programados en hora europea (Europe/Madrid).** Automatizaciones: Atlas 07:00, Diario Obsidian 00:05, Changelog 20:00, Resumen semanal domingo 20:00, Warren 09-21/22:30, Ubuntu Ops 08:30/14:30/20:30.

6. **Privacidad y seguridad como prioridad.** No actuar externamente sin confirmación en acciones sensibles. No publicar en nombre del usuario sin permiso.

7. **No inventar estado.** Los agentes deben declarar incertidumbre en lugar de fingir certeza.

---

## 5. Pendientes detectados

| # | Pendiente | Fuente |
|---|---|---|
| 1 | Migrar Mara a otra máquina (checklist incompleto, versiones "No especificado") | `MaraOs/Backup/migracion.md` |
| 2 | Actualizar ruta de usuario: `enriquetecfan` → `erodriguez` (Windows) | `MaraOs/Documentacion Operativa/usuario.md` |
| 3 | Cambios en MCPs — lista marcada "A actualizar" | `MaraOs/Documentacion Operativa/memoria.md` |
| 4 | Actualizar ruta del vault en migración: `/home/enriquetecfan/Documents/` → `C:\Users\erodriguez\Documents\` | `MaraOs/Backup/migracion.md` |
| 5 | Rutas, MCPs, agentes o prompts — pendientes de actualización | `MaraOs/Documentacion Operativa/memoria.md` |

---

## 6. Posibles contradicciones y desactualizaciones

### 🔴 Contradicción detectada
- **Usuario en migración:** `enriquetecfan` (Linux) vs `erodriguez` (Windows actual)
  - El archivo `MaraOs/Documentacion Operativa/usuario.md` está en inglés con nombre "Kike"
  - El archivo `MaraOs/Backup/usuario.md` tiene `username: erodriguez`
  - Las rutas en `migracion.md` usan `/home/enriquetecfan/` pero el sistema actual es Windows con `C:\Users\erodriguez\`
  - **Conclusión:** El usuario migró de Linux a Windows sin actualizar las rutas en los archivos de migración.

### 🟡 Posibles desactualizaciones
- **Tono de los documentos:** Los archivos de `Documentacion Operativa/` están en inglés, mientras que las notas personales y de IA están en español. El usuario parece bilingüe.
- **Plataforma:** El sistema operativo de los archivos de migración es Linux (Ubuntu Desktop, `/home/`), pero el sistema actual es Windows. Los cronjobs y MCPs probablemente ya no son accesibles desde esta máquina.
- **N8N endpoints:** Los MCPs apuntan a `core-n8n.832gky.easypanel.host` — no hay nota de si este N8N sigue activo o migrado.

### 🟢 Observaciones positivas
- Estructura muy limpia y bien organizada con README, README.md espejo, y reglas de uso claras.
- Git versionado del vault con remote en GitHub.
- Separación clara entre agentes (papeles definidos) y orquestación.
- Guardrails bien definidos para cada agente.

---

## 7. Próximos pasos propuestos (basados en el vault)

1. **Sincronizar el vault a Git en la nueva máquina (Windows).** El remote es `https://github.com/enriquetecfan11/obisidian-vault.git`. Actualizar las rutas de migración de `enriquetecfan` a `erodriguez` y de `/home/` a `C:\Users\`.

2. **Actualizar las rutas en `MaraOs/Documentacion Operativa/usuario.md` y `configuracion.md`** para reflejar el entorno Windows actual. El usuario está en `C:\Users\erodriguez\`.

3. **Verificar el estado del N8N self-hosted** (`core-n8n.832gky.easypanel.host`) — si sigue activo, los MCPs de calendario, tareas y Linear deberían seguir funcionando. Si no, migrar los MCPs a una nueva instancia.

4. **Documentar el entorno actual de Windows** en `MaraOs/Documentacion Operativa/configuracion.md` — agregar rutas de Windows, ruta del vault actual, y estado de los cronjobs (si se han reconfigurado en Windows).

5. **Revisar si los cronjobs de OpenClaw se han migrado** — el checklist de migración lista cronjobs específicos (Atlas 07:00, Diario 00:05, etc.) que deben existir en la nueva máquina. Verificar su estado.

---

## Notas consultadas (lista completa)

### MaraOS
- `MaraOs/Agents/Mara/Mara.md`
- `MaraOs/Agents/Mara/system-prompt.md`
- `MaraOs/Agents/Atlas/Atlas.md`
- `MaraOs/Agents/Atlas/system-prompt.md`
- `MaraOs/Agents/Warren/Warren.md`
- `MaraOs/Agents/Warren/system-prompt.md`
- `MaraOs/Agents/Arvis/Arvis.md`
- `MaraOs/Agents/Arvis/system-prompt.md`
- `MaraOs/Documentacion Operativa/README.md`
- `MaraOs/Documentacion Operativa/AGENTS-ARCHITECTURE.md`
- `MaraOs/Documentacion Operativa/IDENTITY.md`
- `MaraOs/Documentacion Operativa/agentes.md`
- `MaraOs/Documentacion Operativa/configuracion.md`
- `MaraOs/Documentacion Operativa/identidad.md`
- `MaraOs/Documentacion Operativa/memoria.md`
- `MaraOs/Documentacion Operativa/prompts.md`
- `MaraOs/Backup/configuracion.md`
- `MaraOs/Backup/identidad.md`
- `MaraOs/Backup/usuario.md`
- `MaraOs/Backup/migracion.md`

### Inteligencia Artificial
- `Inteligencia Artificial/Ollama Docker.md`
- `Inteligencia Artificial/obsidian-segundo-cerebro.md`
- `Inteligencia Artificial/Scrum/MARA_SCRUM_v3.md`
- `Inteligencia Artificial/Scrum/MARA_SCRUM_PROMPT.md`
- `Inteligencia Artificial/CAI Framework - Inteligencia Artificial Seguridad.md`

### N8N
- `N8N/influencer-ia-n8n.md`
- `N8N/chatbot-n8n-angular.md`
- `N8N/builderbot-whatsapp-n8n.md`
- `N8N/n8n-api-endpoints.md`

### Notas Personales
- `Notas Personales/Guía Completa - Raspberry Pi Gateway con Tailscale, WireGuard y Pi-hole.md`
