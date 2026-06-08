---
 title: resumen-semanal-17-05-2026
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

#mara-os #diario

# Resumen semanal 11-05-2026 a 17-05-2026

## 1) Resumen general
Semana con buena cobertura de registros diarios, centrada en tres ejes: agenda/tareas operativas vía Atlas, movilidad diaria y consolidación de reglas del sistema Mara. El hito operativo más importante fue fijar de forma explícita que tareas y calendario se gestionan siempre por MCP: tareas en `agents-notes` y eventos en el MCP de calendario configurado, sin sistemas paralelos salvo petición explícita.

La semana tiene entrada diaria general los 7 días. Hay contenido sustancial en 5 de 7 días; el 15-05 y 16-05 existen pero están prácticamente vacíos. También hay resúmenes Atlas todos los días y changelogs diarios del 11 al 17. Warren tiene resúmenes completos del lunes al viernes; no se localizaron resúmenes Warren para sábado ni domingo.

## 2) Hitos por día
- lunes 11-05-2026: se registraron 2 viajes, 90 km y 1 h 21 min. Atlas no detectó eventos del día y listó tareas relevantes: Bizum Amigo Javi, llamar a Iberdrola, Comet Net4Gym, crear post Instagram y escribir a David sobre nginx en Docker.
- martes 12-05-2026: se registró 1 viaje de 45 km y 41 min. Agenda con mentoría y bloques de publicación LinkedIn/Instagram; Atlas alertó de solape a las 17:15. Tareas relevantes: Terminar Okre, Subir Origen, Enviar correo reunión y Llamar a Iberdrola.
- miércoles 13-05-2026: Kike fijó la regla estable de tareas y calendario por MCP. Agenda intensa: Reunión Telemáticos, mentoría y consultoría con Carlos Adams. Atlas listó tareas técnicas/operativas: Mirar Api Wazuh, Subir Okre, Correo Okre y Crear post intagram. El resumen semanal de viajes registra 2 viajes ese día, aunque no aparecen en el diario principal.
- jueves 14-05-2026: se registraron 2 viajes, 90 km y 1 h 22 min, además de gasolina: 46,19 €, depósito entero, 1,61 €/l, aprox. 28,69 l. Agenda con reunión gimnasio, mentoría y Post LinkedIn, con solape parcial entre mentoría y publicación.
- viernes 15-05-2026: el diario existe pero está prácticamente vacío. Atlas no detectó eventos confirmados y señaló `Post LinkedIn` como tarea vencida del 14-05. Próximas tareas: escribir a David, subir docker wireguard dashboard y viene Iberdrola.
- sábado 16-05-2026: el diario existe pero está prácticamente vacío. Atlas no detectó eventos ni tareas con vencimiento ese día; señaló próximas tareas: Corrida de Toros, Cumple Isa, escribir a David, wireguard dashboard e Iberdrola. También alertó de que la tarea “llamar a Iberdrola” para el lunes no figuraba en el listado actual.
- domingo 17-05-2026: se registró 1 viaje de 62 km y 52 min, con salida estimada 12:08. Atlas detectó evento `Toros Las Ventas` 19:00–21:00 y tarea asociada `Corrida de Toros (Las Ventas)`.

## 3) Operativa y sistemas
- Queda reforzada la regla fija: tareas y calendario siempre por MCP.
- Tareas: `agents-notes`; eventos: MCP de calendario configurado (`calendar-mara` cuando esté disponible).
- No usar calendarios locales, archivos `.ics`, cron, Obsidian ni listas paralelas salvo petición explícita.
- El documento operativo `MaraOs/SystemFiles/TOOLS.md` fue actualizado durante la semana con reglas de tareas/calendario y criterio de fecha por defecto para viajes.
- Las integraciones MCP de calendario y tareas aparecen disponibles y respondiendo correctamente en los resúmenes Atlas revisados.
- Estado operativo Ubuntu/OpenClaw registrado en changelogs: Docker disponible con 13/13 contenedores en ejecución y sin incidencias críticas visibles. Se detectaron 1–2 actualizaciones pendientes del sistema en los registros de final de semana.

