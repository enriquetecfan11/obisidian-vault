#mara-os #diario #changelog

# Changelog diario - 29-05-2026

Actualizado: 2026-05-29 20:00 Europe/Madrid

## Resumen
Actualizacion automatica del changelog diario de Mara en Obsidian. Se revisaron el diario del dia, el resumen Atlas, los analisis Warren disponibles para el 29-05-2026, archivos del vault modificados durante el dia, la ultima captura operativa local y el estado Git.

## Cambios principales detectados
- Diario del dia creado en `MaraOs/diario/diario/diario-29-05-2026.md`.
  - Contiene cabecera, tags y enlace al resumen Atlas.
  - No hay entradas manuales adicionales registradas en el diario del dia.
- Atlas:
  - Resumen diario generado en `MaraOs/diario/diario/resumen-atlas-29-05-2026.md`.
  - Calendario MCP no disponible en la ejecucion de las 07:00 CEST por fallo DNS contra `core-n8n.832gky.easypanel.host`.
  - Tareas MCP no disponible en la ejecucion de las 07:00 CEST por el mismo fallo DNS.
  - No hay eventos ni tareas verificados para hoy desde Atlas porque las integraciones no estuvieron accesibles.
  - Posibles arrastres no verificados desde el ultimo resumen correcto del 28-05-2026:
    - `Hooks Telegram`.
    - `Dashboard SIEM mejorar el sidebar`.
    - `Imagen Linkedin Publicacion Instagram`.
  - Prioridad sugerida por Atlas: recuperar conectividad con los MCPs de calendario y tareas antes de asumir huecos libres o ausencia de vencimientos.
- Warren:
  - Se encontro bloque completo de analisis diario en `MaraOs/Warren/analisis-diario/29-05-2026/`:
    - `01-espana.md`.
    - `02-crypto.md`.
    - `03-eeuu-crypto.md`.
  - España: IBEX 35 en 18.279,3 puntos, -0,55%, con fallo de continuidad por debajo de 18.300 tras acercarse a maximos.
  - España mantiene estructura de fondo fuerte, pero queda en modo digestion mientras no recupere 18.300-18.377 con banca acompanando.
  - Crypto: BTC cerca de 73.530 USD y ETH alrededor de 2.008,79 USD en el bloque de mediodia; sentimiento en `Extreme Fear` 23.
  - Crypto mejora tacticamente, pero BTC sigue bajo la zona 74k-76k y ETH necesita sostener 2.000-2.030 para confirmar reparacion.
  - EEUU + Crypto: apertura positiva en Wall Street con liderazgo Nasdaq/growth; SPY +0,55%, QQQ +0,83% y DIA +0,04% en la foto usada por Warren.
  - Tecnologia/IA mejora con AMD +4,56%, MSFT +3,48%, AVGO +1,11% y NVDA +0,79%.
  - Macro EEUU sigue como freno: PCE headline +0,4% mensual y +3,8% interanual; core PCE +0,2% mensual y +3,3% interanual.
  - En el bloque EEUU + Crypto, BTC vuelve bajo 73k y ETH bajo 2.000, por lo que Warren no trata el dia como risk-on amplio y limpio.
- Estado operativo Ubuntu/OpenClaw registrado en `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`:
  - Captura de las 18:31 Europe/Madrid.
  - Estado `WARNING`.
  - CPU 21,7%, memoria 8,9%, carga 1,67, raiz 5%, vault 5%.
  - Contenedor registrado: `dockge`.
  - `problem_containers`: `dockge`.
  - Red local: `192.168.1.200`; interfaz `enp4s0`; gateway `192.168.1.1`; Tailscale: `100.124.173.115`.
  - IP publica no comprobada.

## Archivos revisados o relacionados
- `MaraOs/diario/diario/diario-29-05-2026.md`
- `MaraOs/diario/diario/resumen-atlas-29-05-2026.md`
- `MaraOs/Warren/analisis-diario/29-05-2026/01-espana.md`
- `MaraOs/Warren/analisis-diario/29-05-2026/02-crypto.md`
- `MaraOs/Warren/analisis-diario/29-05-2026/03-eeuu-crypto.md`
- `MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
- `MaraOs/diario/diario/changelog-29-05-2026.md`

## Estado Git observado
- Se observaron commits en `MaraOs` durante el 29-05-2026:
  - `f1d46e2 2026-05-29 09:02:56 +0200 Add Warren Spain analysis 2026-05-29`
  - `8632d5b 2026-05-29 13:33:29 +0200 Add Warren crypto analysis for 2026-05-29`
  - `0ff2360 2026-05-29 15:33:29 +0200 Añade análisis EEUU crypto 29-05-2026`
- Antes de esta actualizacion, `git status --short` mostraba:
  - `M MaraOs/SystemFiles/ops/ubuntu-hourly-last.json`
  - `?? .mobiai/`
  - `?? MaraOs/diario/diario/changelog-27-05-2026.md`
  - `?? MaraOs/diario/diario/diario-28-05-2026.md`
  - `?? MaraOs/diario/diario/diario-29-05-2026.md`
  - `?? MaraOs/diario/diario/resumen-atlas-29-05-2026.md`
- Esta ejecucion añade:
  - `MaraOs/diario/diario/changelog-29-05-2026.md`

## Incidencias / limites de datos
- No se hizo una nueva consulta directa al MCP de calendario o tareas en esta ejecucion; el estado de agenda/tareas procede del resumen Atlas de las 07:00.
- Atlas indica que calendario y tareas no estaban verificados por fallo DNS, asi que no se debe asumir que no haya eventos o vencimientos.
- El diario manual del dia no contiene decisiones, notas o actividad posterior al resumen Atlas.
- No se encontro `MaraOs/diario/warren/resumen-warren-29-05-2026.md`; los datos Warren proceden de los tres bloques en `MaraOs/Warren/analisis-diario/29-05-2026/`.
- El bloque EEUU + Crypto indica fallos DNS locales contra varios endpoints de mercado; algunas cifras proceden del feed financiero disponible y otras de fuentes macro primarias.
- La ultima captura operativa marca `WARNING` por `dockge` en `problem_containers`; esta automatizacion no intervino sobre Docker ni servicios.
- Hay cambios y archivos sin seguimiento en el vault; esta automatizacion no hizo commit ni push.

## Proximos pasos
- Recuperar o verificar conectividad de los MCPs de calendario y `agents-notes`.
- Revisar si siguen vivos los posibles arrastres `Hooks Telegram`, `Dashboard SIEM mejorar el sidebar` e `Imagen Linkedin Publicacion Instagram`.
- Revisar el estado del contenedor `dockge` si el aviso operativo persiste.
- Decidir si conviene generar un resumen Warren diario consolidado para el 29-05-2026 a partir de los tres bloques disponibles.
