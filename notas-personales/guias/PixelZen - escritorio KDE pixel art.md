---
title: "PixelZen — escritorio KDE de Japón antiguo en pixel art"
type: resource
tags:
  - linux
  - documentacion
  - configuracion
  - claude-code
  - open-source
status: active
project: none
date_created: 2026-11-17
date_modified: 2026-11-17
source: https://ralcaniz.dev/posts/pixelzen-escritorio-kde-pixel-art/
---
# PixelZen — escritorio KDE de Japón antiguo en pixel art

> Artículo de Rubén Alcañiz (1/11/2026, blog *De Reparto a Root*) sobre **PixelZen**, un tema completo para KDE Plasma 6: paisaje japonés en pixel art que cambia con la hora de tu ciudad, iconos y cursor a juego, y un panel de datos que se adapta al tamaño de la pantalla. Lo construyó paso a paso con Claude Code. Paquete de 1 MB, sin dependencias externas. Nota del vault: 17/11/2026.

Fuente: [Me hice un escritorio KDE de Japón antiguo en pixel art (y su fondo sigue al sol)](https://ralcaniz.dev/posts/pixelzen-escritorio-kde-pixel-art/).

## Qué es

Un tema de escritorio para KDE Plasma 6 (el autor lo usa en un T14s con CachyOS) con estas piezas:

- Un fondo animado con pagoda, torii, lago, montaña nevada y cerezo en flor, en pixel art.
- Un panel de datos (HUD) en la columna libre de la derecha, que se escala con la altura de la pantalla: ocupa lo mismo en un portátil de 1200 px que en un monitor de 1440.
- Iconos, cursor, ventanas y terminal a juego.
- Una barra superior mínima, porque los datos ya viven en el HUD.

Todo se genera con Python puro: ni Inkscape, ni ImageMagick, ni librerías; los píxeles salen de bucles y matrices.

El autor avisa que no salió de una sola petición del tipo «hazme un tema bonito»: lo fue construyendo pieza a pieza con Claude Code, revisando el resultado en pantalla y corrigiendo en cada ronda.

## El fondo sigue al sol

El fondo no es una imagen fija: es una escena que cambia con la hora real de tu ciudad.

- El sol sale por el este, cruza el cielo y se pone por el oeste según la fecha y tu latitud. El cálculo (fórmulas astronómicas estándar) lo hace el propio widget; no gasta nada mientras lo usas.
- El paisaje tiene tres iluminaciones (noche, hora dorada y día) que se mezclan según la altura del sol.
- De noche aparecen la luna, las estrellas, las luces de la pagoda y las luciérnagas; de día desaparecen.
- El camino de luz sobre el lago sigue al sol o a la luna.
- La animación va a 8 fotogramas por segundo: nubes, farolillos, pétalos, grullas y alguna estrella fugaz.

No manda datos a ningún sitio. La ubicación sale de la zona horaria (o de una ciudad que fijes tú) y el sol se calcula en local. El autor pensó en añadir el tiempo real (nubes, lluvia), pero eso implicaría enviar coordenadas a un tercero y no le compensaba.

Es interactivo:

```bash
hora.sh 21:30   # congela esa hora
hora.sh demo    # 24 horas en 90 segundos, para ver cómo anochece
hora.sh real    # vuelve a la hora del reloj
```

El mismo fondo animado se ve en la pantalla de bloqueo.

### Cómo calcula la posición del sol

No usa una tabla de amaneceres por ciudad. Parte de la fecha y el lugar:

1. Cuenta los días desde el año 2000 en UTC.
2. Calcula la declinación (órbita e inclinación del eje).
3. Mide cuánto ha girado la Tierra (tiempo sidéreo).
4. Convierte ese giro en ángulo horario con tu latitud y longitud.
5. Obtiene la altura del sol en grados sobre (o bajo) el horizonte.

Esa altura lo controla todo: por debajo de unos −14° es noche cerrada; entre −14° y 0° el cielo se tiñe de dorado; a partir de unos 16° es pleno día. Las estrellas aparecen cuando el sol baja de unos −6°. Las transiciones se suavizan con una curva (*smoothstep*).

La zona horaria del equipo (buscando su punto en `zone1970.tab`, sin red) o una ciudad fija basta para saber dónde estás. Si cambias de zona, el paisaje se ajusta. **Limitación que el autor reconoce:** la luna no se calcula así; es un arco decorativo de este a oeste repartido según lo que dura la noche. No es su posición real ni sus fases.

## Cómo está hecho

**Paisaje en capas.** Cielo y escena van separados para que el sol pase por detrás de las montañas. El generador dibuja cada fase dos veces (fondo negro y fondo blanco) y saca la transparencia por la diferencia (*difference matting*). Cielo, escena y nubes son PNG de 640×400 que el widget amplía ×3 sin suavizar. Los degradados usan una matriz de Bayer 4×4 (tramado ordenado). Las montañas salen de ruido fractal.

**HUD.** Un plasmoide en QML con un motor de datos en Python que solo lee (`/proc`, `sysfs`, `ss`, `ip`, `git`). Sin red y sin `sudo`. Incluye:

- Tiempo: reloj, calendario japonés (令和八年) y fase lunar en píxeles.
- Sistema: CPU, RAM, temperatura y batería con barras segmentadas.
- Red: Wi-Fi, IP, VPN, velocidad y puertos en escucha (los expuestos a toda la red, en ámbar).
- Dev: estado de repos, versiones de Python/Node/Go/Rust, servicios fallidos y errores de la última hora.
- Herramientas: botones que abren una terminal con `btop`, `ss`, `dig`, `ping`… y detectan lo instalado. El de `nmap` propone instalarlo, sin ejecutarlo.
- Haiku: un verso de Bashō, Buson o Chiyo-ni que rota con fundido.

**Iconos y cursor.** El tema traduce unos 3000 nombres de icono de KDE a glifos de Pixelarticons (MIT) y dibuja azulejos de apps, carpetas y tipos de archivo. Lo que no cubre cae a Breeze. El cursor está escrito a mano en formato Xcursor: flecha con punta roja de torii, mano, lupa, «prohibido» y una espera animada.

**Tipografía.** La primera fuente pixel era muy decorativa y costaba leerla. Tras probar ocho, eligió Departure Mono, que distingue `0`/`O`, `I`/`l`/`1` y no confunde la `~` con una N.

## Cómo lo hizo

Lo construyó conversando con Claude Code en muchas rondas cortas: él ponía la idea, el criterio y el ojo; Claude Code escribía el código y lo probaba con él delante. El orden, a grandes rasgos: paisaje estático; HUD tarjeta a tarjeta; tipografía, iconos y cursor; fondo animado y ciclo día/noche; pantalla de bloqueo, barra mínima y modo demo; paquete instalable, probado en un usuario vacío.

Iteró con capturas reales del escritorio. Ejemplos de fallos que cuenta: un reloj que pisaba la fecha; una fuente ilegible; nombres de iconos ilegibles sobre el cerezo claro (Plasma los pinta en blanco fijo, así que oscureció esa esquina del fondo con un velo); un panel diminuto en el monitor 2560×1440 porque lo había diseñado en el portátil (ahora se escala con la altura). Para las capturas usó un escritorio virtual vacío y un modo demo que sustituye red, IP y VPN por datos ficticios.

Su conclusión: una IA acelera el trabajo, pero el gusto, las decisiones y la comprobación siguen siendo tuyos.

## Lo que no hace

- La luna sale siempre llena, con un arco decorativo; no usa la fase real (el HUD sí muestra una fase lunar en píxeles, según el artículo; el ciclo del fondo no).
- Solo lo ha probado en Plasma 6.8 con Wayland, en dos pantallas: 1920×1200 al 125 % y 2560×1440 al 100 %. El fondo se recorta para llenar cualquier proporción y el HUD se escala con la altura, pero en pantallas muy pequeñas o ultraanchas no lo ha probado.
- Las aplicaciones externas de la bandeja del sistema no las controla el tema.
- Es un proyecto personal: úsalo, rómpelo y mejóralo.

## Instalarlo y desinstalarlo

Hace falta KDE Plasma 6 (el fondo animado y el panel son componentes de Plasma) y tener `python3`, `qdbus6` y `kwriteconfig6`. Si falta algo, el instalador lo dice.

Se puede instalar con doble clic en «Instalar PixelZen» o desde la terminal:

```bash
tar xzf pixelzen-1.0.tar.gz && cd pixelzen-1.0
./instalar.sh                                  # usa tu zona horaria para calcular el sol
./instalar.sh --casa=39.5,-0.4,"Mi ciudad"     # o fija tu ubicación
```

Solo toca tu usuario (nada de `sudo`) y, antes de cambiar nada, guarda una copia de tus ajustes. Si no detecta Plasma 6, lo dice y no toca nada. Para volver atrás: `~/.local/share/pixelzen/revertir.sh`. Para quitarlo:

```bash
~/.local/share/pixelzen/desinstalar.sh          # vuelve a tus ajustes y borra los temas instalados
~/.local/share/pixelzen/desinstalar.sh --todo   # además borra la carpeta de PixelZen y su configuración
```

`revertir.sh` vuelve a los ajustes anteriores sin borrar nada. Con `./instalar.sh --portable` se instalan solo iconos, cursor y fuentes, para elegirlos en otro escritorio; el autor lo marca como experimental y no lo ha probado fuera de Plasma. El tema completo no funciona sin Plasma.

## Descarga y licencia

- Paquete: `pixelzen-1.0.tar.gz` (1 MB), al final del artículo.
- Código, README e issues: [github.com/mosqui1988/pixelzen](https://github.com/mosqui1988/pixelzen)
- SHA-256 del paquete, según el artículo: `d11705d136cf5e91ca4bc23061971ad66b7fe0ab895d3a112123022c729d89ba`
- Código y arte: GPL-3.0-or-later. Fuentes (Departure Mono, Pixelify Sans, DotGothic16, VT323): SIL OFL 1.1. Glifos de iconos: Pixelarticons, MIT. Los textos de las licencias van dentro del paquete.

## Relacionado

- [[02 - PCs]] — inventario de PCs; el PC1 tiene destino Omarchy/Linux
- [[notas-personales/configuraciones/INDEX|Configuraciones — índice]] — configuraciones de escritorio en macOS (Yabai, Ghostty, SKHD)
- [[Cómo construir una landing premium con Claude Code]] — otro trabajo hecho iterando con Claude Code
