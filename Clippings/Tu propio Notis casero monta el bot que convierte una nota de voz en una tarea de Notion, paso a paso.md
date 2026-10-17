---
title: "Tu propio Notis casero: monta el bot que convierte una nota de voz en una tarea de Notion, paso a paso"
source: "https://www.javiggil.com/e83ee63f7f13?r=email"
author:
  - "[[Javi Gil]]"
published: 2026-08-20
created: 2026-10-17
description: "El montaje completo, pieza por pieza: la petición a tu ayudante de IA por etapas, el código real de cada pieza, cuánto cuesta operarlo por mensaje, por qué la entrada es Telegram y no WhatsApp, y cómo venderlo a quien ya cobra por Notion."
tags:
  - "clippings"
---
En el reel te di el plan entero y gratis: **abres un bot de Telegram, le mandas una nota de voz, un modelo la transcribe y decide qué tarea es, y la crea sola en tu Notion, sin que abras la app.** Eso ya lo tienes, sin pedir nada.

Esto es lo que no cabía en 70 segundos: **el montaje completo, pieza por pieza.** La petición a tu ayudante de IA por etapas, el código real de cada pieza (para que sepas qué te está montando), cuánto cuesta operar esto por mensaje, por qué WhatsApp no es la puerta de entrada aunque sea la primera que se te ocurra, cómo sumar más canales y más herramientas de destino cuando el primero funcione, cómo montar el cobro por suscripción, y cómo conseguir tus primeros clientes de pago sin escribir a nadie en frío.

No lo montas a mano: se lo dictas a tu ayudante de IA. Tú tienes que saber **qué pedir, en qué orden, y qué mirar cuando algo falle.** Eso es lo que te da esto.

## Cómo usar esta guía

Cada bloque se sostiene solo; salta al que necesites.

1. **El mecanismo, sin humo** — las tres piezas reales, sin misterio.
2. **La petición entera a tu ayudante de IA** — el núcleo, para pegar por etapas.
3. **El montaje pieza por pieza** — Telegram, transcripción, la IA que decide, Notion, con código.
4. **Cuánto cuesta operar esto** — el coste real por mensaje y dónde se dispara.
5. **La letra pequeña: por qué no empiezas por WhatsApp** — lo que tienes que saber antes de tocar nada.
6. **Sumar más canales** — Telegram ya montado, WhatsApp por QR con sus cautelas, email.
7. **Conectar más de una herramienta** — CRM, Gmail, Calendar, el mismo patrón repetido.
8. **El cobro por suscripción con tope de uso** — cómo se factura sin perder dinero.
9. **Tus primeros clientes de pago** — dónde están y qué les dices.
10. **Checklist: hazlo este fin de semana.**
- **Fuentes** — de dónde sale cada cosa, y lo que no afirmo.

## Qué es gratis y qué amplía esto (para que no haya trampa)

El **plan de 3 pasos** te lo llevaste entero en el reel: un canal (Telegram), una herramienta de destino (Notion), y la petición que hace que tu ayudante de IA te lo monte. Con eso ya puedes tener tu primer bot funcionando. Esto **amplía la implementación**: el código de cada pieza, el coste real, la letra pequeña completa de por qué WhatsApp no es el punto de partida, cómo crecer a más canales y más herramientas, y cómo convertirlo en un negocio con suscriptores de pago. No retiene nada del plan; es la mano en el hombro mientras lo montas y mientras lo escalas.

## La frontera honesta

Esto es **mi recomendación para que montes el tuyo**, no una radiografía de cómo está construido Notis por dentro (no publica su stack técnico). Lo que sí es verdad del caso, verificado: Notis conecta cinco canales de entrada y más de 1.000 herramientas de destino, cobra por suscripción con una asignación de uso incluida en cada plan, y factura del orden de 16.700 dólares al mes con 529 clientes. Tú vas a montar un tramo mucho más pequeño —un canal, una herramienta— y es ese tramo pequeño el que ya es vendible.

---

## 1 · El mecanismo, sin humo

