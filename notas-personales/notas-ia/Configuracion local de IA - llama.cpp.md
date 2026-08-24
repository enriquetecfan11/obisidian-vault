---
title: configuracion-local-ia-llama-cpp
type: index
tags:
  - llama-cpp
  - inteligencia-artificial
  - ia-local
  - configuracion
  - personal
project: none
status: active
date_created: 2026-08-23
date_modified: 2026-08-23
---

# Configuración local de IA — llama.cpp

Índice de la configuración de `llama.cpp` para ejecutar modelos locales en este equipo.

## Notas

1. [[llama.cpp - Equipo y modelo recomendado]]
2. [[llama.cpp - Descargar modelos GGUF]]
3. [[llama.cpp - Ejecutar servidor e interfaz web]]
4. [[llama.cpp - Solución de problemas]]

## Inicio rápido

En PowerShell:

```powershell
llama-server `
  -m "C:\llama\models\Qwen3-14B-Uncensored.Q4_K_S.gguf" `
  -ngl all `
  -c 8192 `
  -np 1 `
  --host 127.0.0.1 `
  --port 8080 `
  --flash-attn on
```

Después abrir <http://localhost:8080>.
