---
title: ejercito-empleados-digitales
type: ia
tags:
  - ia
  - agentes
  - empleados-digitales
  - automatizacion
  - llm
  - ml
  - active
status: active
created: 2026-03-01
updated: 2026-04-06
source: ""
---

## Idea central
- Pasar de usar chat (pregunta → respuesta) a [[Inteligencia Artificial/gpts-recursos-herramientas]] (objetivo → resultado) para multiplicar x10–x20 la productividad diaria.[page:1]
- El “stack” real no es una app, sino una estructura de carpetas con markdown: `agents.md`, `memory.md`, skills y conexiones MCP que puedes mover entre harnesses.[page:1]

---

## De chat a agentes

- Chat: tú haces las preguntas y el trabajo; es como jugar al ping pong con el modelo.[page:1]
- Agentes: les das un objetivo, ellos planifican, ejecutan y entregan resultados.[page:1]
- Fundadores y empleados que usan agentes sistemáticamente acumulan ventaja con el tiempo.[page:1]

---

## Bucle del agente: observar → pensar → actuar

Ejemplo: “Construye un portfolio para Greg Eisenberg”.[page:1]

1. **Observar**: revisa el workspace y archivos existentes.[page:1]  
2. **Pensar**: decide qué investigar o planificar.[page:1]  
3. **Actuar**: ejecuta la acción (investigar, escribir plan, generar código, desplegar, verificar).[page:1]

El agente itera este bucle hasta considerar que el objetivo está cumplido según los parámetros marcados.[page:1]

---

## Agent harnesses

- Herramientas como Claude Code, Codex, Antigravity, Cowork, Manus, OpenClaw son “agent harnesses”: distintas interfaces para el mismo bucle de agentes.[page:1]
- Metáfora: aprender a conducir; una vez dominas volante/frenos, puedes usar cualquier coche (cambia el “coche”, no los fundamentos).[page:1]

---

## Paso 1: `agents.md` – cerebro del agente

- Crea una carpeta, por ejemplo `executive assistant`.[page:1]
- Dentro, define `agents.md` como **system prompt persistente** del agente.[page:1]
- Incluir:
  - Rol del agente.
  - Contexto de negocio.
  - Preferencias personales.
  - Herramientas que usa.
  - Manera de trabajar deseada.[page:1]
- Los harnesses lo llaman distinto:
  - Claude Code → `claude.md`.[page:1]
  - Codex / OpenClaw → `agents.md`.[page:1]
  - Gemini → `gemini.md`.[page:1]
- Puedes generarlo pidiendo a un modelo que haga una entrevista y luego construya el archivo a partir de tus respuestas.[page:1]
- Cambio de paradigma: de “prompt engineering” a **context engineering**.[page:1]

---

## Paso 2: `memory.md` – memoria controlada por ti

Problema: los agentes no recuerdan entre sesiones a menos que tú lo diseñes.[page:1]

Solución:

1. En `agents.md`, añade instrucciones como:
   - “Lee `memory.md` antes de cada tarea”.
   - “Cuando te corrija o aprendas algo nuevo, actualiza `memory.md`”.[page:1]
2. Crea `memory.md` en la misma carpeta.[page:1]

Efectos:

- Preferencias y correcciones se guardan (ej: “tono casual, nunca formal”).[page:1]
- El agente mejora como un buen empleado que recuerda cómo te gusta trabajar.[page:1]

Buenas prácticas:

- Mantener `agents.md` por debajo de ~200 líneas.[page:1]
- Afinar las instrucciones para que `memory.md` sólo guarde correcciones sustanciales.[page:1]

---

## Paso 3: Conectar herramientas con MCP

- Por defecto, los harnesses suelen traer solo web search.[page:1]
- MCP (Model Context Protocol) actúa como **traductor universal** entre el agente y tus apps (Gmail, Calendar, Notion, Stripe, etc.).[page:1]
- Antes: cada integración era custom; ahora, MCP gestiona los “idiomas” de cada herramienta.[page:1]
- Muchos harnesses ofrecen menús de “connectors/skills” para vincular apps con un clic y login.[page:1]
- Ejemplo demo:
  - Un único agente resume inbox, saca notas de reuniones (Granola), crea link de pago en Stripe, abre proyecto en Notion y redacta email de follow-up sin cambiar de pestaña.[page:1]

