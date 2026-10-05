---
title: pasada-final-tags-enlaces-2026-10-05
type: changelog
tags:
  - documentacion
  - pkm
date_created: 2026-10-05
date_modified: 2026-10-05
---
# Pasada final de tags y enlaces internos (2026-10-05)

Revisión final tras [[_tag-migración-2026-10-05]] y [[_enlaces-moc-2026-10-05]]. Backup previo: `(eliminado; el registro queda solo en esta nota y en `_tag-migración-2026-10-05.md` / `_enlaces-moc-2026-10-05.md`)`.

## Tags (frontmatter)

- Tags únicos: **159 → 121**. Usos: **714 → 678**. Notas con tags modificados: **41**.
- **Eliminados (17)**, por ser genéricos, de formato o redundantes: `json`, `comandos`, `sintaxis`, `recursos`, `herramientas`, `empresas`, `definiciones`, `planificacion`, `migracion`, `troubleshooting`, `interfaz-web`, `terminal`, `crm`, `pdf`, `protocolo`, `audio`, `servidor`.
- **Fusionados (22)**:
  - `gguf` → `llama-cpp`
  - `modelos-ia` → `llm`
  - `gpu`, `pc`, `sistemas-embebidos` → `hardware`
  - `atajos` → `macos`
  - `embeddings` → `base-de-datos-vectorial`
  - `sql` → `bases-de-datos`
  - `agile` → `scrum`
  - `infografias` → `diseño`
  - `formacion` → `educacion`
  - `npm` → `nodejs`
  - `microservicios` → `backend`
  - `fraseologia` → `aviacion`
  - `cartografia`, `mapas` → `gis`
  - `chatgpt` → `openai`
  - `deuda-tecnica` → `desarrollo`
  - `landing` → `frontend`
  - `maquinas-proxmox` → `proxmox`
  - `operaciones` → `devops`
  - `topologia-de-red` → `red`
- **Mantenidos aunque tengan menos de 5 usos** (herramientas, tecnologías, proyectos, agentes o conceptos): p. ej. `arvis`, `atlas`, `mara`, `warren`, `ollama`, `qdrant`, `docker`, `tailscale`, `wireguard`, `pi-hole`, `linear`, `scrum`, `mcp`, `skills`, `claude-code`, `codex`, `make`, `builderbot`, `chatwoot`, `evolution-api`, `whatsapp`, `stable-diffusion`, `midjourney`, `postgresql`, `sqlite`, `react`, `angular`, `nextjs`, `spring-boot`, `java`, `python`, `leaflet`, `gis`, `aviacion`, `drones`, `meteorologia`, `rrhh`, `biavent`, `hackathon`, `indice`, `fine-tuning`, `evaluacion-ia`.
- Sin tocar (ambiguos): `origen`, `usuario`, `identidad`, `operativo`, `estado`, y también `proyecto-saas`.

## Enlaces internos

- **Eliminados (22):**
  - `[[MOC DevOps]]` en 8 notas hoja que ya cuelgan de su subíndice (`Index CheckMK`, `Index Wazuh`, `INDEX` de configuraciones).
  - Relaciones débiles: Landing Claude Code → LLM Prompts; LLM Prompts → MOC Custom GPTs; obsidian-segundo-cerebro → MOC OpenClaw; Docker → Evolution-API; builderbot e influencer-ia-n8n → n8n-api-endpoints; chatgpt-make-n8n → MOC Custom GPTs.
  - Duplicados de enlaces que ya estaban en el cuerpo de la nota.
  - Secciones «Relacionado» de `templates/` (Templater las copiaría a cada nota nueva).
- **Enlaces rotos reparados (11):** rutas antiguas «Inteligencia Artificial/…», «Agentes OpenClaw» → nota `agentes`, «04 - Red…» → «03 - Red…», «03 - Raspberry Pi 5 - MaraOS» → `mara-device`; «N8N» en títulos y el autoenlace «Evolution API» pasan a texto, y se corrige el markdown roto del enlace «N8N Assistant».
- **Añadidos (42), solo relaciones semánticas claras:**
  - Custom GPTs: Drones ↔ Fraseología Aérea, Facturas ↔ Ticket App, Infografías ↔ Creador Visual (prompt duplicado).
  - Configuración macOS: Ghostty, SKHD y Yabai.
  - Posts de LinkedIn agrupados por tema: Claude 4.5, GPT-5, chips/GPU, Perplexity/Comet y navegadores con IA, MCP, open source, asistentes de programación (Codex, Gemini Code Assist, Qwen3-Coder, Cursor), y Gemma 3n/GPT-OSS → [[MOC IA Local]].
- Todos los bloques «Relacionado» fuera de los MOCs tienen **6 enlaces como máximo**. Los MOCs se mantienen como nodos principales.
- Grafo: unos 637 → 664 enlaces únicos entre notas.

## Huérfanas restantes

- `Untitled.md`: vacía, 0 bytes. Conviene borrarla.
- `templates/nota-base 1.md`: plantilla duplicada de `nota-base`. Se deja sin enlaces a propósito.

## Formato

Registro y cambios documentados en Markdown dentro del vault. El backup `.tgz` externo se eliminó a petición: las notas deben vivir solo como `.md`.
