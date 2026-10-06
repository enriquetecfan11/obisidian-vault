---
type: article
tags:
  - ia
status: active
pipeline: raw
created: 2026-10-06
updated: 2026-10-06
source: https://ai.manz.dev/learn/setup/opencode-orquestador/
promotes_to:
title: OpenCode — orquestador de agentes (local + barato + frontera)
project: none
date_created: 2026-10-06
date_modified: 2026-10-06
---
# OpenCode — orquestador de agentes (local + barato + frontera)

> Guía de ManzDev para montar un agente orquestador en OpenCode V2: el modelo frontera decide y delega; el trabajo mecánico lo hacen un modelo local (llama.cpp) o un modelo nube barato. Ahorro de coste, menos contexto en el modelo caro y nada sensible sale del equipo.

## Resumen ejecutivo

La idea central es no pagar un modelo frontera por leer ficheros, renombrar variables o formatear. Casi todo el trabajo de un agente es mecánico, así que se enruta a modelos ~100x más baratos o a un modelo local gratuito. El orquestador solo razona, descompone y coordina mediante subagentes con contexto limpio: el padre recibe únicamente el resumen final, no los 40 ficheros leídos.

## TL;DR

- 3 agentes: `orquestador` (frontera, `mode: primary`), `local` (llama.cpp, coste cero), `barato` (Luna / DeepSeek Flash en nube).
- El orquestador no toca ficheros ni ejecuta shell: solo lanza subagentes `local` y `barato`.
- Los permisos se evalúan en orden y gana el último: denegar todo y luego permitir solo lo necesario.
- Un subagente **sin `model` hereda el del padre**: fijar siempre el modelo o se pierde el ahorro.
- llama.cpp necesita `--jinja` para que el modelo local pueda pedir tools; cuantizar el KV cache (`-ctk`/`-ctv q4_0`) puede degradar el tool-calling.
- Pasar rutas, no contenidos; evitar `@fichero.md` en el prompt del padre.

## Los 3 agentes

| Agente | Modelo (según el artículo) | Dónde corre | Cuándo usarlo | Coste |
| --- | --- | --- | --- | --- |
| `orquestador` | frontera (ej. `gpt-6-astra`) | nube | diseño, descomponer, decidir, responder | alto |
| `barato` | `gpt-6-luna` / `deepseek-v4-flash` | nube | renombrados, formateo, redacción simple, referencias | bajo |
| `local` | GGUF en llama.cpp (ej. Qwen 35B) | tu máquina | leer, buscar, edición masiva, refactors mecánicos | cero |

Precios citados por millón de tokens (entrada/salida): `gpt-6-astra` 10 $/50 $, `deepseek-v4-flash` 0,15 $/0,6 $, `gpt-6-luna` 0,1 $/0,5 $. Si el 80 % de los tokens cae en el modelo barato, la factura cambia radicalmente; lo local además da privacidad.

## Orquestador: definición

Archivo `~/.config/opencode/agents/orquestador.md` (global) o `.opencode/agents/<nombre>.md` (por proyecto; si va en subcarpeta, el nombre incluye la ruta). Para que sea el agente por defecto: `"default_agent": "orquestador"` en `opencode.jsonc`.

```md
---
description: "Coordina el trabajo y delega a otros modelos baratos/locales"
mode: primary
model: openai/gpt-6-astra#high
---
```

Permisos clave: denegar `edit`, `write`, `shell` y `subagent: *`, y permitir solo `subagent: local` y `subagent: barato`. Reglas del system prompt: nunca hacer la tarea él mismo, reducir cada subtarea a un objetivo verificable, pasar rutas en vez de contenidos, desempatar hacia `local`, y lanzar en paralelo lo independiente (`background: true`).

Enrutado sugerido: `nano`/`small` → `local`; `medium`/`large` → `barato`. Decisiones de arquitectura: preguntar al usuario con la tool `question` antes de lanzar.

## Agente local (llama.cpp)

Servidor con plantilla de chat Jinja para tool-calling:

```bash
llama-server \
  -m Qwen3.6-35B-A3B-UD-IQ2_XXS.gguf \
  --alias qwen-local \
  --jinja -fa on --ctx-size 32768 \
  --host 0.0.0.0 --port 8080
```

En `opencode.jsonc` se registra como provider compatible con la API de OpenAI (`baseURL: http://localhost:8080/v1`) con `capabilities.tools: true`. El agente `local.md` (`mode: subagent`, `steps: 40`) prohíbe `subagent`, `webfetch`, `websearch` y el acceso a `.env`: así nada sale del equipo aunque el modelo lo intente. Devuelve resumen de 15 líneas máximo con rutas y líneas, nunca el contenido completo.

## Agente barato (nube)

`barato.md` (`mode: subagent`, `model: openai/gpt-6-luna#low`, `steps: 12`). El sufijo `#low` baja el esfuerzo de razonamiento; con `/models` se comprueban las variantes del modelo. `edit` y `shell` en `ask` como red de seguridad hasta ganar confianza, luego `allow`. Responde en 10 líneas máximo, sin justificar el porqué.

## Probar y vigilar

1. Abrir OpenCode con el agente `orquestador` y pedir algo que obligue a delegar (no puede editar nada él mismo).
2. Verificar la llamada a `subagent` con el agente y modelo correctos; el hijo devuelve resumen, el padre decide.
3. Forzar agentes a mano (`usa el subagente local para esto`) y probar dos refactors en paralelo.
4. Medir con `opencode stats` (tokens/sesión, coste por modelo) y `pnpx tokscale` para análisis fino.

Señales de que falla: el coste no baja (el orquestador hace el trabajo él mismo → reforzar el prompt), todo el coste viene de un modelo (un hijo heredó el modelo del padre → revisar `model`), o la sesión del padre es enorme (se están pegando contenidos → pasar rutas).

## Avisos del artículo

- Escrito para **OpenCode V2**: `permissions` (no `permission`), acciones `shell` y `subagent` (no `bash`/`task`), y el campo `tools` ya no existe.
- Los planes gratuitos de OpenCode pueden dar `Error: Opencode's free tier can only be used from within OpenCode` al abusar de subagentes: usar modelos de pago para orquestar.
- Los nombres de modelo (`gpt-6-astra`, `gpt-6-luna`, `deepseek-v4-flash`, Qwen 3.6 35B) son los citados en el artículo; no verificados aquí contra el catálogo actual.

## Relacionado

- [[MOC Inteligencia Artificial]] — índice del área
- [[MOC IA Local]] — llama.cpp en local
- [[Ollama Docker]] — alternativa de runtime local en contenedor
