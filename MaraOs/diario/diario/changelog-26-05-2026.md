#mara-os #diario #changelog

# Changelog diario - 26-05-2026

Actualizado: 2026-05-26 20:00 Europe/Madrid

## Resumen
Actualizacion automatica del changelog diario de Mara en Obsidian. Se revisaron el diario del dia, el resumen Atlas, el resumen Warren, los analisis Warren generados, archivos del vault modificados durante el 26-05-2026, la ultima captura operativa local y el estado Git.

## Cambios principales detectados
- Diario del dia creado en `MaraOs/diario/diario/diario-26-05-2026.md`.
  - Contiene cabecera, tags y enlace al resumen Atlas.
  - No hay entradas manuales adicionales registradas en el diario del dia.
- Atlas:
  - Resumen diario generado en `MaraOs/diario/diario/resumen-atlas-26-05-2026.md`.
  - Calendario MCP consultado correctamente en la captura de las 07:00 CEST.
  - Tareas MCP consultado correctamente en la captura de las 07:00 CEST.
  - Eventos de hoy:
    - 16:00-17:00: `¡Resuelve tus dudas!`.
    - 19:00-20:00: `Explorando Gemini Omni`.
  - Proximos eventos detectados:
    - 27-05-2026 19:00-20:00: `Construye tu MVP en menos de una hora`.
    - 28-05-2026 16:30-17:30: `¡Resuelve tus dudas!`.
  - Tareas con vencimiento hoy:
    - `Hooks Telegram`.
    - `Pruebas Origen`.
    - `Dashboard SIEM mejorar el sidebar`.
    - `Pruebas Okre`.
  - Proxima tarea visible:
    - 27-05-2026: `Imagen Linkedin Publicación Instagram`.
- Warren:
  - Resumen diario generado en `MaraOs/diario/warren/resumen-warren-26-05-2026.md`.
  - Bloques generados en `MaraOs/Warren/analisis-diario/26-05-2026/`:
    - `01-espana.md`.
    - `02-crypto.md`.
    - `03-eeuu-crypto.md`.
  - España: IBEX en zona 18.350-18.400 tras rally fuerte, con banca como motor y soporte tactico en 18.200-18.220.
  - Crypto: BTC cerca de 76,7k-77,3k y ETH alrededor de 2.114-2.120; sentimiento mejora a 34 / Fear, pero BTC sigue sin recuperar 78k-80k.
  - EEUU + Crypto: Wall Street reabre tras Memorial Day con tono inicial positivo; lectura tomada cerca de apertura y pendiente de confirmacion de sesion.
- Estado operativo Ubuntu/OpenClaw registrado en `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`:
  - Captura de las 18:32 Europe/Madrid.
  - CPU 3,1%, memoria 8,3%, carga `0.97, 0.67, 0.53`, raiz 5%, vault 5%.
  - OpenClaw y Gateway aparecen activos.
  - Docker disponible; `dockge` aparece parado: `Exited (0) 3 days ago`, estado `unhealthy`.
  - Red local: `192.168.1.76`; Tailscale: `100.124.173.115`; IP publica: `88.27.13.225`.
  - Actualizaciones pendientes: 9; actualizaciones de seguridad: 0; reinicio requerido: no.

## Archivos revisados o relacionados
- `MaraOs/diario/diario/diario-26-05-2026.md`
- `MaraOs/diario/diario/resumen-atlas-26-05-2026.md`
- `MaraOs/diario/warren/resumen-warren-26-05-2026.md`
- `MaraOs/Warren/analisis-diario/26-05-2026/01-espana.md`
- `MaraOs/Warren/analisis-diario/26-05-2026/02-crypto.md`
- `MaraOs/Warren/analisis-diario/26-05-2026/03-eeuu-crypto.md`
- `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
- `MaraOs/diario/diario/changelog-26-05-2026.md`

## Estado Git observado
- No se observaron commits en `MaraOs` durante el 26-05-2026 mediante `git log --since='2026-05-26 00:00' -- MaraOs`.
- Antes de esta actualizacion, `git status --short` mostraba cambios pendientes y archivos sin seguimiento, incluyendo:
  - `M MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
  - `M MaraOs/diario/warren/resumen-warren-21-05-2026.md`
  - `?? MaraOs/Warren/analisis-diario/22-05-2026/`
  - `?? MaraOs/Warren/analisis-diario/25-05-2026/`
  - `?? MaraOs/Warren/analisis-diario/26-05-2026/`
  - `?? MaraOs/diario/diario/changelog-21-05-2026.md`
  - `?? MaraOs/diario/diario/changelog-22-05-2026.md`
  - `?? MaraOs/diario/diario/changelog-23-05-2026.md`
  - `?? MaraOs/diario/diario/changelog-24-05-2026.md`
  - `?? MaraOs/diario/diario/changelog-25-05-2026.md`
  - `?? MaraOs/diario/diario/diario-22-05-2026.md`
  - `?? MaraOs/diario/diario/diario-24-05-2026.md`
  - `?? MaraOs/diario/diario/diario-25-05-2026.md`
  - `?? MaraOs/diario/diario/diario-26-05-2026.md`
  - `?? MaraOs/diario/diario/resumen-atlas-22-05-2026.md`
  - `?? MaraOs/diario/diario/resumen-atlas-24-05-2026.md`
  - `?? MaraOs/diario/diario/resumen-atlas-25-05-2026.md`
  - `?? MaraOs/diario/diario/resumen-atlas-26-05-2026.md`
  - `?? MaraOs/diario/diario/resumen-semanal-24-05-2026.md`
  - `?? MaraOs/diario/warren/resumen-warren-22-05-2026.md`
  - `?? MaraOs/diario/warren/resumen-warren-25-05-2026.md`
  - `?? MaraOs/diario/warren/resumen-warren-26-05-2026.md`
- Esta ejecucion añade:
  - `MaraOs/diario/diario/changelog-26-05-2026.md`

## Incidencias / limites de datos
- No se hizo una nueva consulta directa al MCP de calendario o tareas en esta ejecucion; el estado de agenda/tareas procede del resumen Atlas de las 07:00.
- El diario manual del dia no contiene decisiones, notas o actividad posterior al resumen Atlas.
- Warren marco limitaciones de datos en EEUU: indices intradia disponibles, pero acciones/ETFs individuales quedaron como ultimo cierre confirmado del 22-05-2026 en la fuente usada.
- `dockge` sigue parado y marcado como `unhealthy` en la ultima captura operativa; no se ha intervenido sobre Docker ni servicios en esta automatizacion.
- Hay 9 actualizaciones pendientes segun la ultima captura; no se aplicaron cambios de sistema.
- Hay cambios y archivos sin commitear en el vault; esta automatizacion no hizo commit ni push.

## Proximos pasos
- Revisar/cerrar las cuatro tareas con vencimiento 26-05-2026 si ya se completaron fuera de las notas automaticas.
- Confirmar si `dockge` debe seguir parado o conviene levantarlo/revisarlo.
- Consolidar en Git los archivos pendientes cuando proceda y no haya conflictos.
