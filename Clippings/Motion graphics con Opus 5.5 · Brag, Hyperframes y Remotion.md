---
title: "Motion graphics con Opus 5.5 · Brag, Hyperframes y Remotion"
source: "https://www.tododeia.com/community/motion-graphics-opus-55"
author:
  - "[[tododeia]]"
published:
created: 2026-10-17
description: "Tres herramientas, un estudio. Brag convierte tu proyecto o sitio en un video de lanzamiento de 20 segundos con música y texto para compartir; Hyperframes te da control total en HTML; Remotion maneja series, plantillas y videos con datos. Aquí van los prompts listos, cómo elegir cuál usar, y cómo hacer que Opus revise sus propios frames."
tags:
  - "clippings"
status: procesado
promoted_to: "[[Motion graphics con IA - Brag, Hyperframes y Remotion]]"
---
Ficha

Motion graphics con Opus 5.5

Nivel

Intermedio

Temas

motion-graphics, brag, hyperframes, remotion

Qué necesitas

Claude Code con Opus 5.5, Node 22 o más nuevo y ffmpeg. No tienes que programar: Claude instala lo demás.

Cuánto toma

Unos 10 minutos de instalación. Tu primer video de 20 segundos sale en una sola sesión.

motion-graphicsbraghyperframesremotion

01 · Cómo funciona

## Opus escribe un programa que dibuja el video

Opus 5.5 recibe texto e imágenes y devuelve texto. No puede entregarte un MP4. Cada video de motion graphics hecho con código es un programa que escribió Opus, y otra herramienta lo convirtió en frames.

El truco es el determinismo. El programa pinta el frame exacto de cualquier segundo; un navegador sin pantalla lo captura frame por frame y ffmpeg junta todo en el video. Como nada depende de un reloj, el mismo programa da siempre el mismo video, y cambiar algo es editar una línea y volver a renderizar.

Esa mecánica ya viene resuelta en las tres herramientas de esta guía. Tú eliges cuál te conviene según lo que vas a hacer.

Brag

Un video de lanzamiento, en un comando

Lee tu proyecto o tu sitio, decide el ángulo y el gancho, y te entrega un video de 15 a 25 segundos con música, movimiento y el texto para compartirlo. Es la forma más rápida de tener algo publicable.

Hyperframes

Control total, en HTML

Defines el video como una página web con tiempos y la animas con GSAP, CSS u otras librerías. Brag lo usa por debajo en su modo completo. Tú lo usas directo cuando el video tiene que ser exactamente como lo imaginas.

Remotion

Series, plantillas y videos con datos

Los videos son componentes de React. Es la mejor opción cuando vas a hacer muchos videos parecidos, o uno que cambia según los datos que le pases.

Cuál uso, según lo que quiero

- Quiero presumir lo que acabo de construir, o el sitio de un cliente: Brag.
- Quiero un video a mi medida, con mi propio guion de tomas y animaciones exactas: Hyperframes.
- Quiero diez, cien o mil videos con la misma plantilla y datos distintos: Remotion.
- No sé: empieza con Brag. Si te queda corto, ya sabes a cuál saltar.

Una nota sobre licencias

Brag es MIT y Hyperframes es Apache 2.0: puedes usarlos para tu trabajo y para clientes sin pagar licencia.

Remotion es gratis para individuos y para empresas de hasta 3 personas. Con 4 o más, necesitas una licencia de empresa. Si vas a vender videos hechos con Remotion desde una agencia, revisa su página de precios antes de empezar.

02 · Instala el estudio

## Diez minutos y tienes las tres herramientas

El chat de Claude puede escribir una animación, pero solo Claude Code (o cualquier agente con terminal) puede renderizarla, escucharla y mirar sus propios frames. Ese ciclo de revisión separa el primer intento flojo del que se quejan muchos de los videos que sí funcionan.

No instalas nada a mano. Abre una carpeta vacía, arranca Claude Code ahí con Opus 5.5 y pega esto.

### Prepara mi estudio de motion graphics

Claude revisa qué tienes, instala lo que falta y confirma que Hyperframes funciona, que es la base de las otras dos.

```
Prepárame un estudio de motion graphics en esta carpeta. Yo no programo: instala todo y dime qué hacer solo cuando haga falta algo mío.

1. Revisa qué tengo instalado (Node 22 o más nuevo, ffmpeg) y dime qué falta. Instala lo que falte con el gestor que corresponda a mi sistema, explicándome cada comando antes de correrlo.
2. Corre npx hyperframes doctor y dime si todo está bien. Si algo falla, arréglalo.
3. Instala las skills de Hyperframes con npx hyperframes skills update.
4. Instala las skills de Remotion con npx skills add remotion-dev/skills.
5. Si el plugin de Brag no está, dime que lo instale yo con los dos comandos de /plugin, porque esos se escriben dentro de Claude Code y no los puedes correr tú.

Al final, dime en tres líneas qué quedó instalado y qué comando uso para empezar un video con cada herramienta.
```

