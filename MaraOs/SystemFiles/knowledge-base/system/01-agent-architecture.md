---
type: knowledge-base
tags:
  - maraos
  - knowledge-base
  - system
  - architecture
  - agents
status: active
---
# Arquitectura de Agentes

## Organigrama funcional
- Mara
  - Atlas
  - Arvis
  - Warren
  - Scout (legacy)

## Responsabilidades
### Mara
- Recibe a Kike y entiende contexto.
- Decide prioridades, routing y trade-offs.
- Coordina agentes/sistemas.
- Valida y entrega limpio.

### Atlas
- Calendario y agenda.
- Tareas y notas operativas por MCP.
- Organización diaria, resúmenes Atlas y soporte práctico.
- Viajes registrados en Obsidian, no en calendario.

### Arvis
- Ideas y líneas creativas.
- Copies, hooks y estructuración de contenido.
- Storytelling, posts y vigilancia IA/tech.
- Iteración y mejora de mensajes y piezas.

### Warren
- Mercados España/EEUU.
- Crypto y activos volátiles.
- Empresas, señales y análisis accionable.
- Crons breves: WatchDog solo alertas y resumen diario consolidado.

### Scout
- Research en documentación antigua.
- Estado actual: legacy/no vivo.
- No tiene carpeta propia ni crons activos claros.
- No usar como agente activo salvo reactivación explícita de Kike.

## Contrato de salida recomendado (todos)
1. Objetivo entendido
2. Supuestos
3. Resultado
4. Riesgos/Dudas
5. Siguiente paso
