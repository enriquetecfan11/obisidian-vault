#mara-os #diario #changelog

# Changelog diario — 13-05-2026

Actualizado: 2026-05-13 20:00 Europe/Madrid

## Resumen
Actualización automática del changelog diario de Mara en Obsidian. Se revisaron el diario del día, resumen Atlas, registro semanal de viajes, análisis Warren, estado operativo local, cambios recientes del vault y estado Git.

## Cambios principales detectados
- Diario del día creado/actualizado en `MaraOs/diario/diario/diario-13-05-2026.md`:
  - Kike fijó una regla operativa estable: tareas y calendario se gestionan siempre mediante MCP.
  - Tareas: usar `agents-notes`; eventos: usar el MCP de calendario configurado (`calendar-mara` cuando esté disponible).
  - No usar calendarios locales, `.ics`, cron, Obsidian ni listas paralelas salvo petición explícita.
- Regla operativa replicada en `MaraOs/SystemFiles/TOOLS.md` según commit del día:
  - Se reforzó que tareas y calendario van por MCP y no por sistemas paralelos.
- Resumen Atlas generado en `MaraOs/diario/diario/resumen-atlas-13-05-2026.md`:
  - Agenda de hoy: Reunión Telemáticos 11:30–13:00, mentorías 13:00–14:00 y consultoría con Carlos Adams 19:00–20:00.
  - Tareas relevantes: Mirar Api Wazuh, Subir Okre, Correo Okre y Crear post intagram.
  - Próximos eventos: reunión gimnasio, mentoría y Post LinkedIn del 14-05-2026.
  - Próximas tareas: Post LinkedIn, escribir a David sobre nginx del docker, subir docker wireguard dashboard y viene Iberdrola.
  - Integraciones MCP de calendario y agents-notes disponibles y respondiendo correctamente según el resumen.
  - Memory search interno no disponible en esa ejecución (`database is not open`); no se usó para inferir agenda ni tareas.
- Resumen semanal de viajes actualizado en `MaraOs/diario/viajes/resumen-semanal-17-05-2026.md`:
  - Semana 11-05-2026 a 17-05-2026.
  - 5 viajes registrados.
  - 225 km totales.
  - 3 h 24 min conduciendo.
  - Viajes del día: 07:17 y 17:36, ambos de 41 min y 45 km.
- Warren generó análisis diarios del 13-05-2026:
  - `MaraOs/Warren/analisis-diario/13-05-2026/01-espana.md`: Ibex débil tras cierre fiable del 12-05 en 17.573,60 (-1,56%); no se obtuvo intradía fiable a las 09:00 y se dejó constancia explícita. Repsol mostró mejor tono relativo, Santander pasó a filtro clave de riesgo e Iberdrola quedó vigilable en 19,4–19,5.
  - `MaraOs/Warren/analisis-diario/13-05-2026/02-crypto.md`: BTC cerca de $80,6k, ETH cerca de $2.301 y Fear & Greed 42/Fear; estabilización cautelosa sin ruptura confirmada.
  - `MaraOs/Warren/analisis-diario/13-05-2026/03-eeuu-crypto.md`: apertura USA lateral-mixta con liderazgo selectivo de IA/semis, presión macro por PPI/CPI y crypto defensiva con BTC testeando zona de $80k.
- Reorganización y generación de conocimiento en el vault:
  - Commits del día muestran reorganización de documentos hacia `Geek/`, incorporación de documentación DevOps/Checkmk/Wazuh y generación de artefactos Graphify en `Graphify/graphify-out/` y `Graphify/graphify-export-social-ai-geek-work/`.
  - También se incorporaron o movieron contenidos de IA, prompts, LinkedIn, Work y recursos técnicos dentro de Graphify según el commit `Reorganize Obsidian vault documents`.
- Estado operativo Ubuntu/OpenClaw registrado en `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`:
  - Captura de las 18:30 Europe/Madrid.
  - CPU 15,1%, memoria 13,6%, raíz 5%, vault 5%.
  - Sin actualizaciones pendientes según el JSON revisado.
  - Docker disponible; servicios principales en ejecución, incluidos grafana, prometheus, homer, redisinsight, n8n, nocodb, flowise, postgres, redis, qdrant, ngrok y dockge.
  - `openclaw_gateway` activo y `docker_service` en estado `active`.

## Archivos revisados o relacionados
- `MaraOs/diario/diario/diario-13-05-2026.md`
- `MaraOs/diario/diario/resumen-atlas-13-05-2026.md`
- `MaraOs/diario/viajes/resumen-semanal-17-05-2026.md`
- `MaraOs/Warren/analisis-diario/13-05-2026/01-espana.md`
- `MaraOs/Warren/analisis-diario/13-05-2026/02-crypto.md`
- `MaraOs/Warren/analisis-diario/13-05-2026/03-eeuu-crypto.md`
- `MaraOs/SystemFiles/TOOLS.md`
- `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
- `Graphify/graphify-out/GRAPH_REPORT.md`
- `Graphify/graphify-export-social-ai-geek-work/GRAPH_REPORT.md`
- `MaraOs/diario/diario/changelog-13-05-2026.md`

## Estado Git observado
- Commits observados durante el 13-05-2026:
  - `97d0c2a` — Fix task and calendar MCP rule.
  - `278c2db` — Register trip on 2026-05-13.
  - `935dc42` — Añadir análisis España 13-05-2026.
  - `59bf8f5` — new docs.
  - `9bee4a3` — Register trip on 2026-05-13 evening.
  - `0060790` — Reorganize Obsidian vault documents.
- Antes de esta actualización, `git status --short` mostraba solo:
  - `M MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
- Esta ejecución añade/actualiza:
  - `MaraOs/diario/diario/changelog-13-05-2026.md`

## Incidencias / límites de datos
- No se confirma finalización de tareas del día: el resumen Atlas lista tareas relevantes, pero no hay registro revisado que permita marcarlas como completadas.
- El diario del día solo contiene la regla fija de tareas/calendario por MCP; los viajes están registrados en el resumen semanal de viajes, no en el archivo diario principal.
- En Warren España no se obtuvo cotización intradía fiable a las 09:00; se usó último cierre verificado del 12-05-2026 y se dejó constancia.
- Memory search interno no estuvo disponible durante la generación del resumen Atlas (`database is not open`).
- El estado Docker se resume desde el JSON local revisado; no se auditaron logs internos de cada servicio.
- La reorganización Graphify se resume desde git/logs y rutas modificadas; no se revalidó el contenido completo de cada artefacto generado.

## Próximos pasos
- Si se completan tareas o aparecen nuevos registros durante la noche, añadirlos al diario del 13-05-2026 o actualizar este changelog.
- Consolidar en Git los archivos pendientes cuando proceda y no haya conflictos.