Todo lo que hace esto son tres pasos encadenados, y ninguno es teórico: son los mismos tres que usa cualquier asistente de este tipo por dentro.

**1\. Transcribir.** Tu nota de voz, sea del canal que sea, es un archivo de audio. Se manda a una API de transcripción y vuelve como texto. Esto ya lo resolvió otra industria hace años; tú solo lo llamas.

**2\. Decidir qué tarea es.** Aquí está el truco real, y se llama **function calling** (o *tool calling*): en vez de pedirle al modelo que "escriba algo" y luego intentar adivinar qué quiso decir, le describes de antemano los campos exactos que tiene tu base de datos de Notion (nombre y tipo de cada uno) como si fuera una función de programación, y el modelo no contesta con prosa: **rellena esos campos con argumentos concretos.** El modelo no improvisa texto libre, elige y rellena una plantilla que tú ya definiste. Es la diferencia entre pedirle a alguien "apúntate algo" y darle un formulario con casillas.

**3\. Ejecutar.** Con esos campos ya rellenos y en la forma correcta, se llama a la API de Notion y se crea la página. Nadie abre la app; nadie hace clic. Es una llamada HTTP con un JSON.

El error de bulto es pensar que esto necesita "un modelo propio" o "un equipo". No hace falta ninguna de las dos cosas: las tres piezas son APIs que ya existen, y montarlas en orden es el trabajo de un fin de semana con un ayudante de IA tipo Claude Code.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 390"><text x="200" y="26" text-anchor="middle" font-size="19" font-weight="700" fill="#4b0a23">Cómo pasa de nota de voz a tarea</text> <rect x="130" y="44" width="140" height="36" rx="18" fill="none" stroke="#4b0a23" stroke-width="1.5"></rect><text x="200" y="67" text-anchor="middle" font-size="14" font-weight="600" fill="#4b0a23">Nota de voz</text> <line x1="200" y1="80" x2="200" y2="94" stroke="#4b0a23" stroke-width="1.5"></line><polygon points="200,100 195,90 205,90" fill="#4b0a23"></polygon><rect x="55" y="100" width="290" height="56" rx="8" fill="none" stroke="#4b0a23" stroke-width="1.5"></rect><text x="70" y="124" font-size="16" font-weight="700" fill="#4b0a23">1 · Transcribir</text> <text x="70" y="145" font-size="13" fill="#6e573d">El audio se manda a una API y vuelve como texto</text> <line x1="200" y1="156" x2="200" y2="170" stroke="#4b0a23" stroke-width="1.5"></line><polygon points="200,176 195,166 205,166" fill="#4b0a23"></polygon><rect x="55" y="176" width="290" height="70" rx="8" fill="rgba(254,70,41,0.07)" stroke="#fe4629" stroke-width="2"></rect><text x="70" y="200" font-size="16" font-weight="700" fill="#4b0a23">2 · Decidir qué tarea es</text> <text x="70" y="221" font-size="13" fill="#6e573d">function calling: rellena tus</text> <text x="70" y="237" font-size="13" fill="#6e573d">campos, no escribe texto libre</text> <line x1="200" y1="246" x2="200" y2="260" stroke="#4b0a23" stroke-width="1.5"></line><polygon points="200,266 195,256 205,256" fill="#4b0a23"></polygon><rect x="55" y="266" width="290" height="56" rx="8" fill="none" stroke="#4b0a23" stroke-width="1.5"></rect><text x="70" y="290" font-size="16" font-weight="700" fill="#4b0a23">3 · Ejecutar</text> <text x="70" y="311" font-size="13" fill="#6e573d">POST a la API de Notion: crea la página</text> <line x1="200" y1="322" x2="200" y2="336" stroke="#4b0a23" stroke-width="1.5"></line><polygon points="200,342 195,332 205,332" fill="#4b0a23"></polygon><rect x="110" y="342" width="180" height="36" rx="18" fill="none" stroke="#4b0a23" stroke-width="1.5"></rect><text x="200" y="365" text-anchor="middle" font-size="14" font-weight="600" fill="#4b0a23">Tarea creada en Notion</text> </svg> Las tres piezas encadenadas: transcribir, decidir con function calling y crear la tarea en Notion, sin que abras la app.

