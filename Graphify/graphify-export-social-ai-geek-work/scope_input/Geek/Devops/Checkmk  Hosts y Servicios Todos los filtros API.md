Aquí tienes el `.md` completo listo para Obsidian con todos los filtros para hosts y servicios:

> Base URL: `http://10.18.95.12/monitoring/check_mk/api/1.0`  
> Auth header: `Authorization: Bearer automation TU_SECRET`  
> Content-Type: `application/json`  
> Accept: `application/json`  
> Swagger UI: `http://10.18.95.12/monitoring/check_mk/api/1.0/ui/#/`

---

## 1. Hosts

### Endpoint
```
GET http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/host_config/collections/all
```

### Estados de hosts

| state | Significado |
|------:|-------------|
| 0 | UP |
| 1 | DOWN |
| 2 | UNREACHABLE |

### 1.1 Todos los hosts
```bash
curl -s -X GET \
  "http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/host_config/collections/all" \
  -H "Authorization: Bearer automation TU_SECRET" \
  -H "Accept: application/json"
```
### Estados de hosts
### 1.2 Hosts con problemas (POST con filtro)
```
POST http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/host/collections/all
```

#### Hosts DOWN (state = 1)
```json
{
  "columns": ["name", "address", "state"],
  "query": {
    "op": "=",
    "left": "state",
    "right": "1"
  }
}
```

#### Hosts UNREACHABLE (state = 2)
```json
{
  "columns": ["name", "address", "state"],
  "query": {
    "op": "=",
    "left": "state",
    "right": "2"
  }
}
```

#### Hosts NO UP (DOWN + UNREACHABLE)
```json
{
  "columns": ["name", "address", "state"],
  "query": {
    "op": "!=",
    "left": "state",
    "right": "0"
  }
}
```

#### Host concreto por nombre
```json
{
  "columns": ["name", "address", "state"],
  "query": {
    "op": "=",
    "left": "name",
    "right": "NOMBRE_HOST"
  }
}
```

---

## 2. Servicios

### Endpoint
```
POST http://10.18.95.12/monitoring/check_mk/api/1.0/domain-types/service/collections/all
```

### Estados de servicios

| state | Significado |
|------:|-------------|
| 0 | OK |
| 1 | WARN |
| 2 | CRIT |
| 3 | UNKNOWN |

### 2.1 Todos los servicios (sin filtro)
```json
{
  "columns": [
    "host_name",
    "description",
    "state",
    "plugin_output"
  ]
}
```

### 2.2 Servicios OK (state = 0)
```json
{
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
}
```

### 2.3 Servicios WARN (state = 1)
```json
{
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
}
```

### 2.4 Servicios CRIT (state = 2)
```json
{
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
}
```

### 2.5 Servicios UNKNOWN (state = 3)
```json
{
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
}
```

### 2.6 Servicios NO OK (WARN + CRIT + UNKNOWN)
```json
{
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
}
```

### 2.7 Servicios WARN + CRIT (sin UNKNOWN)
```json
{
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
}
```

### 2.8 Servicios de un host concreto
```json
{
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
}
```

### 2.9 Servicios CRIT de un host concreto
```json
{
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
}
```

### 2.10 Servicios NO OK de un host concreto
```json
{
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
}
```

### 2.11 Servicios por descripción (nombre del servicio)
```json
{
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
}
```

### 2.12 Servicios CRIT + host concreto + columnas extendidas (con perf_data)
```json
{
  "columns": [
    "host_name",
    "description",
    "state",
    "plugin_output",
    "perf_data",
    "check_command"
  ],
  "query": {
    "op": "and",
    "expr": [
      { "op": "=", "left": "host_name", "right": "NOMBRE_HOST" },
      { "op": "=", "left": "state", "right": "2" }
    ]
  }
}
```

---

## 3. Servicios por host (endpoint alternativo)

```
POST http://10.18.95.12/monitoring/check_mk/api/1.0/objects/host/{host_name}/collections/services
```

Sustituye `{host_name}` en la URL directamente. El body puede llevar o no filtros:

#### Todos los servicios del host
```json
{
  "columns": [
    "description",
    "state",
    "plugin_output"
  ]
}
```

#### Solo CRIT del host
```json
{
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
}
```

---

## 4. Operadores disponibles en `query`

| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| `=` | Igual | `state = 2` |
| `!=` | Distinto | `state != 0` |
| `>` | Mayor que | `state > 1` |
| `<` | Menor que | `state < 2` |
| `>=` | Mayor o igual | `state >= 1` |
| `<=` | Menor o igual | `state <= 2` |
| `and` | Y lógico | host X AND state = 2 |
| `or` | O lógico | state = 1 OR state = 2 |
| `not` | Negación | NOT state = 0 |

---

## 5. Columnas disponibles más útiles

### Servicios
| Columna | Descripción |
|---------|-------------|
| `host_name` | Nombre del host |
| `description` | Nombre del servicio |
| `state` | Estado numérico (0-3) |
| `plugin_output` | Texto corto del resultado |
| `perf_data` | Métricas crudas para gráficos |
| `check_command` | Comando de check usado |
| `last_check` | Timestamp del último check |
| `last_state_change` | Timestamp del último cambio de estado |
| `acknowledged` | Si está acknowledgeado (0/1) |
| `scheduled_downtime_depth` | Si está en downtime (0 = no) |

### Hosts
| Columna | Descripción |
|---------|-------------|
| `name` | Nombre del host |
| `address` | IP o FQDN |
| `alias` | Alias del host |
| `state` | Estado (0=UP, 1=DOWN, 2=UNREACHABLE) |
| `num_services` | Número total de servicios |
| `num_services_crit` | Servicios en CRIT |
| `num_services_warn` | Servicios en WARN |
| `num_services_ok` | Servicios en OK |

---

## 6. Curl de referencia rápida

```bash
BASE="http://10.18.95.12/monitoring/check_mk/api/1.0"
AUTH="Authorization: Bearer automation TU_SECRET"

# Todos los servicios NO OK
curl -s -X POST "$BASE/domain-types/service/collections/all" \
  -H "$AUTH" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "columns": ["host_name","description","state","plugin_output"],
    "query": {"op":"!=","left":"state","right":"0"}
  }'

# Servicios CRIT
curl -s -X POST "$BASE/domain-types/service/collections/all" \
  -H "$AUTH" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "columns": ["host_name","description","state","plugin_output"],
    "query": {"op":"=","left":"state","right":"2"}
  }'

# Servicios de un host concreto
curl -s -X POST "$BASE/objects/host/NOMBRE_HOST/collections/services" \
  -H "$AUTH" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "columns": ["description","state","plugin_output"]
  }'
```
```