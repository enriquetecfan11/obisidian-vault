---
title: "Tu propio Tamagotchi de Meta — Muse Gadgets (repo, placas y montaje)"
type: resource
tags:
  - ia
  - hardware
  - raspberry-pi
  - infraestructura
status: active
project: none
date_created: 2026-10-17
date_modified: 2026-10-17
source: https://comunidad.eriktaveras.com/resources/tamagotchi-meta-muse-gadgets/
---
# Tu propio Tamagotchi de Meta — Muse Gadgets (repo, placas y montaje)

> Recurso de Erik Taveras (3-oct-2026) sobre el SDK abierto de **Muse Gadgets** de Meta: una placa ESP32 con pantalla o una Raspberry Pi que se empareja con tu agente Muse y le da «manos y pies» en tu red local (impresora, tele, bombillas, cualquier API HTTP local). Incluye repo, lista de placas, pasos de instalación y los riesgos.

## Enlaces clave (según el autor)

| Qué | Enlace |
| --- | --- |
| Repo oficial | `github.com/facebookincubator/muse-gadget-sdk` (Apache 2.0) |
| Web oficial (placas, token, términos) | `gadgets.muse.ai` |
| Discord | Muse Gadgets Discord |

## Qué es

Un «gadget» de Muse es un dispositivo que tú armas y emparejas con la app de Muse. Dos caminos:

- **ESP32:** flasheas el firmware abierto; en placas con pantalla aparece el avatar («tamagotchi»), con push-to-talk e imágenes que Muse le manda.
- **Linux / Raspberry Pi:** instalas un servicio y Muse puede correr comandos, leer/escribir archivos y revisar la salud de la máquina.

En placas ESP32 con **PSRAM** viene además el **túnel a tu red de casa** (Muse alcanza tus dispositivos y APIs HTTP locales). Ahí está la gracia y también el riesgo.

## Placas soportadas (lista del repo)

Las que dicen **UI** corren el avatar completo: Waveshare ESP32-S3-Touch-AMOLED-1.75/1.75C, Espressif ESP32-S3-BOX-3, AIPI Lite, Waveshare ESP32-C6-Touch-AMOLED-1.8, Seeed SenseCAP Watcher, M5Stack StickS3/StopWatch/CoreS3/StickC Plus2, M5Stack Cardputer ADV (experimental). Sin avatar: ESP32-C5 DevKitC-1, ideaspark 1.9", Seeed SenseCAP Indicator, Seeed reTerminal E1001, Home Assistant Voice Preview. Ojo: la placa del vídeo (ESP32-S3 táctil de ~19 $) **no** está en la lista; hay que adaptarla con la guía «Add a board».

## Requisitos previos

Placa ESP32 o Raspberry Pi 3B+/4/5/Zero 2 W; cable USB **de datos** (no solo de carga); macOS o Linux; un **token del SDK** (`gadgets.muse.ai/settings/sdk-tokens`); la app de Muse en el móvil.

## ESP32 — camino rápido (Muse Code)

El repo trae un `AGENTS.md` para que un agente de código (Claude Code incluido) haga el trabajo pesado:

```bash
curl -fsSL https://dev.meta.ai/install.sh | sh
git clone https://github.com/facebookincubator/muse-gadget-sdk
cd muse-gadget-sdk/esp32
muse --disable-sandbox
```

Con la placa conectada, se le pide «compila este firmware y flashealo», «vigila el log hasta que esté listo para emparejar», etc. Solo necesita acceso al puerto USB.

## ESP32 — a mano

1. Instalar **ESP-IDF v6.0.1** (versión exacta).
2. Compilar con el token (`idf.py menuconfig` → Muse Gadgets SDK token) y `idf.py build`; para placas de la lista hay `tools/board.sh <placa> build`.
3. Flashear (`idf.py -p /dev/ttyACM0 flash monitor`; en Mac, `ls /dev/cu.usb*`). Si no conecta: BOOT → RESET → soltar BOOT.

**Placa no listada:** copiar el `sdkconfig` más parecido, ajustar chip/GPIO/estado/flash; sin PSRAM se apagan `CONFIG_SPIRAM` y `CONFIG_HOMEHUB_TUNNEL`; una pantalla nueva requiere código.

## Emparejar con Muse

App → Settings → Devices → Developer mode; luego Add Device (aparece como `MuseGadget-XXXXXX`); luz **azul** respirando → pulsar BOOT; **verde** = conectado (5 s el botón reinicia). Luces: naranja (listo para configurar), azul (confirmar), verde (conectado), amarillo (reconectando), morado (sin emparejar), rojo (falló).

## Raspberry Pi

```bash
curl -fsSL https://raw.githubusercontent.com/facebookincubator/muse-gadget-sdk/main/linux/install.sh -o install.sh
less install.sh
bash install.sh --sdk-token mgst_TU_TOKEN
```

Muse recibe los permisos de la cuenta con la que se instala → **crear una cuenta aparte sin sudo** (`bash install.sh --run-as otro_usuario`). Estado/log: `systemctl status musegadget`, `journalctl -u musegadget -f`.

## Errores y riesgos

- Cable de solo carga; versión de ESP-IDF distinta a 6.0.1; no activar Developer mode.
- Comprar placa sin PSRAM esperando el túnel de red (no lo hay).
- Instalar en la Pi con tu usuario principal (le das acceso a todo).
- Emparejar en red pública (no hay verificación del fabricante).

**Advertencia del autor:** lo dice el propio repo — hecho por hackers, para hackers, y **puede brickear placas**. Empezar con algo que no duela perder. «Un agente con manos en tu red es tan seguro como los permisos que tú le des.»

## Relacionado

- [[MOC IA Local]] — agentes e IA en local
- [[Guía Completa - Raspberry Pi Gateway con Tailscale, WireGuard y Pi-hole]] — otra guía de homelab con Raspberry Pi
- [[MOC Automatizaciones]] — conectar gadgets y flujos
