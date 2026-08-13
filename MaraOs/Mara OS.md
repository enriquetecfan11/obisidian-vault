---
title: Mara OS
type: document
tags:
  - mara-os
  - arquitectura
  - indice
project: MaraOS
status: active
date_created: 2026-08-13
date_modified: 2026-08-13
---
# Mara OS

Asistente personal propio, local y autoalojado. Corre sobre modelos locales vía Ollama, se controla desde Telegram o desde una interfaz visual, y está pensado para vivir en una Raspberry Pi 5.

Esta carpeta documenta **el software**: los tres repositorios que forman el sistema. No documenta la capa de agentes de IA (Mara, Atlas, Warren, Arvis), que vive en `OpenClaw/`.

## Los tres repositorios

| Repo | Rol | Ruta local | Estado |
|---|---|---|---|
| `mara-os` | El cerebro. Bot de Telegram, bucle del agente, memoria, MCP, TTS/STT | `~/Documents/dev/projects/mara-os` | Funcional, en desarrollo activo |
| `mara-ui` | La cara. Interfaz visual React para pantalla táctil | `~/Documents/dev/projects/mara-ui` | Funcional, conectada al cerebro |
| `mara-device` | El hardware. Abstracción de la Raspberry Pi | `~/Documents/dev/projects/mara-device` | **Solo especificación, sin código** |

Los tres están en GitHub bajo `enriquetecfan11/`.

## Índice

- [[Arquitectura del sistema]] — cómo encajan las tres capas, flujo completo y topología de red
- [[mara-os]] — el cerebro por dentro
- [[mara-ui]] — la interfaz por dentro
- [[mara-device]] — la capa de hardware (pendiente de implementar)
- [[Protocolo de eventos v1]] — el contrato entre el cerebro y la UI
- [[Memoria y contexto]] — memoria a corto y largo plazo, ficheros de contexto
- [[MCP y skills]] — servidores MCP, tools y detección de skills
- [[Puesta en marcha]] — runbook: arrancar el sistema completo
- [[Estado y pendientes]] — qué funciona, qué no, y dónde la doc del repo miente

## Cómo usar esta documentación

Estas notas son una **capa de síntesis**. El detalle profundo vive en el propio repo:

```
mara-os/docs/          # 20 ficheros: arquitectura, configuración, operaciones, referencia
mara-os/CLAUDE.md      # guía para agentes de código
mara-ui/README.md      # incluye el contrato de comunicación y el modo kiosko
```

Aviso importante: **`mara-os/docs/` tiene deriva significativa** respecto al código actual. Antes de fiarte de un dato de ahí, contrástalo con la tabla de [[Estado y pendientes]].
