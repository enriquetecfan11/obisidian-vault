---
title: mara-os
type: document
tags:
  - mara-os
  - backend
  - telegram
  - ollama
project: MaraOS
status: active
date_created: 2026-08-13
date_modified: 2026-08-13
---
# mara-os — el cerebro

Bot de Telegram + bucle de agente sobre Ollama + capa MCP + memoria persistente. Es el proceso central del sistema.

- **Ruta:** `~/Documents/dev/projects/mara-os`
- **Repo:** `github.com/enriquetecfan11/mara-os`
- **Paquete:** `agente-bolsillo` v0.1.0 (el nombre del `package.json` no coincide con el del proyecto)
- **Stack:** TypeScript ESM ejecutado con `tsx`, sin paso de build (`tsc --noEmit` solo verifica tipos)
- **Tamaño:** 24 ficheros, ~3800 líneas en `src/`

## Dependencias

| Paquete | Para qué |
|---|---|
| `grammy` | Framework del bot de Telegram |
| `@modelcontextprotocol/sdk` | Cliente MCP (stdio y HTTP) |
| `better-sqlite3` | Memoria a corto y largo plazo |
| `ws` | Servidor WebSocket "brain" |
| `@xenova/transformers` | STT local (whisper en WASM/ONNX) |

Ollama se llama por `fetch` directo, sin SDK.

## Módulos de `src/`

### Núcleo

- **`bot.ts`** (841 líneas, el más grande) — handler de Telegram, comandos, cola por chat, aprobaciones, entrega de respuesta, arranque y apagado.
- **`ollama.ts`** (213) — `askPi()` y `askPiWithRetry()`. Bucle del agente contra `/api/chat`.
- **`mcp.ts`** (204) — conexión a servidores MCP y despacho de tools. Ver [[MCP y skills]].
- **`events.ts`** (342) — servidor WebSocket "brain". Ver [[Protocolo de eventos v1]].
- **`skills.ts`** (95) — detección de skills por keywords.

### Memoria (`src/memory/`)

`memory-manager.ts`, `conversation-store.ts`, `context-builder.ts`, `memory-extractor.ts`, `migrate.ts`, `types.ts` y los backends `stores/sqlite.ts` y `stores/engram.ts`. Todo el detalle en [[Memoria y contexto]].

### Voz

- **`stt.ts`** (79) — transcripción local con `@xenova/transformers`, modelo `Xenova/whisper-*`.
- **`voicebox.ts`** (188) — cliente REST de Voicebox: `generateVoice()`, `transcribeAudio()`, `checkVoicebox()`.
- **`audio.ts`** (31) — `wavToOggOpus()`, transcodifica con `ffmpeg` para que Telegram lo reciba como nota de voz real.

### Soporte

- **`config.ts`** (43) — lectura de variables de entorno con defaults.
- **`logger.ts`** (53) — log estructurado con colores y niveles (`LOG_LEVEL`).
- **`cache.ts`** (34) — caché de ficheros de contexto por `mtime`. Baja la latencia de ~40-60 ms a ~1 ms por request.
- **`approvals.ts`** (13) — puerta de confirmación para acciones de riesgo.
- **`telegram-files.ts`** (24) — descarga de adjuntos a `config/uploads/`.

## Los dos puntos de entrada

| | `bot.ts` | `bot-lite.ts` |
|---|---|---|
| MCP | Sí | **No** |
| Memoria y migración | Sí | **No** |
| Skills | Sí | **No** |
| Comandos | `/start /reset /help /status /context /skill /cancel /memory /feedback /voz` | `/start /reset /help /cancel` |
| Handlers | texto, foto, voz, audio | texto, foto, voz |
| `/voz` por chat | Sí | No |

`bot-lite.ts` (463 líneas) es una variante mínima para probar el canal de Telegram sin levantar toda la infraestructura. Comparte bastante código copiado de `bot.ts` (`stripMarkdown`, `enqueue`, `handleBrowserAudio`…).

```bash
pnpm bot        # agente completo
pnpm bot:lite   # variante mínima
pnpm typecheck  # tsc --noEmit
```

## Bucle del agente (`askPi`)

1. Guarda el mensaje del usuario en el `ConversationStore`.
2. `buildContext()` arma el system prompt y devuelve `recentMessages`.
3. Crea un `AbortController` por chat con timeout de **60 s**.
4. Llama a Ollama:

```ts
fetch(`${ollamaUrl}/api/chat`, {
  method: "POST", signal: controller.signal,
  body: JSON.stringify({
    model: ollamaModel, messages, stream: false,
    tools: ollamaTools,
    tool_choice: ollamaTools.length > 0 ? "required" : "none",
    temperature: 0.3,
  }),
})
```

