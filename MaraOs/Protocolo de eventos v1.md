---
title: Protocolo de eventos v1
type: document
tags:
  - mara-os
  - protocolo
  - websocket
project: MaraOS
status: active
date_created: 2026-08-13
date_modified: 2026-08-13
---
# Protocolo de eventos v1

El contrato entre el cerebro ([[mara-os]]) y la interfaz ([[mara-ui]]). Es la pieza más estable del sistema y la única con tests automáticos.

## El envelope

Todo mensaje JSON, en ambas direcciones, tiene esta forma:

```ts
interface MaraEventEnvelope<T = unknown> {
  type: string
  version: number      // siempre 1 (PROTOCOL_VERSION)
  timestamp: number
  data: T
}
```

`normalizeEvent(raw)` acepta también una **forma plana legacy** (las claves que no son `data` se agrupan bajo `data`). Si falta el `type` o no es válido, se convierte en `mara:error`. Si falta el `timestamp`, se rellena con `Date.now()`.

## Quién es servidor

**`mara-os` es el servidor.** El bridge de `mara-ui` es el cliente que se conecta a él y difunde a los navegadores.

```
navegador ──ws──▶ bridge :8765 ──ws──▶ brain :9001
```

El brain se levanta con host y puerto parseados de `MARA_BRAIN_WS_URL`. Valor vacío = desactivado (no-op, el bot funciona igual). `EADDRINUSE` solo desactiva los eventos, no tumba el bot.

## Eventos: brain → UI

| `type` | `data` | Cuándo |
|---|---|---|
| `mara:state` | `{ state }` | Transición del agente. Deduplicado |
| `mara:message` | `{ text }` | Respuesta generada |
| `mara:network` | `{ connected }` | Estado del transporte |
| `mara:error` | `{ message }` | Fallo |
| `mara:confirm` | `{ id, title, message, action }` | Un mensaje requiere aprobación |
| `voice.speaking.started` | `{}` | Empieza la síntesis TTS |
| `voice.speaking.finished` | `{}` | Termina la síntesis TTS |
| `voice.audio` | `{ text?, audio }` | WAV en base64 para que la UI lo reproduzca |
| `mara:audio-level` | `{ level }` | Nivel RMS suavizado. **Lo emite el bridge**, no el cerebro |
| `mara:system` | `{ temperature, microphone, camera }` | Estado del dispositivo. Hoy sin emisor — ver [[mara-device]] |
| `mara:volume` | `{ volume }` | Hoy sin emisor |
| `mara:mute` | `{ muted }` | Hoy sin emisor |
| `mara:camera` | `{ enabled }` | Hoy sin emisor |
| `mara:numpad` | `{ key, press }` | Hoy sin emisor. La UI ya sabe pintarlo |

### Estados posibles

```ts
type MaraState = 'idle' | 'listening' | 'thinking' | 'speaking'
               | 'seeing' | 'error' | 'offline'
```

| Estado | Significado | Etiqueta en la UI |
|---|---|---|
| `idle` | En espera | "Esperando..." |
| `listening` | Transcribiendo audio | "Escuchando..." |
| `thinking` | Procesando | — |
| `speaking` | Sintetizando o reproduciendo voz | "RESPONDIENDO..." |
| `seeing` | Procesando una foto | "Observando..." |
| `error` / `offline` | Fallo o sin conexión | — |

> El ciclo `voice.speaking.*` envuelve **la generación de TTS**, no el envío a un canal concreto. La UI pasa a `speaking`/`idle` según la síntesis; Telegram es solo un canal de salida más y no controla el estado visual.

## Comandos: UI → brain

```ts
type MaraCommand =
  | { type: 'mara:start-listening' }
  | { type: 'mara:stop-listening' }
  | { type: 'mara:interrupt' }
  | { type: 'mara:settings'; data: Partial<DeviceSettings> }
  | { type: 'mara:confirm-response'; data: { id: string; accepted: boolean } }
  | { type: 'mara:numpad'; data: { key: NumpadKey; press?: NumpadPress } }
  | { type: 'mara:audio-start'; data: { sampleRate: number; channels: number } }
  | { type: 'mara:audio-stop' }
```

Qué envía realmente la UI hoy:

| Comando | Emisor | ¿Tiene efecto en el cerebro? |
|---|---|---|
| `mara:start-listening` / `stop-listening` / `interrupt` | `MainScreen.tsx` | Sí |
| `mara:confirm-response` | `ConfirmOverlay.tsx` | Sí, reenvía el mensaje con prefijo `"Confirmo "` |
| `mara:audio-start` / `mara:audio-stop` | `maraMic.ts` | Sí |
| `mara:settings` | `Menu.tsx`, `SettingsPanel.tsx` | **No.** Se recibe, se loguea y no hace nada |
| `mara:numpad` | **Nadie** | El tipo existe, no hay emisor |

El bridge reenvía **verbatim al cerebro todo frame de texto**, lo entienda o no.

## Sub-protocolo binario (audio del micro)

```
1. UI → { type: 'mara:audio-start', data: { sampleRate: 16000, channels: 1 } }
2. UI → N frames binarios: PCM Int16, mono, 16 kHz, buffer de 2048 muestras
3. UI → { type: 'mara:audio-stop' }
```

En el bridge, cada frame binario requiere una sesión activa (si no, se descarta). Calcula el nivel `min(1, rms * 3)`, lo suaviza, difunde `mara:audio-level` y reenvía los bytes crudos al cerebro.

En el cerebro, los frames se acumulan en un buffer por socket. Al recibir `mara:audio-stop` se sintetiza una cabecera WAV de 44 bytes (16000 Hz mono por defecto) y se entrega al handler de audio, que transcribe y responde.

## Re-sincronización

Ambos extremos reenvían estado a los clientes que llegan tarde:

- **El brain** reenvía el `mara:state` actual, el último `mara:message` y el `mara:network`.
- **El bridge** reenvía `mara:state`, `mara:network`, `mara:message`, `voice.speaking.started` y `voice.speaking.finished`, y corrige `mara:network` con el valor real de su conexión al cerebro.

`voice.audio` **no** se guarda para re-sync, así que un cliente que se conecta tarde no recibe audio pendiente.

## Reconexión

Ambos lados usan el mismo backoff exponencial:

```js
Math.min(1000 * 2 ** intentos, 30000)
```

El bridge añade un timeout manual de 10 s en estado `CONNECTING` seguido de `terminate()`.

## Detalles de implementación a tener en cuenta

- El bridge **solo parsea JSON**; los frames de texto no válidos se ignoran para el broadcast pero **igualmente se reenvían al cerebro**.
- `toEnvelope()` contiene un ternario que no hace nada (`version === PROTOCOL_VERSION ? PROTOCOL_VERSION : PROTOCOL_VERSION`); la versión siempre se fuerza a 1. Aparece en tres sitios: `server/index.mjs`, `server/send.mjs` y `src/types/mara.ts`.
- En `events.ts` hay código muerto: `handleIncomingMessage()`, `emitNetwork()`, `getState()` e `isUiEnabled()` no tienen llamadas.

## Notas relacionadas

- [[Arquitectura del sistema]]
- [[mara-os]]
- [[mara-ui]]
- [[mara-device]]
