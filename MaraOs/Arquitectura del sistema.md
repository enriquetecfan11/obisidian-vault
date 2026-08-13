---
title: Arquitectura del sistema
type: document
tags:
  - mara-os
  - arquitectura
project: MaraOS
status: active
date_created: 2026-08-13
date_modified: 2026-08-13
---
# Arquitectura del sistema

## Las tres capas

```
┌─────────────────────────────────────────────────────────┐
│  ENTRADAS                                               │
│  Telegram (texto, foto, voz)   ·   Micro del navegador  │
└──────────────────┬──────────────────────────────────────┘
                   ▼
┌─────────────────────────────────────────────────────────┐
│  mara-os  ·  EL CEREBRO                                 │
│  bot.ts → context-builder → Ollama → MCP → respuesta    │
│  + memoria SQLite  + skills  + Voicebox TTS  + STT      │
│  Expone un servidor WebSocket "brain"                   │
└────────┬─────────────────────────────┬──────────────────┘
         │ eventos v1                  │ tools
         ▼                             ▼
┌──────────────────────┐   ┌──────────────────────────────┐
│  mara-ui             │   │  Servidores MCP              │
│  bridge (Node)       │   │  engram · macos_automator    │
│     ↕                │   │  calendar (n8n) · notes (n8n)│
│  React (navegador)   │   └──────────────────────────────┘
└──────────────────────┘
         ▲
         │ (previsto, aún sin código)
┌──────────────────────┐
│  mara-device         │
│  teclado · cámara    │
│  micro · sensores    │
└──────────────────────┘
```

## Flujo completo de un mensaje

1. **Entrada.** `bot.ts` recibe texto, foto o audio de Telegram; o llega audio PCM desde el micro del navegador vía WebSocket.
2. **Cola.** El mensaje se encola por `chatId` (`enqueue`) para procesar secuencialmente y evitar condiciones de carrera. Se lanza el indicador "escribiendo…" que se repite cada 4 s.
3. **Aprobación.** Si el texto contiene palabras de riesgo (`publicar`, `postear`, `tuitear`…), se bloquea y se pide confirmación explícita. Ver [[mara-os]].
4. **Contexto.** `buildContext()` arma el system prompt: plantilla `SYSTEM.md` + `SOUL` + `USER` + `AGENTS` + historial reciente (6000 tokens) + top-5 recuerdos relevantes + skills detectados. Ver [[Memoria y contexto]].
5. **LLM.** `POST {OLLAMA_URL}/api/chat` con `tool_choice: "required"`, `temperature: 0.3`, timeout 60 s.
6. **Tools.** Si el modelo pide tools, todas se ejecutan en paralelo (`Promise.all`) contra el servidor MCP correspondiente. Ver [[MCP y skills]].
7. **Respuesta.** Cuando no hay más `tool_calls`, el texto se limpia de markdown y se entrega.
8. **Salida.** Texto siempre primero a Telegram; voz encima si toca (Voicebox TTS → WAV → OGG/Opus). En paralelo se emiten eventos a la UI.
9. **Extracción.** En background (`setImmediate`, no bloquea) un LLM analiza la conversación y extrae hechos que guarda como memoria a largo plazo.

## Topología de red

```
mara-ui (React, navegador)
   │  ws://localhost:8765          VITE_MARA_WS_URL
   ▼
bridge  (mara-ui/server/index.mjs, puerto 8765)
   │  ws://127.0.0.1:9001          MARA_BRAIN_WS_URL
   ▼
mara-os (brain, src/events.ts)
```

El bridge hace tres cosas a la vez: sirve el build estático de `dist/`, es hub WebSocket de los clientes de UI, y hace de proxy hacia el cerebro. También expone una API HTTP (`/api/event`, `/api/status`, `/api/help`) para inyectar eventos a mano.

La UI **puede** apuntar directamente al cerebro saltándose el bridge; ningún camino de código distingue ambos casos.

### Puertos

| Puerto | Proceso | Variable |
|---|---|---|
| `11434` | Ollama | `OLLAMA_URL` |
| `8765` | Bridge de mara-ui (HTTP + WS) | `MARA_SERVER_PORT` |
| `9001` | Brain de mara-os (WS) | `MARA_BRAIN_WS_URL` |
| `17493` | Voicebox (TTS/STT remoto) | `VOICEBOX_URL` |
| `5173` / `4173` | Vite dev / preview | — |

> El README y `docs/` de `mara-os` dicen **9000**. Los `.env` reales de ambos repos usan **9001**. `Pendiente de confirmar` cuál es el valor definitivo.

## Decisiones de diseño observadas

- **Todo local por defecto.** Ollama para inferencia, SQLite para memoria, whisper en WASM para STT. Los únicos servicios remotos son los dos MCP de n8n y Voicebox.
- **El estado visual lo manda el cerebro, no Telegram.** El ciclo `speaking` envuelve la *generación* de TTS; Telegram es un canal de salida más.
- **Degradación elegante.** Si Ollama, Voicebox, un servidor MCP o el brain no están disponibles, el bot arranca igual y avisa por log. `EADDRINUSE` en el brain no tumba el bot.
- **Contexto en Markdown versionable.** La personalidad y las reglas viven en ficheros `.md`, no en código.
- **El hardware es una capacidad, no una dependencia.** Principio declarado en [[mara-device]]: si un dispositivo no está, Mara sigue funcionando.

## Notas relacionadas

- [[Mara OS]]
- [[Protocolo de eventos v1]]
- [[Puesta en marcha]]
- [[Estado y pendientes]]
