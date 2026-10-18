---
title: "Company brain — el cerebro de tu empresa para que la IA trabaje de verdad"
type: article
tags:
  - ia
  - pkm
  - agentes-ia
  - claude-code
status: active
project: none
date_created: 2026-10-17
date_modified: 2026-10-17
source: https://www.javiggil.com/abca36661667
---
# Company brain — el cerebro de tu empresa para que la IA trabaje de verdad

> Guía de javiggil (7-oct-2026) para montar el «company brain» de una empresa: el conocimiento del negocio en una carpeta markdown (suya, portable) con el motor LLM enchufado encima. Explica su propio cerebro (740 notas, ocho capas, cifras reales), da plantillas y código (`build_index.py`, hooks, CLAUDE.md), y su parte más valiosa: cómo meterlo en una empresa que ya funciona con un plan de 90 días y 15 jugadas.

## La idea central: el motor y el cerebro

- **El motor** es el modelo (Claude, ChatGPT, Gemini): de alquiler, cambia cada pocos meses.
- **El cerebro** es lo que sabe de TU negocio: procesos, precios, clientes, decisiones. No lo sabe ningún modelo.

El error caro es meter el cerebro dentro del motor (subirlo todo a una plataforma). El company brain es lo contrario: **tu conocimiento en una carpeta que es tuya**, en markdown, con el motor enchufado. El motor cambiará diez veces; la carpeta se queda.

## Por qué la IA «no funciona» en la empresa

El informe del MIT (NANDA, *The GenAI Divide*, jul-2025) da un 95 % de organizaciones sin retorno medible, pero la cifra tiene críticas serias (muestra de cuatro conferencias, datos no públicos, definición estrecha de fracaso) → **señal, no dato**. La causa que apuntan es la «brecha de aprendizaje»: IA sin contexto = IA sin cerebro.

Los wikis clásicos (Notion/Confluence) se pudren por cinco razones; la IA arregla el **escribir/vigilar**, pero **no** el dueño de la página ni vivir dentro del trabajo (decisiones humanas).

## Lo que cambió en 2025-2026

- La IA ya busca sola con herramientas (`grep`, listar carpetas) mejor que un RAG clásico y sin desincronizarse (medición interna de Anthropic, no estudio publicado).
- **Revelación progresiva** (Anthropic, *Effective context engineering* sep-2025 y Agent Skills oct-2025): el agente lleva un índice ligero y abre el detalle solo cuando hace falta.
- Karpathy y su «LLM Wiki» (abr-2026): un wiki markdown que el propio modelo escribe y mantiene, con reglas en un `CLAUDE.md`. Con RAG el modelo «redescubre el conocimiento desde cero»; con el wiki, se acumula.

## El suyo por dentro (medido el 7-oct-2026)

| Métrica | Cifra |
| --- | --- |
| Notas | 740 |
| Días de vida | 134 |
| Cambios en git | 615 (419 automáticos) |
| Decisiones registradas | 105 |
| Skills que lo leen/escriben | 7 |
| Peso total | ~17 MB ≈ 5,2 M tokens |

**Las ocho capas** (de lo que se lee siempre a lo que se abre solo cuando hace falta): 0 · `CLAUDE.md` (portero que enruta, no reglas), 1 · orientación (quiénes somos, reglas, glosario), 2 · contexto por área (`_contexto.md`), 3 · índices (`_index/`: `mapa.md` se busca con grep, `hechos.md` se lee, `pesados.md` avisa), 4 · las notas, 5 · decisiones y evidencia, 6 · los que trabajan (skills, tareas, conectores), 7 · la salud (chequeo).

**Coste de contexto:** leer el vault entero ≈ 5,2 M tokens (no cabe ni en 1M de ventana); la ruta con índices + grep ≈ 12.000 tokens. **~450 veces menos**, con la nota correcta delante.

## Lo que les salió mal

1. El vault «mentía con solemnidad» (jun-2026) → arreglado con 4 niveles de evidencia: **dato duro / hipótesis con datos / oficio / adorno**.
2. El chequeo de salud llegó tarde: 56 notas → 0 avisos; 615 notas → 709 avisos. Se pone en el calendario desde el día uno.
3. Los documentos muertos seguían «hablando» → el portero avisa de lo que NO existe.
4. Un número escrito a mano en el `CLAUDE.md` caducó → los números importantes los calcula un script, y los demás llevan fecha y caducidad.
5. Datos de memoria con cara de datos → la fila lo dice y la IA debe avisar.

## Cómo construirlo (piezas, con plantillas)

