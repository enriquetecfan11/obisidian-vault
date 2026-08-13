---
title: mara-ui
type: document
tags:
  - mara-os
  - frontend
  - react
project: MaraOS
status: active
date_created: 2026-08-13
date_modified: 2026-08-13
---
# mara-ui — la cara

Interfaz visual de Mara. No es un dashboard: es una cara para una pantalla táctil en la Raspberry Pi. Un orbe central que reacciona al estado del asistente, y todo lo demás son superposiciones.

- **Ruta:** `~/Documents/dev/projects/mara-ui`
- **Repo:** `github.com/enriquetecfan11/mara-ui`
- **Stack:** React 19 · Vite 6 · Tailwind 4 · zustand 5 · framer-motion 12
- **Historia:** solo 3 commits. Nació con datos simulados, en `c9d4778` se eliminó el modo mock y se conectó al cerebro real.

## Dos procesos

```
navegador  ──ws──▶  bridge (Node)  ──ws──▶  mara-os brain
 React app          server/index.mjs
                    puerto 8765
```

### El bridge — `server/index.mjs`

Un solo proceso Node que hace cuatro cosas:

1. **Servidor estático** de `../dist/` con fallback SPA a `index.html` y guardia contra path traversal. Si no hay build, responde `Build no encontrado. Ejecuta primero: npm run build`.
2. **Hub WebSocket** de todos los clientes de UI, en el mismo puerto que el HTTP.
3. **API HTTP:**

| Método | Ruta | Qué hace |
|---|---|---|
| POST | `/api/event` | Inyecta un evento y lo difunde. Responde `{ok, sent, event}` |
| GET | `/api/status` | `{clients, micSessions, brain}` |
| GET | `/api/help` | Documentación del protocolo en texto plano |

4. **Proxy hacia el cerebro** si `MARA_BRAIN_WS_URL` está definido. Reconecta con backoff exponencial hasta 30 s y timeout manual de 10 s en `CONNECTING`.

**Re-sync:** cuando un cliente se conecta tarde, el bridge le reenvía el último `mara:state`, `mara:network`, `mara:message` y los `voice.speaking.*`. `voice.audio` **no** se guarda, así que un cliente que llega tarde no recibe audio pendiente.

**Audio del micro:** los frames binarios requieren una sesión activa. El bridge calcula el RMS, lo suaviza (`smoothed * 0.6 + level * 0.4`), difunde `mara:audio-level` y reenvía los bytes crudos al cerebro.

### `server/send.mjs`

CLI para inyectar eventos a mano durante el desarrollo:

```bash
npm run send -- state=thinking
npm run send -- message text="hola"
npm run send -- '{"type":"mara:state","data":{"state":"speaking"}}'
```

Apunta a `MARA_HTTP_URL` (default `http://localhost:8765`). Esa variable **no está en `.env.example`**.

## La aplicación React

`App.tsx` tiene 9 líneas: llama a `useMara()` y `useVoicePlayback()` y renderiza `<MainScreen/>`. **No hay router ni tabla de rutas** — una sola pantalla y todo lo demás son overlays condicionales.

### Componentes

| Componente | Qué es |
|---|---|
| `Orb/Orb.tsx` | El núcleo visual: brillo, 3 anillos, ondas, esfera volumétrica, halo reactivo al audio, línea de escaneo |
| `MainScreen.tsx` | Única pantalla. Orbe dimensionado a `min(w*0.5, h*0.46, 300)` |
| `StatusText.tsx` | Etiqueta de estado en mayúsculas ("Esperando…", "Escuchando…", "RESPONDIENDO…") |
| `MessageText.tsx` | Texto de la respuesta bajo el orbe, con atenuado y auto-ocultado |
| `SystemBar.tsx` | Barra superior: reloj, wordmark, punto de conexión, temperatura, iconos de micro/cámara |
| `SettingsPanel.tsx` | Hoja inferior arrastrable: volumen, brillo, micro, cámara, wake word, micro del navegador |
| `Menu.tsx` | Mini menú por pulsación larga |
| `Overlays.tsx` | Superposiciones transitorias con TTL (volumen, mute, cámara, red, numpad, error) |
| `ConfirmOverlay.tsx` | Modal de confirmación. Enter acepta, `.` cancela |
| `ui/` | `Icon` (15 SVG inline), `Slider`, `Toggle` |

### Gestos

- **Toque en el orbe** → según el estado, envía `mara:start-listening`, `mara:stop-listening` o `mara:interrupt`.
- **Pulsación larga** (600 ms, cancela a los 14 px de movimiento) → abre el menú.
- **Botón de engranaje** abajo a la derecha → panel de ajustes.
- **Arrastrar hacia abajo** el panel más de 90 px o con velocidad > 400 → lo cierra.

### Estado (zustand)

