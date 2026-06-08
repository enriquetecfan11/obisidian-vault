---
type: nota
tags:
  - agente-ia
  - claude
  - code
status: active
updated: 2026-06-08
fuente: Rackslabs / Notion, "Cómo construir una landing premium con Claude Code"
URL: https://rackslabs.notion.site/C-mo-construir-una-landing-premium-con-Claude-Code-352faea97468803389f1ccdb53ebb6eb
---
## Tesis central

La idea principal es que una landing premium con Claude Code no se consigue con un prompt genérico tipo "hazme una landing bonita", sino con un flujo disciplinado: diseño claro, contexto explícito, Plan Mode antes de tocar código, iteraciones pequeñas y verificación continua.

El caso de referencia es la construcción de `racks.group`: una landing en Next.js con una pieza 3D animada por scroll, modal de contacto, SEO completo, páginas legales, optimización mobile y despliegue en Vercel. La promesa práctica del artículo es que, con diseño base y buen uso de Claude Code, se puede llegar a algo production-ready en una sesión larga, aproximadamente 5-7 horas reales desde cero, o 2-3 horas si el diseño ya está bien resuelto.

El aprendizaje más importante para Kike/Mara: Claude Code multiplica velocidad cuando se le da una dirección de producto y diseño muy concreta, pero también puede romper sistemas delicados si se le deja "mejorar" sin límites. Hay que tratarlo como un agente senior rápido, no como una caja mágica.

## Flujo recomendado end-to-end

1. **Definir intención visual y producto antes del código.**
   - Referencias visuales.
   - Secciones esperadas.
   - Tono de marca.
   - Interacciones clave.
   - Qué debe sentirse premium y qué no puede parecer plantilla genérica.

2. **Generar o preparar un diseño base.**
   - Si hay Claude Design, exportar el prototipo.
   - Si no hay diseñador, describir con precisión layout, ritmo, estética, secciones y comportamiento.
   - No tratar el prototipo como producción; usarlo como especificación visual.

3. **Iniciar el repo con higiene básica.**
   - Crear `.gitignore` desde el primer día.
   - Crear `README.md` con instrucciones de proyecto.
   - Elegir stack estable antes de iterar.
   - Instalar dependencias y comprobar `pnpm build` temprano.

4. **Usar Plan Mode antes de modificar código.**
   - Obligar a Claude Code a leer contexto.
   - Pedirle que haga preguntas si falta información.
   - Pedir un plan Markdown concreto.
   - Aprobar el plan antes de ejecutar.

5. **Construir por bloques atómicos.**
   - Setup y build limpio.
   - Layout base.
   - Escena 3D.
   - Scroll/cámara.
   - Modal/contacto.
   - SEO/legal.
   - Performance.
   - Mobile.
   - Deploy.

6. **Bloquear lo que funciona.**
   - Si una animación 3D queda bien, no permitir mejoras amplias encima sin motivo.
   - Pedir análisis antes de fixes cuando aparezcan bugs visuales.
   - Mantener cambios reversibles y pequeños.

7. **Cerrar con producción real.**
   - Build sin errores.
   - Test local con `pnpm start`.
   - Variables en Vercel.
   - DNS, SSL, sitemap, robots, OG, analytics y Search Console.

## Stack y decisiones técnicas

Stack recomendado por la guía para una landing 3D moderna:

- **Next.js 14.**
- **React 18.**
- **@react-three/fiber v8.**
- **drei.**
- **zustand.**
- **pnpm.**

La recomendación evita Next 15 / React 19 si el ecosistema de `r3f` y `drei` no está suficientemente estable para el proyecto. La clave no es usar lo más nuevo, sino reducir fricción entre dependencias cuando el valor diferencial está en la experiencia visual y el 3D.

Zustand aparece como decisión relevante frente a Context por dos motivos:

- Permite re-render selectivo.
- Permite lectura síncrona de estado desde `useFrame`, útil en animaciones y escenas 3D.

Reglas prácticas:

- Verificar `pnpm install` y `pnpm build` antes de seguir.
- No meter endpoints reales en código salvo producción inmediata y consciente.
- Usar `.env.local` para pruebas y variables locales.
- Si el repo puede acabar público, asumir que cualquier webhook hardcodeado se filtrará.

## Diseño, Claude Design y Plan Mode

Claude Design puede exportar un `.tar.gz` con prototipo HTML/CSS/JS. Según la guía, ese bundle debe entenderse como material de diseño, no como código final.

Qué revisar dentro del export:

