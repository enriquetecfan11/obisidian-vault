#mara-os #diario #changelog

# Changelog diario - 27-05-2026

Actualizado: 2026-05-27 20:00 Europe/Madrid

## Resumen
Actualizacion automatica del changelog diario de Mara en Obsidian. Se revisaron el diario del dia, el resumen Atlas, los analisis Warren disponibles para el 27-05-2026, archivos del vault modificados durante el dia, la ultima captura operativa local y el estado Git.

## Cambios principales detectados
- Diario del dia creado en `MaraOs/diario/diario/diario-27-05-2026.md`.
  - Contiene cabecera, tags y enlace al resumen Atlas.
  - No hay entradas manuales adicionales registradas en el diario del dia.
- Atlas:
  - Resumen diario generado en `MaraOs/diario/diario/resumen-atlas-27-05-2026.md`.
  - Calendario MCP consultado correctamente en la captura de las 07:00 CEST.
  - Tareas MCP consultado correctamente en la captura de las 07:00 CEST.
  - Evento de hoy:
    - 19:00-20:00: `Construye tu MVP en menos de una hora`.
  - Proximos eventos detectados:
    - 28-05-2026 16:00-18:30: `Reunion Gimnasio`.
    - 28-05-2026 16:30-17:30: `¡Resuelve tus dudas!`.
    - 02-06-2026 16:00-17:00: `¡Resuelve tus dudas!`.
  - Tarea con vencimiento hoy:
    - `Imagen Linkedin Publicación Instagram`.
  - Tareas vencidas pendientes:
    - 26-05-2026: `Hooks Telegram`.
    - 26-05-2026: `Pruebas Origen`.
    - 26-05-2026: `Dashboard SIEM mejorar el sidebar`.
    - 26-05-2026: `Pruebas Okre`.
  - Alertas destacadas:
    - Hay cuatro tareas vencidas pendientes desde el 26-05-2026.
    - Mañana hay solape parcial entre `Reunion Gimnasio` y `¡Resuelve tus dudas!` de 16:30 a 17:30.
- Warren:
  - No se encontro `MaraOs/diario/warren/resumen-warren-27-05-2026.md` en esta ejecucion.
  - Se encontro un bloque generado en `MaraOs/Warren/analisis-diario/27-05-2026/`:
    - `01-espana.md`.
  - España: el IBEX 35 aparece en 18.290,9 puntos, -0,52%, tras no sostener la zona de 18.400.
  - Banca en rojo: Santander -1,60%, BBVA -0,75%, CaixaBank -1,11%, Bankinter -1,42% y Sabadell -1,21%.
  - Energia y defensivas amortiguan: Repsol +2,67%, Iberdrola +0,94%, Acciona +0,78%, Enagas +0,52% y Endesa +0,36%.
  - Naturgy es el evento corporativo local: CVC vende su 13,8% por 3.821,4 millones, a 28,55 euros por accion y con descuento del 4,6%.
  - Lectura Warren: mercado español constructivo mientras preserve 18.200-18.220, pero sin confirmacion de continuacion alcista.
- Estado operativo Ubuntu/OpenClaw registrado en `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`:
  - Captura de las 18:35 Europe/Madrid.
  - Estado `WARNING`.
  - CPU 12%, memoria 8%, carga `1.34,1.30,0.85`, raiz 5%, vault 5%.
  - Contenedores Docker: 0 en ejecucion de 1 total; `docker_problem_count`: 1.
  - Red local: `192.168.1.200`; interfaz `enp4s0`; gateway `192.168.1.1`; Tailscale: `100.124.173.115`.
  - IP publica no comprobada.
  - Actualizaciones pendientes: 0; actualizaciones de seguridad: 0; reinicio requerido: no.

## Archivos revisados o relacionados
- `MaraOs/diario/diario/diario-27-05-2026.md`
- `MaraOs/diario/diario/resumen-atlas-27-05-2026.md`
- `MaraOs/Warren/analisis-diario/27-05-2026/01-espana.md`
- `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
- `MaraOs/diario/diario/changelog-27-05-2026.md`

## Estado Git observado
- Se observo un commit en `MaraOs` durante el 27-05-2026:
  - `71b3d71 2026-05-27 08:08:39 +0200 test`
- El commit `71b3d71` incluye la consolidacion de diarios, changelogs, resumenes Atlas y analisis Warren de dias anteriores y del 27-05-2026.
- Antes de esta actualizacion, `git status --short` mostraba:
  - `M MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
  - `?? .mobiai/`
  - `?? MaraOs/Warren/analisis-diario/27-05-2026/`
- Esta ejecucion añade:
  - `MaraOs/diario/diario/changelog-27-05-2026.md`

## Incidencias / limites de datos
- No se hizo una nueva consulta directa al MCP de calendario o tareas en esta ejecucion; el estado de agenda/tareas procede del resumen Atlas de las 07:00.
- El diario manual del dia no contiene decisiones, notas o actividad posterior al resumen Atlas.
- No se encontro resumen Warren diario para el 27-05-2026; solo hay un analisis de España disponible.
- No se encontraron bloques Warren de crypto o EEUU + crypto para el 27-05-2026 en esta ejecucion.
- La ultima captura operativa marca `WARNING` por contenedor Docker parado o problematico; esta automatizacion no intervino sobre Docker ni servicios.
- Hay cambios y archivos sin seguimiento en el vault; esta automatizacion no hizo commit ni push.

## Proximos pasos
- Revisar/cerrar las cuatro tareas vencidas del 26-05-2026 si ya se resolvieron fuera de las notas automaticas.
- Revisar el solape del 28-05-2026 entre `Reunion Gimnasio` y `¡Resuelve tus dudas!`.
- Confirmar si falta generar el resumen Warren completo del 27-05-2026 o los bloques de crypto / EEUU + crypto.
- Decidir si conviene revisar el contenedor Docker parado o problematico reflejado en la captura operativa.
