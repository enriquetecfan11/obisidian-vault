---
title: "Ornith en tu homelab — instalarlo y conectarlo a n8n y a Hermes"
type: resource
tags:
  - ia
  - ia-local
  - llama-cpp
  - ollama
  - n8n
status: active
project: none
date_created: 2026-10-17
date_modified: 2026-10-17
source: https://comunidad.eriktaveras.com/resources/ornith-en-tu-homelab/
---
# Ornith en tu homelab — instalarlo y conectarlo a n8n y a Hermes

> Guía de Erik Taveras (11-oct-2026) para poner **Ornith-1.5** (familia de modelos abiertos, licencia MIT, según el autor) a servir una API LLM en tu red local y conectarla a **n8n** y a **Hermes Agent**. Cubre elección de tamaño/equipo, Ollama vs llama.cpp, exponerlo de forma segura y ajustes finos.

> Nota: los nombres, tamaños y benchmarks de Ornith-1.5 son los que reporta el autor / la ficha del modelo; no están verificados aquí de forma independiente.

## Qué modelo según tu equipo

| Tu equipo | Tamaño | Qué esperar |
| --- | --- | --- |
| 8-16 GB RAM, Mac M1/M2 base | `Ornith-1.5-9B` en Q4 | Chat, resúmenes, clasificar, respuestas cortas |
| 32 GB unificada o GPU 24 GB | `Ornith-1.5-35B-A3B` en Q4_K_M (~21,7 GB) | Agentes, código, n8n |
| Strix Halo / Mac 64-128 GB | 35B-A3B con contexto largo y varias peticiones | 128K-256K contexto, 4 tareas a la vez |
| Servidor con varias GPU | `Ornith-1.5-397B` | Empresas, no homelab normal |

El 35B es **mezcla de expertos (MoE)**: 35B de parámetros, pero ~3B activos por token → rápido como uno de 3B, pesado como uno de 35B (hay que cargar el modelo entero en memoria). Soporta imágenes (`mmproj`) y hasta 262.144 tokens de contexto (según el autor).

## Elegir el archivo (GGUF)

- **Q4_K_M**: el punto dulce y recomendado.
- **Q5/Q6**: mejor, bastante más pesado.
- **Q3 o menos**: cabe en menos pero falla en tareas largas → no para agentes.

Regla de bolsillo: tamaño del archivo **+ 4-10 GB** para contexto y sistema. En Mac hay versiones **MLX** más rápidas.

## Camino rápido: Ollama (~10 min)

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run hf.co/ornith-ai/Ornith-1.5-35B-A3B-GGUF:Q4_K_M
```

API en `http://127.0.0.1:11434/v1` (compatible OpenAI). Límite: Ollama no trae API key.

## Camino fino: llama.cpp (más control y velocidad)

Binario según GPU (Vulkan para AMD/Intel, CUDA, o Metal en Mac). Crear API key:

```bash
mkdir -p ~/.config/ia-local
openssl rand -hex 24 | sed 's/^/sk-local-/' > ~/.config/ia-local/api-key
chmod 600 ~/.config/ia-local/api-key
```

Arrancar servidor:

```bash
~/llama.cpp/current/llama-server \
  -hf ornith-ai/Ornith-1.5-35B-A3B-GGUF:Q4_K_M \
  --alias ornith \
  --host 127.0.0.1 --port 8081 \
  --api-key-file ~/.config/ia-local/api-key \
  -c 65536 --jinja -ngl 999 -fa on \
  --temp 0.6 --top-p 0.95 --top-k 20
```

Claves: `--jinja` es **imprescindible** para que funcionen las herramientas (tool calls); `-c 65536` (Hermes exige mínimo 64K); `-ngl 999` manda todo a GPU; `-fa on` flash attention. Se puede dejar como servicio systemd de usuario (`loginctl enable-linger`). En AMD integrada (Strix Halo, 780M) subir en BIOS la memoria reservada a GPU.

## Exponerlo a la red sin regalarlo a internet

1. **Nunca** abrir el puerto en el router.
2. Usar **Tailscale** (IP `100.x`).
3. Cambiar a `--host 0.0.0.0` y cerrar el puerto a la LAN con firewall, dejando pasar solo la interfaz de Tailscale:

```bash
sudo ufw allow in on tailscale0
sudo ufw deny 8081/tcp
sudo ufw enable
```

Regla: la API key protege de un vecino curioso; Tailscale y el firewall protegen de internet. Hacen falta las dos.

## Conectar a n8n

n8n lo trata como OpenAI, sin nodo especial. Credencial OpenAI → API Key (la del archivo, o cualquier texto con Ollama) → **Base URL** `http://100.x.x.x:8081/v1`. Si n8n va en Docker en la misma máquina, usar `host.docker.internal` (con `extra_hosts: host-gateway` en Linux). En un nodo AI Agent / Basic LLM Chain, elegir la credencial y escribir el modelo a mano (`ornith`).

**Ejemplo que usa el autor:** responder comentarios de Instagram (Schedule → Graph API → filtrado en Code → Basic LLM Chain que devuelve `{sentimiento, respuesta}` → guarda → POST reply). Claves aprendidas: temperatura 0.2-0.3 para tareas repetitivas, respuestas cortas (~90-140 caracteres), dar ficha con datos reales, `Retry On Fail` con modelo cloud de respaldo, y ritmo humano (1 cada 2-4 min con tope diario) para no ser limitado por Meta.

## Conectar a Hermes Agent

`~/.hermes/config.yaml`, bloque `model:` con `provider: "custom"`, `base_url: http://127.0.0.1:8081/v1`, `api_key`, y `context_length: 65536` (debe coincidir con el `-c` del servidor).

**Tareas programadas (cron)** — donde un modelo local brilla porque no se paga por token:

```bash
hermes cron create "0 7 * * *" "Resumen de correos..." --name resumen-diario --deliver telegram
hermes cron list
hermes cron run resumen-diario
```

Necesita el **gateway** de Hermes corriendo y revisar la **zona horaria** del equipo.

## Ajustes que mueven la aguja

Razonamiento (pedir respuestas directas / `--reasoning off`), paralelo (`--parallel 4 --kv-unified`), contexto (`-c` 131072/262144), visión (`--mmproj`). Velocidad de referencia del autor: ~30 tokens/s en Ryzen AI Max+ 395 con Vulkan (un denso de 27B le daba 9).

## Errores que cometió el autor

Olvidar `--jinja` (fallan las herramientas); contexto < 64K con Hermes; `127.0.0.1` dentro de Docker; memoria de GPU en el mínimo en AMD integrada; dos modelos grandes a la vez; exponer el puerto a internet «un ratito»; creerse los benchmarks a ciegas.

## Relacionado

- [[MOC IA Local]] — índice de IA local (llama.cpp y Ollama)
- [[llama.cpp - Ejecutar servidor e interfaz web]]
- [[llama.cpp - Equipo y modelo recomendado]]
- [[Ollama Docker]] — Ollama en Docker para n8n
- [[MOC Automatizaciones]] — flujos n8n que consumen el modelo
- [[Company brain - El cerebro de tu empresa]] — el conocimiento (cerebro) que el motor local sirve
