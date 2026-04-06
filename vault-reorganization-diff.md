---
title: vault-reorganization-diff
type: task
tags:
  - vault
  - reorganizacion
  - obsidian
  - diff
  - task
  - pending
  - active
status: active
created: 2026-04-06
updated: 2026-04-06
---

# Vault Reorganization Diff — 2026-04-06

---

## MOVED

```
moved: daily-workflow.md → Work/kanban-workflow.md
  ⚠️  Nota: contenido era tablero kanban (kanban-plugin:board), no workflow diario.
       Reasignado a Work/ en vez de diario/. Si quieres un daily-workflow.md real,
       créalo nuevo en diario/.

moved: Inteligencia Artificial/N8N API - Referencia Completa de Endpoints.md → N8N/n8n-api-endpoints.md
  → Temática N8N/automatización, no IA pura. Reubicado en N8N/.
```

---

## RENAMED

```
renamed: Code/Api.md                                                    → Code/npm-libs-api-postgres.md
renamed: Code/Markdown Template.md                                      → Code/markdown-template.md
renamed: Code/GIS y Programacion.md                                     → Code/gis-programacion-cartografia.md

renamed: Inteligencia Artificial/ChatGPT + MakeN8N .md                  → Inteligencia Artificial/chatgpt-make-n8n-integracion.md
renamed: Inteligencia Artificial/GPTS (Custom GPTS).md                  → Inteligencia Artificial/gpts-recursos-herramientas.md
renamed: Inteligencia Artificial/Enviorment - Evolution API.md           → Inteligencia Artificial/evolution-api-environment.md  (typo: Enviorment → Environment)
renamed: Inteligencia Artificial/"Ejército" de Empleados Digitales.md   → Inteligencia Artificial/ejercito-empleados-digitales.md
renamed: Inteligencia Artificial/Obsidian como segundo cerebro auto‑gestionado.md → Inteligencia Artificial/obsidian-segundo-cerebro.md
renamed: Inteligencia Artificial/N8N API - Referencia Completa de Endpoints.md    → N8N/n8n-api-endpoints.md  (también movido)

renamed: Inteligencia Artificial/Custom GPTS/Crear podscat con IA.md    → Inteligencia Artificial/Custom GPTS/crear-podcast-con-ia.md  (typo: podscat → podcast)
renamed: Inteligencia Artificial/Custom GPTS/Preguntas y repuestas.md   → Inteligencia Artificial/Custom GPTS/preguntas-y-respuestas.md  (typo: repuestas → respuestas)

renamed: N8N/BuilderBot - Enviar Whatsapp N8N.md                        → N8N/builderbot-whatsapp-n8n.md
renamed: N8N/ChatBot N8N.md                                             → N8N/chatbot-n8n-angular.md
renamed: N8N/Influencer AI + N8N.md                                     → N8N/influencer-ia-n8n.md

renamed: Work/Usuarios Chatwoot.md                                      → Work/chatwoot-activar-usuarios.md
renamed: Work/Renta Variable/Empresas a Ojear.md                        → Work/Renta Variable/empresas-a-vigilar.md

renamed: redes sociales/linkedin/Linkedin Ghostwritter.md               → redes sociales/linkedin/linkedin-ghostwriter-prompt.md  (typo: Ghostwritter → Ghostwriter)

renamed: Notas Personales/Guía Completa - Raspberry Pi Gateway con Tailscale WireGuard y Pi-hole.md
       → Notas Personales/raspberry-pi-tailscale-wireguard-pihole.md
```

---

## TAGGED (frontmatter corregido / añadido)

```
tagged: Code/markdown-cheat-sheet.md
  +#markdown +#cheatsheet +#sintaxis +#code +#documentacion
  fix: tags estaban como strings con # prefijo → convertidos a array YAML limpio

tagged: Work/Renta Variable/empresas-a-vigilar.md
  +#finanzas +#inversiones +#renta-variable +#bolsa +#empresas
  fix: tags mal formateados con # prefijo → corregidos

tagged: Work/kanban-workflow.md
  +#kanban +#workflow +#proyecto +#gestion
  fix: tipo corregido a "task"

tagged: Code/markdown-template.md
  fix: frontmatter doble/anidado → limpiado, frontmatter único válido
  +#markdown +#sintaxis +#code +#documentacion +#plantilla

tagged: Inteligencia Artificial/obsidian-segundo-cerebro.md
  frontmatter añadido (no tenía ninguno)
  type: ia  +#obsidian +#segundo-cerebro +#ia +#productividad +#pkm

tagged: redes sociales/linkedin/linkedin-ghostwriter-prompt.md
  frontmatter añadido (no tenía ninguno)
  type: social  +#linkedin +#ghostwriter +#prompt +#redes-sociales +#contenido
```

---

## LINKED (wikilinks añadidos)

```
linked: Code/npm-libs-api-postgres.md          → [[Bases de Datos]]
linked: Code/Comandos de Qdrant Database.md    → [[QDrant]]
linked: Inteligencia Artificial/chatgpt-make-n8n-integracion.md → [[N8N]]
linked: Inteligencia Artificial/Ollama Docker.md → [[N8N]], [[Docker]]
linked: Work/chatwoot-activar-usuarios.md      → [[Docker]]
```

---

## FLAGGED (posibles duplicados — revisar y hacer merge)

```
flagged: Code/QDrant.md
  → DUPLICADO PARCIAL de Code/Comandos de Qdrant Database.md
  → QDrant.md (1.4 KB) es subconjunto de Comandos (3.8 KB)
  → Acción recomendada: merge QDrant.md → Comandos de Qdrant Database.md, eliminar QDrant.md

flagged: Inteligencia Artificial/Custom GPTS/LLM as Judge.md
  → DUPLICADO SEMÁNTICO de Custom GPTS/LM Como Juez.md
  → Mismo contenido, una en inglés y otra en español
  → Acción recomendada: mantener LM Como Juez.md, redirigir LLM as Judge.md con alias o eliminar

flagged: redes sociales/linkedin/linkedin-ghostwriter-prompt.md
  → DUPLICADO de Inteligencia Artificial/Custom GPTS/Linkedin Agents/Linkedin Ghostwriter.md
  → Mismo prompt de ghostwriter de LinkedIn
  → Acción recomendada: mantener la versión en Custom GPTS/ como canónica; en redes sociales/ poner wikilink

flagged: Inteligencia Artificial/evolution-api-environment.md
  → DUPLICADO PARCIAL de Inteligencia Artificial/Evolution API.md
  → Ambas cubren configuración de Evolution API + Docker
  → Acción recomendada: merge en Evolution API.md, eliminar evolution-api-environment.md
```

---

## NOTAS ADICIONALES

```
note: Vault.md y "Untitled Kanban.md" no encontrados en raíz — probablemente ya movidos o no creados.
      El archivo daily-workflow.md era en realidad un tablero kanban-plugin:board.

note: diario/ existe dentro de MaraOs/diario/ pero NO como carpeta raíz.
      Si quieres diario/ en raíz para journaling personal, créala manualmente.

note: templates/nota-base.md existe como plantilla base. Todos los archivos nuevos
      deberían seguir ese template.

note: MaraOs/ y todo su contenido interno (Arvis, Atlas, Mara, Warren, SystemFiles)
      NO fueron modificados — respetando la regla "No romper estructura MaraOs/".
```

---

## RESUMEN EJECUTIVO

| Acción     | Cantidad |
|------------|----------|
| moved      | 2        |
| renamed    | 19       |
| tagged/fm  | 6        |
| linked     | 5        |
| flagged    | 4 duplicados |
