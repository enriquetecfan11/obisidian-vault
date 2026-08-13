---
title: MCP y skills
type: document
tags:
  - mara-os
  - mcp
  - skills
project: MaraOS
status: active
date_created: 2026-08-13
date_modified: 2026-08-13
---
# MCP y skills

Dos mecanismos distintos que se complementan:

- **MCP** aporta las **capacidades reales** (las tools que el modelo puede ejecutar).
- **Skills** aportan **instrucciones en lenguaje natural** sobre cuándo y cómo usarlas.

Los skills **no filtran** el esquema de tools que se envía al modelo: solo inyectan texto en el prompt.

## Servidores MCP

Definidos en `mara-os/mcp.json`:

```json
{
  "servers": [
    { "name": "engram", "type": "stdio",
      "command": "/Users/enriquetecfan/.local/bin/uv",
      "args": ["--directory", "/Users/enriquetecfan/Engram", "run", "engram-server"] },
    { "name": "macos_automator", "type": "stdio",
      "command": "/opt/homebrew/bin/npx",
      "args": ["-y", "--package", "@steipete/macos-automator-mcp", "macos-automator-mcp"] },
    { "name": "calendar", "type": "http",
      "url": "https://core-n8n.832gky.easypanel.host/mcp/calendar" },
    { "name": "notes", "type": "http",
      "url": "https://core-n8n.832gky.easypanel.host/mcp/agents-notes" }
  ]
}
```

| Servidor | Tipo | Qué aporta |
|---|---|---|
| `engram` | stdio (Python, `uv`) | Memoria persistente. Backend alternativo a SQLite |
| `macos_automator` | stdio (npx) | Ejecución de AppleScript/JXA en el Mac |
| `calendar` | HTTP (n8n) | Google Calendar |
| `notes` | HTTP (n8n) | Notas y tareas |

Los dos primeros son locales; los dos de n8n son remotos y dependen de que el VPS esté arriba.

## Registro y despacho

`initMcpClients()` en `src/mcp.ts`:

1. Lee `mcp.json` desde `process.cwd()`.
2. Conecta **todos los servidores en paralelo** con `Promise.allSettled`, con un timeout de **15 s por servidor**. Si uno falla, el bot arranca igual.
3. Transporte según el tipo: `StdioClientTransport` o `StreamableHTTPClientTransport`. Si se omite `type`, se asume `http`.
4. Por cada tool devuelta por `client.listTools()`: la mapea en `toolToClientMap` y la añade a `ollamaTools` con formato compatible con OpenAI:

```ts
{ type: "function",
  function: { name, description, parameters: tool.inputSchema } }
```

5. Marca `hasMemoryServer` si el nombre está en `memoryServerNames = new Set(["engram"])`.

`callMcpTool(name, args)` busca el cliente en el mapa, invoca la tool y concatena las partes de texto de la respuesta.

**Curiosidad:** las descripciones se limpian con regex antes de enviarlas al modelo, quitando `" on Google Calendar"`, `" in Google Calendar"`, `" on my calendar"` y `" of Kike"`.

**No hay tools locales.** Todas las capacidades del agente vienen de servidores MCP en tiempo de ejecución; no hay ninguna tool codificada en `src/`.

> La tool `update_memory` aparece documentada en `CLAUDE.md` y en `docs/` como fallback cuando Engram no está disponible. **No existe en el código** — fue sustituida por el backend SQLite de [[Memoria y contexto]].

## Tools que los ficheros de contexto dan por existentes

Estos nombres salen de `config/AGENTS.md` y de los skills, **no del código**. Su existencia real depende de lo que exponga cada servidor en tiempo de ejecución.

| Dominio | Tools |
|---|---|
| Calendario | `Get_all_Events`, `Create_an_event`, `Reschedule_Event`, `Delete_Calendar_Event`, `Check_Availability`, `Date_Time1` |
| Notas / tareas | `Create_a_Task`, `Get_a_Task`, `Get_many_Tasks`, `Delete_a_Task`, `Complete_a_Task` |
| macOS | `execute_script`, `get_scripting_tips` |
| Engram | `remember`, `recall`, `forget`, `list_memories`, `get_memory`, `update_memory_access` |

`Pendiente de confirmar`: la doc del repo habla de **27 tools en total** y **14 de Engram**. Esas cifras no son verificables desde el código. Para ver el inventario real en vivo, usa `/context` en Telegram.

## Skills

Un skill es un fichero Markdown en `config/skills/` con frontmatter YAML:

```markdown
---
name: calendario
keywords: [calendario, evento, reunión, cita, schedule]
---

Cuando Kike pida crear un evento, usa Create_an_event con título, fecha y hora.
Cuando pregunte por eventos, usa Get_all_Events.
Para modificar, usa Reschedule_Event.
```

### Skills actuales

| Fichero | Propósito |
|---|---|
| `calendario.md` | Google Calendar |
| `notas.md` | Notas y tareas |
| `automatizacion.md` | Automatización del Mac con AppleScript/JXA |
| `memoria.md` | Gestión de memoria persistente |

> Las listas de keywords que aparecen en `docs/architecture/skill-system.md` **no coinciden exactamente** con el frontmatter real de los ficheros. Fíate de los ficheros.

### Ciclo de vida (`src/skills.ts`)

- `loadAllSkills()` — escanea `config/skills/*.md`, parsea el frontmatter y cachea en un `Map` de módulo.
- `detectSkills(mensaje)` — pasa el mensaje a minúsculas y comprueba si contiene alguna keyword. Coincidencia por subcadena.
- `loadSkillsContext(nombres)` — concatena los cuerpos con el prefijo `"\n\nSKILLS ACTIVOS:\n"`.
- `reloadSkills()` — limpia la caché y recarga desde disco.

La autodetección está **siempre activa**.

## Cómo añadir cosas

### Un skill nuevo

1. Crea `config/skills/miskill.md`.
2. Frontmatter con `name` y `keywords`.
3. Cuerpo en Markdown con las instrucciones.
4. Listo. No hace falta tocar código. Con `/skill recargar` lo cargas sin reiniciar.

### Un servidor MCP nuevo

1. Añade la entrada a `mcp.json` con `name`, `type` y `url` (http) o `command`/`args` (stdio).
2. **Reinicia el bot** — los servidores solo se conectan al arrancar.
3. `initMcpClients()` conecta, lista las tools y las registra automáticamente.

## Diagnóstico

```
/context     # tools registradas y servidores conectados
```

Con `LOG_LEVEL=debug` verás `[Ollama] Tools available: ...` y `[Ollama] Received tool calls: ...`.

Si el modelo responde con texto en vez de llamar tools, suele ser el modelo. `ornith:9b` es el recomendado por su fiabilidad en tool calling; hay que mantener `tool_choice: "required"` y `temperature: 0.3`.

## Código sin uso en `mcp.ts`

- `getToolsByServer()` — devuelve las descripciones vacías y no tiene llamadas.
- `callServerTool()` — importado por `bot.ts` pero nunca invocado.

## Notas relacionadas

- [[mara-os]]
- [[Memoria y contexto]]
- [[Arquitectura del sistema]]
- [[Estado y pendientes]]
