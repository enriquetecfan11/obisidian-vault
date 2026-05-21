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
En Checkmk cada **servicio** tiene siempre:
- Un **estado numérico** (`state`)
- Un **estado textual** (OK, WARN, CRIT, UNKNOWN)
- Un **summary / plugin_output** (texto corto con el detalle) [web:71][web:143]

Estos estados aparecen igual en la GUI, en Livestatus, en la REST API y en los checks locales [web:136][web:143].

---

## 1. Mapa de estados

| state | Nombre   | Significado típico                                  |
|------:|----------|-----------------------------------------------------|
| 0     | OK       | Todo correcto, dentro de umbrales normales          |
| 1     | WARN     | Advertencia, se acerca a límites o condición leve   |
| 2     | CRIT     | Crítico, requiere acción inmediata                  |
| 3     | UNKNOWN  | Estado desconocido / error del check / sin datos    |

Estos valores son los mismos que usas en checks locales, agentes especiales, active checks, etc.

---

## 2. Campos clave en la API (services)

Cuando consultas servicios vía REST:

`GET /check_mk/api/1.0/domain-types/service/collections/all`

Las columnas importantes para “modo monitor”:

- `host_name` – nombre del host donde vive el servicio
- `description` – nombre del servicio (“CPU load”, “HTTP 443”, etc.) 
- `state` – el código numérico 0–3 de la tabla anterior
- `plugin_output` o `summary` – frase corta con el estado actual (“HTTP OK – 120 ms”, “Disk 95% used…”) 
- `perf_data` – métricas crudas (para gráficos, umbrales)

Ejemplo de estructura típica de respuesta (recortado):

```json
{
  "id": "web-01;HTTP 443",
  "extensions": {
    "host_name": "web-01",
    "description": "HTTP 443",
    "state": 2,
    "plugin_output": "CRIT - Response time 5.2s > 5s",
    "perf_data": "time=5.2s;3;5;0;"
  }
}
```

[web:26][web:71][web:143]

---

## 3. Estados en filtros (`query`) de la REST API

En los endpoints de servicios puedes filtrar por `state` usando la sintaxis JSON `query` [web:26][web:80]:

- Todos los servicios **CRIT**:

```bash
--data-urlencode 'query={"op":"=","left":"state","right":"2"}'
```

- Todos los servicios **no OK**:

```bash
--data-urlencode 'query={"op":"!=","left":"state","right":"0"}'
```

- Servicios **WARN o CRIT** (combinación AND/OR):

```bash
--data-urlencode 'query={
  "op":"or",
  "expr":[
    {"op":"=","left":"state","right":"1"},
    {"op":"=","left":"state","right":"2"}
  ]
}'
```

[web:26][web:80][web:34]

Esto es lo que usarás para contar servicios por estado, alimentar dashboards o generar alertas fuera de Checkmk.

---

## 4. Estados en checks locales / active checks

Los **checks locales** y muchos scripts personalizados devuelven el estado como primer campo numérico en la línea de salida [web:137][web:143]:

```text
0 "My Service" - Todo OK
1 "My Service" - Advertencia
2 "My Service" - Crítico
3 "My Service" - Estado desconocido
```

[web:137][web:143]

Ejemplo con perfdata:

```text
2 "Disk usage /var" used=95%;80;90;0;100 CRIT - 95% used
```

Esto se traduce directamente en `state=2` y en el `plugin_output`/`perf_data` que ves por API y GUI [web:137][web:143].

---

## 5. Traducciones y “modificadores” de estado

En las ediciones Enterprise existen reglas para **traducir estados**:

- `Service state translation`
- `Host state translation` [web:134][web:139]

Sirven para mapear, por ejemplo:

- Dejar un servicio en OK aunque internamente esté CRIT
- Cambiar WARN por CRIT bajo ciertas condiciones [web:138][web:139]

Tenlo en cuenta cuando montes dashboards: lo que sale por REST/GUI ya puede venir “traducido” respecto al valor original del check [web:139][web:143].

---

## 6. Resumen para dashboards

Para cualquier panel de estado de servicios, normalmente te bastan:

- `state` (0–3) → mapping a texto/colores (verde/amarillo/rojo/azul)
- `host_name`
- `description`
- `plugin_output`
- `perf_data` (opcional, para gráficos) [web:26][web:71][web:143]

Y a nivel de API:

- Endpoint base: `/check_mk/api/1.0/domain-types/service/collections/all`
- Filtros con `query` sobre `state` para agrupar por OK/WARN/CRIT/UNKNOWN [web:26][web:80].
