#mara-os #diario

# Resumen semanal 18-05-2026 a 24-05-2026

## 1) Resumen general
Semana con cobertura diaria completa en Obsidian, pero con bastante diferencia de densidad entre días. Hay entradas generales los 7 días, aunque varias son cabeceras o enlaces automáticos sin notas manuales posteriores.

Los ejes principales fueron: seguimiento operativo diario por Atlas, tareas de contenido y calendario, cita de Iberdrola, registros de viajes de lunes y martes, análisis Warren de martes a viernes, y mantenimiento operativo de Ubuntu/OpenClaw. El domingo quedó actualizado también el resumen semanal específico de viajes.

## 2) Hitos por día
- lunes 18-05-2026: se registró 1 viaje, 41 km y 41 min. Atlas detectó evento `¡Resuelve tus dudas!` de 11:00 a 12:00, tareas `Cumple Isa` y escribir a David sobre quitar nginx del Docker, y una tarea vencida de `Corrida de Toros (Las Ventas)`.
- martes 19-05-2026: se registraron 2 viajes y 90 km; uno con 50 min y otro sin duración indicada. No se localizó resumen Atlas del día. Warren creó cierre pendiente por ausencia de los tres bloques base de análisis.
- miércoles 20-05-2026: el diario existe pero está prácticamente vacío. Atlas no detectó eventos y señaló tareas de contenido con vencimiento ese día: `Imagen publicacion Linkedin` y `Crear publicacion Instragram mañana`, además de posibles duplicados para el 25-05.
- jueves 21-05-2026: el diario automático registró evento `iberdrola coche` 09:00-10:30, tarea `Viene Iberdrola`, dos tareas atrasadas de contenido desde el 20-05 y alerta de mentoría para el 22-05. También se registró un backup operativo de conocimiento de Mara.
- viernes 22-05-2026: diario creado con cabecera, sin notas manuales adicionales. Atlas detectó mentoría `¡Resuelve tus dudas!` 11:00-12:00, sin tareas con vencimiento ese día, y mantuvo como próximas las dos tareas de contenido del 25-05.
- sábado 23-05-2026: diario con enlace al resumen Atlas, sin entradas manuales. Atlas no detectó eventos ni tareas con vencimiento ese día. La captura operativa marcó `dockge` parado y `unhealthy`.
- domingo 24-05-2026: diario con enlace al resumen Atlas, sin entradas manuales. Atlas no detectó eventos ni tareas abiertas con vencimiento hoy; señaló como próximas las tareas de LinkedIn e Instagram para el 25-05. Se actualizó el resumen semanal de viajes.

## 3) Agenda, tareas y coordinación Atlas
- Cobertura Atlas localizada: 5/7 días con archivo propio o bloque automático claro.
- Días sin resumen Atlas localizado en el patrón revisado: 19-05-2026. El 21-05 tiene resumen automático dentro del diario, no archivo `resumen-atlas-21-05-2026.md` localizado.
- Eventos principales detectados: mentorías `¡Resuelve tus dudas!` el 18-05 y 22-05, y `iberdrola coche` el 21-05.
- Tareas destacadas: `Cumple Isa`, escribir a David sobre nginx/Docker, `Subir docker wireguard dashboard`, `Viene Iberdrola`, `Imagen publicacion Linkedin` y `Crear publicacion Instragram mañana`.
- Alertas repetidas: tareas de contenido duplicadas o reprogramadas entre 20-05 y 25-05, posible errata `Instragram`, y tarea vencida de `Corrida de Toros (Las Ventas)` al inicio de la semana.

## 4) Viajes y movilidad
Según `MaraOs/diario/viajes/resumen-semanal-24-05-2026.md`:
- Viajes registrados: 3
- Kilómetros registrados: 131 km
- Tiempo conduciendo registrado: 1 h 31 min
- Media por viaje: 43,7 km

Detalle:
- 18-05-2026: 1 viaje, 41 km, 41 min.
- 19-05-2026: 2 viajes, 90 km en total; el viaje de vuelta no tiene duración indicada.
- 20-05 a 24-05-2026: sin viajes registrados en el resumen semanal disponible.

## 5) Warren / mercados
Cobertura Warren localizada:
- 18-05-2026: existen bloques de análisis en `MaraOs/Warren/analisis-diario/18-05-2026/`, pero no se localizó resumen diario Warren en `MaraOs/diario/warren/`.
- 19-05-2026: resumen diario creado como pendiente por ausencia de bloques base.
- 20-05-2026: resumen generado con Crypto y EEUU + Crypto; España pendiente/no localizada.
- 21-05-2026 y 22-05-2026: resúmenes completos con España, Crypto y EEUU + Crypto.
- 23-05-2026 y 24-05-2026: no se localizaron resúmenes Warren ni análisis diarios fechados.

Lectura semanal:
- España mantuvo una estructura constructiva pero frágil alrededor del IBEX 18.000, con Santander como filtro de calidad y sectores defensivos/energía condicionando la lectura.
- EEUU tuvo rebotes tácticos apoyados por semis/IA, pero con presión recurrente de yields, petróleo y digestión de resultados.
- Crypto estabilizó sin confirmar giro: BTC siguió cerca de zonas defensivas, ETH rezagado y los flujos ETF aún como freno principal.

## 6) Operativa local / OpenClaw
- Las capturas operativas muestran OpenClaw gateway activo durante la semana.
- Docker estuvo disponible, pero `dockge` aparece parado y `unhealthy` desde el 23-05 y continúa así en la captura del 24-05.
- El 21-05 se registró backup de conocimiento de Mara en `MaraOs/SystemFiles/backups/`, documentado como local y potencialmente sensible.
- El número de actualizaciones pendientes varió durante la semana; el 24-05 constan 9 actualizaciones pendientes y sin reinicio requerido.
- El 24-05 la captura no detectó n8n, Redis, Postgres, NocoDB ni Qdrant, aunque en días previos aparecían activos; conviene revisar si fue esperado o una captura parcial.

## 7) Métricas simples
- Días de la semana revisados: 7/7
- Entradas diarias generales encontradas: 7/7
- Entradas con contenido sustancial o automático útil: 5/7
- Entradas vacías o casi vacías: 4/7
- Resúmenes Atlas propios/localizados: 5/7
- Changelogs diarios localizados: 5/7, del 20-05 al 24-05
- Resúmenes Warren localizados: 4/7
- Días con viajes registrados: 2/7
- Viajes registrados: 3
- Pendientes/incidencias detectadas: 9

## 8) Pendientes detectados
- Completar, si procede, los diarios manuales del 20-05, 22-05, 23-05 y 24-05, porque contienen poca o ninguna actividad personal fuera de automatizaciones.
- Añadir duración del viaje del 19-05-2026 con llegada a las 17:20, si se conoce.
- Revisar si falta el resumen Atlas del 19-05-2026 o si no se generó.
- Valorar si el resumen Atlas del 21-05 debe existir también como archivo separado, no solo incrustado en el diario.
- Revisar o cerrar la tarea vencida `Corrida de Toros (Las Ventas)` si ya quedó resuelta.
- Revisar duplicidad/reprogramación de `Imagen publicacion Linkedin` y `Crear publicacion Instragram mañana` para el 25-05.
- Corregir `Instragram` en la fuente de tareas si no es intencionado.
- Revisar `dockge`, que figura parado y `unhealthy`.
- Verificar si la ausencia de n8n, Redis, Postgres, NocoDB y Qdrant en la captura del 24-05 fue esperada o requiere intervención.
