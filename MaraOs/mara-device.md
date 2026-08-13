---
title: mara-device
type: document
tags:
  - mara-os
  - hardware
  - raspberry-pi
project: MaraOS
status: pendiente
date_created: 2026-08-13
date_modified: 2026-08-13
---
# mara-device — la capa de hardware

> **Estado: solo especificación.** El repositorio contiene únicamente un `README.md` de 24 líneas y un solo commit (`06bb87c`, 10 ago 2026, creado desde la web de GitHub). **No hay código, ni `package.json`, ni estructura de proyecto.**

Esta nota documenta la *intención* declarada, no una implementación.

- **Ruta:** `~/Documents/dev/projects/mara-device`
- **Repo:** `github.com/enriquetecfan11/mara-device`

## Propósito declarado

Conectar Mara con el hardware físico de la Raspberry Pi, de forma que `mara-os` no tenga que saber nada de Linux de bajo nivel.

## Responsabilidades declaradas

- Teclado numérico USB y atajos físicos
- Cámara y captura de imágenes
- Detección y gestión del micrófono
- Altavoces, volumen y mute
- Temperatura, CPU, RAM y estado del sistema
- Integración con Raspberry Pi 5
- Integración con Pironman 5 Pro Max
- Acciones de sistema: reinicio, apagado y servicios

## Arquitectura prevista

```
Hardware → mara-device → MaraOS → Mara UI / Mara Voice
```

Dos principios explícitos en el README:

1. **`mara-os` nunca debe depender directamente** de `/dev/input`, cámara, GPIO, I2C, ALSA ni otros detalles específicos de Linux. `mara-device` los abstrae y los convierte en eventos y acciones.
2. **El hardware es una capacidad, no una dependencia.** Si un dispositivo no está disponible, Mara debe seguir funcionando siempre que sea posible.

## Encaje con lo que ya existe

Aunque no haya código, el resto del sistema ya tiene huecos preparados que encajan con estas responsabilidades:

| Hueco existente | Dónde | Encaje |
|---|---|---|
| Evento `mara:system` con `{temperature, microphone, camera}` | [[Protocolo de eventos v1]] | Es exactamente lo que `mara-device` debería emitir |
| Evento `mara:numpad` con `{key, press}` | [[Protocolo de eventos v1]] | La UI ya sabe pintar el overlay; falta quien lo emita |
| Comando `mara:settings` con `volume`, `brightness`, `microphone`, `camera` | [[Protocolo de eventos v1]] | Hoy el cerebro lo recibe, lo loguea y **no hace nada** |
| Estado visual `seeing` | [[mara-ui]] | Tiene visuales completas y nadie lo produce |
| `brightness` en el panel de ajustes | [[mara-ui]] | Se guarda y se envía, pero no se aplica |

Es decir: **el contrato ya está definido en el protocolo v1; lo que falta es el proceso que lo cumpla del lado del hardware.**

## Pendiente de confirmar

- Lenguaje y stack previstos (¿Python por acceso a GPIO/I2C, o Node por coherencia con el resto?).
- Cómo se comunicará con `mara-os`: ¿como cliente WebSocket del brain reutilizando el protocolo v1, o como servidor MCP más en `mcp.json`?
- Si el Pironman 5 Pro Max requiere su propio SDK o expone sysfs.
- Calendario o prioridad dentro del proyecto. No hay issues ni ramas.

## Notas relacionadas

- [[Arquitectura del sistema]]
- [[Protocolo de eventos v1]]
- [[Estado y pendientes]]
