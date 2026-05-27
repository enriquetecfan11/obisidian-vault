#mara-os #diario #changelog

# Changelog diario — 25-05-2026

Actualizado: 2026-05-25 20:00 Europe/Madrid

## Resumen
Actualización automática del changelog diario de Mara en Obsidian. Se revisaron el diario del día, el resumen Atlas, el resumen Warren, los análisis Warren generados, archivos del vault modificados durante el 25-05-2026, la última captura operativa local y el estado Git.

## Cambios principales detectados
- Diario del día creado en `MaraOs/diario/diario/diario-25-05-2026.md`.
  - Contiene cabecera, tags y enlace al resumen Atlas.
  - No hay entradas manuales adicionales registradas en el diario del día.
- Atlas:
  - Resumen diario generado en `MaraOs/diario/diario/resumen-atlas-25-05-2026.md`.
  - Calendario MCP consultado correctamente en la captura de las 07:00 CEST.
  - Tareas MCP consultado correctamente en la captura de las 07:00 CEST.
  - No aparecen eventos de calendario para hoy, lunes 25-05-2026, en el listado devuelto.
  - Tareas con vencimiento hoy:
    - `Hooks Telegram`.
    - `Terminar entrenamiento origen`.
    - `Pruebas Origen`.
    - `Dashboard SIEM mejorar el sidebar`.
  - Tarea vencida pendiente desde el 24-05-2026:
    - `Imagen publicacion Linkedin y publicación de Instagram`.
  - Próximas tareas visibles:
    - 26-05-2026: `Pruebas Okre`.
    - 27-05-2026: `Imagen Linkedin Publicación Instagram`.
- Warren:
  - Resumen diario generado en `MaraOs/diario/warren/resumen-warren-25-05-2026.md`.
  - Bloques generados en `MaraOs/Warren/analisis-diario/25-05-2026/`:
    - `01-espana.md`.
    - `02-crypto.md`.
    - `03-eeuu-crypto.md`.
  - España: IBEX cerca de 18.000, sesión condicionada por Wall Street cerrado y divergencia entre futuros europeos alcistas y contado plano.
  - Crypto: BTC cerca de $77,3k y ETH alrededor de $2,113-$2,116; estabilización defensiva con Fear & Greed en 30 / Fear y flujos ETF spot todavía débiles.
  - EEUU + Crypto: NYSE y Nasdaq cerrados por Memorial Day; la lectura de acciones usa el cierre del viernes 22-05-2026 y deja la reapertura del 26-05-2026 como señal principal.
- Estado operativo Ubuntu/OpenClaw registrado en `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`:
  - Captura de las 18:33 Europe/Madrid.
  - CPU 16,7%, memoria 8,1%, carga `0.80, 0.67, 0.58`, raíz 5%, vault 5%.
  - OpenClaw y Gateway aparecen activos como procesos.
  - Docker disponible; `dockge` aparece parado: `Exited (0) 2 days ago`, estado `unhealthy`.
  - Red local: `192.168.1.76`; Tailscale: `100.124.173.115`; IP pública: `88.27.13.225`.
  - Actualizaciones pendientes: 9; actualizaciones de seguridad: 0; reinicio requerido: no.

## Archivos revisados o relacionados
- `MaraOs/diario/diario/diario-25-05-2026.md`
- `MaraOs/diario/diario/resumen-atlas-25-05-2026.md`
- `MaraOs/diario/warren/resumen-warren-25-05-2026.md`
- `MaraOs/Warren/analisis-diario/25-05-2026/01-espana.md`
- `MaraOs/Warren/analisis-diario/25-05-2026/02-crypto.md`
- `MaraOs/Warren/analisis-diario/25-05-2026/03-eeuu-crypto.md`
- `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
- `MaraOs/diario/diario/changelog-25-05-2026.md`

## Estado Git observado
- No se observaron commits en `MaraOs` durante el 25-05-2026 mediante `git log --since='2026-05-25 00:00' -- MaraOs`.
- Antes de esta actualización, `git status --short` mostraba cambios pendientes y archivos sin seguimiento, incluyendo:
  - `M MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
  - `M MaraOs/diario/warren/resumen-warren-21-05-2026.md`
  - `?? MaraOs/Warren/analisis-diario/22-05-2026/`
  - `?? MaraOs/Warren/analisis-diario/25-05-2026/`
  - `?? MaraOs/diario/diario/changelog-21-05-2026.md`
  - `?? MaraOs/diario/diario/changelog-22-05-2026.md`
  - `?? MaraOs/diario/diario/changelog-23-05-2026.md`
  - `?? MaraOs/diario/diario/changelog-24-05-2026.md`
  - `?? MaraOs/diario/diario/diario-22-05-2026.md`
  - `?? MaraOs/diario/diario/diario-24-05-2026.md`
  - `?? MaraOs/diario/diario/diario-25-05-2026.md`
  - `?? MaraOs/diario/diario/resumen-atlas-22-05-2026.md`
  - `?? MaraOs/diario/diario/resumen-atlas-24-05-2026.md`
  - `?? MaraOs/diario/diario/resumen-atlas-25-05-2026.md`
  - `?? MaraOs/diario/diario/resumen-semanal-24-05-2026.md`
  - `?? MaraOs/diario/warren/resumen-warren-22-05-2026.md`
  - `?? MaraOs/diario/warren/resumen-warren-25-05-2026.md`
- Esta ejecución añade:
  - `MaraOs/diario/diario/changelog-25-05-2026.md`

## Incidencias / límites de datos
- No se hizo una nueva consulta directa al MCP de calendario o tareas en esta ejecución; el estado de agenda/tareas procede del resumen Atlas de las 07:00.
- El diario manual del día no contiene decisiones, notas o actividad posterior al resumen Atlas.
- Warren tiene análisis del día generados, pero EEUU cash market estuvo cerrado por Memorial Day; las referencias de acciones no son intradía del 25-05-2026.
- `dockge` sigue parado y marcado como `unhealthy` en la última captura operativa; no se ha intervenido sobre Docker ni servicios en esta automatización.
- Hay 9 actualizaciones pendientes según la última captura; no se aplicaron cambios de sistema.
- Hay cambios y archivos sin commitear en el vault; esta automatización no hizo commit ni push.

## Próximos pasos
- Priorizar o cerrar las tareas con vencimiento 25-05-2026 si ya se completaron fuera de las notas automáticas.
- Decidir qué hacer con la tarea vencida de LinkedIn/Instagram del 24-05-2026.
- Revisar si `dockge` debe estar activo.
- Consolidar en Git los archivos pendientes cuando proceda y no haya conflictos.
