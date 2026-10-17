---
title: "Tu propio Tamagotchi de Meta: repo, placas y guía de instalación"
source: "https://comunidad.eriktaveras.com/resources/tamagotchi-meta-muse-gadgets/"
author:
  - "[[Erik Taveras]]"
published: 2026-10-03
created: 2026-10-17
description: "Comunidad de desarrollo, automatización y AI. Aprende Python, JavaScript, automatización y más con Erik Taveras. Cursos, foro y recursos gratuitos."
tags:
  - "clippings"
---
## Tu propio “Tamagotchi de Meta”: el código abierto de Muse Gadgets, la placa y cómo instalarlo

Meta liberó el SDK para que construyas tu propio gadget de Muse: una placa ESP32 con pantalla o una Raspberry Pi que se conecta a tu agente Muse y le da manos y pies dentro de tu red local. Desde ahí puede hablar con tu impresora, tu televisión, tus bombillas o cualquier cosa con una API HTTP local.

Aquí tienes todo lo que prometí en el reel: el repositorio, la web oficial con la lista de placas, la placa que usé y los pasos para dejarlo funcionando. También los riesgos, que los tiene.

---

## Si solo vas a leer una cosa, que sea esta

| Qué | Enlace | Para qué |
| --- | --- | --- |
| **Repositorio oficial** | [facebookincubator/muse-gadget-sdk](https://github.com/facebookincubator/muse-gadget-sdk) | El código completo: SDK de ESP32 y SDK de Linux (Raspberry Pi). Licencia Apache 2.0. |
| **Web oficial** | [gadgets.muse.ai](https://gadgets.muse.ai/) | La lista de placas, el token del SDK y los términos de uso. |
| **La placa del video** | [ESP32-S3 con pantalla táctil (Amazon)](https://amzn.to/3VhfULU) | Ronda los US$19. Es link de afiliado: si compras por ahí me ayudas sin pagar más. |
| **Discord de la comunidad** | [Muse Gadgets Discord](https://discord.gg/3bhjCkZdd6) | Gente adaptando placas nuevas y compartiendo lo que construye. |

---

## Parte 1 — Qué es esto exactamente

Un “gadget” de Muse es un dispositivo que tú mismo armas y emparejas con la app de Muse. Hay dos caminos:

- **ESP32:** flasheas el firmware abierto en una placa. En las placas con pantalla aparece el avatar animado (el “tamagotchi”), tiene push-to-talk y puede mostrar imágenes que Muse le manda.
- **Linux / Raspberry Pi:** instalas un servicio y Muse puede correr comandos, leer y escribir archivos y revisar la salud de la máquina.

En las placas ESP32 con PSRAM viene además el **túnel a tu red de casa**: Muse puede alcanzar los dispositivos que ya tienes y cualquier cosa con una API HTTP local. Ahí está la gracia, y también el riesgo.

---

## Parte 2 — Las placas que ya funcionan

Lista oficial del repositorio. Las que dicen “UI” corren el avatar completo.

| Placa | Qué obtienes |
| --- | --- |
| ESP32-C5 DevKitC-1 | Luz de estado y botón (la más rápida para empezar) |
| ideaspark ESP32 con pantalla de 1.9" | Estado en pantalla, imágenes |
| Seeed SenseCAP Indicator | Estado en pantalla de 4", imágenes |
| Seeed reTerminal E1001 | Estado en e-paper de 7.5" |
| Home Assistant Voice Preview Edition | Anillo LED, push-to-talk, perilla de volumen |
| Waveshare ESP32-S3-Touch-AMOLED-1.75 / 1.75C | **UI**, push-to-talk, ajustes, imágenes |
| Espressif ESP32-S3-BOX-3 | **UI**, táctil, push-to-talk, imágenes |
| AIPI Lite | **UI**, push-to-talk, menú de dos botones |
| Waveshare ESP32-C6-Touch-AMOLED-1.8 | **UI**, push-to-talk con respuestas en texto |
| Seeed SenseCAP Watcher | **UI**, push-to-talk, imágenes, cámara opcional |
| M5Stack StickS3, StopWatch, CoreS3, StickC Plus2 | **UI**, push-to-talk, imágenes |
| M5Stack Cardputer ADV | **UI** experimental, con teclado |

> Ojo: la placa del link de Amazon no viene en esta tabla. Es una ESP32-S3 con pantalla táctil que se adapta siguiendo la guía “Add a board” del repositorio (Parte 5). Si quieres algo que funcione sin tocar nada, elige una de la lista.

---

## Parte 3 — Antes de empezar

- Una placa ESP32 (o una Raspberry Pi 3B+, 4, 5 o Zero 2 W con Bluetooth).
- Un cable USB **de datos**, no solo de carga. Es el error número uno.
- Una computadora con macOS o Linux.
- Un **token del SDK**: entra en [gadgets.muse.ai/settings/sdk-tokens](https://gadgets.muse.ai/settings/sdk-tokens) y lee los [términos del SDK](https://gadgets.muse.ai/sdk-terms). Todo gadget lo necesita para emparejarse.
- La app de Muse en el teléfono.

---

## Parte 4 — ESP32: el camino rápido con Muse Code

El repositorio trae un `AGENTS.md` pensado para que un agente de código haga el trabajo pesado: instalar el toolchain, compilar, flashear y leer los logs.

```bash
curl -fsSL https://dev.meta.ai/install.sh | sh
git clone https://github.com/facebookincubator/muse-gadget-sdk
cd muse-gadget-sdk/esp32
muse --disable-sandbox
```

Con la placa conectada, pídele cosas como:

- “Build this firmware for my ESP32-C5 DevKitC-1 and flash it.”
- “Watch the serial log and tell me when it's ready to pair.”
- “Add support for my board. It's an ESP32-S3 with 16 MB flash, a button on GPIO 0 and no PSRAM.”

Cualquier agente que lea `AGENTS.md` sirve (Claude Code incluido). Solo necesita acceso al puerto USB para flashear.

---

## Parte 5 — ESP32: hacerlo a mano

### 1\. Instala ESP-IDF v6.0.1

Tiene que ser esa versión exacta; otras no están soportadas.

```bash
git clone -b v6.0.1 --recursive https://github.com/espressif/esp-idf.git ~/esp/esp-idf-v6
~/esp/esp-idf-v6/install.sh esp32c5,esp32s3,esp32c6,esp32
. ~/esp/esp-idf-v6/export.sh   # en cada terminal nueva
```

### 2\. Compila con tu token

```bash
cd muse-gadget-sdk/esp32
idf.py menuconfig   # ESP32 Device SDK > Muse Gadgets SDK token
idf.py build
```

Para las placas de la lista hay un script que ya trae la configuración de cada una:

```bash
tools/board.sh ideaspark build
tools/board.sh sensecap-indicator flash-monitor /dev/ttyACM0
```

### 3\. Flashea

```bash
idf.py -p /dev/ttyACM0 flash monitor   # en Mac: ls /dev/cu.usb*
```

Si no conecta: mantén **BOOT**, toca **RESET**, suelta **BOOT** y vuelve a intentar.

### Si tu placa no está en la lista

1. Copia el archivo más parecido de `devices/` como `sdkconfig.tuplaca`.
2. Ajusta el chip, el GPIO del botón, la luz de estado y el tamaño de la flash.
3. Sin PSRAM, apaga `CONFIG_SPIRAM` y `CONFIG_HOMEHUB_TUNNEL` (te quedas sin el túnel a la red local).
4. Una pantalla nueva necesita código además del archivo: ahí es donde el agente con `AGENTS.md` te ahorra horas.

---

## Parte 6 — Emparejarlo con Muse

1. En la app: **Settings > Devices > Developer mode**.
2. **Settings > Devices > Add Device** (el **+** arriba a la derecha). Aparece como `MuseGadget-XXXXXX`.
3. Cuando la luz respire en **azul**, aprieta el botón BOOT para confirmar que eres tú.
4. **Verde** = conectado. Para reiniciarlo todo, mantén el botón 5 segundos.

| Luz | Significa |
| --- | --- |
| Naranja respirando | Listo para configurar |
| Azul respirando | Aprieta el botón para confirmar |
| Verde | Conectado |
| Amarillo parpadeando | Reconectando |
| Morado | Sin emparejar |
| Rojo parpadeando | Algo falló: revisa el log |

---

## Parte 7 — Raspberry Pi: el otro camino

```bash
curl -fsSL https://raw.githubusercontent.com/facebookincubator/muse-gadget-sdk/main/linux/install.sh -o install.sh
less install.sh   # léelo antes de correrlo
bash install.sh --sdk-token mgst_TU_TOKEN
```

Luego empareja desde la app igual que arriba (aparece como `MuseGadgetXXXXXX`). Muse podrá correr comandos, leer y escribir archivos y reportar uptime, disco y temperatura. Le puedes pedir “qué se está comiendo el disco de mi Pi” o “instálame Home Assistant”.

```bash
sudo systemctl status musegadget      # está corriendo
sudo journalctl -u musegadget -f      # log en vivo
bash install.sh --run-as otro_usuario # dale una cuenta SIN sudo
```

> Muse recibe exactamente los permisos de la cuenta con la que lo instalas. Si esa cuenta puede usar sudo, Muse también. Crea una cuenta aparte sin sudo.

---

## Los errores que te vas a encontrar

- **Cable de solo carga.** La placa enciende pero la computadora no la ve.
- **Versión de ESP-IDF distinta a la 6.0.1.** Falla la compilación con errores raros.
- **No activar Developer mode** en la app: el gadget nunca aparece en la lista.
- **Comprar una placa sin PSRAM** esperando el control de la red local: sin PSRAM no hay túnel.
- **Instalar en la Pi con tu usuario principal.** Le estás dando a un agente acceso a todo.
- **Emparejar en una red pública.** El emparejamiento no tiene verificación del fabricante; hazlo en tu red de casa.

---

## Plan de una semana

1. **Día 1:** saca el token del SDK, lee los términos y elige placa.
2. **Día 2-3:** llega la placa. Instala ESP-IDF 6.0.1 o Muse Code.
3. **Día 4:** compila, flashea y empareja. Meta: luz verde.
4. **Día 5:** pídele a Muse algo de tu red local (una bombilla, la impresora).
5. **Día 6-7:** adapta algo: el brillo, una pantalla, un comando nuevo.

---

## Recursos

- [Repositorio muse-gadget-sdk](https://github.com/facebookincubator/muse-gadget-sdk) (README y AGENTS.md en cada carpeta)
- [gadgets.muse.ai](https://gadgets.muse.ai/): placas, tokens y términos
- [La placa ESP32-S3 del video](https://amzn.to/3VhfULU) (afiliado)
- [Muse Code](https://developer.meta.com/ai/lp/muse-code/), el agente de código de Meta
- [Requisitos de ESP-IDF 6.0.1](https://docs.espressif.com/projects/esp-idf/en/v6.0.1/esp32c5/get-started/linux-macos-setup.html)
- [Discord de Muse Gadgets](https://discord.gg/3bhjCkZdd6)

---

## Última cosa

Esto es divertido de verdad: por menos de 20 dólares tienes un agente con cara, voz y acceso a tu casa. Pero lo dice el propio repositorio: está hecho por hackers, para hackers, y puede brickear placas. Empieza con algo que no te duela perder y dale los permisos mínimos.

**Un agente con manos en tu red es tan seguro como los permisos que tú le des.**

*Erik Taveras — Taveras Solutions, LLC*

Si armas el tuyo, etiquétame en Instagram y cuéntame qué placa usaste.

## Reseñas

5,0 de 5 · 1 reseña

Entra para dejar tu reseña.

[Entrar](https://comunidad.eriktaveras.com/accounts/login/?next=/resources/tamagotchi-meta-muse-gadgets/)

- Enrique gutierrez
	Me encanta y no es tan costoso para las posibilidades que tiene.