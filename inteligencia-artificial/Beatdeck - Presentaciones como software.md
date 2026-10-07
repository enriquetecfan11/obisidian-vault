---
type: article
tags:
  - agentes-ia
  - frontend
  - ia
  - presentaciones
status: active
pipeline: raw
created: 2026-10-07
updated: 2026-10-07
source: https://x.com/borjaperfra/status/2107767562020761763
promotes_to:
title: "Beatdeck — presentaciones como software, no como slides"
project: none
date_created: 2026-10-07
date_modified: 2026-10-07
---
# Beatdeck — presentaciones como software, no como slides

> Artículo de Borja Pérez (@borjaperfra, Helmcode) sobre cómo pasó la charla de Cristian Córdova (@barckode) en Kernel Panic! de Keynote a HTML, y el sistema que construyó para ello: Beatdeck. Repo: `github.com/borjaperfra/beatdeck`. Demo: `helmcode.com/slides/kernel-panic`.

## Resumen ejecutivo

La tesis es que una charla no tiene slides, tiene momentos: una buena presentación es una secuencia de beats con ritmo, no la diapositiva número 22. Hacer eso en HTML siempre fue posible (Reveal.js, Slidev…), pero costaba demasiado frente a arrastrar cajas en PowerPoint. Con agentes de código el coste cae a cero: una especificación visual se convierte en prompt iterativo. Beatdeck sistematiza ese flujo en escenas + beats con estados deterministas direccionables por URL, más una skill que enseña al agente cómo trabajar y un `npm run verify` con tests para la keynote.

## TL;DR

- Talks as beats, not slides: escenas con beats; cada combinación escena.beat (ej. `#3.4`) es un estado idéntico siempre, recargable y enlazable por URL.
- Una escena se construye por clicks en vez de N diapositivas (servidor → +GPU → +Kubernetes → +Cloudflare → kernel panic con pantalla negra 500 ms).
- Skill para agentes: fuentes → content audit → beat map → dirección visual → implementación → verificación. Extrae de un PPTX y reconstruye (`Turn talk.pptx into a Beatdeck`).
- `npm run verify`: recorre adelante/atrás, entra en beats directos, comprueba determinismo, errores de consola, desbordes, solapes, dependencias externas y genera un contact sheet.
- Presenter view (posición, siguiente, notas, tiempo), overview, fullscreen y blackout; funciona sin internet.

## Por qué dejar PowerPoint (según el autor)

- Como diseñador: sin control de tracking, interlineado, estilos ni píxel exacto; Figma no sirve cuando otros equipos tienen que editar precios.
- Los decks acaban en PDF por email: actualizar y versionar es un infierno.
- La IA elimina la única ventaja de PowerPoint, la comodidad: describir una escena animada es ahora un prompt que se itera en segundos.

## Cómo lo construyó

1. Partió del deck original en Google Slides y del sistema de diseño propio.
2. Prompt simple pidiendo un microsite espectacular para presentar con ratón, teclado o pasador, con animaciones, interacciones y ritmo.
3. En un par de prompts tenía el motor de renderizado y el sistema.
4. Resultado: decenas de beats, arquitecturas que crecen durante la charla, terminales, animaciones persistentes y un crash a negro.

## El problema que resuelve la skill

Sin contexto, el modelo decide qué cifras, benchmarks, nombres o citas conservar, reescribir o simplificar. La skill fija el criterio antes de diseñar: primero entender fuentes, luego mapa de contenido (qué se conserva literal, qué se resume, qué se elimina), después beat map, dirección visual, implementación y verificación. Empaqueta decisiones ya tomadas en vez de dejar que el agente reinvente el sistema cada vez.

## Cuándo seguir usando PowerPoint

- Algo en 20 minutos.
- Ocho personas editando el mismo deck (aunque un repo Git también vale).
- Documento para mandar por email; sirve además como boceto/guion inicial que luego un LLM convierte en guion técnico para Beatdeck.

## Relacionado

- [[MOC Inteligencia Artificial]] — índice del área
- [[OpenCode - Orquestador de agentes]] — orquestar agentes baratos/locales (mismo patrón: sistematizar + delegar)
- [[MOC Programacion]] — frontend y código del vault
