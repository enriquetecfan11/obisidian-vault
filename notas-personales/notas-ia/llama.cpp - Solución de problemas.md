---
title: llama-cpp-solucion-de-problemas
type: resource
tags:
  - llama-cpp
  - troubleshooting
  - gpu
  - ia-local
  - personal
project: none
status: active
date_created: 2026-08-23
date_modified: 2026-08-23
---

# llama.cpp — Solución de problemas

Volver a [[Configuracion local de IA - llama.cpp]].

## El comando no existe

Si PowerShell muestra que `llama-server` no se reconoce, usar la ruta completa a `llama-server.exe` o añadir la carpeta del ejecutable al `PATH`.

## Falta memoria de GPU

Probar en este orden:

1. Bajar el contexto de `-c 8192` a `-c 4096`.
2. Reducir las capas cargadas en GPU, por ejemplo de `-ngl all` a `-ngl 35`.
3. Usar una cuantización o un modelo más pequeño.

## El puerto está ocupado

Usar `--port 8081` y abrir <http://localhost:8081>.

## La interfaz no responde

- Esperar a que termine de cargar el modelo.
- Revisar la ventana del servidor por si muestra un error.
- Probar `Invoke-RestMethod http://localhost:8080/health`.
- Confirmar que se abrió el mismo puerto indicado en el comando.

## La generación es muy lenta

- Confirmar que la salida indica que las capas se descargaron a la GPU.
- Cerrar aplicaciones que estén usando mucha VRAM.
- Evitar el modelo de 27B en este equipo.
- Para priorizar velocidad, usar un modelo de 8B/9B en `Q4_K_M` o `Q5_K_M`.