El único paso que tienes que hacer tú es instalar Brag. Esos dos comandos se escriben dentro de Claude Code, no en la terminal. El plugin incluye también brag-slim, la versión ligera que usa Opus 5.5.

Brag, dentro de Claude Code

`/plugin marketplace add latent-spaces/brag /plugin install brag@brag`

Brag en otro agente (Cursor, Codex, Gemini CLI…), en la terminal

`npx skills add https://github.com/latent-spaces/brag --skill brag`

Solo la versión ligera de Brag, en la terminal

`npx skills add https://github.com/latent-spaces/brag --skill brag-slim`

Opus 5.5 arranca en esfuerzo medium y siempre piensa antes de responder. Para un video nuevo conviene subirlo. Escribe /effort dentro de Claude Code y elige el nivel. La opción max solo dura la sesión en la que la pones.

medium

Arreglos y re-renders

Para cambiar un color, mover una toma o volver a renderizar. Es el nivel con el que arranca Opus 5.5.

xhigh

Un video nuevo

El nivel para un video de lanzamiento desde cero. Alcanza para que el resultado se vea trabajado.

max

Cuando los primeros 3 segundos cargan todo

Para el video que tiene que enganchar de inmediato. Es más lento; guárdalo para la pieza importante.

Reglas de la casa (CLAUDE.md)

El archivo que Claude Code lee en cada corrida: qué herramienta usar para qué, el look prohibido, el sonido y el bucle de crítica. Va en la raíz de la carpeta donde trabajas y no tienes que repetirlo en cada video.

