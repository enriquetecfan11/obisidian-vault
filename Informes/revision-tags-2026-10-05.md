---
title: "Revisión de tags — 2026-10-05"
type: auditoria
tags:
  - documentacion
  - pkm
status: active
project: ninguno
date_created: 2026-10-05
date_modified: 2026-10-05
---

# Revisión de tags — 2026-10-05

Inventario real medido sobre los 196 `.md` del vault. **No se ha modificado nada todavía.**

## Corrección importante

En la auditoría anterior dije "25 grupos de variantes de tags". Al medirlo bien, la cifra era errónea: el script anterior mezclaba tags del cuerpo de notas con hashtags de LinkedIn y contaba variantes que no compiten entre sí.

Cifras reales:

| Métrica | Valor |
| --- | --- |
| Notas del vault | 196 |
| Tags distintos en la clave `tags:` | 122 |
| Usos de `tags:` en total | 688 |
| Tokens que Obsidian indexa (`tags:` + `linkedin_hashtags:`) | 194 distintos, 1694 usos |
| Grupos de variantes reales entre esos tokens | **3** |
| Tags escritos con `#` dentro del cuerpo | 54 distintos, 184 usos, en 4 archivos |

## Dónde vive cada cosa

| Ubicación | Qué es | Qué hacer |
| --- | --- | --- |
| `tags:` (196 notas) | taxonomía propia del vault,Controlled por ti | normalizar |
| `linkedin_hashtags:` (35 notas, 77 tokens) | hashtags literales que tú publicaste en LinkedIn | **dejar como están** |
| `#algo` dentro del cuerpo (4 archivos) | en su mayoría hashtags citados en tablas de datos | decidir archivo por archivo |

`linkedin_hashtags:` es un campo propio, no una lista de Obsidian: Obsidian no lo indexa como tags, así que `#IA` ahí dentro convive con `ia` en `tags:` sin colisionar en búsquedas.

## Los 3 grupos de variantes reales

### 1. `ia` / `IA` — el que te preocupa

| Token | Veces | Dónde |
| --- | --- | --- |
| `ia` | 96 | clave `tags:` |
| `ia` | 11 | `linkedin_hashtags:` (hashtags literales) |
| `IA` | 18 | `linkedin_hashtags:` (hashtags literales) |

**Dato clave: en la clave `tags:` solo existe `ia` en minúscula. No hay ni una sola `IA` mayúscula.**

Los 18 `IA` que alarmaban son de notas de LinkedIn, en `linkedin_hashtags:`, y ahí `IA` es el hashtag que tú escribiste al publicar. Cambiarlo a `ia` falsearía el registro de lo publicado.

Sobre tu preferencia de usar `IA`:

- **Tecnicamente viable.** Renombrar `ia` → `IA` en 96 notas es un cambio mecánico, y Obsidian distingue mayúsculas (`#IA` y `#ia` son tags distintos, igual que en este informe).
- **Coste.** Con `IA` would obligatorio escribir `ia` a mano en cualquier nota nueva, y cualquier Mac o teclado que normalice mayúsculas en un tag lo rompe. `#ia` sobrevive a la línea de comandos, a los plugins y a las importaciones.
- **Consecuencia de la razón inversa.** Si hoy tienes `ia` en 96 notas y escribes `#IA` en una nueva, no la ves en la búsqueda de `ia` sin generar las dos.

Conclusión: la razón por la que "el peor es `ia` contra `IA`" no se sostiene una vez medida. El problema no era la variante, era que el conteo sumaba campos distintos. `ia` en minúscula es la forma correcta aquí.

## Problemas reales que sí quedan

### Tags con acento (rompen búsquedas por acento)

| Actual | Notas | Propuesta |
| --- | --- | --- |
| `diseño` | 2 | `diseno` |

Solo 2 notas, ambas en `inteligencia-artificial/Custom GPTS/`: `Infografias GPT.md` y `Linkedin Agents/Thumbnail Builder.md`.

El resto de tags con eñes ya están resueltos: `automatizacion`, `configuracion`, `redes-sociales`, `base-de-datos-vectorial`, `analisis-datos`, `meteorologia`, `ciberseguridad`. Son la convención correcta, minúsculas sin tilde.

### Tags en el cuerpo de notas

| Archivo | Usos | Naturaleza |
| --- | --- | --- |
| `redes-sociales/linkedin_posts_full_analytics.md` | 171 | hashtags de 47 posts dentro de una tabla. Datos, no taxonomía |
| `notas-personales/configuraciones/SKHD Configuration.md` | 5 | encabezados `## Instalación` leídos como tag |
| `notas-personales/configuraciones/Yabai y Ghostty Setup.md` | 4 | igual, encabezados de sección |
| `redes-sociales/linkedin/Linkedin Posts/Ayer viví... Hackathon NoCode....md` | 2 | falso positivo: `#n8n` dentro de una URL |
| `inteligencia-artificial/_tag-migración-2026-10-05.md` | 2 | informe puntual ya terminado, `#n8nón` es ruido |