---

## 2 · La petición entera a tu ayudante de IA

En el reel dictaste la versión corta. Aquí va la larga, por etapas, para que Claude Code (o el Claude de escritorio, o Cursor) te acompañe en el montaje entero. **No tienes que saber programar de fondo: tienes que saber qué pedir y en qué orden, y hacer las cuentas que él no puede crear por ti** (la cuenta de Telegram para tu bot y la integración de Notion en tu workspace van a tu nombre). Pégale esto como primer mensaje:

> Quiero montar un bot de Telegram que reciba notas de voz y cree tareas en mi base de datos de Notion, sin que yo tenga que abrir ninguna app. Guíame por etapas y no avances a la siguiente hasta que la anterior funcione:
> 
> 1. Dime los pasos exactos para crear un bot hablando con @BotFather en Telegram y sacar el token. Monta un endpoint (o un script con `getUpdates` si no quiero exponer un servidor todavía) que reciba mis mensajes y detecte cuándo traen una nota de voz. Descarga el audio con `getFile`.
> 2. Manda ese audio a una API de transcripción (Whisper o `gpt-4o-mini-transcribe` de OpenAI) y quédate con el texto que devuelva.
> 3. Pregúntame el `database_id` de mi base de datos de Notion y pídeme que te copie el nombre y el tipo exacto de cada una de sus propiedades (título, select, fecha, etc.). Con eso, define una herramienta de **function calling** que reciba esos mismos campos como argumentos, y manda el texto transcrito al modelo para que la rellene.
> 4. Con el JSON que devuelva el modelo, llama a la API de Notion (`POST /v1/pages`) y crea la página en mi base de datos. Ayúdame a generar el token de integración interna en mi propio workspace de Notion antes de este paso.
> 5. Prueba el flujo completo conmigo con tres notas de voz distintas antes de darlo por terminado, y corrige lo que falle en el paso 3 si el modelo mete algo en el campo equivocado.
> 
> Antes de empezar, hazme las preguntas que necesites sobre mi base de datos de Notion.

**Las etapas (y quién hace qué en cada una):**

1. **El bot.** Claude Code te da el paso a paso de BotFather y el código del endpoint o del script de *polling*. Tú creas el bot (dos minutos, dentro de Telegram) y le pasas el token.
2. **La transcripción.** Claude Code te monta la llamada a la API de transcripción. Tú generas tu propia clave de API en tu cuenta de OpenAI (o el proveedor que elijas) y se la das.
3. **La decisión.** Aquí es donde tienes que trabajar CON él, no solo pedirle: tienes que enseñarle el esquema real de tu base de datos, campo por campo. Esta es la parte que se prueba y se corrige, no la que se pega y ya está (ver §4).
4. **La ejecución.** Claude Code te ayuda a crear la integración interna en Notion (Configuración → Conexiones → Nueva integración, sin coste) y te da el código de la llamada final.
5. **La prueba.** No lo des por bueno a la primera nota de voz que funcione. Mándale tres distintas, alguna ambigua a propósito, y mira qué campo rellena mal.

---

## 3 · El montaje pieza por pieza (con código)

**Pieza 1 · Recibir la nota de voz.** Cuando alguien te manda un mensaje de voz por Telegram, el `Update` que te llega trae esto:

```json
{
  "message": {
    "voice": {
      "file_id": "AwACAgIAAxk...",
      "duration": 14,
      "mime_type": "audio/ogg"
    }
  }
}
```

Con ese `file_id` pides el archivo y lo descargas:

```
GET https://api.telegram.org/bot<TOKEN>/getFile?file_id=AwACAgIAAxk...
→ devuelve file_path

GET https://api.telegram.org/file/bot<TOKEN>/<file_path>
→ el audio, descárgalo
```

