---
title: Puesta en marcha
type: document
tags:
  - mara-os
  - operaciones
  - runbook
project: MaraOS
status: active
date_created: 2026-08-13
date_modified: 2026-08-13
---
# Puesta en marcha

Runbook para levantar el sistema completo.

## Requisitos

- **Node.js 18+** y `pnpm` (mara-os) / `npm` (mara-ui)
- **Ollama** corriendo con el modelo `ornith:9b` descargado
- **Bot de Telegram** creado con [@BotFather](https://t.me/BotFather)
- **ffmpeg** — obligatorio para las notas de voz de Telegram (WAV → OGG/Opus)
- *(Opcional)* **Voicebox** para TTS
- *(Opcional)* **Engram** en `~/Engram`, ejecutado con `uv`

## Orden de arranque

```
1. Ollama          →  puerto 11434
2. mara-os         →  brain WebSocket en 9001
3. mara-ui bridge  →  HTTP + WS en 8765
4. Navegador       →  http://localhost:8765
```

Ollama primero: `mara-os` hace un `checkOllama()` al arrancar y, si falla, se pone en estado `offline` (aunque sigue funcionando y reintenta).

### 1. Ollama

```bash
ollama serve
ollama list          # comprobar que ornith:9b está
```

### 2. mara-os

```bash
cd ~/Documents/dev/projects/mara-os
pnpm install
cp .env.example .env      # solo la primera vez
pnpm bot
```

Salida esperada al arrancar: conexión de los servidores MCP, migración de memoria, ping a Ollama, health de Voicebox, `getMe()` de Telegram y, si hay `TELEGRAM_CHAT_ID`, un mensaje `🤖 Mara OS iniciado…` en el chat.

### 3. mara-ui

```bash
cd ~/Documents/dev/projects/mara-ui
npm install
npm run build       # el bridge sirve dist/; sin build no hay UI
npm run server
```

Para desarrollo con recarga en caliente, `npm run dev` en `:5173` **además** del bridge (la UI necesita el WebSocket del bridge igualmente).

## Variables de entorno

### `mara-os/.env`

| Variable | Para qué | Default |
|---|---|---|
| `TELEGRAM_TOKEN` | Token del bot. **Obligatorio** | — |
| `TELEGRAM_CHAT_ID` | Chat del mensaje de arranque y destino del espejado del micro | — |
| `MARA_USER_NAME` | Cómo se etiqueta al usuario al espejar a Telegram | `Kike` |
| `OLLAMA_URL` | Endpoint de Ollama | `http://localhost:11434` |
| `OLLAMA_MODEL` | Modelo | `ornith:9b` |
| `TIMEZONE` | Zona horaria | `Europe/Madrid` |
| `STT_LOCAL_ENABLED` | `false` → usar Voicebox para transcribir | `true` |
| `STT_MODEL` | Modelo whisper de transformers.js | `Xenova/whisper-tiny` |
| `STT_LANGUAGE` | Idioma ISO, o `auto` | `es` |
| `VOICEBOX_ENABLED` | Activa el TTS | `false` |
| `VOICEBOX_URL` | Base de Voicebox | `http://192.168.1.79:17493` |
| `VOICEBOX_PROFILE` | Perfil de voz | `Mara` |
| `VOICEBOX_TRANSCRIBE_MODEL` | Modelo de STT remoto | `whisper-turbo` |
| `TELEGRAM_SEND_VOICE` | Voz en todas las respuestas por defecto | `false` |
| `MARA_BRAIN_WS_URL` | URL de escucha del brain. Vacío = desactivado | `""` |
| `LOG_LEVEL` | `debug\|info\|warn\|error`. **No está en `.env.example`** | `info` |
| `NODE_ENV` | `production` fuerza la BD a `/var/lib/mara/memory/`. **No está en `.env.example`** | — |

Valores reales en uso ahora mismo: `OLLAMA_URL=http://100.91.66.127:11434` (host en rango Tailscale), `STT_MODEL=Xenova/whisper-base`, `VOICEBOX_ENABLED=true`, `TELEGRAM_SEND_VOICE=false`, `MARA_BRAIN_WS_URL=ws://0.0.0.0:9001`.

### `mara-ui/.env`

| Variable | Para qué | Default |
|---|---|---|
| `VITE_MARA_WS_URL` | WebSocket al que conecta el navegador | `ws://localhost:8765` |
| `MARA_SERVER_PORT` | Puerto del bridge | `8765` |
| `MARA_BRAIN_WS_URL` | Cerebro al que hacer de proxy | `null` |
| `MARA_HTTP_URL` | Destino de `npm run send`. **No documentada** | `http://localhost:8765` |

> Los dos repos tienen una variable llamada `MARA_BRAIN_WS_URL` con significados distintos: en `mara-os` es **dónde escuchar**, en `mara-ui` es **a dónde conectarse**. Deben apuntar al mismo puerto.
>
> El `.env` de `mara-ui` usa `127.0.0.1` explícitamente para evitar que Node resuelva `::1`.

## Verificación

```bash
# ¿Ollama vivo?
curl http://localhost:11434/api/version

# ¿Bridge vivo y conectado al cerebro?
curl http://localhost:8765/api/status
# → {"clients":1,"micSessions":0,"brain":true}

# Inyectar un evento a mano y comprobar que la UI reacciona
cd ~/Documents/dev/projects/mara-ui
npm run send -- state=thinking
```

En Telegram, `/context` devuelve el volcado completo: ficheros de contexto, skills, tools registradas, servidores MCP conectados y backend de memoria activo.

## Comandos útiles

```bash
# mara-os
pnpm bot            # arrancar
pnpm bot:lite       # variante mínima, sin MCP ni memoria
pnpm typecheck      # tsc --noEmit
pnpm reset-bot      # vaciar MEMORY.md
pnpm reset-memory   # restaurar MEMORY.md desde git

# mara-ui
npm run dev         # Vite :5173
npm run build       # producción
npm run preview     # :4173
npm run server      # bridge :8765
npm test            # vitest
```

## Fallos típicos

| Síntoma | Causa probable |
|---|---|
| La UI muestra "offline" y un overlay de red persistente | El bridge no alcanza el brain. Comprueba que `MARA_BRAIN_WS_URL` coincide en ambos repos y que `mara-os` arrancó |
| `Build no encontrado. Ejecuta primero: npm run build` | Falta `dist/` en mara-ui |
| El bot arranca pero no ejecuta acciones | Servidores MCP caídos. Mira `/context` y los logs de `initMcpClients` |
| El modelo responde texto en vez de llamar tools | Modelo poco fiable en tool calling. Usa `ornith:9b` |
| Las notas de voz llegan como fichero de audio, no como nota de voz | Falta `ffmpeg` o el códec opus; cae al fallback WAV |
| El micro del navegador no arranca | Requiere `localhost` o HTTPS; o falta el permiso |
| Warning `EADDRINUSE` al arrancar | El puerto del brain está ocupado. El bot sigue, pero sin eventos a la UI |
| El bot no responde nada | Con `LOG_LEVEL=debug`, revisa timeout de Ollama (60 s) y los reintentos |

## Despliegue en la Raspberry Pi

`mara-ui/README.md` documenta el modo kiosko: Chromium con `--kiosk`, una unidad systemd `/etc/systemd/system/mara-ui.service` apuntando a `http://localhost:4173`, y desactivación del apagado de pantalla con `xset` y en la tty.

`Pendiente de confirmar`: no hay Dockerfile, ni unidad systemd para `mara-os`, ni configuración de CI en ninguno de los tres repos. El despliegue de producción del cerebro no está automatizado.

## Notas relacionadas

- [[Arquitectura del sistema]]
- [[mara-os]]
- [[mara-ui]]
- [[Estado y pendientes]]
