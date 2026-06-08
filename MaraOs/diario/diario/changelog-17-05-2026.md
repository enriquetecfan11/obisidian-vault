---
 title: changelog-17-05-2026
 type: diario
 tags:
  - "#diario"
 status: active
 created: 2026-06-08
 updated: 2026-06-08
 source:
 related: []
---
---

#mara-os #diario #changelog

# Changelog diario — 17-05-2026

Actualizado: 2026-05-17 20:00 Europe/Madrid

## Resumen
Actualización automática del changelog diario de Mara en Obsidian. Se revisaron el diario del día, resumen Atlas, resumen semanal de viajes, cambios recientes del vault, estado operativo local y estado Git.

## Cambios principales detectados
- Diario del día creado en `MaraOs/diario/diario/diario-17-05-2026.md`:
  - Registro de viaje a las 13:00: llegada tras 52 min y 62 km recorridos.
  - Salida estimada registrada: 12:08.
- Resumen semanal de viajes actualizado en `MaraOs/diario/viajes/resumen-semanal-17-05-2026.md`:
  - Añadido el viaje del domingo 17-05-2026.
  - Métricas de la semana: 6 viajes, 287 km, 4 h 16 min conduciendo y media de 47,8 km por viaje.
- Resumen Atlas generado en `MaraOs/diario/diario/resumen-atlas-17-05-2026.md`:
  - Calendario MCP disponible y consultado correctamente.
  - Tareas MCP disponible y consultado correctamente.
  - Evento de hoy: `Toros Las Ventas` de 19:00 a 21:00.
  - Tarea relevante de hoy: `Corrida de Toros (Las Ventas)` con vencimiento 17-05-2026.
  - Próximas tareas visibles: `Cumple Isa` y escribir a David sobre quitar nginx del Docker el 18-05, subir docker wireguard dashboard el 19-05 y `Viene Iberdrola` el 21-05.
  - No aparecen tareas vencidas anteriores a hoy en los datos devueltos por `agents-notes`.
- Documento operativo del sistema actualizado en `MaraOs/SystemFiles/TOOLS.md`:
  - Commit del día `6e915a0` registra el cambio junto al viaje del 17 de mayo.
- Estado operativo Ubuntu/OpenClaw registrado en `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`:
  - Captura de las 18:31 Europe/Madrid.
  - CPU 16,6%, memoria 12,7%, carga 1 min 0,61, raíz 4,1%, vault 4,1%.
  - Docker disponible con 13/13 contenedores en ejecución y sin anomalías críticas visibles: grafana, prometheus, homer, redisinsight, n8n, nocodb, flowise, postgres, redis, flowise-db, qdrant, ngrok y dockge.
  - Hay 2 actualizaciones pendientes del sistema según el JSON local.
- Warren:
  - No se encontraron análisis diarios de Warren para `17-05-2026` en las rutas revisadas durante esta ejecución.

## Archivos revisados o relacionados
- `MaraOs/diario/diario/diario-17-05-2026.md`
- `MaraOs/diario/diario/resumen-atlas-17-05-2026.md`
- `MaraOs/diario/viajes/resumen-semanal-17-05-2026.md`
- `MaraOs/SystemFiles/TOOLS.md`
- `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
- `MaraOs/diario/diario/changelog-17-05-2026.md`

## Estado Git observado
- Commits observados durante el 17-05-2026:
  - `cc0ee75` — `Add Atlas daily summary 2026-05-17`.
  - `6e915a0` — `Registrar viaje del 17 de mayo`.
- Antes de esta actualización, `git status --short` mostraba cambios pendientes no consolidados, incluyendo:
  - `M MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
  - análisis Warren de 14-05 y 15-05 sin seguimiento,
  - changelogs/diarios/resúmenes Atlas recientes de 14-05 a 16-05 sin seguimiento,
  - resúmenes Warren recientes sin seguimiento.
- Esta ejecución añade:
  - `MaraOs/diario/diario/changelog-17-05-2026.md`

## Incidencias / límites de datos
- No se hizo una nueva consulta directa al MCP de calendario o tareas en esta ejecución; el estado de calendario/tareas procede del resumen Atlas generado a las 07:00.
- No se confirma desde estas notas si el evento `Toros Las Ventas` o la tarea asociada fueron completados; solo consta que estaban programados para hoy.
- No hay análisis Warren del 17-05-2026 disponibles en la ruta revisada; se deja constancia sin inventar contenido.
- El estado Docker se resume desde el JSON local revisado; no se auditaron logs internos de cada servicio.

## Próximos pasos
- Si aparecen entradas personales, viajes adicionales o tareas completadas durante la noche, actualizar el diario del 17-05-2026 y este changelog.
- Consolidar en Git los archivos pendientes cuando proceda y no haya conflictos.