**Pieza 2 · Transcribir.** Mandas ese audio a la API de transcripción:

```
POST https://api.openai.com/v1/audio/transcriptions
  file: <el audio descargado>
  model: whisper-1   (o gpt-4o-mini-transcribe, más barato)
→ devuelve el texto
```

**Pieza 3 · Decidir la tarea (function calling).** Le describes al modelo, en JSON, la forma EXACTA de tu base de datos de Notion. Ejemplo con una base con tres campos (Título, Estado, Fecha límite):

```json
{
  "name": "crear_tarea_notion",
  "description": "Crea una tarea nueva en la base de datos de Notion del usuario",
  "parameters": {
    "type": "object",
    "properties": {
      "titulo": { "type": "string" },
      "estado": { "type": "string", "enum": ["Por hacer", "En curso", "Hecho"] },
      "fecha_limite": { "type": "string", "description": "formato ISO, opcional" }
    },
    "required": ["titulo"]
  }
}
```

Mandas el texto transcrito al modelo junto con esta herramienta, y el modelo responde con una llamada a `crear_tarea_notion` con los argumentos ya rellenos, no con una frase. Esa es la pieza que "decide qué tarea es": no clasifica en abstracto, rellena tu formulario real.

**Pieza 4 · Crear la página en Notion.** Con esos argumentos, la llamada final:

```
POST https://api.notion.com/v1/pages
Authorization: Bearer <tu-token-de-integracion>
Notion-Version: 2022-06-28

{
  "parent": { "database_id": "<tu-database-id>" },
  "properties": {
    "Título": { "title": [{ "text": { "content": "Llamar al proveedor" } }] },
    "Estado": { "select": { "name": "Por hacer" } }
  }
}
```

El token de integración lo generas gratis en tu propio workspace de Notion (Configuración → Conexiones → Desarrollar o gestionar integraciones → Nueva integración), sin plan de pago.

**Dónde vive esto corriendo.** No necesitas un servidor propio: una función serverless (Vercel, Cloudflare Workers) que reciba el webhook de Telegram y encadene las cuatro piezas es suficiente para empezar; es lo que Claude Code te monta más rápido en un fin de semana.

---

## 4 · Cuánto cuesta operar esto

Con precios públicos de hoy (2026-08-19; los precios de las APIs cambian, pídele a tu ayudante de IA que confirme los vigentes al montarlo):

| Pieza | Coste aproximado |
| --- | --- |
| Transcripción (Whisper / gpt-4o-mini-transcribe) | 0,003-0,006 $/minuto de audio |
| Decidir la tarea (modelo barato tipo gpt-5-nano) | Una fracción de céntimo por mensaje (prompt y respuesta cortos) |
| Crear la página en Notion | Gratis |

Una nota de voz típica de 20-30 segundos sale, de punta a punta, por bastante menos de un céntimo de dólar. **Dónde se dispara el coste:** notas de voz muy largas (varios minutos, el coste de transcripción escala directo con la duración) y volumen alto sin control (si vas a revenderlo a varios clientes, necesitas saber cuántos mensajes manda cada uno al mes para no perder margen con el que más habla). El coste NO se dispara por el paso de decidir la tarea ni por el de escribir en Notion: los dos son casi gratis comparados con la transcripción.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 290"><text x="200" y="24" text-anchor="middle" font-size="18" font-weight="700" fill="#4b0a23">Cuánto cuesta operar esto, pieza a pieza</text> <text x="16" y="46" font-size="14" font-weight="600" fill="#4b0a23">Transcripción</text> <rect x="16" y="54" width="260" height="22" rx="4" fill="#fe4629"></rect><text x="16" y="94" font-size="13" fill="#6e573d">0,003-0,006 $/minuto de audio</text> <text x="16" y="112" font-size="14" font-weight="600" fill="#4b0a23">Decidir la tarea</text> <rect x="16" y="120" width="34" height="22" rx="4" fill="#4b0a23" fill-opacity="0.3"></rect><text x="16" y="160" font-size="13" fill="#6e573d">una fracción de céntimo / mensaje</text> <text x="16" y="178" font-size="14" font-weight="600" fill="#4b0a23">Crear la página en Notion</text> <rect x="16" y="186" width="56" height="22" rx="4" fill="none" stroke="#4b0a23" stroke-width="1.5"></rect><text x="44" y="201" text-anchor="middle" font-size="13" font-weight="700" fill="#4b0a23">Gratis</text> <text x="16" y="244" font-size="13" fill="#6e573d">Una nota de 20-30 s sale, de punta a punta,</text> <text x="16" y="262" font-size="13" fill="#6e573d">por bastante menos de 1 céntimo de dólar.</text> </svg> El coste vive en la transcripción; decidir la tarea y escribir en Notion son casi gratis en comparación.