- `README.md`: instrucciones que el propio prototipo deja para el coding agent.
- `chats/`: intención real entre usuario y diseñador, útil para entender decisiones no obvias.
- `project/`: HTML/JSX/CSS/assets que expresan la dirección visual.

Flujo recomendado con Claude Code:

- Entrar en Plan Mode antes de tocar archivos.
- Forzar lectura del contexto relevante.
- Pedir que formule dudas con `AskUserQuestion` si hay ambigüedad.
- Pedir un plan Markdown antes de modificar.
- Esperar aprobación explícita con `ExitPlanMode`.

Para Mara, esto se traduce en una norma operativa: cuando Kike pida landings premium, no conviene empezar por componentes. Primero hay que capturar dirección visual, stack, secciones, assets, restricciones y criterios de aceptación.

## 3D con Three.js/r3f y scroll

La guía distingue entre dos tipos de 3D:

- **Formas simples o técnicas:** usar geometría procedural, por ejemplo `BoxGeometry`.
- **Modelos orgánicos, personajes, naturaleza o piezas complejas:** usar glTF con `useGLTF` de drei.

Para el caso del rack, la solución fue procedural: bandejas, contenedores y piezas simples que se podían animar con precisión.

Métodos de animación recomendados:

- `useFrame` + `damp` para estados discretos.
- `useFrame` + scroll directo para experiencias scroll-driven y cámara.
- GSAP ScrollTrigger para timelines más complejos.

En el proyecto de referencia se usó scroll directo dentro de `useFrame` para controlar cámara y continuidad visual, buscando una sensación fluida. El efecto deseado era que la bandeja activa estuviera abierta y las contiguas medio abiertas, con transición continua al hacer scroll.

Punto crítico: no leer `window.scrollY` directamente dentro de `useFrame` a 60 fps, porque puede provocar layout thrashing. La solución descrita es un singleton/cache de scroll y resize:

- El navegador actualiza la cache cuando hay scroll/resize.
- Componentes como `Trays` y `Rack` leen la cache.
- El frame loop no toca DOM directamente.

Otros detalles 3D importantes:

- Si hay salto visual entre hero y sección, probar `damp` antes de ajustar offsets de forma agresiva.
- `drei <Html transform>` sirve para pegar UI a una mesh, pero hay que controlar `pointer-events`.
- Un patrón útil: wrapper del canvas con `pointer-events: none` para permitir scroll y UI interna con `pointerEvents: auto` para clicks.
- No usar `frameloop="demand"` si hay movimiento continuo o animación idle, porque puede romper la sensación viva de la escena.

## Performance y mobile

La guía propone optimizar al final y en fases atómicas, no mezclar performance con features. Orden recomendado:

1. Imágenes.
2. Código.
3. 3D.

Optimizaciones concretas:

- Reducir previews y assets grandes al tamaño real de render.
- Convertir imágenes a WebP cuando encaje.
- Bajar logos sobredimensionados, por ejemplo de 600px a 256px o 512px si van como fondo.
- Usar geometrías compartidas para meshes idénticas.
- Aplicar anisotropy y mipmaps en texturas cuando mejore el look sin coste excesivo.
- Usar `next/font` para preload, evitar FOUT y mejorar cache.
- Limitar DPR en mobile, por ejemplo cap 1.5.
- Usar `100dvh` en lugar de `100vh` para iOS Safari.
- Mantener singleton de scroll/resize para no castigar el frame loop.

Falsas optimizaciones a evitar:

- `frameloop="demand"` si rompe animaciones idle.
- Reducir luces de forma agresiva si destruye el look premium.
- Añadir `React.memo` por todas partes sin medición ni ganancia clara.

Riesgos mobile reales:

- GPU y batería.
- Memoria por texturas.
- Carga inicial en 3G/4G.
- Quirks de iOS Safari.

La recomendación no es crear una landing mobile completamente distinta, sino mantener el mismo flujo y ajustar:

- Cámara.
- Zoom.
- Rack centrado en X=0.
- DPR.
- Peso de assets.
- Alturas con `100dvh`.

## SEO, formularios y despliegue

Next.js 14 cubre parte importante del SEO si se usa bien, pero la guía insiste en cerrar el paquete completo:

- Metadata.
- Sitemap.
- Robots.
- Open Graph.
- Imagen OG 1200x630 en `/public/og.png`.
- Páginas legales.
- Formularios reales.
- Deploy verificado.

Las páginas legales deben ser Server Components:

- Sin estado.
- Indexables.
- Simples.
- Sin JS cliente innecesario.

Para formularios/contact modal:

- Guardar endpoint en `.env.local` durante desarrollo.
- En producción, configurar variable en Vercel.
- No hardcodear webhook en el código aunque sea público.
- Probar el formulario real antes de darlo por listo.

