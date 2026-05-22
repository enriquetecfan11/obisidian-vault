#mara-os #diario #changelog

# Changelog diario — 14-05-2026

Actualizado: 2026-05-14 20:00 Europe/Madrid

## Resumen
Actualización automática del changelog diario de Mara en Obsidian. Se revisaron el diario del día, resumen Atlas, análisis Warren, estado operativo local, cambios recientes del vault y estado Git.

## Cambios principales detectados
- Diario del día creado/actualizado en `MaraOs/diario/diario/diario-14-05-2026.md`:
  - 2 viajes registrados:
    - Llegada 07:45, salida estimada 07:04, 45 km, 41 min.
    - Llegada 18:45, salida estimada 18:04, 45 km, 41 min.
  - Gasolina registrada: 46,19 €, depósito entero, 1,61 €/l, aprox. 28,69 l.
- Resumen Atlas generado en `MaraOs/diario/diario/resumen-atlas-14-05-2026.md`:
  - Agenda de hoy: Reunión gimnasio 15:00–16:30, mentorías 16:30–17:30 y Post LinkedIn 17:00–17:15.
  - Tarea relevante del día: Post LinkedIn.
  - Próximas tareas: escribir a David sobre nginx/docker el 18-05, subir docker wireguard dashboard el 19-05 y viene Iberdrola el 21-05.
  - Alertas: solape parcial entre Post LinkedIn y mentoría, y ausencia de margen entre reunión gimnasio y mentoría.
  - Integraciones MCP de calendario y agents-notes disponibles y respondiendo correctamente según el resumen.
  - Memory search interno disponible; se usó solo para confirmar reglas operativas.
- Regla operativa actualizada en `MaraOs/SystemFiles/TOOLS.md` según commit del día:
  - Cuando Kike diga “añade el viaje”, “un viaje” o similar sin fecha, interpretarlo como para hoy por defecto.
  - No volver a pedir fecha salvo ambigüedad real o conflicto horario.
- Warren generó análisis diarios del 14-05-2026:
  - `MaraOs/Warren/analisis-diario/14-05-2026/01-espana.md`: rebote táctico del Ibex con último cierre fiable 17.654,90 (+0,46%) del 13-05; mejora incompleta mientras no recupere 17.850/18.000. Santander estabiliza, Iberdrola recupera 19,5 y Repsol mantiene mejor fuerza relativa aunque descansa. Se dejó claro que no hubo cotización intradía fiable a las 09:00 y no se inventó apertura.
  - `MaraOs/Warren/analisis-diario/14-05-2026/02-crypto.md`: deterioro táctico en crypto; BTC cerca de $79,3k, ETH cerca de $2.255-$2.257 y Fear & Greed 34/Fear. Mercado en modo defensa, con CLARITY Act, ETF flows y macro como catalizadores/riesgos.
  - `MaraOs/Warren/analisis-diario/14-05-2026/03-eeuu-crypto.md`: apertura USA positiva pero liderazgo mixto; SPY y DIA positivos, QQQ casi plano, NVDA liderando por catalizadores China/H200, ASML débil y crypto defensiva. Yahoo Finance devolvió 429/401 y VIX no tuvo dato actualizado fiable, por lo que se evitó inventar valores.
- Resumen Warren del 13-05-2026 creado en `MaraOs/diario/warren/resumen-warren-13-05-2026.md`:
  - Consolida España, Crypto y EEUU + Crypto del 13-05.
  - Lectura principal: corrección táctica y estabilización frágil, con selectividad máxima y no perseguir rebotes.
- Nuevos documentos técnicos incorporados al vault según commit `afabfae` (`New docs`):
  - Documentación DevOps/CheckMK en `Geek/Devops/CheckMK/`.
  - Documentación DevOps/Wazuh en `Geek/Devops/Wazuh/`.
  - Archivos auxiliares Graphify en `Graphify/` y `RECOMENDACIONES_GRAPHIFY.md`.
  - Cambio de apariencia de Obsidian en `.obsidian/appearance.json`.
- Estado operativo Ubuntu/OpenClaw registrado en `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`:
  - Captura de las 18:31 Europe/Madrid.
  - Estado general OK.
  - CPU 12,3%, memoria 13,6%, carga 1 min 0,55, raíz 5%, vault 5%.
  - Docker disponible con 13/13 contenedores en ejecución y sin incidencias críticas: dockge, flowise, flowise-db, grafana, homer, n8n, ngrok, nocodb, postgres, prometheus, qdrant, redis y redisinsight.

## Archivos revisados o relacionados
- `MaraOs/diario/diario/diario-14-05-2026.md`
- `MaraOs/diario/diario/resumen-atlas-14-05-2026.md`
- `MaraOs/diario/warren/resumen-warren-13-05-2026.md`
- `MaraOs/Warren/analisis-diario/14-05-2026/01-espana.md`
- `MaraOs/Warren/analisis-diario/14-05-2026/02-crypto.md`
- `MaraOs/Warren/analisis-diario/14-05-2026/03-eeuu-crypto.md`
- `MaraOs/SystemFiles/TOOLS.md`
- `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
- `Geek/Devops/CheckMK/`
- `Geek/Devops/Wazuh/`
- `Graphify/`
- `RECOMENDACIONES_GRAPHIFY.md`
- `MaraOs/diario/diario/changelog-14-05-2026.md`

## Estado Git observado
- Commits observados durante el 14-05-2026:
  - `a2ac5a5` — Merge branch `main` de `https://github.com/enriquetecfan11/obisidian-vault`.
  - `df20635` — Merge branch `main` de `https://github.com/enriquetecfan11/obisidian-vault`.
  - `679f451` — Document default date for travel entries.
  - `afabfae` — New docs.
  - `ab1b2cd` — Add Warren EEUU crypto analysis 2026-05-14.
- Antes de esta actualización, `git status --short` mostraba:
  - `M MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
  - `?? MaraOs/Warren/analisis-diario/14-05-2026/01-espana.md`
  - `?? MaraOs/Warren/analisis-diario/14-05-2026/02-crypto.md`
  - `?? MaraOs/diario/diario/diario-14-05-2026.md`
  - `?? MaraOs/diario/diario/resumen-atlas-14-05-2026.md`
  - `?? MaraOs/diario/warren/resumen-warren-13-05-2026.md`
- Esta ejecución añade/actualiza:
  - `MaraOs/diario/diario/changelog-14-05-2026.md`

## Incidencias / límites de datos
- No se confirma finalización de tareas del día: el resumen Atlas lista `Post LinkedIn`, pero no hay registro revisado que permita marcarlo como completado.
- No se detectaron eventos posteriores en la consulta actual del calendario MCP según el resumen Atlas.
- Warren España no obtuvo cotización intradía fiable a las 09:00; usó último cierre verificado del 13-05-2026 y lo dejó indicado.
- En Warren EEUU + Crypto, Yahoo Finance devolvió 429/401 y VIX no tuvo dato actualizado fiable; se evitaron valores no verificados.
- Los análisis España y Crypto del 14-05 aparecían sin trackear en Git al revisar el estado; el bloque EEUU + Crypto sí aparece en commit `ab1b2cd`.
- El estado Docker se resume desde el JSON local revisado; no se auditaron logs internos de cada servicio.

## Próximos pasos
- Si se completan tareas o aparecen nuevos registros durante la noche, añadirlos al diario del 14-05-2026 o actualizar este changelog.
- Consolidar en Git los archivos pendientes cuando proceda y no haya conflictos.
