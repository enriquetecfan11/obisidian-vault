---
title: "Mi IA local: el mapa de montaje completo"
source: "https://comunidad.eriktaveras.com/resources/mi-ia-local-mapa-de-montaje/"
author:
  - "[[Erik Taveras]]"
published: 2026-10-13
created: 2026-10-17
description: "Comunidad de desarrollo, automatización y AI. Aprende Python, JavaScript, automatización y más con Erik Taveras. Cursos, foro y recursos gratuitos."
tags:
  - "clippings"
---
## 4 modelos, una máquina, 0 suscripciones: así trabaja mi IA mientras duermo

Esto es exactamente lo que corre en mi homelab: 4 modelos en una sola máquina, conectados a [Hermes](https://github.com/NousResearch/hermes-agent), trabajando de 12 de la noche a 7 de la mañana. Sin nube y sin suscripciones.

La pregunta que me llega cada semana es “qué modelo uso”. La respuesta corta: no es un modelo, es un reparto. Uno grande que piensa, uno pequeño que filtra, uno que recuerda y uno que escucha. Aquí tienes las 5 partes que prometí en el reel, con los comandos que uso yo.

---

## Parte 1 — El mapa de montaje

**Si solo vas a leer una cosa, que sea esta.**

```bash
┌──────────────────────────────────────────┐
                 │  GMKtec EVO-X2 · Ryzen AI Max+ 395       │
                 │  128 GB · 64 GB asignados a la GPU       │
                 │                                          │
Hermes ────────► │  Ornith-1.5 35B   :8081  el cerebro      │
(7 perfiles)     │  Qwen3.5 4B       :8082  rápido/portero  │
                 │  Qwen3-Embedding  :8084  la memoria (RAG)│
n8n ───────────► │  Whisper turbo    bajo demanda (audio)   │
                 └──────────────────────────────────────────┘
                                  │
                 Mattermost (self-hosted): un canal por perfil
                 + #avisos-ventas para los posibles clientes
```

- **Una sola máquina** con memoria unificada: CPU y GPU comparten la RAM. En la BIOS le doy 64 GB a la GPU (Radeon 8060S integrada).
- **Los 4 modelos activos ocupan ~39 GB** de esa memoria.
- **Todo habla por API compatible con OpenAI** (`llama-server` de [llama.cpp](https://github.com/ggml-org/llama.cpp)). Hermes, n8n o cualquier app los usan como si fueran un proveedor más.
- **Las conversaciones también son locales:** los agentes me hablan por [Mattermost](https://mattermost.com/) en mi propio servidor, no por Discord ni Telegram.

---

## Parte 2 — Los modelos

| Modelo | Tamaño | Para qué lo uso | Cuánto rinde en mi equipo |
| --- | --- | --- | --- |
| **Ornith-1.5 35B-A3B** (Q4\_K\_M) | 35B, solo 3B activos por token (MoE) | El cerebro: razona, decide herramientas, interpreta resultados y escribe | ~100 tok/s en total con 4 conversaciones a la vez; 262.144 tokens de contexto |
| **Qwen3.5 4B** (Q4\_K\_M) | 4B | El rápido: clasifica comentarios (cliente / marca / pregunta / spam) y hace de portero de comandos | ~0,6 s por comentario |
| **Qwen3-Embedding 0.6B** (Q8\_0) | 0,6B | Convierte correos, publicaciones y notas en vectores para buscar por significado | ~30 ms por búsqueda en 800+ documentos |
| **Whisper large-v3-turbo** | — | Transcribe audio y vídeo (tendencias de YouTube, llamadas, mis propios vídeos) | ~14–19× tiempo real: 1 hora en 3–4 minutos |

> **Por qué este reparto:** el modelo grande solo hace lo que necesita cabeza. Todo lo repetitivo y de volumen (filtrar, clasificar, aprobar) lo hace el pequeño, que responde al instante y no le quita turno al cerebro.

Si quieres ir a fondo con Ornith (qué tamaño te toca según tu RAM), tienes la guía aparte: [Ornith en tu homelab](https://comunidad.eriktaveras.com/resources/ornith-en-tu-homelab/).

---

## Parte 3 — Cómo instalarlos

Lo hago todo con **llama.cpp compilado con Vulkan** (funciona con la GPU integrada de AMD sin ROCm) y **[whisper.cpp](https://github.com/ggml-org/whisper.cpp)**. Linux (Ubuntu).

### 3.1 Compilar llama.cpp con Vulkan

```bash
sudo apt install -y build-essential cmake git libvulkan-dev glslc
git clone https://github.com/ggml-org/llama.cpp && cd llama.cpp
cmake -B build -DGGML_VULKAN=ON -DCMAKE_BUILD_TYPE=Release
cmake --build build -j
```

### 3.2 Descargar los modelos

Busca en [Hugging Face](https://huggingface.co/) el **GGUF** de cada modelo y bájalo a `~/models/<nombre>/`:

- Ornith-1.5-35B → `Q4_K_M` (+ el `mmproj` si quieres visión). Está en [ornith-ai/Ornith-1.5-35B-A3B-GGUF](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B-GGUF).
- Qwen3.5-4B → `Q4_K_M`
- Qwen3-Embedding-0.6B → `Q8_0`

```bash
pip install -U "huggingface_hub[cli]"
huggingface-cli download <repo-del-gguf> <archivo>.gguf --local-dir ~/models/<nombre>
```

### 3.3 Levantar cada modelo (los comandos que uso yo)

Crea una API key propia y guárdala en `~/.config/ia-local/api-key`. Todos los servidores la piden.

**Ornith (el cerebro), puerto 8081**

```bash
llama-server -m ~/models/ornith-1.5-35b/Ornith-1.5-35B-Q4_K_M.gguf \
  --alias ornith-1.5-35b --host 0.0.0.0 --port 8081 \
  --api-key-file ~/.config/ia-local/api-key \
  -c 262144 --parallel 4 --jinja --reasoning on \
  -ngl 999 -fa on -b 2048 -ub 512 --metrics
```

**Qwen3.5 4B (rápido / portero), puerto 8082**

```bash
llama-server -m ~/models/qwen3.5-4b/Qwen3.5-4B-Q4_K_M.gguf \
  --alias qwen3.5-4b --port 8082 --api-key-file ~/.config/ia-local/api-key \
  -c 65536 --jinja --reasoning off -ngl 999 -fa on --parallel 2 --kv-unified
```

**Qwen3-Embedding (memoria), puerto 8084**

```bash
llama-server -m ~/models/qwen3-embedding-0.6b/Qwen3-Embedding-0.6B-Q8_0.gguf \
  --alias qwen3-embedding-0.6b --host 127.0.0.1 --port 8084 \
  --api-key-file ~/.config/ia-local/api-key \
  --embedding --pooling last -c 8192 -b 8192 -ub 8192 -ngl 999 -fa on --parallel 2
```

**Whisper (bajo demanda)**

```bash
git clone https://github.com/ggml-org/whisper.cpp && cd whisper.cpp
cmake -B build -DGGML_VULKAN=ON && cmake --build build -j
./models/download-ggml-model.sh large-v3-turbo
./build/bin/whisper-cli -m models/ggml-large-v3-turbo.bin -l es -f audio.wav
```

### 3.4 Que arranquen solos

Cada `llama-server` va en un servicio de **systemd de usuario** (`~/.config/systemd/user/ia-ornith.service`, `ia-aux.service`, `ia-embed.service`) con `Restart=always`. Después:

```bash
systemctl --user daemon-reload
systemctl --user enable --now ia-ornith ia-aux ia-embed
loginctl enable-linger $USER     # que sigan vivos sin sesión abierta
```

**Comprueba que todo está arriba:**

```bash
curl -s http://localhost:8081/v1/models -H "Authorization: Bearer $(cat ~/.config/ia-local/api-key)"
```

---

## Parte 4 — Las conexiones con Hermes

### 4.1 El modelo principal

En `~/.hermes/config.yaml`, Ornith como proveedor personalizado:

```bash
model:
  provider: custom
  base_url: http://localhost:8081/v1
  default: ornith-1.5-35b
  api_key: <tu-api-key>
  context_length: 262144     # Hermes rechaza modelos con menos de 64K
```

### 4.2 Las tareas auxiliares van al modelo pequeño

Aprobaciones de comandos, títulos y MCP no necesitan al cerebro:

```bash
auxiliary:
  approval:          # el portero: decide si un comando es delicado y te pregunta antes
    provider: custom
    base_url: http://localhost:8082/v1
    model: qwen3.5-4b
  title_generation:
    provider: custom
    base_url: http://localhost:8082/v1
    model: qwen3.5-4b
  mcp:
    provider: custom
    base_url: http://localhost:8082/v1
    model: qwen3.5-4b
```

### 4.3 Los 7 perfiles (cada uno con su canal y sus permisos)

| Perfil | Qué hace | Lo que NO puede hacer |
| --- | --- | --- |
| `negocio` | Correo, CRM, marcas, cotizaciones | Enviar correos (solo deja borradores) |
| `contenido` | Instagram, comunidad, noticias, guiones | Publicar en Instagram |
| `homelab` | Vigila la infraestructura | Apagar contenedores |
| `clientes` | Datos sensibles de clientes | Web, navegador, visión |
| `tecnico`, `critico`, `sintesis` | El consejo: opinan, verifican y resumen | Nada fuera del consejo |

> Crea cada uno con `hermes profile create <nombre>` y dale **solo** las herramientas que necesita. Ese es todo el truco de la seguridad: un perfil no puede hacer lo que no tiene.

### 4.4 La memoria (RAG)

Un script indexa cada noche lo nuevo (correos, posts de IG, notas, transcripciones) con el modelo de embeddings y lo guarda en SQLite. Hermes lo consulta con una herramienta MCP `buscar` y encuentra cosas **por significado**, no por palabra exacta. Cada perfil solo busca en su colección.

### 4.5 n8n: el clasificador de comentarios

El flujo “Clasificador de comentarios (Qwen 4B) → #avisos-ventas” en [n8n](https://n8n.io/):

```bash
Comentario de IG/FB → extraer texto → Qwen 4B (HTTP a :8082) → leer etiqueta
   → guardar → ¿posible cliente o marca? → aviso en #avisos-ventas
```

Prompt que uso para clasificar:

> Clasifica el comentario de Instagram en una palabra. **cliente**: pide que le hagan o le monten algo, o pregunta precio. **marca**: una empresa propone colaborar. **pregunta**: duda técnica que quiere resolver por su cuenta. **spam**: promesas de dinero o enlaces. Responde solo la palabra.

Con `temperature: 0` y `max_tokens: 5` tarda menos de un segundo.

---

## Parte 5 — Las tareas que puedes adaptar a tu sistema

**La regla:** lo pesado va de madrugada y **una sola tarea a la vez**. A las 7:00 se entrega todo junto en un parte por perfil.

| Hora | Tarea | Perfil |
| --- | --- | --- |
| 0:30 | **Focus group:** 50 personajes, sacados de comentarios reales, critican lo que pegues (hook, precio, guion, landing) | contenido |
| 1:00 | **Tendencias:** vídeos de la semana de YouTube sobre tus temas, transcritos con Whisper, con ideas | contenido |
| 2:00 | **Radar diario de IA** | contenido |
| 2:30 | **Indexar la memoria** (solo lo nuevo) | default |
| 3:00 | **Producir contenido:** reel + LinkedIn, 3 versiones de cada uno; el crítico las puntúa y elige | contenido |
| 4:15 | **Enriquecer el CRM:** propone datos y hasta 3 borradores de reactivación | negocio |
| 5:00 | **Barrido de correo:** hasta 5 borradores marcados | negocio |
| 5:00 | **Resumen del homelab** (solo si hay que actuar) | homelab |
| 6:15 | **Sintetizar el parte** de cada perfil | default |
| 6:45 | **Bitácora** del día en el vault de notas | default |
| 7:00 | **Entregar** el parte en cada canal | default |

### De día, solo lo ligero

- **Turnos de respuestas en la comunidad** (máx. 5 por turno; lo delicado se escala a mí)
- **Pasada ligera de correo** por la tarde
- **Clasificador de comentarios** en tiempo real (n8n + Qwen 4B)
- **Vigía de sitios** cada 15 minutos y **salud de la máquina** cada 30 (sin IA)

### Cómo adaptarlo a tu negocio

Quédate con 3 tareas para empezar. Las que más rinden:

1. **Correo:** borradores, nunca envío automático.
2. **Clasificar mensajes o comentarios entrantes:** el modelo pequeño basta.
3. **El parte de las 7:00:** un resumen de lo que pasó y lo que necesita tu atención.

---

## Los errores que me costaron tiempo

- **Hermes exige 64K de contexto o más.** Si el servidor arranca con menos, falla sin explicar mucho.
- **No pongas dos trabajos pesados del mismo perfil a la vez** (`max_parallel_jobs: 1`). Se pisan y los dos van lentos.
- **Ornith puede responder sin razonar** (`"chat_template_kwargs": {"enable_thinking": false}` por petición): tarda la mitad en tareas simples.
- **Nada que publique o envíe va en automático.** Los agentes dejan borradores con bandera y yo apruebo.

---

## Tu primera semana

1. **Día 1:** compila llama.cpp con Vulkan y levanta el modelo pequeño. Comprueba con el `curl` de la Parte 3.
2. **Día 2:** conecta n8n al modelo pequeño y monta el clasificador de comentarios o de correos.
3. **Día 3:** si tu RAM lo permite, levanta el modelo grande y conéctalo a Hermes.
4. **Día 4:** crea un solo perfil con pocas herramientas y una tarea de madrugada.
5. **Día 5:** mira el parte de las 7:00 y ajusta el prompt.
6. **Días 6–7:** añade la segunda y la tercera tarea. Nada más hasta que esas tres funcionen solas.

---

## Recursos

- [llama.cpp](https://github.com/ggml-org/llama.cpp): el servidor de todos los modelos.
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp): transcripción local con Vulkan.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent): el agente con perfiles y tareas programadas.
- [Ornith en Hugging Face](https://huggingface.co/ornith-ai): los GGUF del cerebro.
- [n8n](https://n8n.io/): los flujos que usan los modelos como un proveedor más.
- [Mattermost](https://mattermost.com/): el chat self-hosted donde me hablan los agentes.

---

## Última cosa

No hace falta mi máquina para empezar. Un modelo pequeño en cualquier PC ya te clasifica comentarios y te deja borradores. Lo grande llega después. **La IA local no es un modelo, es un reparto: el grande piensa, el pequeño filtra y tú apruebas.**

*Erik Taveras — Taveras Solutions, LLC*

Si lo montas, etiquétame y cuéntame con qué equipo (RAM y GPU) y qué tareas pusiste a correr.