---

## 5 · La letra pequeña: por qué no empiezas por WhatsApp

Es el canal que se te va a ocurrir primero, porque es el que todo el mundo tiene abierto. No es el punto de partida, y aquí está el porqué, verificado hoy, no de oídas:

**La puerta oficial está cerrada desde el 15 de enero de 2026.** La política de negocio de WhatsApp prohíbe explícitamente a los "proveedores de IA" usar su API de negocio cuando la tecnología de IA es la funcionalidad **primaria** del servicio (no un añadido dentro de otra cosa). Un asistente de propósito general al que le hablas para que te gestione tareas es exactamente ese caso. OpenAI confirmó que su propio contacto de WhatsApp dejaría de funcionar tras esa fecha. Lo que SIGUE permitido: una empresa que usa IA como parte accesoria de su soporte al cliente, no como el producto en sí.

**El atajo del número personal + código QR no es gratis de riesgo.** La forma técnica habitual de automatizar así un número personal es con librerías no oficiales (tipo Baileys) que emulan WhatsApp Web por ingeniería inversa. Sus propios creadores avisan de que esto no está afiliado a WhatsApp y desaconsejan la mensajería automatizada; usarlo así va contra los términos de WhatsApp y el riesgo real es que te bloqueen el número, sin aviso ni recurso. No es un detalle técnico menor: es apostar tu canal de entrada a una cuenta que puede desaparecer.

**Telegram no tiene ninguna de las dos restricciones.** Su Bot API es oficial, gratuita, y no hay ninguna política que prohíba montar un asistente de IA sobre ella. Es el mismo mecanismo técnico (bot, token, mensajes entrantes) sin la letra pequeña de arriba. Por eso el plan empieza ahí.

**El punto real donde se abandona no es este.** Es el paso 3 del montaje (§3, pieza 3): hacer que el modelo rellene EXACTAMENTE el esquema de TU base de datos, sin inventar campos ni duplicar filas. Eso no se pega y funciona a la primera: se prueba con notas de voz reales y se ajusta.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300"><text x="200" y="24" text-anchor="middle" font-size="17" font-weight="700" fill="#4b0a23">Por qué el plan empieza en Telegram</text> <rect x="12" y="46" width="182" height="190" rx="8" fill="rgba(254,70,41,0.05)" stroke="#fe4629" stroke-width="2"></rect><rect x="206" y="46" width="182" height="190" rx="8" fill="none" stroke="#4b0a23" stroke-width="1.5"></rect><text x="103" y="72" text-anchor="middle" font-size="16" font-weight="700" fill="#fe4629">Telegram</text> <text x="297" y="72" text-anchor="middle" font-size="16" font-weight="700" fill="#4b0a23">WhatsApp</text> <line x1="28" y1="84" x2="178" y2="84" stroke="rgba(75,10,35,.18)" stroke-width="1"></line><line x1="222" y1="84" x2="372" y2="84" stroke="rgba(75,10,35,.18)" stroke-width="1"></line><text x="28" y="108" font-size="13" fill="#4b0a23">– API oficial,</text> <text x="34" y="126" font-size="13" fill="#4b0a23">gratuita</text> <text x="28" y="150" font-size="13" fill="#4b0a23">– Sin restricción</text> <text x="34" y="168" font-size="13" fill="#4b0a23">para asistentes de IA</text> <text x="28" y="192" font-size="13" fill="#4b0a23">– Por eso</text> <text x="34" y="210" font-size="13" fill="#4b0a23">empieza aquí</text> <text x="222" y="108" font-size="13" fill="#4b0a23">– Cerrada a IA</text> <text x="228" y="126" font-size="13" fill="#4b0a23">desde 15-ene-2026</text> <text x="222" y="150" font-size="13" fill="#4b0a23">– Atajo QR: no oficial,</text> <text x="228" y="168" font-size="13" fill="#4b0a23">riesgo de bloqueo</text> <text x="222" y="192" font-size="13" fill="#4b0a23">– Canal de segunda,</text> <text x="228" y="210" font-size="13" fill="#4b0a23">no el principal</text> </svg> Telegram no tiene ninguna restricción para asistentes de IA; la puerta de WhatsApp está cerrada desde enero de 2026.