## 4) Agenda, tareas y coordinación Atlas
- Cobertura Atlas: 7/7 días.
- Días con agenda destacada: 12-05, 13-05, 14-05 y 17-05.
- Eventos principales detectados: mentorías, publicaciones LinkedIn/Instagram, Reunión Telemáticos, Consultoría con Carlos Adams, Reunión gimnasio y Toros Las Ventas.
- Tareas recurrentes o relevantes de la semana: Okre, Origen, Iberdrola, post Instagram/LinkedIn, mensaje a David sobre nginx/Docker, API Wazuh y wireguard dashboard.
- Alertas repetidas: solapes de publicaciones con mentorías, tarea `Post LinkedIn` vencida el 15-05, y posible ausencia/corrección necesaria de la tarea “llamar a Iberdrola” para el lunes.

## 5) Viajes y movilidad
Según el resumen semanal específico de viajes en `MaraOs/diario/viajes/resumen-semanal-17-05-2026.md`:
- Viajes registrados: 6
- Kilómetros registrados: 287 km
- Tiempo conduciendo: 4 h 16 min
- Media por viaje: 47,8 km

Detalle por día:
- 11-05-2026: 2 viajes, 90 km, 1 h 21 min.
- 12-05-2026: 1 viaje, 45 km, 41 min.
- 13-05-2026: 2 viajes, 90 km, 1 h 22 min. Nota: aparecen en el resumen semanal de viajes, no en el diario principal del día.
- 14-05-2026: 2 viajes en el diario principal, 90 km, 1 h 22 min. Nota: el resumen semanal específico de viajes marca jueves “sin viajes registrados todavía”, por lo que hay discrepancia con el diario principal y el changelog.
- 15-05-2026: sin viajes registrados.
- 16-05-2026: sin viajes registrados.
- 17-05-2026: 1 viaje, 62 km, 52 min.

Nota de consistencia: sumando los viajes visibles en diarios principales más los dos viajes del 13-05 citados en changelog/resumen de viajes, salen 8 viajes, 377 km y 5 h 38 min. El resumen semanal específico de viajes actualmente reporta 6 viajes, 287 km y 4 h 16 min. Conviene reconciliar esa diferencia antes de usar las métricas como definitivas.

## 6) Warren / mercados
Cobertura Warren localizada:
- 11-05 a 15-05: resúmenes diarios Warren completos.
- 16-05 y 17-05: no se localizaron resúmenes Warren ni análisis diarios en las rutas revisadas.

Lectura semanal:
- España: semana de rebote y corrección táctica bajo zonas de confirmación. Ibex necesitaba recuperar 17.850/18.000; Santander aparece como filtro clave, Repsol mantuvo mejor fuerza relativa e Iberdrola se comportó más defensiva.
- EEUU: fuerza selectiva en IA/semiconductores, pero con presión por yields largos, dólar y macro de inflación. Warren recomendó no perseguir beta amplia sin margen de seguridad.
- Crypto: BTC defendió la zona de 80k con episodios de reparación, pero ETH siguió débil y el sentimiento pasó entre Neutral y Fear. La lectura fue de prudencia hasta confirmar ruptura por precio y volumen.

## 7) Métricas simples
- Días de la semana revisados: 7/7
- Entradas diarias generales encontradas: 7/7
- Entradas con contenido sustancial: 5/7
- Entradas vacías o casi vacías: 2/7
- Resúmenes Atlas encontrados: 7/7
- Changelogs diarios encontrados: 7/7
- Resúmenes Warren encontrados: 5/7
- Días sin resumen Warren localizado: 2/7
- Viajes detectados en resumen semanal específico de viajes: 6
- Viajes detectables al cruzar diario principal + changelogs/resumen de viajes: 8
- Pendientes/incidencias detectadas: 6

## 8) Pendientes detectados
- Completar o enriquecer, si procede, los diarios del 15-05-2026 y 16-05-2026: existen pero están prácticamente vacíos.
- Reconciliar métricas de viajes: el resumen específico de viajes no incluye los 2 viajes del 14-05 que sí constan en el diario principal y changelog.
- Revisar si los 2 viajes del 13-05 deben copiarse también al diario principal del 13-05 para evitar dispersión de fuente.
- Verificar o corregir la tarea “llamar a Iberdrola” para el lunes, porque Atlas indicó que no figuraba en `agents-notes` el 16-05.
- Revisar estado de `Post LinkedIn`, que aparecía vencida en Atlas el 15-05.
- No se localizaron resúmenes Warren de 16-05 ni 17-05; si debían existir, generarlos o marcar la ausencia como esperada por fin de semana.
