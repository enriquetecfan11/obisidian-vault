---
title: "Ornith en tu homelab: instálalo y conéctalo a n8n y a Hermes"
source: "https://comunidad.eriktaveras.com/resources/ornith-en-tu-homelab/"
author:
  - "[[Erik Taveras]]"
published: 2026-10-11
created: 2026-10-17
description: "Comunidad de desarrollo, automatización y AI. Aprende Python, JavaScript, automatización y más con Erik Taveras. Cursos, foro y recursos gratuitos."
tags:
  - "clippings"
status: procesado
promoted_to: "[[Ornith en tu homelab - instalar y conectar a n8n y Hermes]]"
---
## Pon Ornith-1.5 a trabajar en tu homelab y conéctalo a n8n y a Hermes

Cada vez que hablo de IA local me hacen la misma pregunta: “Sí, pero, ¿sirve para algo de verdad o es un juguete?”. Ornith-1.5 es la primera familia open source con la que la respuesta es fácil: el modelo de 35B corre en un mini PC y aguanta trabajo agéntico real. Esta guía te lleva de cero a tener Ornith sirviendo una API en tu red, protegida, y conectada a n8n y a Hermes. Sirve tengas el equipo que tengas: hay un tamaño para cada máquina.

**Si solo vas a leer una cosa, que sea esta tabla.**

| Tu equipo | Tamaño de Ornith | Qué esperar |
| --- | --- | --- |
| Laptop o PC con **8–16 GB** de RAM, Mac M1/M2 base | `Ornith-1.5-9B` en Q4 | Chat, resúmenes, clasificar texto, respuestas cortas |
| Mini PC o Mac con **32 GB** de memoria unificada, o GPU de **24 GB** | `Ornith-1.5-35B-A3B` en Q4\_K\_M (~21.7 GB) | Agentes, código, n8n. Contexto moderado |
| Ryzen AI Max (Strix Halo), Mac con **64–128 GB** | `Ornith-1.5-35B-A3B` en Q4\_K\_M con contexto largo y varias peticiones en paralelo | Lo mismo, pero con 128K–256K de contexto y 4 tareas a la vez |
| Servidor con varias GPU o cientos de GB de RAM | `Ornith-1.5-397B` | Para equipos y empresas, no para un homelab normal |

---

## Parte 1 — Qué es Ornith-1.5 y qué no