[Descargar CLAUDE.md](https://www.tododeia.com/docs/motion-graphics-opus-55/CLAUDE.md)

03 · Tu primer video con Brag

## Una frase con un género que Opus ya conoce

Un buen prompt corto funciona cuando fija un género con reglas conocidas. Eso es Brag: la frase vamos a presumir esto le dice a Opus que hable de un lanzamiento, y todo lo demás (cómo se estructura, cuánto dura, qué se muestra) ya viene escrito dentro de la skill.

Entra a la carpeta de tu proyecto, abre Claude Code y escribe la frase. Brag lee el código (los colores y las tipografías exactas, el README, las pantallas principales), decide el ángulo y el gancho, y arma el video.

### La frase mínima

Dentro de la carpeta de tu proyecto. Claude Code arma plan, video, portada y texto para compartir.

```
vamos a /brag este proyecto
```

### Con el plan primero

La versión que recomiendo. Brag escribe el plan antes de construir, y tú lo ajustas antes de que se gaste el render.

```
Vamos a /brag este proyecto. Formato vertical, 20 segundos.

Antes de construir nada, enséñame brag-plan.md con el ángulo, el gancho, los 2 o 3 momentos que se van a mostrar, el remate y el storyboard escena por escena. Espera mi visto bueno. Si algo no me gusta, lo cambiamos y solo entonces construyes y renderizas.
```

Dos modos, y Opus 5.5 elige el ligero

- En Opus 5.5, /brag pasa solo a brag-slim: Opus arma el video completo él mismo, sin Hyperframes y sin recursos empaquetados, con las mismas reglas creativas. Es el que vas a usar casi siempre.
- Si quieres el flujo clásico con Hyperframes (o la voz), pide el modo completo con /brag --full.

Las opciones, en lenguaje normal

- Tono: elige uno de los siete (en la sección siguiente) o descríbelo con tus palabras. Si no dices nada, Brag lo infiere.
- Formato: horizontal (1920x1080, el que viene por defecto), vertical (1080x1920) o cuadrado (1080x1080), a 30 cuadros por segundo.
- Duración: unos 20 segundos. Entre 15 y 25 es el rango sano.
- Música y efectos: vienen prendidos. En el modo completo puedes apagarlos con no-music y no-sfx.
- Voz: narración con Kokoro a través de Hyperframes. Solo existe en el modo completo y viene apagada.

Qué te deja en la carpeta

- brag-output/brag.mp4: el video.
- brag-output/brag.jpg: la portada, un frame fuerte y ya asentado. También queda como primer frame del video, para que cualquier plataforma la muestre de miniatura.
- brag-output/share-copy.txt: de una a tres frases listas para publicar, sin el estoy emocionado de compartir.
- brag-output/brag-plan.md: el ángulo y el storyboard. En el modo completo se suma el brief de composición.
- Si ya existe esa carpeta, la nueva sale con fecha y hora para no pisar la anterior.

Las reglas de Brag que sirven para cualquier video

- Corto: de 15 a 25 segundos. Entre 18 y 22 es el punto dulce.
- El gancho lo es todo: los primeros 2 segundos deciden si alguien sigue viendo. Se planea primero.
- Claro para un desconocido: tras verlo una vez, entiende qué hace, para quién es y cómo conseguirlo.
- Muestra lo real: la interfaz del producto haciendo su trabajo, no una descripción de ella. Nada de relleno abstracto.
- Específico: tiene que sentirse hecho para ese proyecto, con su propio texto y sus propias afirmaciones. Frases como optimiza tu flujo de trabajo están prohibidas.
- Legible: un texto que hay que leer se queda completo y quieto unos 0.3 segundos por palabra.
- Cada frame se puede publicar: cualquier cuadro congelado tiene que valer la pena compartirse.

04 · Tonos y tu producto

## El mismo proyecto, siete personalidades

El tono cambia el ritmo, la escritura, la tipografía y las transiciones. Son puntos de partida: una dirección libre los afina o los reemplaza.

default

Juguetón, limpio, para compartir

De 4 a 5 escenas con transiciones suaves. El producto es gracioso a su manera.

polished

Serio y elegante

De 3 a 4 escenas con pausas largas y fundidos suaves. Para productos que no son un chiste.

yc-parody

Lanzamiento de startup, dicho muy en serio

De 4 a 5 escenas, una afirmación en cada una y cortes secos. La gracia sale de decirlo sin guiñar el ojo.

chaotic

Rápido, fuerte, TODO EN MAYÚSCULAS

De 6 a 8 escenas, algunas de menos de 2 segundos, con cortes de destello y zoom.

deadpan

Calmado y seco

De 3 a 4 escenas con mucho espacio vacío y fundidos lentos. Nada es un chiste, y de ahí sale el chiste.

cinematic

Escala de tráiler

De 4 a 5 escenas con tipografía enorme, afirmaciones épicas y cortes dramáticos.

app-store

Tarjetas de funciones limpias

De 4 a 6 escenas con deslizamientos suaves. Corporativo, pero no aburrido.

Una dirección libre funciona mejor que un adjetivo suelto. Estas tres ideas salen del propio repo y cambian por completo cómo se siente el video:

### Un lanzamiento falso de una Serie A de 2016

Parodia de startup, con la gravedad que le pondrías a una ronda de inversión.

```
/brag --tone "lanzamiento falso de una Serie A de 2016"
```

### Una pieza de museo

El producto como si fuera una exposición, con ficha técnica y todo.

```
/brag --tone "pieza de museo, con ficha técnica y silencio entre salas"
```

### Un anuncio sobreproducido de un juego móvil

Todo exagerado: zooms, explosiones de color, una promesa absurda.

```
/brag --tone "anuncio sobreproducido de un juego móvil"
```

### Apúntalo a un sitio, no solo a tu código

Brag también puede partir de una dirección web: la de tu producto o la de un cliente. Entra al sitio como lo vería un visitante (cierra los avisos de cookies y baja sección por sección, porque lo que se anima al hacer scroll sale en blanco en una sola captura), junta el texto, los colores, la tipografía, el logo y las capturas, y arma el video con eso.

La regla de oro es la misma: usa lo real. Recorta y anima la interfaz de verdad en vez de redibujarla de memoria. Una cifra, un testimonio o una afirmación inventados quedan prohibidos.

### Video de lanzamiento de un sitio

Cambia la dirección, el formato y el tono. Brag pide el plan antes de construir para que ajustes el ángulo.

```
/brag [URL DEL PRODUCTO] --format vertical --duration 20 --tone [polished, yc-parody, el que quieras]

Reglas para este video:
- Entra al sitio, usa capturas reales, el logo real, los colores y las tipografías reales. Guarda lo que descargues en la carpeta de trabajo y enséñame la lista antes de animar.
- Nunca redibujes la interfaz del producto de memoria: recorta y anima la real.
- Estructura: gancho de máximo 5 palabras con la tipografía enorme, aparece el producto y la interfaz se arma pieza por pieza, tres funciones cada una como un momento real de uso, [UNA CIFRA REAL del sitio] y el cierre con el logo y [LLAMADA A LA ACCIÓN].
- Música original, y efectos suaves por debajo de la música.

Antes de construir, enséñame brag-plan.md y espera mi visto bueno. Al final, genera también las versiones cuadrada y horizontal.
```

### Si quieres que el video hable

La narración existe solo en el modo completo, con la voz de Kokoro a través de Hyperframes, y hay que pedirla: viene apagada. Va escrita para complementar lo que se ve, no para leer el texto en pantalla.

Cuando uses un servicio de voz o cualquier otro que pida llave, guárdala en un archivo.env y dile a Claude el nombre de la variable. Nunca pegues una llave real en un prompt, sobre todo si vas a tomar captura de pantalla.

### Un video con narración

Modo completo y voz. Más lento que el ligero, pero con un narrador que acompaña a la imagen.

```
/brag --full --voice --format vertical --tone polished

Escribe una narración corta, natural y específica de este producto. Que complemente lo que se ve en pantalla y no lea el texto que ya está escrito. Que cada frase caiga en su escena y que el ritmo no se pase de 25 segundos. Enséñame el guion de la voz junto con el plan antes de renderizar.
```

05 · Referencia

## Nombra un estilo y dale un frame para copiar

Sin referencia, Opus cae en su default: texto centrado, fondo con degradado y todo entrando con un fade. Nombrar un estilo funciona mejor que describirlo, y un video o un frame le da ritmo, tipografía y transiciones que imitar.

Un detalle importante con Brag: usa los colores y las tipografías reales de tu proyecto, así que la referencia le da otras cosas, que son el ritmo, el tipo de cortes, la textura y cómo entra y sale el texto. Para la identidad visual, la que vale es la tuya.

Un frame

Una captura de un video que te gusta

Adjúntala y di qué tomar (ritmo, grano, tipo de transición) y qué no (el tema). Con un solo frame ya se puede arrancar.

Un video

El archivo o el enlace

Pídele que extraiga frames con ffmpeg y que describa el ritmo toma por toma antes de escribir una sola línea de código.

Una biblioteca

Tu propia carpeta de imágenes o trabajos

Pídele que escriba primero un style\_guide.md a partir de ella. Tu biblioteca es una referencia que nadie más puede copiar.

Dónde buscar

De dónde sacar referencias

Videos de lanzamiento de productos de tu categoría, Dribbble en la sección de motion y las películas de lanzamiento de tu competencia.

### Estudia la referencia y úsala en el video

Claude saca los frames, escribe la guía de estilo y se detiene a esperar tu visto bueno. Después la usa como dirección de Brag.

```
Referencia: ./refs/lanzamiento.mp4 (y ./refs/frames/*.png)

1. Extrae un frame cada 0.5 s con ffmpeg y estúdialos.
2. Escribe ./docs/style_guide.md: duración típica de las tomas, tipos de transición, movimientos de cámara, textura y grano, tipografía (peso, espaciado) y cómo entra y sale el texto. Toma la gramática de la referencia, nunca su contenido, logos ni personajes.
3. Enséñame el archivo y espera mi visto bueno.
4. Cuando lo apruebe, corre /brag con esa guía como dirección de tono: el ritmo y los cortes salen de style_guide.md, y los colores, tipografías y recursos salen de mi proyecto.
```

Cuando das una referencia, deja que el modelo elija la técnica. Especifica el look y las restricciones, no la librería.

06 · Hyperframes

## Cuando el video tiene que ser exactamente como lo imaginas

Hyperframes define un video como una página HTML: tiempos en atributos, pistas, y animaciones con GSAP, CSS, Lottie, Three.js u otras librerías. Un renderizador captura cada frame en Chrome sin pantalla y ffmpeg los junta, así que el mismo archivo da siempre el mismo video.

Es el motor que Brag usa en su modo completo. Cuando quieres tu propio guion de tomas, animaciones exactas o un video que no es un lanzamiento (un explicador, un pitch, subtítulos animados sobre tus notas), lo usas directo.

Trae unas veinte skills, y la que enruta es /hyperframes: le dices qué video quieres y ella carga la que toca. Claude Code las usa solo.

Hyperframes · 1. En la terminal

`npx hyperframes init mi-video && cd mi-video npx hyperframes skills update claude`

Hyperframes · 2. Para ver y exportar, en la terminal

`npx hyperframes preview npx hyperframes render`

Hyperframes · si algo falla, en la terminal

`npx hyperframes doctor`

### De tus notas a un video pitch

Dentro de Claude Code, ya en la carpeta del proyecto. Claude enruta con /hyperframes, escribe la composición y te da la vista previa.

```
Usando /hyperframes, convierte ./notas.md en un video pitch de 45 segundos con subtítulos animados. Vertical, 9:16.

1. Léelas y dime en una frase cuál es el mensaje central. Si hay más de uno, elige el más fuerte.
2. Escribe docs/shotlist.md con cada toma, su duración, el texto que aparece y el movimiento. Enséñamela y espera mi visto bueno.
3. Construye la composición, corre npx hyperframes check y arregla todo lo que reporte (incluido el contraste del texto).
4. Abre la vista previa con npx hyperframes preview y dame el enlace local para verla antes de renderizar.
```

Para un render de prueba usa calidad draft; para el final, calidad high. Dile a Claude cuál quieres y él agrega la opción al comando de render.

07 · Remotion

## Una plantilla y mil videos

Remotion trata cada video como un componente de React. Esa idea sirve sobre todo cuando el video es una plantilla: le pasas datos (un título, una cifra, una foto) y sale uno distinto. Con una tabla de cien filas, salen cien videos.

Las skills le enseñan a Claude a crear y renderizar proyectos de Remotion. Tú describes el video y él escribe los componentes; el estudio de Remotion te deja previsualizar y recorrer la línea de tiempo mientras afinas.

Remotion · 1. En la terminal

`npx create-video@latest mi-serie && cd mi-serie npx skills add remotion-dev/skills claude`

Remotion · 2. Dentro de Claude

`/remotion-create un video de 20 s, 9:16, solo resortes y un color de acento`

Remotion · 3. Para verlo y exportarlo, en la terminal

`npx remotion studio npx remotion render Main out/video.mp4`

### Una plantilla que se llena con datos

Para series: un boletín en video, una cifra de la semana, el catálogo de un cliente. Claude arma la plantilla y renderiza una versión por fila.

```
Usando /remotion-create, quiero una plantilla de video vertical de 12 segundos para [TIPO DE VIDEO: por ejemplo la cifra de la semana, un producto del catálogo, una frase del día].

1. La plantilla recibe estos datos: [LISTA: título, cifra, texto corto, imagen]. Con ellos arma el video completo; nada de texto escrito a mano dentro de la animación.
2. Un solo color de acento, una tipografía de display y una de lectura. Los resortes con un rebote mínimo.
3. Crea un archivo datos.csv con 3 filas de ejemplo y renderiza un video por fila en la carpeta out/.
4. Enséñame una hoja de contacto de uno de los tres videos antes de seguir con más filas.
5. Dime cuánto tarda cada render, para saber cuántos puedo hacer de una sola vez.
```

Recuerda la licencia: Remotion es gratis para individuos y empresas de hasta 3 personas. Para equipos de 4 o más, necesitas la licencia de empresa.

08 · La lista de estados

## Escribe los estados, no la vibra

Cuando Brag se queda corto (porque quieres una película de producto con una interfaz que se transforma, por ejemplo), el prompt que mejor funciona no es una línea. Es una especificación: qué datos pedirte, la dirección, una lista de estados toma por toma, reglas de construcción y trampas que evitar.

La idea detrás es una forma que nunca se corta. Un solo elemento cambia de tamaño, radio y color de un estado al siguiente (botón, cargador, reproductor, gráfica, paleta de comandos), un cursor dispara cada cambio con clics reales, y el último frame es igual al primero para que haga loop.

Esta plantilla funciona igual en Hyperframes que en Remotion. Cuando la pegas, Claude primero te pregunta los datos y te enseña la lista de estados sobre el ritmo de la música, antes de escribir código.

### Plantilla de lista de estados para un video de producto

Una sola forma que se transforma por toda la película. Sustituye la herramienta por la que vayas a usar.

```
Herramienta: [/hyperframes o /remotion-create].

<datos>
Pídeme: mi producto y su URL, de 8 a 12 estados de la interfaz que cuenten su historia, los datos reales que se ven en cada estado, colores y tipografías de la marca más un acento, una pista libre de derechos cerca de 120 BPM, y los formatos.
</datos>

<direccion>
Movimiento de interfaz estilo película de producto. Un contenedor que nunca se corta: cada estado es el mismo elemento cambiando de tamaño, radio y relleno mientras su contenido cambia detrás de un desenfoque corto. Un cursor dispara cada cambio. Lienzo neutro cálido y un solo acento. Resortes con apenas un poco de rebote.
Prohibido: easing rebotón, brillos, degradados en la interfaz, explosiones de partículas, tiempo muerto.
</direccion>

<estructura>
120 BPM, 8 compases, algo pasa en cada beat.
logo, botón de llamada a la acción, campo de correo (se escribe), cargador, palomita de éxito, tarjeta de panel, la gráfica se dibuja sola, tooltip al pasar el cursor, paleta de comandos, aviso, logo.
</estructura>

<construccion>
1. Todo es función pura del tiempo: sin timers, sin transiciones que corran solas, sin estado que pase entre frames.
2. Resortes de forma cerrada. Un valor con varios destinos es la suma de un resorte por cada cambio, nunca un resorte que se reinicia.
3. El texto dentro de un contenedor que se transforma entra después de que empieza el cambio y sale antes del siguiente.
4. Los indicadores de pestañas: el borde de adelante y el de atrás con resortes distintos, para que se estiren.
5. Cuadrícula de tiempos desde la pista. Empieza en un tiempo fuerte. Los sonidos de interfaz van sobre los picos medidos.
6. Render a 30 cuadros por segundo, o 60 si la herramienta lo permite sin que se arrastre.
</construccion>

<trampas>
Nunca uses will-change en nada que la cámara escale (el texto se ve borroso).
El último frame tiene que ser igual al primero, con la posición y la velocidad del cursor incluidas.
</trampas>

<empezar>
Pídeme los datos y luego enséñame la lista de estados sobre la cuadrícula de tiempos antes de escribir código.
</empezar>
```

09 · Movimiento y sonido

## Que se sienta caro, y que suene a una sola pieza

El movimiento barato va de A a B por una curva fija. El movimiento caro tiene masa: acelera, se pasa un pelo y se asienta. Eso son los resortes, y Remotion trae uno nativo, spring(). En Hyperframes, Claude escribe el resorte como una función del tiempo y GSAP la anima. En los dos casos el movimiento sigue siendo función pura del tiempo.

Cuando un valor cambia de destino varias veces (un cursor, el ancho de un contenedor), no reinicias el resorte: sumas uno por cada cambio, cada uno empezando en su momento. El movimiento queda continuo y puedes renderizar cualquier frame sin simular los anteriores.

Los parámetros se eligen por personalidad, no por números. Dile a Claude cuál quieres y él los ajusta.

Seco

Botones, interruptores y bordes de ataque

Rápido y sin rebote. Para todo lo que el cursor activa.

Estándar

Tarjetas, contenedores y cámara

El punto medio. Si dudas, empieza aquí.

Pesado

Tipografía grande, objetos 3D y logos

Lento al arrancar, con peso. Los cierres con logo se ven mejor así.

Juguetón

Mascotas y stickers

Con rebote visible. Solo para lo que tiene que sentirse vivo.

### Cambia todo el easing por resortes

Claude refactoriza toda la composición de una pasada. Úsalo cuando el movimiento se vea plano o mecánico.

```
Reemplaza cada curva de easing de esta composición por resortes (spring() si es Remotion; si es Hyperframes, una función de resorte que alimente a GSAP). Rebote mínimo en la interfaz, ninguno en la tipografía. Cualquier valor con más de un destino suma un resorte por cada cambio. Los botones y bordes de ataque con el perfil seco; las tarjetas y la cámara, con el estándar; la tipografía grande y los logos, con el pesado.

Al terminar, renderiza 3 segundos y dime qué cambió en la sensación del movimiento.
```

### El sonido

El sonido es lo que más cambia cómo se siente un video. Brag lo trae resuelto: música y efectos de sonido por defecto, una cama de música con buen gusto y unos pocos efectos bien puestos, escritos como una sola pieza, con los efectos suaves por debajo de la música y nada agudo ni filoso.

Con música presente, el modo completo agrega un tratamiento sutil que reacciona al audio: un brillo que respira con los graves, una tarjeta que gana presencia. Nada de ecualizadores ni de barras de onda. Y una advertencia honesta: la sincronía exacta con los beats solo se promete cuando hay un detector de ritmo de verdad.

### Pon mi canción y alinea el video a su ritmo

Con una pista tuya. Claude mide el ritmo con un detector real, reacomoda los cortes y mezcla los efectos por debajo.

```
Mi canción está en ./audio/track.mp3. Úsala sin modificarla.

1. Detecta su ritmo con un detector real (no a ojo) y dime el BPM que mediste y el segundo del primer tiempo fuerte.
2. Reacomoda la lista de tomas para que cada cambio de estado caiga en un beat y los momentos grandes en un tiempo fuerte. Empieza el video en un tiempo fuerte.
3. Pon los efectos de sonido (clics, pops, whooshes) sobre los golpes medidos, suaves y por debajo de la música.
4. Mezcla todo, normaliza a -14 LUFS y entrégame el video final. Si la herramienta no puede medir el ritmo de verdad, dímelo en vez de inventar una sincronía.
```

10 · La pieza larga

## Para algo de más de 30 segundos, contrata un equipo

Brag es para piezas de 15 a 25 segundos. Cuando el video es largo (una película de marca, un video musical, un explicador de varios minutos), ya no alcanza una frase: necesitas un brief que se parezca al de un director: en vez de describir un video, le asigna un papel a cada parte del equipo.

- La película en una línea. El logline y el chiste, para poder revisar cada decisión contra eso.
- Referencias. El video fuente, la canción, la biblioteca de imágenes o un repo de trabajo previo. Qué se conserva y qué se empuja más lejos.
- Herramientas y llaves. Qué skills cargar (/hyperframes, /remotion-best-practices), qué servicios hay y el presupuesto. Gasta con cuidado.
- Biblia del personaje, si hay uno. Proporciones, paleta, expresiones y un bloqueo de identidad que sobreviva a cualquier cambio de estilo.
- Hoja de beats. Actos con tiempos, una recompensa visual cada 3 a 5 segundos y un gancho en los primeros 2.
- Texto en pantalla. Cuándo la letra o los subtítulos se hacen enormes y cuándo se quedan como subtítulo. La composición deja lugar para ellos.
- Puertas del proceso. Plan, imágenes fijas, animática, pasada completa, pulido, audio, render. No te saltes ninguna.
- Bucle de crítica. Renderiza fotos fijas, califícalas, anota los 3 peores problemas, arregla y repite hasta que todas las notas sean 8 o más.
- Entregables. El MP4 final, la prueba del loop, el póster, la hoja de contacto y el código limpio con un README.

Cuando la pieza es larga, que Claude reparta el trabajo en subagentes por capítulo. Pídele dos archivos por nombre: ANIMATION\_GUIDE.md, que escribe primero para que todos los subagentes trabajen con el mismo estilo, y STORYBOARD.md, que deja después de la primera pasada.

### Plantilla de brief de director

Para películas de más de 30 segundos o varias sesiones. Rellena lo que va entre corchetes y borra lo que no uses.

```
Eres el director, animador, diseñador de sonido e ingeniero de render de una película de [DURACIÓN] hecha en código con [/hyperframes o /remotion-create]. Trátalo como una producción de varias sesiones. No corras al render final.

## La película en una línea
[LOGLINE. Qué debe sentir quien la ve al terminar.]

## Referencias y recursos
- ./refs/ : [video / frames / biblioteca de imágenes]. Toma la gramática, nunca el contenido.
- ./audio/track.mp3 : úsala sin modificarla. Mide primero su ritmo con un detector real.
- Llaves de servicios en .env: [NOMBRE DE LAS VARIABLES]. Presupuesto: [$X]. Sé económico.

## Look
[3 a 5 líneas: paleta, tipografía, textura, lenguaje de cámara. Looks prohibidos.]

## Hoja de beats
0:00-0:02  gancho: [la imagen más llamativa]
0:02-0:10  [acto 1]
...        una recompensa visual nueva cada 3 a 5 segundos
[FINAL]    el último frame prepara el primero (loop)

## Proceso, con puertas
1. Escribe docs/style_guide.md y docs/shotlist.md (cada toma: frames, cámara, texto, efectos). Enséñame la lista. Si no contesto en 10 minutos, sigue.
2. Construye imágenes fijas de cada toma. Hoja de contacto. Crítica.
3. Animática a 960x540 con audio provisional. Arregla el ritmo antes de pulir.
4. Animación completa, pasada de pulido, pasada de sonido y render final.
5. Reparte el trabajo en subagentes por capítulo. Escribe antes docs/ANIMATION_GUIDE.md para que todos trabajen con el mismo estilo, y deja docs/STORYBOARD.md.

## Bucle de crítica (cada toma, mínimo 3 rondas)
Renderiza de 3 a 5 fotos fijas y califícalas del 1 al 10 en: gancho, lectura a 360 px de ancho, movimiento, composición, profundidad, sincronía con el sonido, acabado. Anota las notas y los 3 problemas más grandes en docs/review_log.md. Arregla. Repite hasta que todo sea 8 o más.

## Entregables
out/final.mp4 · out/loop_check.mp4 · out/poster.png · out/contact.png · README.md
```

11 · Crítica

## Haz que Opus mire sus propios frames

Opus 5.5 lee imágenes. Eso significa que puede mirar lo que renderizó, y ese hábito separa a los clips que funcionan de los que se publican con un disclaimer de que quedaron medio flojos. Iterar es parte del método.

Cada herramienta ya trae su compuerta. Hyperframes tiene npx hyperframes check, que revisa errores, contraste del texto y desbordes, y npx hyperframes snapshot, que saca frames clave en PNG. Brag la usa como su única revisión antes de renderizar. Remotion tiene npx remotion still, que renderiza un solo frame para mirarlo.

Sobre eso, pídele a Claude cuatro imágenes con ffmpeg: una hoja de contacto con 2 frames por segundo, una prueba de teléfono a 360 px de ancho, una tira de 12 frames seguidos alrededor de una acción rápida y el video repetido dos veces para ver la costura del loop. Renderizar el mismo tramo dos veces tiene que dar el mismo archivo: esa es la prueba de que el render es determinista.

### Sé un director duro, no un autor orgulloso

Pégalo después de cada render. Claude genera las imágenes, las mira, se califica y arregla.

```
Con ffmpeg, genera a partir de out/final.mp4 estas cuatro imágenes y mira las tres primeras bien: una hoja de contacto (2 frames por segundo, 6 de ancho), una prueba de teléfono (1 frame por segundo a 360 px de ancho), una tira de 12 frames seguidos alrededor de [SEGUNDO DE LA ACCIÓN MÁS RÁPIDA], y el video repetido dos veces para revisar la costura del loop. Sé un director de motion exigente, no un autor orgulloso.

Califica del 1 al 10: gancho en los primeros 2 s · lectura a tamaño de teléfono · calidad del movimiento (resortes, sin frames muertos) · variedad (algo nuevo cada 2 a 4 s) · composición · fidelidad a la marca · sincronía con el sonido.

Dame los 3 problemas más grandes con su segundo exacto. Busca en especial: texto encimado durante los cambios, cosas que se deslizan en vez de suavizarse, etiquetas en las esquinas y marcos, tomas con texto centrado sobre degradado, texto escalado y borroso, un beat muerto en el que no pasa nada y un salto en la costura del loop.

Arréglalos, vuelve a renderizar solo los segundos afectados, enséñame la nueva hoja de contacto y las nuevas notas.
```

Lo que más conviene cazar

- Texto que se encima mientras una caja cambia de contenido.
- Cosas que se deslizan a velocidad constante en lugar de acelerar y asentarse.
- Etiquetas en las esquinas y marcos alrededor del frame, la firma de un video genérico.
- Tomas de texto centrado sobre un degradado.
- Texto borroso porque la cámara lo escala con will-change.
- Un beat sin nada pasando, o un salto en la costura donde el loop se repite.

12 · Entrégalo

## Todos los formatos, una skill y, si quieres, un servicio

Tres movimientos finales convierten un buen clip en algo repetible. Exporta todos los formatos desde una sola línea de tiempo. Empaqueta tu proceso como skill para que el próximo video sea una frase. Y, si quieres, véndelo.

### Todos los formatos desde una línea de tiempo

Brag entrega en horizontal, vertical o cuadrado con una opción. Para cualquier video propio, escribe las escenas contra una función de layout, no contra píxeles fijos, y pide los tres formatos. Reencuadra el texto y la interfaz para cada uno: no recortes un video horizontal para volverlo vertical.

### Un video, tres formatos

Para un video que ya está terminado en un formato y lo quieres en los otros dos.

```
Convierte las escenas de esta composición para que se escriban contra una función de layout (ancho y alto como parámetros) en vez de píxeles fijos. Después renderiza el video en 9:16, 1:1 y 16:9 desde la misma línea de tiempo.

Reencuadra el texto y la interfaz para cada formato; no recortes el horizontal para sacar el vertical. Al terminar, genera una hoja de contacto de cada formato y dime cuál quedó más débil.
```

### Empaquétalo como skill

Cuando tu proceso ya funciona, pásalo a una skill. Es la guía de esta página convertida en una carpeta: qué datos pedir, qué herramienta elegir según el video, qué hacer en qué orden y qué reglas no se rompen. Desde ahí, todo el curso se reduce a una línea: usa motion-reel para esta URL, 20 s, vertical.

Descarga el archivo y guárdalo en la carpeta de skills de Claude Code, dentro de una carpeta llamada motion-reel. Puedes compartirla con tu equipo o publicarla como plugin.

Skill motion-reel

Todo el proceso en una sola skill: elige la herramienta correcta, junta los datos, hace el plan, renderiza, critica y entrega. Va en la carpeta de skills de Claude Code y se invoca con una frase.

[Descargar SKILL.md](https://www.tododeia.com/docs/motion-graphics-opus-55/motion-reel/SKILL.md)

### Instala la skill motion-reel

Después de bajar SKILL.md, Claude la pone donde corresponde y la prueba.

```
Tengo un archivo SKILL.md de una skill llamada motion-reel. Instálala para que Claude Code la encuentre: crea la carpeta correcta dentro de mi carpeta de skills y copia ahí el archivo. Dime la ruta exacta donde quedó.

Después pruébala con esta frase: usa motion-reel para [URL], 20 segundos, vertical. Pídeme los datos que falten, todos juntos, y no sigas hasta que te los dé.
```

### Si quieres, véndelo

Un video de lanzamiento es un servicio que se puede cobrar, y con este estudio lo entregas en una tarde. Arma un paquete fácil de explicar: música, las funciones del producto, una oferta al final, y los tres formatos.

Dos cosas para no meterte en problemas. Pon un tope de rondas de cambios, o el tiempo de entrega se come lo que cobras. Y si el trabajo lo haces con Remotion desde una empresa de 4 personas o más, revisa su licencia antes de cobrar.

Qué incluye

Un paquete fácil de explicar

Música, las funciones del producto, una oferta al final y los tres formatos.

Cuántas ediciones

Pon un tope

Hasta tres rondas de cambios. Sin tope, el tiempo de entrega se come lo que cobras.

Qué entregas

Todo listo para publicar

El video en 9:16, 1:1 y 16:9, la portada y el texto para compartirlo, que Brag ya deja escrito.

Guía de la bóveda

Las tres herramientas

- [latent-spaces/brag](https://github.com/latent-spaces/brag)
	La skill que convierte tu proyecto o sitio en un video de lanzamiento, con música y texto para compartir.
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)
	El motor en HTML. Brag lo usa por debajo en su modo completo, y tú lo usas directo cuando quieres control total.
- [remotion-dev/remotion](https://github.com/remotion-dev/remotion)
	Videos con React: la opción para series, plantillas y videos con datos.
- [Skills de Remotion](https://www.remotion.dev/docs/ai/skills)
	Las skills que le enseñan a Claude a crear y renderizar con Remotion.

Guías vecinas

- [Hyperframes, videos con Claude Design](https://www.tododeia.com/community/hyperframes-claude-design)
	El mismo render en HTML, pero desde Claude Design y sin terminal.
- [Animaciones](https://www.tododeia.com/community/animaciones)
	Animaciones listas para meter en tus proyectos.
- [Claude Animador Web](https://www.tododeia.com/community/claude-animador-web)
	Movimiento para interfaces web, no para películas.

Con qué te quedas

Para un lanzamiento, Brag. Para algo a tu medida, Hyperframes. Para una serie, Remotion. Con cualquiera de las tres, dale una referencia, pídele el plan antes del render y haz que Opus mire sus propios frames hasta que todas las notas sean 8.

[

Lo nuevo sale primero en Instagram

Ahí publico lo que voy probando antes de que se vuelva guía.

@soyenriquerocha

](https://www.instagram.com/soyenriquerocha/)