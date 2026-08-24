---
title: llama-cpp-servidor-interfaz-web
type: resource
tags:
  - llama-cpp
  - servidor
  - interfaz-web
  - ia-local
  - personal
project: none
status: active
date_created: 2026-08-23
date_modified: 2026-08-23
---

# llama.cpp — Ejecutar servidor e interfaz web

Volver a [[Configuracion local de IA - llama.cpp]].

## Ejecutar el servidor

Abrir PowerShell y ejecutar:

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

Si `llama-server` no está en el `PATH`, usar la ruta del ejecutable. Por ejemplo, desde la carpeta de `llama.cpp`:

```powershell
.\build\bin\Release\llama-server.exe `
  -m "C:\llama\models\Qwen3-14B-Uncensored.Q4_K_S.gguf" `
  -ngl all `
  -c 8192 `
  -np 1 `
  --host 127.0.0.1 `
  --port 8080 `
  --flash-attn on
```

## Abrir la interfaz

Cuando termine de cargar el modelo, abrir <http://localhost:8080>.

La interfaz web viene integrada en `llama-server`; no hace falta instalar otra aplicación.

## Parámetros

- `-m`: ruta del modelo GGUF.
- `-ngl all`: intenta cargar en la GPU todas las capas posibles.
- `-c 8192`: contexto máximo de 8.192 tokens.
- `-np 1`: una secuencia paralela.
- `--host 127.0.0.1`: acceso solamente desde este ordenador.
- `--port 8080`: puerto de la interfaz web y la API.
- `--flash-attn on`: activa Flash Attention cuando está disponible.

## Comprobar el estado

La salida debería mostrar que todas, o casi todas, las capas están en la GPU:

```text
offloaded 41/41 layers to GPU
```

Desde otra ventana de PowerShell:

```powershell
Invoke-RestMethod http://localhost:8080/health
```

## API compatible con OpenAI

El endpoint de chat es `http://localhost:8080/v1/chat/completions`.

## Detener el servidor

Volver a su ventana de PowerShell y pulsar `Ctrl + C`.

## Acceder desde otro dispositivo de la red

Cambiar `--host 127.0.0.1` por `--host 0.0.0.0`. Desde el otro dispositivo, abrir la IP local del PC, por ejemplo `http://192.168.1.50:8080`. Puede ser necesario permitir el puerto 8080 en el firewall de Windows.

No exponer el puerto directamente a Internet.