---

## 6 · Sumar más canales

El reel te dio uno. Cuando el de Telegram funcione, el patrón se repite:

**Telegram (ya lo tienes).** El más simple, el más limpio, y el primero por algo.

**WhatsApp por QR, con sus cautelas.** Si aun así quieres sumarlo, hazlo sabiendo lo del §5: usa tu propio número personal, no el de tu negocio principal (si lo bloquean, no te llevas por delante tu canal de atención a clientes real), y trátalo como un canal de segunda, no el principal, hasta que Meta abra otra vía oficial para esto. La mecánica técnica es la misma que Telegram (recibir un mensaje, extraer el audio, transcribir, decidir, ejecutar); lo único que cambia es la capa de conexión.

**Email.** Reenviar un correo a una dirección propia (`tareas@tudominio.com`) y procesarlo con un webhook de tu proveedor de correo (SendGrid Inbound Parse o equivalente) es el tercer canal más pedido: el texto del correo hace de "transcripción" ya hecha, así que te ahorras la pieza 2 entera para ese canal.

---

## 7 · Conectar más de una herramienta

El mismo patrón de function calling escala a varias herramientas de destino a la vez: en vez de darle al modelo UNA función (`crear_tarea_notion`), le das varias (`crear_tarea_notion`, `crear_evento_calendar`, `crear_contacto_crm`, `enviar_email`), cada una con su propio esquema de campos, y el modelo elige cuál llamar según lo que dijiste en la nota de voz ("recuérdame llamar a Juan el martes" dispara Calendar, "apunta que Juan pidió presupuesto" dispara el CRM). No es más complejo de montar, es más largo: repites la pieza 3 del §3 una vez por herramienta, con el esquema real de cada una (los campos de tu CRM, el formato de un evento de Google Calendar).

---

## 8 · El cobro por suscripción con tope de uso

Si vas a cobrarlo (a ti o a un cliente), la forma sana de facturar, dado que el coste real vive en la transcripción (§4): un plan mensual con un número de mensajes incluidos (por ejemplo, 300 notas de voz al mes) y un aviso o un tope duro al superarlo. Con Stripe, esto se monta con **facturación por uso** (*usage-based billing*): registras un evento cada vez que se procesa una nota de voz, y Stripe factura según el volumen del mes contra el plan contratado. Es la misma lógica de "asignación incluida en el plan" que usan los productos de este tipo, y con los costes del §4 el margen por mensaje es amplio incluso en el plan más barato.

---

## 9 · Tus primeros clientes de pago

No empieces buscando usuarios finales uno a uno; empieza donde ya hay gente cobrando por Notion a otros.

