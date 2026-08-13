---
title: Estado y pendientes
type: document
tags:
  - mara-os
  - estado
  - deuda-tecnica
project: MaraOS
status: active
date_created: 2026-08-13
date_modified: 2026-08-13
---
# Estado y pendientes

Foto tomada el **13 de agosto de 2026**. Todo lo de aquí está verificado contra el código, salvo lo marcado como `Pendiente de confirmar`.

## Estado por repositorio

| Repo | Commits | Último commit | Estado |
|---|---|---|---|
| `mara-os` | 31 | `bb3bad0` "new memory system" (12 ago) | Funcional, desarrollo activo |
| `mara-ui` | 3 | `94e4d6c` "new TTS and voice system" (12 ago) | Funcional, conectado al cerebro real |
| `mara-device` | 1 | `06bb87c` (10 ago) | **Solo README. Sin código** |

Los tres tienen el árbol de trabajo limpio y sincronizado con `origin/main`.

## Qué funciona de punta a punta

**mara-os:** Telegram (texto, foto, voz, audio), cola por chat e indicadores, puerta de aprobaciones, bucle del agente con tools MCP en paralelo, reintentos, cancelación y timeout de 60 s, capa MCP stdio+HTTP con conexión paralela y cierre limpio, autodetección de skills, caché de contexto por mtime, memoria SQLite a corto y largo plazo con FTS5, extracción de memorias en background, brain WebSocket con re-sync e ingesta de PCM del micro, TTS con Voicebox, STT local con transformers.js, transcodificación a OGG/Opus, log estructurado, apagado ordenado y la variante `bot-lite.ts`.

**mara-ui:** transporte WebSocket con reconexión, normalización del protocolo v1 en ambos sentidos, mapeo completo de eventos a la UI, máquina de estados del orbe con animaciones, overlays con TTL, flujo de confirmación con teclado, panel de ajustes persistido, streaming del micro del navegador, reproducción del TTS remoto, bridge con servido estático + API HTTP + proxy + re-sync, y tests unitarios del protocolo y el store.

## Deriva entre la documentación del repo y el código

**Esta es la parte más importante de esta nota.** `mara-os/docs/` tiene 20 ficheros y una parte quedó obsoleta con el commit `bb3bad0`.

| Tema | Dice la doc | Dice el código |
|---|---|---|
| Modelo LLM | `gemma4:e2b` | `ornith:9b` |
| STT local | whisper.cpp / `nodejs-whisper` | `@xenova/transformers` (WASM/ONNX) |
| Puerto del brain | `9000` | `9001` en los `.env` reales |
| Timeout de Ollama | 30 s | 60 s |
| Historial | 20 mensajes en memoria | SQLite por presupuesto de 6000 tokens |
| Tool `update_memory` | Fallback documentado | **No existe** |
| Voicebox | `POST /generate/stream` | `POST /generate` + polling de `GET /audio/{id}` |
| `{{MEMORY}}` | Contenido de `MEMORY.md` | Resultados de la búsqueda en memoria |

### Ficheros afectados

| Fichero | Fiabilidad |
|---|---|
| `docs/memory-system.md` | ✅ Actual y correcto |
| `docs/VOICEBOX_INTEGRATION.md` | ⚠️ Endpoints y nombres de función desfasados |
| `docs/operations/memory-management.md` | ❌ Describe el sistema anterior completo |
| `docs/operations/session-management.md` | ❌ Describe el historial FIFO de 20 mensajes |
| `docs/STT_LOCAL.md` | ❌ Documenta whisper.cpp, dependencia no instalada |
| `docs/reference/api-reference.md` | ⚠️ Anterior a `src/memory/`, con referencias a líneas erróneas |
| `docs/architecture/*` | ⚠️ Correcto en lo estructural, desfasado en detalles |
| `CLAUDE.md` | ⚠️ Buena guía general, varias afirmaciones obsoletas |
| `README.md` (mara-os) | ⚠️ La sección "Estructura del Proyecto" solo lista 4 ficheros de 24 |
| `README.md` (mara-ui) | ⚠️ El árbol lista `useKeyboardNumpad.ts` (borrado) y omite `useVoicePlayback.ts` |

## Bugs y limitaciones detectados

### Probables bugs

1. **Los resultados de las tools no vuelven al bucle.** En `src/ollama.ts`, el array `messages` se reconstruye desde el mismo `recentMessages` capturado *antes* del bucle. Los resultados se persisten en SQLite pero no se reinyectan en la misma invocación de `askPi`, así que el array no crece entre iteraciones. Es el hallazgo más serio.
2. **STT local no decodifica OGG/Opus.** `wavToFloat32()` exige WAV PCM y lanza `"Formato de audio no soportado"` en otro caso. Las notas de voz de Telegram son OGG/Opus y **no se convierten antes**. El STT local funcionaría con el micro del navegador (WAV) pero fallaría con `message:voice` y `message:audio`.
3. **FTS5 recibe entrada sin escapar.** El mensaje del usuario va directo al `MATCH`. Caracteres con sintaxis FTS5 podrían provocar una excepción que salga por `askPi`.

