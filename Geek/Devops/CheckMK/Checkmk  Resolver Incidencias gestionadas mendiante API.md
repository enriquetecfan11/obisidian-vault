---
type: nota
tags:
  - check-mk
  - devops
  - geek
  - automation
status: active
updated: 2026-05-13
---
## Qué significa “resolver” en Checkmk
En Checkmk, la REST API devuelve códigos HTTP para indicar si la petición se ha transmitido correctamente, pero la propia documentación aclara que eso no garantiza por sí solo que la acción haya producido el efecto operativo esperado; la verificación del resultado debe hacerse después.[1]

Por eso, cuando se habla de “resolver una incidencia” vía API, normalmente hay tres escenarios distintos:

- Reconocer el problema para indicar que ya está siendo tratado por un operador.[1]
- Programar un downtime para suprimir alertas durante una intervención planificada.[2]
- Considerar la incidencia realmente resuelta cuando el host o servicio vuelve a estado OK y el problema desaparece del estado activo de monitorización.[1]

## API REST disponible
La documentación oficial indica que la API usa HTTP/1.1, cuerpos JSON, autenticación HTTP y versionado, y que desde Checkmk 2.5.0 la URL de la API utiliza la versión `v1`.[1]

Para scripts, Checkmk recomienda autenticación **Bearer** con un usuario de automatización y su automation secret, enviados en la cabecera `Authorization` de cada petición.[1]

Ejemplo base de autenticación:

```bash
curl -X GET \
  -H "Authorization: Bearer automation TU_AUTOMATION_SECRET" \
  -H "Accept: application/json" \
  "https://CHECKMK_SERVER/SITE/check_mk/api/v1/..."
```

## Acciones útiles para incidencias
La guía oficial explica que la REST API está pensada como subconjunto funcional de la interfaz web y que puede usarse para ejecutar acciones operativas desde scripts.[2][1]

En un flujo de incidencias, lo más útil suele ser esto:

| Acción | Uso | Resultado esperado |
|---|---|---|
| Acknowledge | Marcar el problema como reconocido o en tratamiento | El problema sigue existiendo, pero queda gestionado por operador.[1] |
| Downtime programado | Silenciar alertas durante mantenimiento | Las notificaciones y el ruido operativo se controlan durante la ventana definida.[2] |
| Consulta de estado | Verificar si el host/servicio ya volvió a OK | Confirmación real de resolución operativa.[1] |

## Reconocer una incidencia
La documentación oficial no presenta en esta página un listado narrativo de todos los endpoints, porque la referencia completa vive en la documentación OpenAPI incluida en cada site, accesible desde `Help > Developer resources > REST API > Version 1 > Documentation` y también mediante la GUI interactiva del propio Checkmk.[1][2]

Eso significa que para reconocer incidencias debes apoyarte en la documentación OpenAPI de tu instancia y localizar la acción de *acknowledge* sobre host o servicio, probándola si quieres en la Interactive GUI antes de integrarla en scripts.[1][2]

Ejemplo orientativo de uso con `curl` para un servicio, a adaptar a la ruta exacta publicada por tu site:

```bash
curl -X POST \
  -H "Authorization: Bearer automation TU_AUTOMATION_SECRET" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "comment": "Incidencia reconocida desde automatización",
    "sticky": true,
    "notify": false
  }' \
  "https://CHECKMK_SERVER/SITE/check_mk/api/v1/.../acknowledge/invoke"
```

## Downtime como alternativa
La visión general de APIs y recursos de Checkmk cita expresamente el tutorial oficial “Working with the Checkmk REST API” y menciona entre sus ejemplos prácticos la creación de *scheduled downtimes*.[2]

Cuando el objetivo no es tanto “resolver” como evitar alertado durante una intervención, el downtime suele ser la acción más correcta desde automatización, porque deja trazabilidad operativa sin fingir que el problema ya está solucionado.[2]

## Cómo confirmar que quedó resuelta
La documentación de la REST API remarca que un código HTTP exitoso solo indica que la petición fue aceptada o procesada a nivel de transporte, no necesariamente que el estado final del problema sea el esperado.[1]

Por eso, un flujo sólido de cierre debería ser:

1. Lanzar el acknowledge o el downtime mediante la REST API.[1][2]
2. Consultar después el estado del host o servicio afectado mediante API o una consulta de estado apropiada.[1][2]
3. Dar la incidencia por cerrada solo cuando el check vuelva a OK o cuando el criterio operativo interno así lo determine.[1]

## Recomendación práctica
Para integrar Checkmk con un sistema externo de tickets, lo más robusto es mapear estados de esta forma: ticket abierto -> problema detectado; ticket en curso -> acknowledge; ventana de intervención -> downtime; ticket resuelto -> validación de que el check ha vuelto a OK.

La documentación oficial también destaca la GUI interactiva de la REST API como punto de entrada práctico para descubrir rutas, payloads y respuestas exactas de tu versión y edición de Checkmk antes de automatizar nada en producción.[2][1]