---

## Paso 4: Skills – SOPs para tu agente

Concepto:

- Una **skill** = un SOP (procedimiento estándar) empaquetado para el agente.[page:1]
- Sin skill: mucho back-and-forth, ajustes manuales cada vez.[page:1]
- Con skill: el agente aplica formato, colores, estructura, etc. automáticamente.[page:1]

Formas de crearlas:

1. **Fuente externa**  
   - Subir contenido (ej: transcripción de curso) y pedir “crea una skill basada en esto”.[page:1]
2. **Desde una sesión**  
   - Trabajar un proceso con el agente y luego decir “crea una skill de lo que acabamos de hacer”.[page:1]

Ejemplo real:

- Skill de análisis de librería de anuncios (scraping, screenshots, análisis copy/creatives, informe maestro) que pasa de 3–4 horas a ejecutarse con dos palabras.[page:1]

Recomendación:

- Automatizar 3–5 procesos pequeños por semana para ir cubriendo todo tu flujo de trabajo.[page:1]

---

## Paso 5: Encadenar skills y programar tareas

- Las skills se vuelven potentes al combinarlas.[page:1]
- Ejemplo:
  - `meeting prep skill`: investiga invitado y genera talking points.[page:1]
  - `podcast research skill`: profundiza en background del invitado.[page:1]
  - `morning brief skill`: revisa agenda y dispara las otras skills si detecta un podcast.[page:1]
- Muchos harnesses permiten programar tareas:
  - Ej: un `morning brief` a las 9:00 cada día para revisar calendario, inbox, Notion y generar plan del día.[page:1]
- Ejemplo adicional:
  - Búsqueda de coche con filtros específicos; un agente scrapea marketplaces cada 3 horas y avisa cuando encuentra algo que encaja.[page:1]

---

## Estructura de carpetas para “correr” un negocio

- Una carpeta principal por empresa o cliente.[page:1]
- Dentro, subcarpetas por “departamento” (ejecutivo, contenido, marketing, ventas).![page:1]
- Cada subcarpeta contiene:
  - `agents.md`
  - `memory.md`
  - Carpeta de skills
  - Configuración de conexiones MCP relevantes.[page:1]
- El agente de marketing sabe reglas de creatividades; el de contenido, tu voz de marca; el asistente ejecutivo, tu forma de firmar emails.[page:1]
- Un agente global coordina al resto.[page:1]
- Skills globales (ej: “haz esto más corto”) se comparten; skills específicas se quedan en su proyecto.[page:1]

---

## Guía rápida para empezar

1. Elige un agent harness (ej: Cowork para empezar).[page:1]
2. Crea una carpeta `executive assistant`.[page:1]
3. Construye `agents.md` usando un flujo de entrevista.[page:1]
4. Añade `memory.md` con instrucciones de auto-actualización.[page:1]
5. Conecta tus herramientas clave vía MCP.[page:1]
6. Usa el agente en tareas reales y convierte procesos repetidos en skills.[page:1]
7. Automatiza 3–5 procesos pequeños por semana.[page:1]

---

## Principios clave

- Los harnesses cambian, **tus archivos markdown** (contexto, memoria, skills) permanecen y se pueden migrar.[page:1]
- Ciclo continuo: conectar herramientas → construir contexto → crear skills → automatizar procesos → repetir.[page:1]
- No se trata de sustituirte, sino de comprimir el “busywork” para que tú te centres en decisiones importantes.[page:1]
- Empieza por un solo agente (ejecutive assistant) y una skill por semana; el efecto compuesto te lleva a “encajar una semana en un día”.[page:1]

# Link Original
https://x.com/startupideaspod/status/2033993454653743191