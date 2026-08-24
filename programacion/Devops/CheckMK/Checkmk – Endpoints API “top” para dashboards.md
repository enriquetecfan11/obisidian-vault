---
type: nota
tags:
  - check-mk
  - devops
  - geek
  - automation
status: active
updated: 2026-05-13
title: checkmk-endpoints-api-top-para-dashboards
project: none
date_created: 2026-05-13
date_modified: 2026-05-13
---

> Base:
> - Sitio: `https://IP_O_HOSTNAME/monitoring`
> - REST base: `https://IP_O_HOSTNAME/monitoring/check_mk/api/1.0`
> - Auth: `Authorization: Bearer automation TU_SECRET`
> - Multisite: añade `_username` y `_secret` como query params o usa sesión de navegador.

---

## 1. Hosts (REST API)

### 1.1 Listar todos los hosts
- **Método**: GET  
- **URL**:  
  `/domain-types/host/collections/all`  
- **Uso típico**: inventario, contar hosts, agrupar por carpetas o labels [web:77][web:34].  
- **Ejemplo**:

```bash
curl -X GET \
  "$API_URL/domain-types/host/collections/all?columns=name&columns=filename&columns=num_services" \
  -H "Authorization: Bearer $BEARER_TOKEN" \
  -H "Accept: application/json" -k
```

### 1.2 Obtener un host concreto
- **Método**: GET  
- **URL**:  
  `/objects/host/{host_name}`  
- **Uso**: detalles de un host (labels, folder, atributos) para mostrar ficha en el dashboard [web:76][web:93].

### 1.3 Crear / modificar / borrar host
- **Crear host**: `POST /domain-types/host_config/collections/all`  
- **Modificar host**: `PUT /objects/host_config/{host_name}`  
- **Borrar host**: `DELETE /objects/host_config/{host_name}`  
- Estos son clave si quieres que el dashboard sea también “panel de control” para automatizar altas/bajas [web:3][web:34].

---

## 2. Servicios (REST API)

### 2.1 Listar servicios (global)
- **Método**: GET  
- **URL**:  
  `/domain-types/service/collections/all`  
- **Uso**: vista global de servicios con filtros por estado para mostrar “health overview” [web:75][web:80].  
- **Parámetros útiles**:
  - `columns=` repetido (p.ej. `columns=host_name&columns=description&columns=state`)
  - `query=` en JSON (filtrado por estado, host, etc.) [web:75].

**Ejemplo: solo servicios en estado != OK**

```bash
curl -G \
  "$API_URL/domain-types/service/collections/all" \
  -H "Authorization: Bearer $BEARER_TOKEN" \
  -H "Accept: application/json" -k \
  --data-urlencode 'columns=host_name' \
  --data-urlencode 'columns=description' \
  --data-urlencode 'columns=state' \
  --data-urlencode 'columns=plugin_output' \
  --data-urlencode 'query={"op":"!=","left":"state","right":"0"}'
```

### 2.2 Servicios de un host
- **Método**: GET  
- **URL típica**:  
  `/domain-types/service/collections/all?query={"op":"=","left":"host_name","right":"NOMBRE_HOST"}`  
- **Uso**: detalle por host para tarjetas en el dashboard tipo “Services of host” [web:73][web:80].

---

## 3. Estado en tiempo real (Multisite / view.py)

Para datos “en vivo” que casan con lo que ves en las vistas de Checkmk, la opción más cómoda es la Multisite API (`view.py` + `output_format=json`) [web:77][web:91].

> Nota: estos endpoints usan `_username` y `_secret` o cookie de sesión, no el Bearer de REST.

### 3.1 Vista de estado de hosts
- **URL base** (ejemplo estándar):  
  `/view.py?view_name=host&output_format=json`  
- **Uso**: listado rápido de hosts con estado (UP/DOWN, etc.) para widgets de “Host status” [web:77][web:90].

### 3.2 Vista de estado de servicios
- **URL base**:  
  `/view.py?view_name=services&output_format=json`  
- **Uso**: lista de servicios con filtros (por hostgroup, servicegroup, carpeta…) para paneles de criticidades [web:78][web:91].

### 3.3 Vistas personalizadas exportadas
1. Creas tu propia **View** en la GUI (ej. “Dashboard_JSON_Services”) con columnas mínimas.  
2. En la vista, usas menú **Export > JSON** y copias la URL base que te da Checkmk [web:75][web:77].  
3. Añades `&_username=automation&_secret=TU_SECRET` para integrarla en tus scripts/Obsidian.

Esto te permite tener un endpoint “a medida” por vista, sin pelearte con todos los parámetros [web:77][web:90].

---

## 4. Información de dashboards y views (REST)

Si quieres versionar dashboards a nivel API:

### 4.1 Listar dashboards definidos
- **Método**: GET  
- **URL**:  
  `/domain-types/dashboard/collections/all`  
- **Uso**: inventario de dashboards para documentar qué hay en Checkmk y quizá referenciarlos desde Obsidian [web:72][web:3].

### 4.2 Detalle de un dashboard
- **Método**: GET  
- **URL**:  
  `/objects/dashboard/{dashboard_name}`  
- **Uso**: guardar el JSON de definición del dashboard (layout, tiles) en tu repo/Obsidian para versionado [web:72].

---

## 5. Otros endpoints útiles

### 5.1 Información de versiones / site
- **Método**: GET  
- **URL**:  
  `/objects/site/{site_id}`  
- **Uso**: mostrar en el dashboard versión de Checkmk, estado del site, etc. [web:93].

### 5.2 Contadores agregados (ejemplo hosts y servicios)
No hay un único “endpoint métrico”, pero puedes reutilizar:

- `/domain-types/host/collections/all` con columnas `num_services` y sumar en tu script [web:34].  
- `/domain-types/service/collections/all` filtrando por `state` para sacar totales OK/WARN/CRIT/UNKNOWN [web:75].

---

## 6. Trozos de curl reutilizables

```bash
# Variables base
CHECKMK_SITE="https://IP_O_HOSTNAME/monitoring"
API_URL="$CHECKMK_SITE/check_mk/api/1.0"
BEARER_TOKEN="automation TU_SECRET"

# Hosts (REST)
curl -X GET "$API_URL/domain-types/host/collections/all" \
  -H "Authorization: Bearer $BEARER_TOKEN" \
  -H "Accept: application/json" -k

# Servicios con problemas (REST)
curl -G "$API_URL/domain-types/service/collections/all" \
  -H "Authorization: Bearer $BEARER_TOKEN" \
  -H "Accept: application/json" -k \
  --data-urlencode 'columns=host_name' \
  --data-urlencode 'columns=description' \
  --data-urlencode 'columns=state' \
  --data-urlencode 'query={"op":"!=","left":"state","right":"0"}'

# Vista Multisite de hosts en JSON
curl "$CHECKMK_SITE/check_mk/view.py?view_name=host&output_format=json&_username=automation&_secret=TU_SECRET" -k
```

---

## 7. Cómo lo integraría en Obsidian

- Crear carpeta `checkmk/` con:
  - `checkmk_endpoints.md` (este documento).
  - `checkmk_queries.md` con ejemplos de queries `query={...}` y combinaciones de columnas.  
- Usar un script externo (Python/n8n) que:
  - Llama a los endpoints anteriores.
  - Genera `.md` con tablas (p. ej. servicios críticos) que Obsidian renderiza.

---

¿Quieres que te genere otro `.md` con ejemplos de payloads (requests) típicos para crear/modificar hosts y servicios?