---
title: obsidian-segundo-cerebro
type: ia
tags:
  - obsidian
  - segundo-cerebro
  - ia
  - productividad
  - pkm
  - ml
  - active
status: active
created: 2026-03-01
updated: 2026-04-06
source: ""

---


## Idea principal
- El truco es que el agente de IA y las notas compartan **exactamente** la misma carpeta.
- Cuando ambos usan el mismo directorio, se convierten en un solo sistema: el agente lee, crea, actualiza y organiza tus notas sin fricción.[page:1]

## 1. Un solo folder para todo
- Crea una carpeta (Workspace, Brain, etc.) y abre ahí el terminal del agente.
- Apunta Obsidian a esa misma carpeta como vault (sin crear uno nuevo).
- Cualquier nota que cree el agente aparece al instante en Obsidian, y lo que edites en Obsidian está disponible para el agente.[page:1]

## 2. El terminal dentro de Obsidian
- Instala el plugin “Terminal” desde los Community Plugins.
- Ábrelo en modo integrado para tener el agente como una pestaña más dentro de Obsidian.
- Mismo contexto, misma ventana, sin cambios de app que rompan el flujo.[page:1]

## 3. AGENTS.md: cerebro del agente
- Crea un archivo `AGENTS.md` en la raíz de la carpeta.
- Especifica quién es el agente, qué hace, cómo manejar archivos y qué formato usar.
- El agente lee este archivo antes de responder, así conserva siempre el contexto de tus proyectos y convenciones.[page:1]
- Regla clave: todo en Markdown (`.md`), el formato nativo de Obsidian y el más limpio para un LLM.[page:1]

## 4. Notas como base de datos viva
- Vuelca en la carpeta todo tu material de trabajo: research, notas de reuniones, decisiones, exportaciones de noticias, etc.[page:1]
- Desde el terminal, puedes preguntar cosas como: “¿Cuál es la actualización más reciente sobre X?” y el agente responde usando tus propios datos.[page:1]

## 5. El grafo que “piensa”
- Aprovecha las notas enlazadas de Obsidian como un grafo de ideas.[page:1]
- Activa la línea de comandos en los ajustes de Obsidian para que el agente tenga acceso directo a funciones internas.
- El agente puede seguir backlinks, leer notas relacionadas y sintetizar insights que sería difícil encontrar a mano.[page:1]

## 6. Kanban que se rellena solo
- Instala el plugin Kanban.
- Pega bloques de texto caóticos (mensajes de Telegram, transcripciones, listas de tareas) y pide al agente que los distribuya en el tablero.
- Para que funcione bien, define una plantilla estricta de tarjeta; con ella, todas las cards serán consistentes y usables.[page:1]

## 7. Nuevo flujo de trabajo
- Dejas de abrir apps, crear archivos manualmente o navegar carpetas.
- Solo hablas con el terminal: “Crea ideas y guárdalas como nueva nota”, “Resume lo que escribí sobre X el mes pasado”, “Convierte este hilo en un proyecto”.[page:1]
- El agente genera, guarda el `.md` en el lugar correcto y lo abre en Obsidian automáticamente.[page:1]

## 8. Tres errores que rompen el sistema
- No tener `AGENTS.md`: el agente siempre empieza desde cero y recreas el contexto en cada sesión.[page:1]
- Usar formatos no Markdown (PDF, .docx, etc.) como estándar: funcionan, pero son más lentos y ruidosos; lo ideal es un solo formato (`.md`).[page:1]
- Separar carpetas del agente y de las notas: terminas con dos sistemas desconectados que “intentan” colaborar.[page:1]

## 9. Mensaje final
- Tus notas ya existen y tu agente también; solo faltaba la carpeta compartida.
- Montar el sistema lleva unos 20 minutos, pero el apalancamiento que genera dura años.[page:1]