**`maraStore`** — estado en vivo que viene del cerebro. Sin persistencia. Guarda `state`, `message`, `audio` (WAV en base64), `audioLevel`, `device`, `connected`, `overlays`, `confirm`.

Detalles que importan:
- Perder la conexión fuerza `state: 'offline'`, vacía `device` y `audio`, y empuja un overlay de red persistente (`ttl: 0`).
- `mara:system` fusiona campo a campo y conserva el valor anterior si el entrante no es del tipo correcto. **Nunca inventa datos** — hay un test que lo cubre explícitamente.
- Algunos eventos entrantes escriben también en `settingsStore`.

**`settingsStore`** — ajustes del usuario, con `persist` en `localStorage` bajo la clave `mara-ui-settings` (versión 2). Defaults: `volume 70`, `brightness 80`, `microphone true`, `camera true`, `wakeWord true`, `browserMic true`.

### Hooks

`useMara` (conecta el WebSocket al store), `useVoicePlayback`, `useBrowserMic`, `useAudioLevel`, `useClock`, `useHold`, `useViewportSize`.

## Voz

**No hay `SpeechSynthesis` ni `SpeechRecognition`.** Ni una sola dependencia de TTS/STT. Todo es remoto.

**TTS (salida):** el cerebro sintetiza y empuja `voice.audio` con un WAV en base64. La UI lo reproduce con un `Audio` sobre data URI:

```ts
const player = new Audio(`data:audio/wav;base64,${audio}`)
```

Al terminar —o si falla, o si el autoplay lo bloquea— vuelve a `idle`. El estado `speaking` se mantiene mientras quede audio en cola.

**STT (entrada):** la UI solo **captura**; la transcripción es remota. `maraMic.ts` usa `getUserMedia` a 16 kHz mono con cancelación de eco y supresión de ruido, un `AudioContext` y un `createScriptProcessor(2048, 1, 1)` (API deprecada, sin ruta de AudioWorklet). Convierte Float32 a Int16 y envía cada frame por WebSocket.

La captura **solo está activa mientras el estado es `listening`**, no de forma continua. Si falla, desactiva `browserMic` e inyecta un `mara:error` en el store. Mensajes de error: `'El micrófono del navegador requiere localhost o HTTPS.'` y `'Permiso de micrófono denegado.'`.

El nivel de audio del orbe **no se calcula en el navegador**: viene del evento `mara:audio-level` que difunde el bridge.

## Tests

Vitest con `environment: 'node'`. `src/test/setup.ts` define un mock de `localStorage` y un `window` que solo contiene `localStorage`, así que **hoy no se pueden testear componentes** (`jsdom` está instalado pero no seleccionado).

Dos ficheros, ambos de lógica pura:

- `src/types/mara.test.ts` — versión del protocolo, `makeEvent`, `normalizeEvent` (envelope v1, forma plana legacy, tipo desconocido → `mara:error`, entrada nula, timestamp ausente) y las formas de los payloads.
- `src/store/maraStore.test.ts` — estado inicial, manejo de cada evento, ciclo de conexión, "sin datos falsos sin backend", overlays y confirmaciones.

**Sin cubrir:** reconexión de `maraSocket`, `maraMic`, `useVoicePlayback`, persistencia de `settingsStore`, todo `server/`, y cualquier componente React.

## Scripts y variables

```bash
npm run dev        # Vite, :5173
npm run build      # tsc -b && vite build
npm run preview    # :4173
npm run server     # el bridge, :8765
npm run send       # CLI de eventos
npm test           # vitest run
```

| Variable | Quién la lee | Para qué | Default |
|---|---|---|---|
| `VITE_MARA_WS_URL` | Navegador | WebSocket al que conecta la UI | `ws://localhost:8765` |
| `MARA_SERVER_PORT` | Bridge | Puerto HTTP + WS | `8765` |
| `MARA_BRAIN_WS_URL` | Bridge | Cerebro al que hacer de proxy. Vacío = solo sirve la UI | `null` |
| `MARA_HTTP_URL` | `send.mjs` | Destino del CLI. **No documentada** | `http://localhost:8765` |

El `.env` real usa `MARA_BRAIN_WS_URL=ws://127.0.0.1:9001`, con `127.0.0.1` explícito para que Node no resuelva a `::1`.

## Modo kiosko en la Raspberry Pi

El `README.md` del repo documenta el despliegue: Chromium con `--kiosk`, una unidad systemd `/etc/systemd/system/mara-ui.service` apuntando a `http://localhost:4173`, y desactivación del apagado de pantalla con `xset` y en la tty.

## Notas relacionadas

- [[Arquitectura del sistema]]
- [[Protocolo de eventos v1]]
- [[mara-os]]
- [[Puesta en marcha]]
- [[Estado y pendientes]]
