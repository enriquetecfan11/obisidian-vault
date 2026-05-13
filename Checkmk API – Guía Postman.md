
> Swagger UI: `http://10.18.95.12/monitoring/check_mk/api/1.0/ui/#/`  
> Base URL: `http://10.18.95.12/monitoring/check_mk/api/1.0`  
> **Cómo importar en Postman**: Import → Raw text → pega el curl → Continue → Import

---

## Configuración global

### Headers requeridos en todas las peticiones

| Header | Valor |
|--------|-------|
| `Authorization` | `Bearer automation TU_SECRET` |
| `Accept` | `application/json` |
| `Content-Type` | `application/json` |

### Variables recomendadas en Postman (Environments)

| Variable | Valor |
|----------|-------|
| `base_url` | `http://10.18.95.12/monitoring/check_mk/api/1.0` |
| `auth` | `Bearer automation TU_SECRET` |

---

## 1. HOSTS

### 1.1 Listar todos los hosts

```bash
curl --location --request GET 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/host_config/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json'
```

### 1.2 Detalle de un host concreto

```bash
curl --location --request GET 'http://10.18.95.12/monitoring/check_mk/api/1.0/objects/host_config/NOMBRE_HOST' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json'
```

---

## 2. SERVICIOS – Filtros

> Endpoint base para todos los filtros de servicios:  
> `POST http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all`

### Estados

| state | Significado |
|------:|-------------|
| 0 | OK |
| 1 | WARN |
| 2 | CRIT |
| 3 | UNKNOWN |

---

### 2.1 Todos los servicios (sin filtro)

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "host_name",
        "description",
        "state",
        "plugin_output"
    ]
}'
```

---

### 2.2 Servicios OK (state = 0)

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "host_name",
        "description",
        "state",
        "plugin_output"
    ],
    "query": {
        "op": "=",
        "left": "state",
        "right": "0"
    }
}'
```

---

### 2.3 Servicios WARN (state = 1)

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "host_name",
        "description",
        "state",
        "plugin_output"
    ],
    "query": {
        "op": "=",
        "left": "state",
        "right": "1"
    }
}'
```

---

### 2.4 Servicios CRIT (state = 2)

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "host_name",
        "description",
        "state",
        "plugin_output"
    ],
    "query": {
        "op": "=",
        "left": "state",
        "right": "2"
    }
}'
```

---

### 2.5 Servicios UNKNOWN (state = 3)

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "host_name",
        "description",
        "state",
        "plugin_output"
    ],
    "query": {
        "op": "=",
        "left": "state",
        "right": "3"
    }
}'
```

---

### 2.6 Servicios NO OK – WARN + CRIT + UNKNOWN (state != 0)

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "host_name",
        "description",
        "state",
        "plugin_output"
    ],
    "query": {
        "op": "!=",
        "left": "state",
        "right": "0"
    }
}'
```

---

### 2.7 Servicios WARN + CRIT (sin UNKNOWN)

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "host_name",
        "description",
        "state",
        "plugin_output"
    ],
    "query": {
        "op": "or",
        "expr": [
            { "op": "=", "left": "state", "right": "1" },
            { "op": "=", "left": "state", "right": "2" }
        ]
    }
}'
```

---

### 2.8 Servicios de un host concreto (todos los estados)

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "host_name",
        "description",
        "state",
        "plugin_output"
    ],
    "query": {
        "op": "=",
        "left": "host_name",
        "right": "NOMBRE_HOST"
    }
}'
```

---

### 2.9 Servicios CRIT de un host concreto

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "host_name",
        "description",
        "state",
        "plugin_output"
    ],
    "query": {
        "op": "and",
        "expr": [
            { "op": "=", "left": "host_name", "right": "NOMBRE_HOST" },
            { "op": "=", "left": "state", "right": "2" }
        ]
    }
}'
```

---

### 2.10 Servicios NO OK de un host concreto

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "host_name",
        "description",
        "state",
        "plugin_output"
    ],
    "query": {
        "op": "and",
        "expr": [
            { "op": "=", "left": "host_name", "right": "NOMBRE_HOST" },
            { "op": "!=", "left": "state", "right": "0" }
        ]
    }
}'
```

---

### 2.11 Servicios por nombre de servicio (description)

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "host_name",
        "description",
        "state",
        "plugin_output"
    ],
    "query": {
        "op": "=",
        "left": "description",
        "right": "CPU load"
    }
}'
```

---

### 2.12 Servicios con columnas extendidas (perf_data, last_check)

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "host_name",
        "description",
        "state",
        "plugin_output",
        "perf_data",
        "check_command",
        "last_check",
        "last_state_change",
        "acknowledged",
        "scheduled_downtime_depth"
    ],
    "query": {
        "op": "!=",
        "left": "state",
        "right": "0"
    }
}'
```

---

## 3. SERVICIOS – Por host (endpoint alternativo)

> Sustituye `NOMBRE_HOST` directamente en la URL.

### 3.1 Todos los servicios del host

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/objects/host/NOMBRE_HOST/collections/services' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "description",
        "state",
        "plugin_output"
    ]
}'
```

### 3.2 Solo CRIT del host

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/objects/host/NOMBRE_HOST/collections/services' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "columns": [
        "description",
        "state",
        "plugin_output"
    ],
    "query": {
        "op": "=",
        "left": "state",
        "right": "2"
    }
}'
```

---

## 4. DOWNTIMES

### 4.1 Listar downtimes activos

```bash
curl --location --request GET 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/downtime/collections/all' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json'
```

### 4.2 Crear downtime en un host

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/downtime/collections/host' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "host_name": "NOMBRE_HOST",
    "start_time": "2026-01-01T00:00:00Z",
    "end_time": "2026-01-01T01:00:00Z",
    "comment": "Mantenimiento programado"
}'
```

### 4.3 Crear downtime en un servicio

```bash
curl --location --request POST 'http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/downtime/collections/service' \
--header 'Authorization: Bearer automation TU_SECRET' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "host_name": "NOMBRE_HOST",
    "service_descriptions": ["CPU load"],
    "start_time": "2026-01-01T00:00:00Z",
    "end_time": "2026-01-01T01:00:00Z",
    "comment": "Mantenimiento programado"
}'
```

---

## 5. Referencia rápida de operadores query

| Operador | Significado |
|----------|-------------|
| `=` | Igual |
| `!=` | Distinto |
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual |
| `<=` | Menor o igual |
| `and` | Y lógico (combina filtros) |
| `or` | O lógico (combina filtros) |
| `not` | Negación |

---

## 6. Columnas útiles de referencia

### Servicios
| Columna | Descripción |
|---------|-------------|
| `host_name` | Nombre del host |
| `description` | Nombre del servicio |
| `state` | Estado 0–3 |
| `plugin_output` | Texto resultado del check |
| `perf_data` | Métricas