---
title: "Crea webs con IA"
source: "https://www.javiggil.com/0d3763dddd65?r=story_web"
author:
  - "[[Javi Gil]]"
published: 2026-08-28
created: 2026-10-17
description: "El proceso entero para montar cualquier web con IA, sin saber programar: el contenido con ChatGPT, el diseño con v0, publicada en Vercel con dominio propio y con funcionalidades de verdad. Con los prompts exactos de cada paso."
tags:
  - "clippings"
---
Esta guía te saca una web real, online y con dominio propio, sin saber programar. Da igual para qué: tu proyecto, tu negocio, un portfolio, una idea que quieres probar. El proceso es el mismo de principio a fin.

> **Truco:** Sube este documento a ChatGPT y dile: *"Esta es mi guía paso a paso. Quiero que me vayas guiando por cada sección. Cuando termine un paso, me explicas el siguiente. Si me atasco, ayúdame a solucionarlo."* Así tendrás un tutor personal durante todo el proceso.

---

## Lo que vas a necesitar

| Herramienta | Para qué | Coste | Link |
| --- | --- | --- | --- |
| ChatGPT | Generar el contenido de la web | Gratis | [chat.openai.com](https://chat.openai.com/) |
| v0.dev | Crear el diseño visual | Gratis (con límite de usos) | [v0.dev](https://v0.dev/) |
| Cursor | Preparar el código para publicar | Gratis (incluye tokens de IA) | [cursor.com](https://cursor.com/) |
| Vercel | Publicar la web en internet | Gratis | [vercel.com](https://vercel.com/) |
| Hostinger | Comprar el dominio (.com,.es...) | ~10€/año (se compra al final, cuando la web ya existe y funciona) | [hostinger.es](https://hostinger.es/) |

---

## Paso 0: Decide qué web vas a montar

Antes de tocar ninguna herramienta, contesta tres preguntas en una nota:

1. **Qué es.** Tu proyecto, tu negocio, tu portfolio, el negocio de un cliente.
2. **Qué tiene que hacer el visitante al llegar.** Llamarte, comprar, dejar el email, escribirte. Una sola cosa: la web entera empuja hacia ahí.
3. **Con qué la vas a llenar.** Datos reales: nombre, qué ofrece, para quién, contacto, y toda la prueba que tengas (reseñas, testimonios, resultados). Sin datos reales la IA rellena con humo, y el humo se nota.

---

## Paso 1: Genera el contenido con ChatGPT

Abre ChatGPT y usa este prompt (copia, pega y rellena los datos):

```
Actúa como un copywriter experto en páginas web.

Necesito el contenido para una página web de una sola página (landing page):

- Qué es: [tu proyecto / tu negocio / el negocio del cliente, en una frase]
- Para quién es: [el tipo de visitante que va a llegar]
- Objetivo de la página: [que llamen / que compren / que dejen el email / que te escriban]
- Datos reales: [nombre, qué ofrece, dirección y horario si los hay, teléfono o email de contacto]
- Prueba: [reseñas, testimonios o resultados reales. Pega los que tengas, literales]

Genera:
1. Un titular principal que transmita confianza
2. Un subtítulo de 1-2 frases
3. 3 secciones de servicios/beneficios con título y descripción corta
4. Sección "Sobre nosotros" (2-3 frases, tono cercano y profesional)
5. Sección de prueba (usa las reseñas o testimonios reales, sin inventar ninguno)
6. Llamada a la acción final (dirigida al objetivo de la página)
7. Datos de contacto en formato de pie de página

Tono: profesional pero cercano. Nada de frases genéricas.
Idioma: español.
```

![El prompt pegado en ChatGPT con los datos de un negocio de ejemplo rellenos, listo para enviar](https://www.javiggil.com/guia-webs/paso2-chatgpt.webp)

*El prompt relleno con un ejemplo (un taller mecánico), listo para enviar. Para esto no hace falta ni cuenta.*

> **Guarda la respuesta de ChatGPT** — la vas a usar en el siguiente paso.

---

## Paso 2: Crea el diseño con v0.dev

1. Ve a [v0.dev](https://v0.dev/) y crea una cuenta gratis
2. En el chat, escribe un prompt como este:

```
Crea una landing page profesional y moderna.

La web es: [qué es, en una frase]

Incluye estas secciones:
- Hero con el nombre, subtítulo y botón de [la acción principal: "Llámanos", "Comprar", "Apúntate"...]
- Servicios o beneficios (3 tarjetas)
- Sobre nosotros
- Reseñas o testimonios (3)
- Footer con los datos de contacto

Estilo: limpio, moderno, colores profesionales.
Que sea responsive (se vea bien en móvil).

Aquí está el contenido:
[PEGA AQUÍ TODO EL CONTENIDO QUE GENERÓ CHATGPT]
```

1. v0 te generará un diseño con preview en vivo
2. Si quieres cambiar algo, simplemente escríbelo en el chat: *"Hazme el botón más grande"*, *"Cambia los colores a azul oscuro"*, *"Pon las reseñas en formato de tarjetas"*
3. Cuando estés satisfecho, haz clic en **"Code"** en la parte superior para ver el código

![El prompt del diseño escrito en la caja de v0](https://www.javiggil.com/guia-webs/paso3-v0.webp)

*El mismo encargo pegado en v0, con el contenido de ChatGPT debajo.*

> **Hasta aquí es lo que te enseñan todos.** Lo que viene a continuación es lo que convierte un diseño bonito en una web real con un link que puedes enviar.

---

## Paso 3: Descarga el proyecto de v0

1. En v0.dev, con tu proyecto abierto, haz clic en el botón **"Add to Codebase"** (arriba a la derecha)
2. v0 te dará un comando `npx` para copiar. **No lo ejecutes todavía** — primero necesitas instalar las herramientas

### Instalar Node.js (si no lo tienes)

Node.js es lo que permite ejecutar el código en tu ordenador. Sin esto, nada funciona.

1. Ve a [nodejs.org](https://nodejs.org/)
2. Descarga la versión **LTS** (la que dice "Recomendado")
3. Instálalo como cualquier programa (siguiente, siguiente, instalar)
4. Para comprobar que se instaló bien, abre la **terminal**:
- **Windows:** busca "cmd" o "PowerShell" en el menú de inicio
- **Mac:** busca "Terminal" en Spotlight
5. Escribe `node --version` y pulsa Enter. Si ves un número como `v20.11.0`, está todo bien

![Página de descarga de Node.js con la versión LTS seleccionada y el instalador de macOS](https://www.javiggil.com/guia-webs/paso4-nodejs.webp)

*La página de descarga. La versión LTS viene marcada; baja el instalador de tu sistema y siguiente, siguiente, instalar.*

### Descargar el código de v0

1. Abre la terminal
2. Navega a donde quieras guardar el proyecto. Por ejemplo:
- `cd Desktop` (para ir al escritorio)
3. Ahora pega el comando que te dio v0 y pulsa Enter
4. Se creará una carpeta con todo el código del proyecto

---

## Paso 4: Prepáralo para publicar con Cursor

Aquí es donde Cursor hace la magia. Cursor es un editor de código con IA integrada - le dices lo que quieres en español y él escribe el código por ti.

### Instalar Cursor

1. Ve a [cursor.com](https://cursor.com/) y descárgalo
2. Instálalo como cualquier programa
3. Al abrirlo por primera vez, te pedirá crear una cuenta - **la cuenta gratuita incluye tokens de IA**, suficiente para este proyecto

![Web de Cursor con el botón de descarga](https://www.javiggil.com/guia-webs/paso5-cursor.webp)

*cursor.com. Descargar, instalar, cuenta gratuita, y ya tienes el editor con la IA dentro.*

### Abrir el proyecto

1. Abre Cursor
2. Ve a **File → Open Folder**
3. Selecciona la carpeta del proyecto que descargaste de v0

### Pedirle a Cursor que prepare el deploy

Abre el chat de IA de Cursor (el panel de la derecha o pulsa `Ctrl+L` / `Cmd+L`) selecciona algún modelo de claude y escríbele:

```
Necesito preparar este proyecto para desplegarlo en Vercel.

Por favor:
1. Revisa que el proyecto tenga un package.json correcto
2. Asegúrate de que tenga un script "build" configurado
3. Si falta algo para que funcione en Vercel, añádelo
4. Ejecuta npm install para instalar las dependencias
5. Haz un build de prueba para confirmar que no hay errores

Dime paso a paso lo que estás haciendo.
```

Cursor hará todo el trabajo. Si hay algún error, simplemente copia el error y pégalo en el chat: *"Me sale este error: \[error\]. Solucionalo"*

> **Si te atascas:** Copia el error exacto, ve a ChatGPT, y pregúntale. Casi siempre tiene la solución.

---

## Paso 5: Publica en Vercel

### Crear cuenta en Vercel

1. Ve a [vercel.com](https://vercel.com/)
2. Haz clic en **"Sign Up"**
3. Regístrate con tu cuenta de GitHub (si no tienes una, créala gratis en [github.com](https://github.com/))

![Pantalla de proyecto nuevo en Vercel con el botón Continue with GitHub](https://www.javiggil.com/guia-webs/paso6-vercel.webp)

*La pantalla de proyecto nuevo en Vercel. Continue with GitHub y a importar tu proyecto.*

### Opción A: Subir desde Cursor (lo más fácil)

En el chat de Cursor, escribe:

```
Ayúdame a subir este proyecto a Vercel.

Quiero:
1. Instalar Vercel CLI si no está instalada (npm i -g vercel)
2. Hacer login en Vercel desde la terminal
3. Desplegar el proyecto

Guíame paso a paso.
```

Cursor te guiará por el proceso. Básicamente:

- Instalará la herramienta de Vercel en tu ordenador
- Te pedirá que inicies sesión (se abre el navegador)
- Subirá el proyecto y te dará un link como `tu-proyecto.vercel.app`

### Opción B: Subir desde la web de Vercel

1. Sube tu proyecto a GitHub (Cursor puede hacerlo por ti — pídele: *"Sube este proyecto a un nuevo repositorio en GitHub"*)
2. Ve a [vercel.com/new](https://vercel.com/new)
3. Conecta tu cuenta de GitHub
4. Selecciona el repositorio de tu proyecto
5. Haz clic en **"Deploy"**
6. En 1-2 minutos tendrás tu web online

> **En este punto ya tienes una web funcional** con un link tipo `nombre-proyecto.vercel.app`. Ya la puedes enseñar a quien quieras. Y no has invertido ni un euro.

---

## Paso 6: Compra un dominio y conéctalo

### Comprar el dominio

1. Ve a [hostinger.es](https://hostinger.es/) → Dominios
2. Busca un dominio que tenga sentido para la web. Ejemplos:
- `restauranteelbuengusto.es`
- `tallergarcia.com`
- `tunombre.com`
3. Compra el dominio (suelen costar entre 5-15€ el primer año)

![Buscador de dominios de Hostinger con tallergarcia.com ocupado y la alternativa .es con su precio](https://www.javiggil.com/guia-webs/paso7-hostinger.webp)

*La búsqueda real: te dice si está libre, y si está pillado te saca alternativas con su precio al lado.*

### Conectar el dominio a Vercel

**En Vercel:**

1. Ve a tu proyecto en [vercel.com](https://vercel.com/)
2. Ve a **Settings → Domains**
3. Escribe tu dominio nuevo (ej: `restauranteelbuengusto.es`) y haz clic en **Add**
4. Vercel te mostrará los datos DNS que necesitas. Apunta:
- **A Record:** los números que te den
- **CNAME para www:** el valor que te indique Vercel

**En Hostinger:**

1. Entra en tu cuenta de Hostinger
2. Ve a **Dominios → tu dominio → Gestionar**
3. Busca **DNS / Nameservers**
4. Edita el **registro A** (el que tiene `@` como host):
- Cambia el valor a los números que te haya dado vercel.
5. Añade un **registro CNAME**:
- Host: `www`
- Valor: el que te dio Vercel (tipo `cname.vercel-dns.com`)
6. Guarda los cambios

> **Importante:** Los cambios de DNS pueden tardar entre 10 minutos y 48 horas en propagarse. Normalmente funciona al instante.

**Vuelve a Vercel** y haz clic en **"Refresh"** en la sección de dominios. Cuando veas que el estado cambia a ✅, tu web ya está online con tu dominio propio.

---

## Meter funcionalidades complejas

Tu web no tiene por qué quedarse en escaparate. Un sistema de reservas, un formulario que te manda email, pagos. El circuito es siempre el mismo:

**1.** Abres chatGPT y le dices que tienes tu web en vercel, que quieres meter (por ejemplo) un sistema de reservas, que te cree un informe muy detallado de lo que conlleva para el equipo de desarrolladores.

**2.** Con ese informe, abres cursor y lo pegas, le dices que vaya paso a paso, que si necesita que hagas algo pare, te lo diga y le avisas cuando lo tengas hecho.

---

## Solución de problemas comunes

| Problema | Solución |
| --- | --- |
| "npm no se reconoce como comando" | Node.js no está instalado. Vuelve al Paso 3 e instálalo. |
| Error en el build de Vercel | Copia el error completo, pégalo en ChatGPT o en el chat de Cursor y pregunta cómo solucionarlo. |
| El dominio no conecta | Espera hasta 48h. Si después de eso sigue sin funcionar, revisa que los registros DNS en Hostinger coincidan exactamente con lo que dice Vercel. |
| Cursor no responde | Comprueba que tienes tokens disponibles en tu cuenta gratuita. Si se han agotado, puedes continuar con ChatGPT copiando y pegando el código. |
| v0 se queda sin usos gratuitos | Crea el diseño con ChatGPT pidiéndole que te genere el HTML y CSS directamente, y luego ábrelo en Cursor para mejorarlo. |

---

## Recursos opcionales para profundizar

Estos tutoriales son **opcionales** — no los necesitas para completar esta guía, pero si quieres entender mejor las herramientas, te ayudarán.

### Cursor (editor de código con IA)

- 🎥 [Cursor Tutorial for Beginners — Tech with Tim](https://www.classcentral.com/course/youtube-cursor-tutorial-for-beginners-ai-code-editor-353514) — 15 min, perfecto para empezar desde cero
- 🎥 [Cursor AI Tutorial 2025 Edition — Volo Builds](https://x.com/VoloBuilds/status/1898034342657433714) — tutorial completo actualizado
- 📖 [Cursor AI: Guía paso a paso — The Prompt Warrior](https://www.thepromptwarrior.com/p/cursor-ai-tutorial-for-beginners) — guía escrita para los que prefieren leer
- 📖 [Cursor directory — Videos y tutoriales](https://cursor.directory/learn) — colección de tutoriales oficiales

### v0.dev (generador de diseños con IA)

- 📖 [v0 by Vercel: Guía con proyecto demo — DataCamp](https://www.datacamp.com/tutorial/vercel-v0) — tutorial paso a paso
- 🌐 [v0.dev Community](https://v0.dev/community) — ejemplos y plantillas de la comunidad

### Vercel (publicar tu web)

- 📖 [Deploy en Vercel — Documentación oficial](https://vercel.com/docs/frameworks/full-stack/nextjs) — la referencia definitiva
- 📖 [Conectar dominio de Hostinger a Vercel — Guía paso a paso](https://medium.com/@rajanraj8979/learn-how-to-connect-your-hostinger-domain-to-your-vercel-deployed-project-with-this-easy-966f082919f3)
- 🎓 [Vercel Academy](https://vercel.com/academy) — cursos gratuitos oficiales

---

## Checklist final

- Decidí qué web monto y qué tiene que hacer el visitante
- Generé el contenido con ChatGPT
- Creé el diseño en v0.dev
- Descargué el código e instalé Node.js
- Preparé el proyecto con Cursor
- Publiqué en Vercel y tengo un link funcionando
- Compré un dominio y lo conecté

---

> **Recuerda:** Esto no es magia. Es una habilidad real que el 99% de la gente no tiene. La primera web te la peleas. La segunda te sale en una tarde. Y cada una te enseña algo.

Si tienes dudas en cualquier paso, sube esta guía a ChatGPT y dile dónde estás atascado. La IA es tu compañero en todo este proceso.