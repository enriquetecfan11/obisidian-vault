---
type: article
tags:
  - ia
  - claude-code
  - landing
  - nextjs
  - threejs
status: active
pipeline: raw
created: 2026-07-07
updated: 2026-07-07
source: https://rackslabs.notion.site/C-mo-construir-una-landing-premium-con-Claude-Code-352faea97468803389f1ccdb53ebb6eb
promotes_to:
title: como-construir-una-landing-premium-con-claude-code
project: none
date_created: 2026-07-07
date_modified: 2026-07-07
---

# Cómo construir una landing premium con Claude Code

> Guía práctica basada en construir `racks.group`: Next.js + Three.js, un rack 3D animado por scroll, modal de contacto y SEO completo, todo con Claude Code en una sola sesión.

## Resumen ejecutivo

La idea central del artículo es sencilla: si quieres una landing premium, no empieces con un prompt vago. Define bien el diseño, fuerza a Claude a razonar en modo plan y trabaja por fases pequeñas y reversibles. El resultado es mejor y además evitas romper animaciones o perder tiempo en iteraciones ciegas.

## TL;DR

- Empieza con un diseño claro, no con un prompt ambiguo.
- Usa `Plan Mode` antes de tocar código.
- Haz que Claude pregunte si hay dudas; no asumas.
- Bloquea lo que ya funciona, sobre todo animaciones.
- Optimiza al final, y en cambios pequeños.
- Usa `.env.local` para pruebas y hardcodea endpoints solo cuando ya estés cerrando producción.

## Setup inicial

### Herramientas

- `Claude Code` como editor + agente.
- `Plan Mode` para razonar antes de codear.
- `plugin caveman` para reducir tokens en respuestas.
- `pnpm` por velocidad y lockfile fiable.
- `Claude Design` para generar un prototipo visual exportable.

### Estructura mínima del repo

El artículo recomienda dejar desde el primer commit:

- `README.md`
- `.gitignore`
- `.env.example`
- `package.json`
- `app/layout.tsx`
- `app/page.tsx`
- `app/globals.css`

La regla práctica es muy clara: `.gitignore` y `README.md` el primer día.

## Plan Mode

Claude Code funciona mejor cuando primero:

1. Lee el contexto.
2. Pregunta dudas con `AskUserQuestion`.
3. Escribe un plan en un archivo markdown.
4. Solo empieza a editar cuando sales de `ExitPlanMode`.

El artículo insiste en que esto evita planes inventados y reduce mucho el retrabajo.

## De Claude Design a código real

`Claude Design` exporta un `.tar.gz` con HTML, CSS y JS de prototipo. No es producción, así que el trabajo real es recrear ese visual en el stack final.

### Qué leer del bundle

- `README.md`: instrucciones para el agente.
- `chats/*.md`: la conversación real con el diseñador.
- `project/`: HTML, JSX, CSS y assets.

### Prompts útiles

El artículo propone pedir primero:

- Qué stack recomienda para producir el diseño.
- Qué assets faltan o son placeholders.
- Qué decisiones críticas necesitan confirmación.

## Stack recomendado

Para una landing 3D moderna, la propuesta del artículo es:

- `Next.js 14` con App Router.
- `@react-three/fiber` para Three.js en React.
- `@react-three/drei` para helpers.
- `zustand` para estado global ligero.
- `next/font/local` para fuentes self-hosted.

La razón de no ir directamente a `Next 15 + React 19` es la compatibilidad del ecosistema `r3f` y `drei`, que aún iba más fino con React 18 en el momento del proyecto.

## Animación 3D

Aquí está el grueso del trabajo.

### Decisiones clave

- Para formas simples o un rack: geometría procedural con `BoxGeometry`.
- Para objetos orgánicos: `glTF` con `useGLTF`.
- Para scroll + cámara: leer el scroll en `useFrame` de forma directa.

### Patrón de apertura por scroll

La idea es calcular una `openness` según la distancia entre la bandeja activa y el índice actual, y aplicarla a posición, opacidad e intensidad emisiva.

### Cache singleton para `window.scrollY`

Para no disparar `layout thrashing`, el artículo sugiere mantener `scrollY` en un cache compartido y actualizarlo con listeners pasivos.

## Lecciones duras

- No sobre-optimices la transición del hero a la primera sección.
- `drei <Html transform>` es muy útil, pero hay que cuidar `pointer-events`.
- `frameloop="demand"` parece una optimización, pero rompe animaciones continuas.

## SEO

El artículo remarca que `Next.js` ya resuelve bastante, pero conviene dejar bien cerrados estos puntos:

- `metadata` con Open Graph y Twitter.
- `canonical`.
- `robots`.
- `sitemap`.
- `JSON-LD` de `Organization`.
- Jerarquía de headings correcta.
- `alt` en imágenes.

## Performance

El orden recomendado es:

1. Imágenes.
2. Código.
3. 3D.

### Fase 1: imágenes

- Convertir PNG a WebP.
- Usar `loading="lazy"` y `decoding="async"`.

### Fase 2: texturas 3D

- Ajustar el tamaño fuente al tamaño real de render.
- No meter texturas enormes para logos o fondos si no hace falta.

## Prompts reutilizables

El artículo termina con varios prompts para:

- arrancar un proyecto,
- iterar animaciones,
- auditar performance,
- depurar saltos entre secciones,
- y refactorizar sin cambiar comportamiento.

La idea no es memorizar prompts, sino obligar al agente a analizar antes de tocar código.

## Takeaways

- La calidad de una landing premium depende más del proceso que del stack.
- El contexto y el plan importan más que el prompt inicial.
- En 3D, lo importante no es solo que se vea bien, sino que el scroll y el rendimiento se sientan sólidos.
- Claude Code funciona mucho mejor cuando le das límites, preguntas concretas y fases de trabajo.

## Referencia

- Fuente: [Notion - Cómo construir una landing premium con Claude Code](https://rackslabs.notion.site/C-mo-construir-una-landing-premium-con-Claude-Code-352faea97468803389f1ccdb53ebb6eb)