### Limitaciones conocidas

- **`mara:settings` no hace nada.** El cerebro lo recibe, lo loguea y ahí se queda. Volumen, brillo, micro y cámara desde la UI no tienen efecto.
- **Las fotos no se analizan.** El modelo es solo texto; la imagen se pasa como una ruta en el prompt.
- **El resumen de conversación no usa LLM**, es una plantilla con las palabras largas del historial.
- **`createScriptProcessor` está deprecada** en `maraMic.ts`, sin ruta de AudioWorklet.
- **`voice.audio` no se re-sincroniza**: un cliente que llega tarde no recibe el audio pendiente.
- **`data/mara.db` tiene 0 filas** en ambas tablas. El sistema de memoria no ha acumulado datos aún.

### Código muerto o sin uso

| Dónde | Qué |
|---|---|
| `ollama.ts` | `getChatHistoryMessageCount()` es un stub que devuelve `0`. Importa 5 símbolos que no usa |
| `memory/memory-store.ts` | 1 línea, solo reexporta |
| `mcp.ts` | `getToolsByServer()` y `callServerTool()` sin llamadas |
| `events.ts` | `handleIncomingMessage()`, `emitNetwork()`, `getState()`, `isUiEnabled()` sin llamadas |
| `bot.ts` | Importa `callServerTool`, nunca lo invoca |
| `mara-ui` | `mara:numpad` saliente sin emisor; estado `seeing` sin productor; `brightness` sin efecto |
| Los tres | El ternario no-op de `version` en `toEnvelope()` |

### Huecos de calidad

- **Sin tests en `mara-os`.** `docs/development/testing.md` lo dice explícitamente. Solo `pnpm typecheck`.
- **Tests parciales en `mara-ui`:** solo protocolo y store. El entorno vitest es `node` con un `window` mínimo, así que **no se pueden testear componentes** (aunque `jsdom` está instalado).
- **Sin CI** en ninguno de los tres repos.
- **Sin lint** en `mara-ui` (ni eslint ni prettier).
- **Sin Dockerfile ni systemd para `mara-os`.**
- **Código duplicado** entre `bot.ts` y `bot-lite.ts` (`stripMarkdown`, `enqueue`, `handleBrowserAudio`…).

## Pendiente de confirmar

- **Inventario real de tools MCP.** Las cifras "27 tools" y "14 de Engram" salen solo de la documentación. Se comprueba en vivo con `/context`.
- **Si Engram y Voicebox están operativos** ahora mismo (`~/Engram`, `192.168.1.79:17493`).
- **Puerto definitivo del brain:** ¿9001 es el valor final o se vuelve a 9000?
- **Por qué `pnpm-workspace.yaml` declara `allowBuilds`** para `@google/genai`, `protobufjs`, `sharp` y `esbuild`, si ninguno es dependencia del paquete.
- **Por qué el `package.json` de `mara-os` se llama `agente-bolsillo`** — ¿nombre heredado o intencional?
- **Plan y calendario de [[mara-device]]:** stack, mecanismo de comunicación y prioridad. No hay issues ni ramas.

## Siguientes pasos sugeridos

Por orden de impacto:

1. **Investigar el bug del bucle de tools** en `ollama.ts` — si se confirma, el agente está perdiendo los resultados de las tools dentro de la misma petición.
2. **Convertir OGG→WAV antes del STT local**, o desactivar `STT_LOCAL_ENABLED` para audio de Telegram. Ya existe `audio.ts` con `ffmpeg` para la dirección contraria.
3. **Sanear la entrada del `MATCH` de FTS5.**
4. **Podar la documentación obsoleta del repo:** borrar o marcar `docs/operations/memory-management.md`, `session-management.md` y `STT_LOCAL.md`, y corregir el modelo y el timeout en `BOT_REFERENCE.md` y `CLAUDE.md`.
5. **Implementar `mara:settings`** en el cerebro, o quitarlo de la UI para que no prometa algo que no hace.
6. **Arrancar `mara-device`** — el contrato ya está definido en [[Protocolo de eventos v1]]; faltan `mara:system`, `mara:numpad`, `mara:volume`, `mara:mute` y `mara:camera`, que hoy no tienen emisor.

## Notas relacionadas

- [[Mara OS]]
- [[mara-os]]
- [[mara-ui]]
- [[mara-device]]
- [[Puesta en marcha]]
