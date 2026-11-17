---
title: "Guía Racks Academy — Instalar Hermes y dejar que aprenda contigo"
type: resource
tags:
  - hermes
  - agentes
  - documentacion
  - ia
  - homelab
status: active
project: none
date_created: 2026-11-17
date_modified: 2026-11-17
source: https://racks-labs.github.io/recursos_y_guias/recursos/hermes.html
---
# Guía Racks Academy — Instalar Hermes y dejar que aprenda contigo

> Guía de Recursos Racks Academy, *Instala Hermes. Y deja que aprenda contigo.* Instalación y uso de **Hermes Agent**, el agente de código abierto que crea sus propias skills y recuerda entre sesiones: de la terminal a Telegram, con tareas programadas. Según la guía, está verificada contra la documentación oficial en septiembre de 2026. Nota del vault: 17/11/2026.

Fuente: [Instala y domina Hermes, el agente que aprende contigo](https://racks-labs.github.io/recursos_y_guias/recursos/hermes.html#que-es). Documentación oficial citada en la guía: [hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs).

**Aviso:** el repo del vault es público. Esta nota no copia contraseñas, tokens ni claves. Esos valores viven en `~/.hermes/.env` (permisos 600) o en `~/.hermes/auth.json` (inicio de sesión de Nous Portal). Si la guía muestra ejemplos de tokens, aquí se omiten.

## Qué es Hermes

Hermes Agent es un agente de IA de código abierto (licencia MIT) publicado por Nous Research en febrero de 2026. Se instala en tu ordenador, en un servidor barato o en un móvil Android, y trabaja con el modelo que tú elijas: Claude, GPT, Gemini, los de Nous o uno local. Su frase de presentación, según la guía: «el agente que crece contigo».

Lo que lo distingue, dice la guía, no son las herramientas (tiene más de cuarenta: terminal, archivos, búsqueda web, navegador, imágenes, voz, mensajería) sino el bucle de aprendizaje:

- **Crea skills** a partir de lo que hace. Cuando resuelve una tarea que se repite, la convierte en un procedimiento guardado y la mejora las siguientes veces.
- **Recuerda entre sesiones.** Mantiene notas sobre tu entorno y un perfil sobre ti, y puede buscar en conversaciones pasadas.
- **Vive donde estás tú.** Un solo proceso, el *gateway*, lo conecta a Telegram, Discord, Slack, WhatsApp, Signal, email y Home Assistant, y ejecuta tareas programadas que te llegan a cualquiera de ellos.

Comparación que hace la guía:

| | Hermes | OpenClaw | Claude Code |
| --- | --- | --- | --- |
| Qué es | Agente personal que aprende: skills propias, memoria, mensajería | Asistente personal de mensajería, el más maduro en canales | Agente de terminal para construir cosas |
| Skills | Las instala del hub y las crea él con la experiencia | Archivos que escribes y mantienes tú (ClawHub) | Carpetas que escribes tú o instalas |
| Memoria | Archivos de texto más una base de datos con búsqueda en sesiones | Archivos Markdown | CLAUDE.md por proyecto |
| Modelo | Cualquiera: Nous Portal, OpenRouter, Anthropic, OpenAI, Google, local | Cualquiera, con tu clave o suscripción | Claude, con tu suscripción |
| Precio | Gratis; pagas el modelo | Gratis; pagas el modelo | Con Claude Pro o Max |

Dos avisos de la guía: Hermes mejora con el uso (la primera semana es peor que la décima) y es un proyecto joven que publica versiones cada pocas semanas. Si un comando de la guía no aparece, primero `hermes update` y luego la documentación oficial.

Si vienes de OpenClaw o de Claude Code: `hermes claw migrate` trae la configuración de OpenClaw (`--dry-run` para ver qué haría) y `hermes import-agent` lee la de Claude Code o Codex.

## Requisitos y proveedor del modelo

- **Sistema:** Linux, macOS, Windows (nativo por PowerShell, o WSL2, la vía más rodada) y Android con Termux. Un VPS Linux barato vale para tenerlo encendido siempre.
- **Previos:** Git y curl. En Linux, también `xz-utils`. El instalador trae su propio Python (3.11), Node.js, `uv`, `ripgrep` y `ffmpeg`.
- **Permisos:** sin `sudo`. Código en `~/.hermes/hermes-agent/`, comando en `~/.local/bin/hermes`, datos en `~/.hermes/`.
- **Modelo:** cualquiera con al menos 64.000 tokens de contexto. Con menos, dice la guía, la compresión no da abasto y el agente se pierde.

Hermes no cobra; el modelo sí. Tres caminos, intercambiables después:

1. **Nous Portal.** Un inicio de sesión da acceso a más de 200 modelos y al Tool Gateway (búsqueda web, imágenes, voz y navegador sin más claves). Hay nivel gratuito; el plan Plus son 20 $/mes con 22 $ de crédito, y hay Super (100 $) y Ultra (200 $), según la guía. Se configura con `hermes setup --portal`. Las credenciales de este camino se guardan en `~/.hermes/auth.json`.
2. **Tus propias claves** (Anthropic, OpenAI, Google u OpenRouter). Pagas por token. La clave se guarda en `~/.hermes/.env`. Las herramientas de servicios externos pedirán las suyas.
3. **Un modelo local** (Ollama, vLLM o llama.cpp). En `hermes model` eliges «Custom endpoint» y la dirección (con Ollama, `http://localhost:11434/v1`). Gratis por token y privado; hace falta un modelo con 64k de contexto que corra decentemente.

## Instalar

Linux, macOS, WSL2 y Android (Termux):

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Windows (PowerShell, instalación nativa, que la guía marca como reciente; si falla, recomienda WSL2):

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

El instalador descarga el código, crea un entorno de Python aislado con `uv`, instala Node.js si hace falta y deja `hermes` en `~/.local/bin`. No usarlo con `sudo`. En Mac y Windows hay además un instalador de escritorio en la web oficial.

Después: `source ~/.bashrc` (en Mac con zsh, `~/.zshrc`), `hermes --version` y `hermes doctor`. `hermes doctor` revisa el entorno y es el primer comando que la guía recomienda cada vez que algo raro pase. Si dice que falta un proveedor de modelo, es el siguiente paso, no un fallo de instalación.

Si `hermes` no se encuentra, recargar el PATH. Si Python es demasiado antiguo, hace falta 3.11 o superior. Si falta `uv`, instalarlo y repetir. «Permission denied» suele significar que se usó `sudo` o que no puedes escribir en `~/.local/bin`.

## Configurar

```bash
hermes setup            # asistente completo
hermes setup --portal   # directo a Nous Portal
hermes model            # elegir o cambiar proveedor y modelo
hermes tools            # encender o apagar conjuntos de herramientas
```

El asistente ofrece Quick Setup (Nous Portal, el recomendado si empiezas), Full Setup y Blank Slate. Si eliges un proveedor con clave, te la pide y la guarda en `~/.hermes/.env`. Los conjuntos de herramientas incluyen `terminal`, `file`, `web`, `browser`, `vision`, `image_gen`, voz, memoria y tareas programadas. Con Nous Portal, búsqueda web, imágenes, voz y navegador funcionan sin claves adicionales. La búsqueda en X (Twitter) viene apagada y requiere credenciales de xAI (van en `.env`, no en esta nota).

Dónde vive todo, según la guía:

| Ruta | Qué es |
| --- | --- |
| `~/.hermes/config.yaml` | Configuración que no es secreta: modelo, terminal, compresión, herramientas, aprobaciones |
| `~/.hermes/.env` | Claves de API y tokens de bots. Solo secretos, permisos 600 |
| `~/.hermes/auth.json` | Credenciales de inicio de sesión (Nous Portal) |
| `~/.hermes/SOUL.md` | Identidad del agente: quién es, cómo habla, qué prioriza |
| `~/.hermes/memories/` | `MEMORY.md` y `USER.md`, memoria persistente |
| `~/.hermes/skills/` | Skills instaladas y las que crea el agente |
| `sessions/`, `state.db`, `logs/` | Conversaciones, búsqueda de sesiones y registros |

Comandos: `hermes config`, `hermes config edit`, `hermes config get`, `hermes config set`, `hermes config check`. Prioridad si algo se define en dos sitios: línea de comandos > `config.yaml` > `.env` > valores por defecto.

Un `config.yaml` mínimo que propone la guía (sin secretos): `model` y `provider`; `terminal.backend: local` (en un servidor, `docker`); `terminal.timeout: 180`; `approvals.mode: smart`; `compression.enabled: true`; memoria y perfil de usuario activados.

## Primer uso, sesiones y permisos

`hermes` abre la interfaz clásica; `hermes --tui`, la moderna con paneles. La guía sugiere empezar en la carpeta de un proyecto con una pregunta pequeña y sin modificar nada, para ver el bucle (listar, leer, resumir). Varias líneas: Alt+Intro (también Ctrl+J o Mayús+Intro). Para interrumpir: un mensaje nuevo, o Ctrl+C.

Comandos de barra que lista la guía: `/help`, `/new`, `/reset`, `/model`, `/tools`, `/skills`, `/personality`, `/memory`, `/reasoning-effort`, `/compression`, `/rollback` (con `--checkpoints`), `/approve`, `/image`, `/browser`, `/voice`, `/status`, `/save`, `/stop`.

Sesiones: `hermes -c` retoma la última; `hermes --resume` una concreta; `hermes sessions list`; `hermes journey` muestra la línea de tiempo de skills y memorias. `hermes chat -q "…"` lanza una sesión con pregunta inicial; `hermes -z "…"` da una respuesta y sale (para scripts). Regla de la guía: una sesión por tarea. Lo que deba sobrevivir va a la memoria, no al chat.

Antes de un comando que pueda hacer daño (borrar, sobrescribir, descargar y ejecutar), Hermes pregunta. En modo `smart`, un modelo auxiliar clasifica lo inocuo (se ejecuta), lo claramente peligroso (se niega) y lo dudoso (te pregunta). Opciones: `once`, `session`, `always` (añade el patrón a `command_allowlist`) o `deny` (por defecto si no contestas). La guía recomienda empezar con `once`. Hay comandos que Hermes no ejecuta nunca.

`SOUL.md` define quién es el agente; `/personality` cambia el tono. Para un Hermes de trabajo y otro personal, con memorias y skills separadas: `hermes profile create trabajo` y `hermes -p trabajo`.

## Skills

Una skill es una carpeta en `~/.hermes/skills/` con un `SKILL.md` que describe cuándo usarla, los pasos, las trampas y cómo comprobar el resultado. Puede llevar plantillas, scripts y referencias. El formato sigue el estándar de [agentskills.io](https://agentskills.io), así que las skills de Claude Code, OpenAI o la comunidad funcionan aquí.

Se cargan solas cuando la petición encaja, o a mano (`/nombre-de-skill`). Se pueden encadenar hasta cinco en un mensaje. Del hub: `hermes skills browse`, `search`, `inspect`, `install`, `list`, `check`, `update`, `uninstall`. Las fuentes `official/` y los repos de `openai/`, `anthropics/`, `huggingface/` y `NVIDIA/` son de confianza; `skills-sh/` y las URLs sueltas son «comunidad». Todas pasan por un escáner de exfiltración, inyección de prompt y comandos destructivos: lo dudoso se puede forzar con `--force` después de leerlo; lo peligroso se bloquea siempre.

Cuando Hermes resuelve algo repetible, puede guardar el procedimiento como skill (`skill_manage`) y afinario al usarlo. Se le puede pedir explícitamente que lo convierta en skill. Si quieres revisar antes de que escriba en disco: `skills.write_approval: true` y luego `/skills pending`, `/skills diff`, `/skills approve` o `reject`. Skills de otras carpetas se apuntan en `skills.external_dirs`; las que vienen dentro de un repo clonado exigen `hermes skills trust`.

## Memoria

Dos archivos en `~/.hermes/memories/`, que el agente mantiene y tú puedes editar:

- **MEMORY.md** — notas sobre tu entorno, convenciones, lo aprendido. Límite de 2.200 caracteres (unos 800 tokens).
- **USER.md** — tu perfil: preferencias y forma de comunicarte. Límite de 1.375 caracteres (unos 500 tokens).

Los límites son a propósito: la memoria se carga entera al arrancar cada sesión. Cuando se llena, la herramienta devuelve un error y hay que consolidar; no se trunca en silencio. Lo guardado en una sesión queda en disco al momento, pero se ve en la siguiente. Además puede buscar en conversaciones anteriores (texto completo sobre `~/.hermes/state.db`). `hermes journey` muestra cómo ha ido creciendo. `hermes memory` conecta proveedores externos (Honcho, Mem0 o Supermemory); la guía dice que, para empezar, los dos archivos bastan. Se puede exigir aprobación de escritura con `memory.write_approval`.

## Gateway: Telegram, Discord, WhatsApp y el resto

El *gateway* es un único proceso que conecta Hermes a las plataformas y ejecuta las tareas programadas. Telegram es, según la guía, el más sencillo y estable para empezar.

```bash
hermes gateway setup     # asistente: plataforma y tokens (van a ~/.hermes/.env)
hermes gateway           # primer plano, para probar
hermes gateway install   # servicio de usuario
sudo hermes gateway install --system   # Linux: que arranque con la máquina
hermes gateway status
hermes gateway stop
```

En WSL2, si los servicios del sistema fallan: `tmux` o `nohup hermes gateway run`.

- **Telegram:** crear el bot con BotFather, obtener tu ID numérico, y guardar token e IDs permitidos en `~/.hermes/.env` (no en el vault). Por defecto, en grupos el bot solo ve comandos; para que lea todos los mensajes hay que desactivar la privacidad de grupo en BotFather y volver a meterlo en el grupo. `/sethome` fija el chat al que llegan las tareas programadas.
- **Discord:** aplicación en el portal de desarrolladores, intents de Server Members y Message Content, invitación con permisos de ver canales, enviar mensajes, enlaces, archivos y leer historial. Token e IDs permitidos, otra vez, en `.env`.
- **WhatsApp:** `hermes whatsapp` muestra un QR (modo bot con número dedicado, o *self-chat* en tu propio número). Necesita Node.js 18 o superior. WhatsApp no admite oficialmente bots fuera de su API de empresa; la guía avisa del riesgo de bloqueo y recomienda un número secundario o `hermes whatsapp-cloud`. Cada perfil admite un solo número; la carpeta de sesión en `~/.hermes/platforms/whatsapp/session` hay que protegerla como una contraseña.
- Slack, Signal, email y Home Assistant se configuran con el mismo `hermes gateway setup`. Para Slack, `hermes slack` genera el manifiesto.

**Quién puede hablar con el agente:** por defecto, nadie. Si no hay listas de permitidos, el gateway rechaza a todo el mundo y lo avisa al arrancar. Se abre la puerta con listas por plataforma o una global (`GATEWAY_ALLOWED_USERS` en `.env`), o con emparejamiento (`hermes pairing approve|list|revoke`). La guía es explícita: `GATEWAY_ALLOW_ALL_USERS=true` en un agente con terminal es dar tu ordenador a cualquiera que encuentre el bot; no existe un caso en que compense.

## Tareas programadas

Con el gateway encendido, Hermes ejecuta tareas a la hora que le digas, en una sesión nueva cada vez, y manda el resultado a donde indiques. Se pueden pedir en lenguaje natural o con `hermes cron create|list|run|pause|edit|remove`. En el chat: `/cron add`. Acepta plazos (`in 30m`), intervalos (`every 2h`), lenguaje natural (`weekdays at 9am`), expresiones cron y una fecha exacta. El resultado puede ir a `origin`, `local` (`~/.hermes/cron/output/`), a una plataforma o a `all`. El gateway mira el reloj cada minuto.

Si una tarea nocturna tropieza con un comando que requiere aprobación y no hay nadie, por defecto deniega (`approvals.cron_mode: deny`). Hay que diseñar esas tareas para que no necesiten comandos delicados, o añadir a la lista de permitidos exactamente los que hagan falta.

## Seguridad

En `config.yaml`, `approvals.mode` puede ser `smart` (recomendado), `manual` u `off`; `timeout` es la espera en segundos; `cron_mode` dice qué hacer sin nadie delante; `deny` añade prohibiciones propias.

Hay una lista negra que no se puede saltar, ni con `--yolo` ni con `mode: off`: borrar la raíz del disco, bombas de procesos, formatear discos montados, descargar-y-ejecutar de una tubería. El agente no puede escribir en `~/.ssh`, `~/.aws`, sus propios `auth.json` y `.env`, ni los `.env` de tus proyectos. `HERMES_WRITE_SAFE_ROOT` restringe las escrituras a las carpetas que digas.

Backends de ejecución: `local` (sin aislamiento, se apoya en las aprobaciones; para tu ordenador, tú delante); `docker` (contenedor con recursos limitados; para un gateway que trabaja solo, y por eso ahí no pide aprobaciones); `ssh` (otra máquina); `modal`, `daytona`, `vercel_sandbox`, `singularity` (sandbox en la nube o HPC).

Si lo montas en un VPS, la guía pide: listas de permitidos o emparejamiento, nunca «permitir a todos»; backend docker con límites y usuario sin privilegios; secretos solo en `~/.hermes/.env` con permisos 600; revisar de vez en cuando `command_allowlist` y `~/.hermes/logs/`; actualizar con `hermes update` (`hermes doctor` avisa también de paquetes de Python comprometidos). Opcional: gateway en una máquina y ejecución en otra por `ssh`, y `security.allow_lazy_installs: false`.

Hermes, según la guía, escanea archivos de contexto (`AGENTS.md`, `SOUL.md`, `.cursorrules`) por instrucciones inyectadas, bloquea peticiones a direcciones internas y de metadatos de la nube, y filtra las variables de entorno que llegan a los servidores MCP. Eso no sustituye las reglas de arriba.

## Mantener

`hermes update` (última versión; sincroniza skills de todos los perfiles), `hermes backup` (zip con configuración, memoria, skills y sesiones; los perfiles exportados no llevan credenciales), `hermes import` para restaurar, `hermes profile create|list`, `hermes status`, `hermes logs`, `hermes insights` (tokens, coste y actividad), `hermes dashboard`, `hermes mcp` (servidores MCP) y `hermes uninstall`. Para pasar a un ordenador nuevo: `backup` en el viejo, instalador en el nuevo, `import`.

## Cuando algo no va

Secuencia de recuperación que da la guía: `hermes doctor` → `hermes model` → `hermes setup` → `hermes sessions list` → `hermes -c` → `hermes gateway status`. Casi todo se arregla en los dos primeros.

| Síntoma | Qué dice la guía |
| --- | --- |
| Respuestas vacías o cortadas | Proveedor mal configurado o clave caducada. `hermes model` y volver a elegir modelo |
| Timeout de un modelo local con contextos grandes | En `.env`: `HERMES_STREAM_READ_TIMEOUT=1800`; probar el endpoint por separado |
| «Session not found» | `hermes sessions list` y el perfil correcto (`-p`) |
| El bot no contesta a nadie | No hay lista de permitidos; el gateway deniega por defecto |
| Contesta en privado pero no en el grupo | Privacidad de grupo en BotFather; desactivarla y volver a meter al bot |
| Las tareas programadas no se ejecutan | El gateway no está encendido |
| Una tarea nocturna «no hizo nada» | Tropezó con una aprobación y denegó; revisar `hermes logs` y rediseñar o permitir el comando |
| WhatsApp se desconecta | Volver a escanear el QR; si se repite, valorar `hermes whatsapp-cloud` |
| Un comando de la guía no existe | `hermes update`; `hermes --help` y `/help` dicen lo que hay en tu versión |
| Ayuda de la comunidad | `hermes dump` genera un resumen de la instalación **sin secretos**; `hermes debug share` sube un informe con registros |

## Relacionado

- [[HermesAgent]] — índice de notas de Hermes en el vault
- [[homelab-api-curls]] — referencia de curls de la API de Hermes (credenciales en `~/.hermes/.env`)
- [[Ornith en tu homelab - instalar y conectar a n8n y Hermes]] — conectar un modelo local a Hermes
- [[Mi IA local - mapa de montaje completo]] — montaje local que incluye Hermes
- [[Rutinas y cronjobs]] — rutinas del vault; cómo programar tareas en Hermes está en esta guía
- [[02 - PCs]] — el PC3 tiene a Hermes Agent entre los servicios candidatos
- [[MOC IA Local]]