Ornith-1.5 es una familia de modelos abiertos con licencia MIT, publicada por [ornith-ai en Hugging Face](https://huggingface.co/ornith-ai). Tiene tres tamaños: 9B, 35B-A3B y 397B. El que importa para un homelab es el del medio.

### Por qué el de 35B cabe en un mini PC

Es una **mezcla de expertos** (MoE). Tiene 35B de parámetros en total, pero en cada token solo trabajan unos 3B. Eso le da la velocidad de un modelo chico. La trampa: **la memoria tiene que cargar el modelo entero**. Rápido como uno de 3B, pesado como uno de 35B.

### Los números, con su asterisco

| Prueba | Ornith-1.5-35B-A3B | Qwen3.5-397B |
| --- | --- | --- |
| Terminal-Bench 2.1 (Terminus-2) | **67.8** | 53.5 |
| SWE-bench Verified | **79** | 76.4 |

Son los números que publica el propio equipo en la [ficha del modelo](https://huggingface.co/ornith-ai/Ornith-1.5-35B). Están medidos en tareas de terminal y código, que es justo el trabajo de un agente. No significa que gane en todo. Trátalos como una señal para probarlo, no como una promesa.

Además entiende imágenes (trae su archivo `mmproj` de visión) y soporta hasta 262,144 tokens de contexto.

**Acción:** mira cuánta memoria tienes (`free -h` en Linux, “Acerca de este Mac” en macOS) y elige tu fila en la tabla de arriba.

---

## Parte 2 — Elige el archivo correcto

Los modelos se bajan en formato **GGUF**, cuantizados. La cuantización recorta precisión para que pese menos.

- **Q4\_K\_M**: el punto dulce. Es la que uso y la que recomiendo para empezar.
- **Q5/Q6**: un poco mejor, bastante más pesada. Solo si te sobra memoria.
- **Q3 o menos**: cabe en menos, pero el modelo empieza a equivocarse en tareas largas. No lo uses para agentes.

Regla de bolsillo: necesitas el tamaño del archivo **más 4–10 GB** para el contexto y el sistema. El Q4\_K\_M de 35B pesa ~21.7 GB, así que con 32 GB vas justo y con 64 GB vas holgado.

Repos oficiales:

- [Ornith-1.5-9B-GGUF](https://huggingface.co/ornith-ai/Ornith-1.5-9B-GGUF)
- [Ornith-1.5-35B-A3B-GGUF](https://huggingface.co/ornith-ai/Ornith-1.5-35B-A3B-GGUF)
- En Mac también hay versiones **MLX** (por ejemplo `Ornith-1.5-9B-MLX-4bit`) que van más rápido en Apple Silicon.

**Acción:** anota el repo y la cuantización que te tocan. Los vas a usar en la parte 3 o en la 4.

---

## Parte 3 — Camino rápido: Ollama (10 minutos)

Si es tu primera vez con IA local, empieza aquí. Ollama baja el modelo y te da una API compatible con OpenAI sin configurar nada.

```bash
# Linux (en macOS y Windows baja el instalador de ollama.com)
curl -fsSL https://ollama.com/install.sh | sh

# 35B (o cambia a Ornith-1.5-9B-GGUF si tienes poca memoria)
ollama run hf.co/ornith-ai/Ornith-1.5-35B-A3B-GGUF:Q4_K_M
```

La primera vez tarda porque baja ~22 GB. Cuando veas el prompt, hazle una pregunta. Si responde, ya tienes IA local.

La API queda en `http://127.0.0.1:11434/v1`. Pruébala:

```bash
curl http://127.0.0.1:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"hf.co/ornith-ai/Ornith-1.5-35B-A3B-GGUF:Q4_K_M",
       "messages":[{"role":"user","content":"Dime en una frase qué es un homelab"}]}'
```

**Su límite:** Ollama no trae API key. Por defecto solo escucha en tu propia máquina, y está bien que así sea. Si lo vas a usar desde otra máquina, lee la parte 5 antes de abrirlo.

**Acción:** si este curl responde, puedes saltar a la parte 5.

---

## Parte 4 — Camino fino: llama.cpp (más control, más velocidad)

Es lo que uso en mi equipo. Más trabajo al principio, pero te deja poner API key, contexto largo y varias peticiones en paralelo.

### Instalar

Baja el binario ya compilado de las [releases de llama.cpp](https://github.com/ggml-org/llama.cpp/releases) según tu GPU:

- **AMD o Intel** (incluye las integradas tipo Radeon 780M/8060S): el zip `ubuntu-vulkan-x64`.
- **NVIDIA**: el build con CUDA.
- **Mac**: el de macOS arm64 (Metal), o `brew install llama.cpp`.

```bash
mkdir -p ~/llama.cpp && cd ~/llama.cpp
unzip ~/Descargas/llama-*-bin-ubuntu-vulkan-x64.zip -d current
./current/llama-server --version
```

### Crear la API key

```bash
mkdir -p ~/.config/ia-local
openssl rand -hex 24 | sed 's/^/sk-local-/' > ~/.config/ia-local/api-key
chmod 600 ~/.config/ia-local/api-key
```

### Arrancar el servidor

```bash
~/llama.cpp/current/llama-server \
  -hf ornith-ai/Ornith-1.5-35B-A3B-GGUF:Q4_K_M \
  --alias ornith \
  --host 127.0.0.1 --port 8081 \
  --api-key-file ~/.config/ia-local/api-key \
  -c 65536 --jinja \
  -ngl 999 -fa on \
  --temp 0.6 --top-p 0.95 --top-k 20
```

Qué hace cada cosa:

- `-hf` baja el modelo la primera vez y lo deja en caché.
- `--alias ornith` es el nombre que vas a poner en n8n y en Hermes.
- `-c 65536` es el contexto. Hermes pide 64K como mínimo. Con 64 GB o más puedes subir a 131072 o 262144.
- `--jinja` activa la plantilla de chat del modelo. **Sin esto las herramientas (tool calls) no funcionan bien.**
- `-ngl 999` manda todas las capas a la GPU. `-fa on` activa flash attention.
- Temperatura 0.6, top\_p 0.95 y top\_k 20 son los valores que recomienda la ficha para uso general.

Abre `http://127.0.0.1:8081` en el navegador: llama.cpp trae su propio chat web.

### Que arranque solo (Linux)

```bash
mkdir -p ~/.config/systemd/user
cat > ~/.config/systemd/user/ornith.service <<'EOF'
[Unit]
Description=Ornith-1.5 en llama.cpp
After=network-online.target

[Service]
ExecStart=%h/llama.cpp/current/llama-server -hf ornith-ai/Ornith-1.5-35B-A3B-GGUF:Q4_K_M --alias ornith --host 127.0.0.1 --port 8081 --api-key-file %h/.config/ia-local/api-key -c 65536 --jinja -ngl 999 -fa on --temp 0.6 --top-p 0.95 --top-k 20
Restart=on-failure

[Install]
WantedBy=default.target
EOF
systemctl --user daemon-reload
systemctl --user enable --now ornith
loginctl enable-linger "$USER"   # que siga vivo aunque cierres sesión
```

### Si tu equipo es AMD con gráfica integrada

En los Ryzen con memoria compartida (Strix Halo, 780M), entra al BIOS y sube la memoria reservada para la GPU (UMA / VRAM). En un equipo de 128 GB yo dejo 64 GB para la GPU. Si la dejas en el mínimo, el modelo corre en CPU y va lentísimo.

**Acción:** prueba el endpoint con la key:

```bash
curl http://127.0.0.1:8081/v1/models \
  -H "Authorization: Bearer $(cat ~/.config/ia-local/api-key)"
```

---

## Parte 5 — Ábrelo a tu red sin regalarlo a internet

n8n y Hermes muchas veces viven en otra máquina. Hay que dejar que lleguen al modelo, pero solo ellos.

1. **Nunca abras el puerto en el router.** Un modelo expuesto es cómputo gratis para cualquiera que lo encuentre.
2. **Usa Tailscale.** Instálalo en la máquina del modelo y en la de n8n, y conéctate por la IP `100.x`. Es gratis para uso personal.
3. Cambia `--host 127.0.0.1` por `--host 0.0.0.0` y cierra el puerto a la LAN con el firewall, dejando pasar solo la interfaz de Tailscale:

```bash
sudo ufw allow in on tailscale0
sudo ufw deny 8081/tcp
sudo ufw enable
```

Con Ollama es igual: `OLLAMA_HOST=0.0.0.0` en el servicio y el mismo firewall. Como Ollama no tiene key, el firewall es tu única puerta. No te la saltes.

> Regla: la API key protege de un vecino curioso. Tailscale y el firewall protegen de internet. Necesitas las dos.

**Acción:** desde la máquina de n8n, corre el curl de `/v1/models` contra la IP `100.x` del equipo del modelo.

---

## Parte 6 — Conectar Ornith a n8n

n8n habla con Ornith como si fuera OpenAI. No necesitas ningún nodo especial.

### La credencial

1. En n8n: **Credentials → Add credential → OpenAI**.
2. **API Key**: el contenido de `~/.config/ia-local/api-key` (con Ollama, pon cualquier texto).
3. **Base URL**: `http://100.x.x.x:8081/v1` (con Ollama: `http://100.x.x.x:11434/v1`).
4. Guárdala con un nombre claro, tipo “IA local (Ornith)”.

Si n8n corre en Docker **en la misma máquina** que el modelo, `127.0.0.1` no sirve: dentro del contenedor eso es el propio contenedor. Usa `http://host.docker.internal:8081/v1` y en Linux añade esto al servicio de n8n en el compose:

```bash
extra_hosts:
  - "host.docker.internal:host-gateway"
```

### Usarla en un flujo

En cualquier nodo **AI Agent** o **Basic LLM Chain**, conecta un sub-nodo **OpenAI Chat Model**, elige la credencial y escribe el modelo a mano: `ornith` (el `--alias` de la parte 4) o el nombre completo si usas Ollama.

### Ejemplo: responder comentarios de Instagram

Es lo que hace Ornith en mi cuenta. El esqueleto:

1. **Schedule Trigger** cada pocos minutos, solo en horario de día.
2. **HTTP Request** a la Graph API: `GET /{media_id}/comments?fields=id,text,username,replies{from}`.
3. **Code**: descarta tus propios comentarios, los que ya tienen respuesta tuya y los que son solo emojis.
4. **Basic LLM Chain** con Ornith: le pasas el comentario y le pides un JSON `{"sentimiento": "...", "respuesta": "..."}`.
5. **Code** de guarda: corta a 140 caracteres, quita URLs y arrobas, rechaza respuestas repetidas.
6. **HTTP Request** `POST /{comment_id}/replies` y una espera aleatoria antes del siguiente.

Lo que aprendí haciéndolo:

- **Temperatura baja** (0.2–0.3) en el nodo para tareas repetitivas. La de 0.6 es para conversar.
- **Respuestas cortas.** En frases de más de 100 caracteres el modelo empezaba a meter errores. Con un tope de ~90 desaparecieron.
- Dale al prompt una **ficha con datos reales** tuyos (qué vendes, qué equipo usas, dónde están tus cursos). Sin ficha, inventa.
- Activa **Retry On Fail** y pon un modelo de la nube como respaldo si el equipo se apaga.
- Ritmo humano: una respuesta cada 2–4 minutos y un tope diario. Responder 300 comentarios en 10 minutos es la forma más rápida de que Meta te limite la cuenta.

**Acción:** monta primero un flujo de prueba con **Manual Trigger → Basic LLM Chain** y un texto fijo. Cuando responda, pasa al flujo real.

---

## Parte 7 — Conectar Ornith a Hermes

[Hermes Agent](https://github.com/NousResearch/hermes-agent) es un agente open source que vive en tu máquina, tiene memoria, usa herramientas y corre tareas programadas. Con Ornith detrás, todo eso pasa sin mandar nada a la nube.

### La configuración

Edita `~/.hermes/config.yaml`, en el bloque `model:`:

```bash
model:
  default: "ornith"
  provider: "custom"
  base_url: "http://127.0.0.1:8081/v1"   # o la IP 100.x si está en otra máquina
  api_key: "sk-local-tu-clave"
  context_length: 65536
```

- `provider: "custom"` sirve para cualquier endpoint compatible con OpenAI: llama.cpp, Ollama o LM Studio.
- `context_length` tiene que coincidir con el `-c` del servidor. Hermes exige 64K como mínimo; con menos, el agente falla al cargar herramientas.

Abre `hermes` y pídele algo que use herramientas, como “lista los archivos de mi carpeta Descargas y dime cuál pesa más”. Si lo hace, la conexión está bien.

### Tareas programadas

Aquí es donde un modelo local brilla: el trabajo que corre solo todos los días, sin pagar por token.

```bash
hermes cron create "0 7 * * *" \
  "Revisa mis correos sin leer de las últimas 24 horas y dame un resumen de 5 líneas: qué es urgente, qué puede esperar y a quién tengo que responder hoy." \
  --name resumen-diario \
  --deliver telegram

hermes cron list
hermes cron run resumen-diario   # pruébalo ya, sin esperar a mañana
```

- Los cron necesitan el **gateway de Hermes corriendo**. Sin gateway no se dispara nada.
- Revisa la **zona horaria** del equipo (`timedatectl`). Si está en UTC, tu resumen de las 7:00 llega de madrugada.
- Ideas que funcionan bien: resumen de correo, agenda del día, pendientes del CRM, noticias de tu sector, vigilar que tus servicios estén arriba.

**Acción:** crea un cron, córrelo a mano con `hermes cron run` y revisa que la entrega te llegue.

---

## Parte 8 — Los ajustes que sí mueven la aguja

| Ajuste | Cuándo tocarlo | Cómo |
| --- | --- | --- |
| Razonamiento | Ornith “piensa” antes de responder. En clasificaciones simples gasta cientos de tokens y segundos de más | Pídele respuestas directas en el prompt o, en builds recientes de llama.cpp, `--reasoning off` en un servidor aparte |
| Paralelo | n8n y Hermes usan el modelo a la vez | `--parallel 4 --kv-unified` (reparte el contexto entre 4 peticiones) |
| Contexto | Te sobra memoria y el agente trabaja con documentos largos | Sube `-c` a 131072 o 262144 |
| Visión | Quieres que lea capturas o fotos | Añade `--mmproj` con el archivo de visión del repo |

Para que te hagas una idea de velocidad: en un Ryzen AI Max+ 395 con Vulkan, el 35B en Q4\_K\_M genera unos **30 tokens por segundo**. Un modelo denso de 27B en el mismo equipo me daba 9. Ahí se nota lo de la mezcla de expertos.

**Acción:** mide tu velocidad. llama.cpp la imprime en el log al final de cada respuesta (`eval time ... tokens per second`).

---

## Los errores que ya cometí para que tú no

- **Olvidar `--jinja`.** El modelo responde, pero las herramientas fallan y el agente parece tonto.
- **Contexto por debajo de 64K con Hermes.** Falla al arrancar o corta las conversaciones a la mitad.
- **`127.0.0.1` dentro de Docker.** n8n no encuentra el modelo. Usa `host.docker.internal` o la IP de Tailscale.
- **Dejar la memoria de la GPU en el mínimo** en equipos AMD con gráfica integrada. Corre en CPU y crees que el modelo es lento.
- **Dos modelos grandes cargados a la vez.** Uno de los dos no lo usabas y te comía 20 GB. Apaga el que no trabaja.
- **Exponer el puerto a internet** “un ratito para probar”. No.
- **Creerte los benchmarks a ciegas.** Pruébalo con tu tarea real antes de mover un flujo de producción.

---

## Tu plan de una semana

1. **Día 1:** elige tamaño (tabla de arriba) y córrelo con Ollama.
2. **Día 2:** si te quedas, pásate a llama.cpp con API key y servicio que arranque solo.
3. **Día 3:** Tailscale + firewall. Prueba el endpoint desde otra máquina.
4. **Día 4:** credencial en n8n y un flujo de prueba con texto fijo.
5. **Día 5:** mueve a Ornith un flujo real que hoy pagas en la nube y compara resultados.
6. **Día 6:** instala Hermes y apúntalo a Ornith.
7. **Día 7:** tu primer cron: el resumen del día a las 7:00.

---

## Recursos

- [ornith-ai en Hugging Face](https://huggingface.co/ornith-ai): los tres tamaños, GGUF, MLX y la ficha con los benchmarks.
- [llama.cpp](https://github.com/ggml-org/llama.cpp): el servidor, con builds para Vulkan, CUDA y Metal.
- [Ollama](https://ollama.com/): el camino rápido.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent): el agente con memoria y tareas programadas.
- [Credencial OpenAI de n8n](https://docs.n8n.io/integrations/builtin/credentials/openai/): dónde va la Base URL.
- [Tailscale](https://tailscale.com/): la red privada entre tus equipos.

---

## Última cosa

Durante años la IA local fue un experimento bonito que terminabas apagando porque no aguantaba trabajo de verdad. Con modelos como Ornith eso cambió: hoy un mini PC puede contestar comentarios, resumirte el día y correr un agente sin pagar un centavo por token. No reemplaza a los modelos grandes de la nube en todo, y no hace falta. **La pregunta ya no es si la IA local sirve, sino qué trabajo le vas a dar.**

*Erik Taveras — Taveras Solutions, LLC*

Si lo montas, etiquétame en Instagram y cuéntame en qué equipo lo corres y qué flujo le diste primero.