Variables citadas para Vercel:

- `NEXT_PUBLIC_SITE_URL=https://racks.group`
- `NEXT_PUBLIC_CONTACT_ENDPOINT=...`

Checklist de despliegue:

- `pnpm build` sin errores.
- `pnpm start` y test local.
- Variables de entorno configuradas.
- DNS apuntando correctamente.
- SSL automático de Vercel activo.
- `/sitemap.xml` accesible.
- `/robots.txt` accesible.
- Search Console configurado con sitemap.
- Analytics con Vercel Analytics o Plausible.

## Errores comunes y fixes

- **Hooks después de `if (!open) return null`:**
  - Mover hooks arriba.
  - Los hooks deben ejecutarse siempre en el mismo orden.

- **`localStorage` durante inicialización del store:**
  - Inicializar estado estático.
  - Leer `localStorage` en `useEffect` post-mount.
  - Evitar errores SSR/hydration.

- **`pointer-events` heredado rompe clicks en UI 3D:**
  - Permitir scroll en el wrapper.
  - Reactivar `pointerEvents: auto` dentro de Html/UI clicable.
  - Revisar z-index frente a secciones HTML.

- **Errores SSR con Three/drei:**
  - Usar dynamic import con `ssr: false` para componentes 3D que dependen del navegador.

- **Ciclos infinitos de fix:**
  - Pedir análisis antes de cambiar.
  - Solicitar hipótesis, causa probable y plan mínimo.
  - Aplicar un cambio atómico y verificar.

- **Animaciones rotas por mejoras posteriores:**
  - Congelar comportamiento cuando ya funciona.
  - Documentar el contrato visual de la animación.
  - No mezclar refactor, performance y ajustes visuales en el mismo paso.

## Checklist operativo para futuras landings de Kike

- Definir objetivo de negocio de la landing.
- Definir audiencia y tono.
- Reunir referencias visuales concretas.
- Listar secciones exactas.
- Definir interacción diferencial: 3D, scroll, modal, comparativa, calculadora, demo, etc.
- Decidir stack estable antes de empezar.
- Crear `.gitignore` y `README.md`.
- Instalar dependencias con pnpm.
- Ejecutar build inicial.
- Entrar en Plan Mode antes de modificar.
- Obligar al agente a preguntar dudas.
- Aprobar plan por fases.
- Construir layout base.
- Recrear visual del prototipo en stack real.
- Implementar 3D con la menor complejidad suficiente.
- Cachear scroll/resize si hay frame loop.
- Verificar scroll, pointer events y z-index.
- Añadir formulario con endpoint en env.
- Añadir metadata, OG, sitemap y robots.
- Crear páginas legales indexables.
- Optimizar imágenes primero.
- Optimizar código después.
- Optimizar 3D al final.
- Revisar mobile real: DPR, cámara, carga, iOS Safari.
- Probar Lighthouse mobile: performance >80, SEO/A11y >90.
- Probar build y start local.
- Configurar variables en Vercel.
- Probar webhook con envío real.
- Apuntar DNS.
- Verificar SSL.
- Enviar sitemap a Search Console.
- Activar analytics.
- Documentar decisiones importantes en Obsidian/SystemFiles.

## Implicaciones para Mara / SystemFiles

Esta guía debe convertirse en patrón operativo reutilizable para landings premium de Kike:

- Mara debe insistir en diseño y dirección antes de código cuando el objetivo sea premium.
- El Plan Mode o equivalente debe ser obligatorio para landings con 3D, animaciones, SEO y despliegue.
- Las animaciones funcionales deben tratarse como piezas delicadas: se bloquean, se verifican y se cambian solo con intención clara.
- Performance debe programarse como fase final por lotes pequeños, no como optimización difusa durante todo el proyecto.
- Para proyectos públicos o potencialmente públicos, endpoints y secretos siempre deben ir a env.
- La checklist anterior puede copiarse como base para futuros briefs de landing, PRDs técnicos o prompts de agente.

Para futuras tareas, Mara puede usar esta nota como referencia de:

- Stack recomendado para landing 3D con Next.
- Flujo Claude Design -> Claude Code.
- Riesgos comunes de r3f/drei/SSR.
- Checklist de producción antes de deploy.
- Criterios para no romper animaciones ya buenas.

## Estado

- **Fecha:** 2026-06-08.
- **Estado local:** nota creada en Obsidian y subida al remoto del vault.
- **Commit de creación:** `2ad09aa` (`Añade resumen Rackslabs landing premium Claude Code`).