5. Si hay `tool_calls`, se ejecutan **todas en paralelo** con `Promise.all` y los resultados se guardan como mensajes `role: "tool"`. El bucle repite.
6. Si no hay `tool_calls`, el contenido es la respuesta final y se dispara la extracción de memorias en background.

**Reintentos:** `askPiWithRetry(chatId, message, maxRetries = 2)` con backoff exponencial (1 s, 2 s, 4 s). Un `AbortError` se relanza de inmediato sin reintentar.

**Sesiones:** `chatSessions` con timeout de 30 min y limpieza cada 5 min.

> ⚠️ Los resultados de las tools se persisten en SQLite pero **no se reinyectan en el array `messages` dentro de la misma llamada a `askPi`**. El array no crece entre iteraciones del bucle. Ver [[Estado y pendientes]].

## Comandos de Telegram

| Comando | Qué hace |
|---|---|
| `/start` | Limpia el historial del chat y saluda |
| `/reset` | Limpia el historial |
| `/help` | Modelo, tamaño de los ficheros de contexto, skills |
| `/status` | Fecha, modelo, URL de Ollama, vista previa del contexto |
| `/context` | Volcado completo: contexto, skills, tools registradas, servidores MCP conectados, backend de memoria |
| `/skill [lista\|recargar\|<nombre>]` | Gestión de skills |
| `/cancel` | Aborta la petición en curso |
| `/memory [query \| search <q> \| list \| forget <id>]` | Consulta la memoria a largo plazo |
| `/feedback <texto>` | Añade una línea a `config/FEEDBACK.log` |
| `/voz on\|off` | Activa o desactiva la voz para ese chat |

## Entradas y salidas

**Texto** → flujo normal.

**Foto** → descarga la resolución mayor a `config/uploads/` y pasa al modelo `"<caption>\n\nImagen local: <ruta>"`. Ojo: el modelo es solo texto; la imagen únicamente se referencia por ruta, no se analiza.

**Voz / audio de Telegram** → descarga, transcribe (`STT_LOCAL_ENABLED` decide entre whisper local y Voicebox), pasa la transcripción por el flujo normal incluida la aprobación, y borra el temporal en `finally`.

**Micro del navegador** (`handleBrowserAudio`) → escribe el WAV en `config/uploads/browser-<ts>.wav`, transcribe, aplica el filtro anti-realimentación `isMeaningfulTranscription()` (mínimo 2 palabras de ≥2 caracteres, descarta lo que empieza por `♪`/`♫`), responde, espeja a Telegram como `🎤 <MARA_USER_NAME>: …` y devuelve el audio a la UI. Usa `setState("thinking")` en vez de `listening` a propósito, para no rearmar el micro y crear un bucle.

**Salida (`deliverReply`)** → el texto **siempre** se envía primero. La voz se añade si `voiceboxEnabled && wantVoiceFor(chatId, isAudioInput)`: gana el override de `/voz`, si no `TELEGRAM_SEND_VOICE`, si no espeja la modalidad de entrada. Se omite para respuestas de más de 500 caracteres. El WAV se convierte a OGG/Opus con `ffmpeg -c:a libopus -b:a 32k -ar 48000 -ac 1`; si falla, cae a `replyWithAudio` con el WAV.

## Aprobaciones

`src/approvals.ts` dispara con la regex:

```
\b(publica|publicar|postea|postear|tuitea|twittea|tweet)\b
```

Para desbloquear, el mensaje debe empezar por `confirmo`, `confirmado`, `sí confirmo` o `si confirmo`. El bloqueo también emite `mara:confirm` a la UI; una respuesta `mara:confirm-response {accepted: true}` reenvía el mensaje con el prefijo `"Confirmo "`.

## Arranque y apagado

```
1. Registra SIGINT / SIGTERM
2. startUiEvents()            ← servidor WebSocket brain
3. Registra handlers de comandos y audio
4. await initMcpClients()
5. await runMemoryMigration()
6. checkOllama()              ← GET /api/version, 5 s; si falla → estado offline y continúa
7. checkVoicebox()            ← GET /health
8. bot.api.getMe() + mensaje de arranque si hay TELEGRAM_CHAT_ID
9. bot.start()                ← long polling
```

Apagado: `closeMcpClients()` → `memoryManager.close()` → `closeUiEvents()` → `bot.stop()` → `exit(0)`. Cerrar los clientes MCP primero evita el traceback de Python de Engram.

## Notas relacionadas

- [[Arquitectura del sistema]]
- [[Memoria y contexto]]
- [[MCP y skills]]
- [[Protocolo de eventos v1]]
- [[Estado y pendientes]]
