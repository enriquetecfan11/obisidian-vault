---
 title: changelog-15-05-2026
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

# Changelog diario — 15-05-2026

Actualizado: 2026-05-15 20:00 Europe/Madrid

## Resumen
Actualización automática del changelog diario de Mara en Obsidian. Se revisaron el diario del día, resumen Atlas, análisis Warren, estado operativo local, cambios recientes del vault y estado Git.

## Cambios principales detectados
- Diario del día creado en `MaraOs/diario/diario/diario-15-05-2026.md`:
  - El archivo existe, pero no contiene entradas operativas más allá del título.
  - No hay datos suficientes en el diario para confirmar viajes, eventos completados, tareas completadas u otras acciones personales del día.
- Resumen Atlas generado en `MaraOs/diario/diario/resumen-atlas-15-05-2026.md`:
  - Calendario MCP disponible y consultado correctamente.
  - Tareas MCP disponible y consultado correctamente.
  - No hay eventos confirmados para hoy en los datos devueltos por calendario.
  - Tarea vencida detectada: `Post LinkedIn`, con vencimiento 14-05-2026.
  - Próximas tareas: escribir a David sobre quitar nginx del Docker el 18-05, subir docker wireguard dashboard el 19-05 y viene Iberdrola el 21-05.
  - Prioridad sugerida: resolver o replanificar `Post LinkedIn`.
- Warren generó análisis diarios del 15-05-2026:
  - `MaraOs/Warren/analisis-diario/15-05-2026/01-espana.md`: mejora táctica del Ibex hasta 17.809,20 (+0,87%) el 14-05, cerca de la resistencia 17.850. Santander no acompañó, Repsol corrigió tras fortaleza previa e Iberdrola se mantuvo defensiva. Se dejó claro que no hubo foto intradía completa y fiable a las 09:00 del 15-05.
  - `MaraOs/Warren/analisis-diario/15-05-2026/02-crypto.md`: rebote cauteloso en crypto, BTC recuperando zona $80k-$81k, ETH más débil cerca de $2,26k y Fear & Greed en 43/Fear. El CLARITY Act aparece como catalizador regulatorio, pero sin confirmación de ruptura.
  - `MaraOs/Warren/analisis-diario/15-05-2026/03-eeuu-crypto.md`: apertura USA negativa, con presión en tecnología/growth por subida de yields largos. SPY, QQQ y DIA abrieron en rojo; NVDA, AMZN y ASML débiles; BTC sostuvo aproximadamente $80k y ETH siguió rezagado. Se registraron limitaciones de fuentes por bloqueos/bot-detection y no se inventaron datos macro no verificados.
- Resumen Warren del 14-05-2026 disponible en `MaraOs/diario/warren/resumen-warren-14-05-2026.md`:
  - Consolida España, Crypto y EEUU + Crypto del 14-05.
  - Lectura principal: rebote incompleto en España, fortaleza selectiva en EEUU y deterioro táctico en crypto.
  - Recomendación Warren: prudencia, selectividad, no perseguir rebotes sin confirmación y priorizar margen de seguridad.
- Estado operativo Ubuntu/OpenClaw registrado en `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`:
  - Captura de las 18:30 Europe/Madrid.
  - Estado general OK.
  - CPU 0,6%, memoria 12,4%, carga 1 min 0,77, raíz 4,1%, vault 4,1%.
  - Docker disponible con 13/13 contenedores en ejecución y sin incidencias críticas: dockge, flowise, flowise-db, grafana, homer, n8n, ngrok, nocodb, postgres, prometheus, qdrant, redis y redisinsight.
  - Hay 1 actualización pendiente del sistema según el JSON local.

## Archivos revisados o relacionados
- `MaraOs/diario/diario/diario-15-05-2026.md`
- `MaraOs/diario/diario/resumen-atlas-15-05-2026.md`
- `MaraOs/diario/warren/resumen-warren-14-05-2026.md`
- `MaraOs/Warren/analisis-diario/15-05-2026/01-espana.md`
- `MaraOs/Warren/analisis-diario/15-05-2026/02-crypto.md`
- `MaraOs/Warren/analisis-diario/15-05-2026/03-eeuu-crypto.md`
- `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
- `MaraOs/diario/diario/changelog-15-05-2026.md`

## Estado Git observado
- Commits observados durante el 15-05-2026:
  - `454a697` — Add Atlas daily summary for 2026-05-15.
  - `8ab760b` — Add Warren crypto analysis 2026-05-15.
- Antes de esta actualización, `git status --short` mostraba:
  - `M MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
  - `?? MaraOs/Warren/analisis-diario/14-05-2026/01-espana.md`
  - `?? MaraOs/Warren/analisis-diario/14-05-2026/02-crypto.md`
  - `?? MaraOs/Warren/analisis-diario/15-05-2026/01-espana.md`
  - `?? MaraOs/Warren/analisis-diario/15-05-2026/03-eeuu-crypto.md`
  - `?? MaraOs/diario/diario/changelog-14-05-2026.md`
  - `?? MaraOs/diario/diario/diario-14-05-2026.md`
  - `?? MaraOs/diario/diario/diario-15-05-2026.md`
  - `?? MaraOs/diario/diario/resumen-atlas-14-05-2026.md`
  - `?? MaraOs/diario/warren/resumen-warren-13-05-2026.md`
  - `?? MaraOs/diario/warren/resumen-warren-14-05-2026.md`
- Esta ejecución añade/actualiza:
  - `MaraOs/diario/diario/changelog-15-05-2026.md`

## Incidencias / límites de datos
- El diario del 15-05-2026 está prácticamente vacío; no se han inferido viajes, acciones personales ni completados no registrados.
- No se confirma finalización o replanificación de `Post LinkedIn`; solo consta como tarea vencida en el resumen Atlas.
- El bloque España de Warren no obtuvo foto intradía completa y fiable a las 09:00; usa últimos datos estructurados verificados y marca las lagunas.
- El bloque Crypto no incorporó cifras nuevas de flujos ETF por falta de fuente pública fiable en la ejecución.
- El bloque EEUU + Crypto encontró bloqueos/bot-detection en Reuters, Investing.com y búsquedas web; se evitaron datos macro no verificados.
- El estado Docker se resume desde el JSON local revisado; no se auditaron logs internos de cada servicio.

## Próximos pasos
- Si aparecen entradas personales, viajes o tareas completadas durante la noche, actualizar el diario del 15-05-2026 y este changelog.
- Consolidar en Git los archivos pendientes cuando proceda y no haya conflictos.