Los tres primeros casos comparten causa: `## Instalación` con tilde produce `#Instalación` porque `##` + ` ` + palabra acentuada. Se arregla con una palabra sin tilde o con `#` explícito para marcar que es un encabezado.

Los grupos de variantes inline, normalizados:

- `Tecnología(24) | Tecnologia(2) | tecnologia(1)`
- `Networking(4) | networking(1)`
- `Eventos(3) | eventos(1)`
- `Startup(2) | startup(1)`
- `Innovacion(1) | Innovación(1)`

Todos en el archivo de analytics de LinkedIn. Al ser hashtags de posts reales, lo correcto es que se queden tal cual y **no** se mergeen.

### Duplicados con distinta grafía que sí conviene unificar

| Actual | Veces en `tags:` | Nota |
| --- | --- | --- |
| `programacion` | 6 | existe una nota aislada con `Programación` en `linkedin_hashtags:` |
| `programacion` | 6 | |
| `Productividad` | 4 | son 4 inline en el archivo de LinkedIn |
| `productividad` | 3 | |

## Taxonomía actual en uso (122 tags)

Agrupados por lo que significan, para que decidas qué se queda:

| Área | Tags | Nº |
| --- | --- | --- |
| IA | `ia`, `ia-local`, `llm`, `agentes-ia`, `evaluacion-ia`, `prompt-engineering`, `rag`, `base-de-datos-vectorial`, `openai`, `claude`, `claude-code`, `codex`, `ollama`, `llama-cpp`, `stable-diffusion`, `midjourney`, `generacion-imagenes`, `fine-tuning`, `gpt-personalizado`, `mcp`, `skills` | 22 |
| Automatización | `automatizacion`, `n8n`, `chatbot`, `api-rest`, `make`, `workflow`-ausente, `evolution-api`, `chatwoot` | 7 |
| DevOps | `devops`, `infraestructura`, `docker`, `postgresql`, `bases-de-datos`, `sqlite`, `qdrant`, `linux`, `proxmox`, `wazuh`, `check-mk`, `tailscale`, `wireguard`, `pi-hole`, `parsec`, `rustdesk`, `red`, `acceso-remoto`, `raspberry-pi`, `ciberseguridad` | 20 |
| Desarrollo | `desarrollo`, `frontend`, `backend`, `java`, `spring-boot`, `python`, `nodejs`, `nextjs`, `react`, `angular`, `threejs`, `leaflet`, `gis`, `markdown`, `arquitectura`, `websocket` | 16 |
| Trabajo | `work`, `personal`, `finanzas`, `inversiones`, `rrhh`, `facturas`, `proyecto-saas`, `scrum`, `linear`, `marketing`, `contenido`, `noticias`, `analisis-datos`, `origen`, `redes-sociales`, `linkedin`, `twitter`, `hackathon`, `biavent` | 19 |
| Sistema | `mara-os`, `mara`, `arvis`, `atlas`, `warren`, `openclaw`, `documentacion`, `pkm`, `plantilla`, `indice`, `estado`, `operativo`, `backup`, `memoria`, `identidad`, `usuario`, `identidad`-dup, `configuracion` | 18 |
| Otros de 1-5 usos | `diaria`, `productividad`, `aviacion`, `drones`, `arduino`, `educacion`, `podcast`, `meteorologia`, `macos`, `ghostty`, `yabai`, `skhd`, `hardware`, `github`, `telegram`, `whatsapp`, `webhook`-ausente, `ai` | 20 |

Cuatro tags con una sola nota y dudosos: `mia` no existe, pero sí `estado`, `operativo`, `ia` huérfanos de contexto, y `programacion` como tag cuando ya existe la carpeta `programacion/` con 25 notas dentro. Ahí hay duplicación entre carpeta y tag que merece decisión.

## Recomendación

Tres cambios, todos pequeños y mecánicos:

1. **`diseño` → `diseno`** en 2 notas. Sincontroversia.
2. **Quitar el falso positivo `#n8n`** de la URL en la nota del hackathon, y borrar o archivar el informe `_tag-migración-2026-10-05.md`.
3. **`linkedin_posts_full_analytics.md`: los hashtags dentro de la tabla se dejan como texto**, sin `#`, para que no se indexen. Son datos de publicaciones, no tags del vault.

Lo que **no** recomiendo: renombrar `ia` → `IA`. El problema que lo motivaba no existe, y el cambio costaría obligarte a escribir la mayúscula a mano en cada nota nueva.

## Pendiente de tu decisión

- ¿Quieres que aplique los 3 cambios de arriba?
- ¿Renombro `ia` → `IA` igualmente, o dejamos `ia`?
- ¿Hay tags que sobren, como `programacion` si ya existe la carpeta?