**Dónde:** el directorio oficial de consultores certificados de Notion, [notion.com/explore-consultants](https://www.notion.com/explore-consultants). Hay más de 100 perfiles activos, con presupuestos de proyecto declarados de 250 a más de 20.000 dólares, y varios ofrecen ya "configuración de bases de datos y automatización" como servicio. Filtra por ese servicio, por tu idioma y por región, y abre los perfiles con más reseñas.

**El gesto:** una tarde, entras en el directorio, filtras, y usas el botón de "Book" de cada perfil para agendar una llamada corta (o les escribes directo si el perfil da esa opción).

**El mensaje, literal:**

> "Hola \[nombre\]. Vi tu perfil en el directorio de consultores de Notion. Monto en un fin de semana un bot de Telegram que deja a tus clientes mandar una nota de voz y que la tarea aparezca ya creada en su Notion, sin abrir la app. ¿Te sirve como añadido de pago para los que ya llevas? Te lo dejo probando gratis en uno de tus proyectos esta semana."

**Por qué esto y no publicidad ni frío:** ellos ya tienen la relación y ya cobran por Notion; tú les das algo que pueden revender el mismo mes sin buscar un solo cliente nuevo. La distribución ya existe.

**Escaparate secundario:** Product Hunt. Ahí ya conviven productos vecinos a este mismo gesto (asistentes de voz, herramientas que conectan mensajería con notas), señal de que ahí busca gente que compraría esto. Lanzarlo como producto propio, aunque sea el tramo pequeño, te pone delante de esa misma audiencia sin escribirle a nadie uno por uno.

---

## 10 · Checklist: hazlo este fin de semana

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 350"><text x="200" y="24" text-anchor="middle" font-size="18" font-weight="700" fill="#4b0a23">Hazlo este fin de semana</text> <rect x="16" y="46" width="368" height="92" rx="8" fill="rgba(254,70,41,0.05)" stroke="#fe4629" stroke-width="2"></rect><circle cx="34" cy="66" r="6" fill="#fe4629"></circle><text x="50" y="71" font-size="15" font-weight="700" fill="#fe4629">HOY</text> <text x="34" y="90" font-size="13" fill="#4b0a23">– Bot con @BotFather + token</text> <text x="34" y="108" font-size="13" fill="#4b0a23">– Integración Notion + database_id</text> <text x="34" y="126" font-size="13" fill="#4b0a23">– Petición del §2 (bot + transcripción)</text> <line x1="34" y1="138" x2="34" y2="152" stroke="rgba(75,10,35,.18)" stroke-width="1.5"></line><rect x="16" y="152" width="368" height="92" rx="8" fill="none" stroke="#4b0a23" stroke-width="1.5"></rect><circle cx="34" cy="172" r="6" fill="none" stroke="#4b0a23" stroke-width="1.5"></circle><text x="50" y="177" font-size="15" font-weight="700" fill="#4b0a23">MAÑANA</text> <text x="34" y="196" font-size="13" fill="#4b0a23">– Esquema de tu base de datos (etapa 3)</text> <text x="34" y="214" font-size="13" fill="#4b0a23">– Etapa 4: crear página, probar 3 notas</text> <text x="34" y="232" font-size="13" fill="#4b0a23">– Corregir lo que falle</text> <line x1="34" y1="244" x2="34" y2="258" stroke="rgba(75,10,35,.18)" stroke-width="1.5"></line><rect x="16" y="258" width="368" height="76" rx="8" fill="none" stroke="#4b0a23" stroke-width="1.5"></rect><circle cx="34" cy="278" r="6" fill="none" stroke="#4b0a23" stroke-width="1.5"></circle><text x="50" y="283" font-size="14" font-weight="700" fill="#4b0a23">LA SEMANA QUE VIENE</text> <text x="34" y="302" font-size="13" fill="#4b0a23">– ¿Solo para ti o producto? (§8)</text> <text x="34" y="320" font-size="13" fill="#4b0a23">– Directorio + 5 mensajes (§9)</text> </svg> El plan de fin de semana repartido en tres tramos: hoy, mañana y la semana que viene.

**Hoy:**

- Crea tu bot con @BotFather y guarda el token.
- Crea tu integración interna en Notion (gratis) y copia el `database_id` de la base que vas a usar.
- Pégale a Claude Code la petición del §2, etapas 1-2 (bot + transcripción).

**Mañana:**

- Copia el esquema exacto de tu base de datos (nombre y tipo de cada campo) y dáselo a Claude Code para la etapa 3 (function calling).
- Monta la etapa 4 (crear la página en Notion) y prueba con tres notas de voz distintas, alguna ambigua a propósito.
- Corrige lo que el modelo rellene mal antes de darlo por terminado.

**La semana que viene:**

- Decide si lo usas solo tú o si lo conviertes en producto (§8, cobro por suscripción).
- Si vas a venderlo, abre el directorio de consultores del §9 y manda tus primeros cinco mensajes.

---

## Fuentes · esto es verdad porque

De dónde sale cada cosa. No me creas a mí, compruébalo.

**El caso (hechos verificados, congelados del episodio):**

- Qué es Notis (asistente al que le hablas por WhatsApp/Telegram/iMessage/Slack/email, ejecuta en Notion/Gmail/Calendar/HubSpot y más de 1.000 integraciones): [notis.ai](https://www.notis.ai/).
- Planes 20/59/149 $/mes con asignación de uso incluida: [notis.ai/pricing](https://www.notis.ai/pricing).
- La cifra: 16.731 $ de MRR y 529 suscripciones activas, verificada en [TrustMRR](https://trustmrr.com/startup/notis-ai).

**El montaje (recomendación, documentación oficial):**

- Telegram Bot API: el objeto `Voice`, `getFile`, `setWebhook`: [core.telegram.org/bots/api](https://core.telegram.org/bots/api).
- Telegram Bot API FAQ: gratis, límites de mensajes, Stars solo para difusión masiva: [core.telegram.org/bots/faq](https://core.telegram.org/bots/faq).
- Precios de transcripción y del modelo de decisión (leídos 2026-08-19, verifica los vigentes al montarlo): [developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing).
- Function calling / tool calling, mecanismo y terminología oficial: [developers.openai.com/api/docs/guides/function-calling](https://developers.openai.com/api/docs/guides/function-calling).
- API de Notion, crear página: [developers.notion.com/reference/post-page](https://developers.notion.com/reference/post-page).
- Límites de tasa de la API de Notion (3 peticiones/segundo por conexión, 500 KB por petición): [developers.notion.com/reference/request-limits](https://developers.notion.com/reference/request-limits).
- Directorio de consultores certificados de Notion (100+ perfiles, presupuestos 250-20.000+ $, servicio de automatización de bases de datos): [notion.com/explore-consultants](https://www.notion.com/explore-consultants).
- La plomería sin capa de decisión ya existe empaquetada en Zapier (disparador Telegram + acción Notion, sin que un modelo decida ni rellene nada): [zapier.com](https://zapier.com/apps/telegram/integrations/notion).

**La letra pequeña de WhatsApp (documentación oficial y verificación técnica):**

- Prohibición de la política de negocio de WhatsApp a proveedores de IA cuando su tecnología es la funcionalidad primaria, desde el 15 de enero de 2026, con cita literal de la política de Meta: [9to5Mac](https://9to5mac.com/2025/10/20/whatsapp-bans-ai-chatbots-from-using-its-business-api/).
- Riesgo de bloqueo al automatizar un número personal por QR con librerías no oficiales (Baileys), avisos de los propios mantenedores: [GitHub, Baileys](https://github.com/WhiskeySockets/Baileys).

**Lo que NO afirmamos (para no mentir):**

- Cómo está construido Notis por dentro técnicamente: no publica su stack; todo el "cómo montarlo" de esta guía es recomendación nuestra, no una radiografía del caso.
- Ningún porcentaje de crecimiento del caso.
- Que Notis use, en concreto, las librerías o el proveedor de IA que se recomiendan aquí: son nuestra elección para que montes el tuyo, no una afirmación sobre la suya.
- Los precios de las APIs y los importes exactos de las tablas: son de hoy, 2026-08-19, y cambian; que tu ayudante de IA confirme los vigentes al montarlo.