- **Estructura de carpetas numeradas** + especiales con guion bajo (`00-inbox/`, `00-orientacion/`, `07-decisiones/`, `99-archivo/`, `_index/`, `_scripts/`, `_templates/`). Empezar solo con las carpetas del primer proceso a documentar.
- **`CLAUDE.md` (portero):** < 200 líneas, solo enruta (qué leer, cómo buscar en el mapa con grep, reglas duras, sección «Lo que NO existe»).
- **La nota:** frontmatter de 5 campos + dueño (`owner`), y **un blockquote de resumen bajo el título** (es la línea más importante: acaba en el índice).
- **`_scripts/build_index.py`:** sin dependencias, genera `_index/mapa.md` y `_index/caducados.md`, y sale siempre con 0 para no bloquear un commit. Con 500 notas es lo que separa encontrar algo en un segundo de perder diez minutos.
- **Los datos con caducidad** (`hechos.md`): tabla `dato | valor | al | fuente | ttl`; al caducar, la IA avisa.
- **El registro de decisiones** (formato ADR adaptado a negocio) con contexto, decisión, quién, evidencia, qué la tumbaría y fecha de revisión. Nunca se borran.
- **La escala de evidencia** (4 niveles) y **entrada/salida** (`00-inbox/` para lo que aún no tiene sitio, `99-archivo/` para lo muerto, que no se indexa).
- **El hook** (`.claude/settings.json`) rehace el índice al arrancar y al terminar cada turno; Obsidian Git guarda cada media hora.
- **Conectarlo:** Claude Code (abre la carpeta), Claude Desktop por MCP (servidor de filesystem), y tareas programadas en la nube («routines») que trabajan en una rama aparte.
- **Las skills** (`SKILL.md`): revelación progresiva, cerebro que hace trabajo. Regla: al principio **ninguna skill manda nada a un cliente sin revisión humana**.

## Meterlo en una empresa que ya funciona (plan de 90 días)

Regla que lo decide todo: **un dolor, un cerebro** — elegir UN proceso que duela y documentar solo lo que ese proceso necesita. No «documentar la empresa».

- **Semana 1:** elegir el dolor (dueño, 5 personas, medir el tiempo actual, inventario de dónde vive el conocimiento, montar el esqueleto).
- **Mes 1:** 30-60 notas del proceso, IA en solo lectura, canal de preguntas, correo del lunes.
- **Trimestre 1:** primera skill que hace trabajo real, dos procesos más, entrevistas, auditoría nocturna, primer onboarding. *Si a los 90 días no ha mejorado ningún número, arregla, no amplíes.*

**Las 15 jugadas** (las marcadas con ★ son por donde empezaría): entrevista al revés ★, escriba silencioso de reuniones, canal «pregúntale al cerebro» ★, lista de lo que no sabemos, cerebro en la sombra, arqueología de chats, correo del lunes ★, auditoría nocturna de contradicciones, onboarding medido en días, examen del cerebro de 20 preguntas, correo a nota, ficha antes de cada llamada, retro de diez minutos, «¿está en el cerebro?» (la jugada del jefe), tarjeta de confianza.

**Quién hace qué:** patrocinador (dirección), responsable del cerebro (persona ordenada, no necesariamente técnica, 20-30 % de su tiempo), dueños de carpeta, protección de datos.

**Lo que lo mata:** documentar todo antes de dar valor, notas sin dueño y datos sin fecha, dar acceso a todo «por si acaso», dejar que la IA escriba sin revisión cosas que cuestan dinero, elegir herramienta antes que proceso, no medir el «antes», montarlo como «proyecto de informática».

## Cómo se alimenta y se enchufa

- **Los conectores no escuchan:** un conector solo lee cuando alguien lo llama → hace falta un **disparador** (tarea programada o webhook) y un **filtro** (el agente escribe en `00-inbox/`, en rama aparte, y una persona aprueba).
- **Seis reglas anti-basura:** lista blanca (nunca volcado), lo vivo se queda en su herramienta, el agente escribe en el inbox, cada entrada con fuente/fecha/dueño, el texto de fuera es dato y no órdenes, y una persona en el último paso (PR + `CODEOWNERS`).
- **Empresa tipo** (reformas, 25 personas): Gmail/Drive/Slack/HubSpot/Holded enchufados; una routine matinal destila a un PR; **el chat de la empresa** con Claude Tag en Slack (lee el repo, no necesita licencia para los que preguntan, tope de gasto). Teams y Proyectos de claude.ai no sirven como chat de equipo. WhatsApp no para el cerebro interno (prohibición de la API de Meta desde el 15-ene-2026).

## Advertencia del autor (frontera honesta)

«Company brain» es el nombre que da el autor al patrón, no término oficial. Separa fuentes leídas (con enlace y fecha), medición propia del vault (con fecha) y criterio propio. Las jugadas de implantación son **criterio razonado, no casos auditados**.

## Relacionado

- [[MOC Inteligencia Artificial]] — índice del área
- [[obsidian-segundo-cerebro]] — Obsidian + agente compartiendo el mismo vault
- [[OpenCode - Orquestador de agentes]] — orquestar agentes sobre el conocimiento
- [[MOC IA Local]] — motor local; el cerebro es portable entre motores
- [[Ornith en tu homelab - instalar y conectar a n8n y Hermes]] — motor local (Ornith + llama.cpp) para alimentar el cerebro
