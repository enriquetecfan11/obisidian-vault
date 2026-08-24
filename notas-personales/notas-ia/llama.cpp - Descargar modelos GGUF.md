---
title: llama-cpp-descargar-modelos-gguf
type: resource
tags:
  - llama-cpp
  - gguf
  - hugging-face
  - ia-local
  - personal
project: none
status: active
date_created: 2026-08-23
date_modified: 2026-08-23
---

# llama.cpp — Descargar modelos GGUF

Volver a [[Configuracion local de IA - llama.cpp]].

## Descargar con Hugging Face CLI

En PowerShell, con Hugging Face CLI instalado y autenticado si el repositorio lo requiere:

```powershell
huggingface-cli download huihui-ai/Qwen3-14B-Uncensored-GGUF Qwen3-14B-Uncensored.Q4_K_S.gguf --local-dir "C:\llama\models" --local-dir-use-symlinks False
```

El archivo esperado quedará en:

```text
C:\llama\models\Qwen3-14B-Uncensored.Q4_K_S.gguf
```

El archivo debe estar en formato `GGUF`, que es el formato que carga `llama.cpp`.

Siguiente paso: [[llama.cpp - Ejecutar servidor e interfaz web]].
