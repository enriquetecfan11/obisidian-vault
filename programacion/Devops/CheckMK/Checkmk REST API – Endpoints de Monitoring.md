---
type: nota
tags:
  - check-mk
  - devops
  - geek
  - automation
status: active
updated: 2026-05-13
title: checkmk-rest-api-endpoints-de-monitoring
project: none
date_created: 2026-05-13
date_modified: 2026-05-13
---

> Base URL: `http://10.18.95.12/monitoring/check_mk/api/1.0`  
> Auth: `Authorization: Bearer automation TU_SECRET`  
> Swagger UI: `http://10.18.95.12/monitoring/check_mk/api/1.0/ui/#/`

---

## 1. Hosts (Configuración)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/domain-types/host_config/collections/all` | Listar todos los hosts |
| POST | `/domain-types/host_config/collections/all` | Crear un host |
| GET | `/objects/host_config/{host_name}` | Detalle de un host |
| PUT | `/objects/host_config/{host_name}` | Modificar un host |
| DELETE | `/objects/host_config/{host_name}` | Borrar un host |
| POST | `/domain-types/host_config/actions/bulk-create/invoke` | Crear hosts en bulk |
| POST | `/domain-types/host_config/actions/bulk-delete/invoke` | Borrar hosts en bulk |

**Columnas útiles (monitoring):**  
`name`, `address`, `alias`, `state`, `check_command`, `notifications_enabled`

---

## 2. Servicios (Monitoring – el que más usarás)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/domain-types/service/collections/all` | Listar servicios con filtros |
| POST | `/objects/host/{host_name}/collections/services` | Servicios de un host concreto |
| GET | `/objects/host/{host_name}/actions/show_service/invoke` | Detalle de un servicio |

**Columnas útiles:**  
`host_name`, `description`, `state`, `plugin_output`, `perf_data`, `check_command`

**Estados numéricos:**

| state | Significado |
|------:|-------------|
| 0 | OK |
| 1 | WARN |
| 2 | CRIT |
| 3 | UNKNOWN |

### Body JSON – Todos los servicios NO OK

```json
{
  "columns": ["host_name", "description", "state", "plugin_output"],
  "query": {
    "op": "!=",
    "left": "state",
    "right": "0"
  }
}
```

### Body JSON – Solo CRIT

```json
{
  "columns": ["host_name", "description", "state", "plugin_output"],
  "query": {
    "op": "=",
    "left": "state",
    "right": "2"
  }
}
```

### Body JSON – WARN o CRIT (combinado)

```json
{
  "columns": ["host_name", "description", "state", "plugin_output"],
  "query": {
    "op": "or",
    "expr": [
      { "op": "=", "left": "state", "right": "1" },
      { "op": "=", "left": "state", "right": "2" }
    ]
  }
}
```

### Body JSON – Servicios CRIT de un host concreto

```json
{
  "columns": ["host_name", "description", "state", "plugin_output"],
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

## 3. Downtimes

| Método | Endpoint                                       | Descripción                        |
| ------ | ---------------------------------------------- | ---------------------------------- |
| GET    | `/domain-types/downtime/collections/all`       | Listar todos los downtimes activos |
| POST   | `/domain-types/downtime/collections/host`      | Crear downtime en un host          |
| POST   | `/domain-types/downtime/collections/service`   | Crear downtime en un servicio      |
| POST   | `/domain-types/downtime/actions/delete/invoke` | Borrar un downtime                 |

**Columnas útiles:**  
`id`, `author`, `comment`, `start_time`, `end_time`, `duration`, `fixed`, `is_service`

---

## 4. Host Groups

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/domain-types/host_group_config/collections/all` | Listar grupos de hosts |
| POST | `/domain-types/host_group_config/collections/all` | Crear grupo |
| GET | `/objects/host_group_config/{name}` | Detalle de un grupo |
| PUT | `/objects/host_group_config/{name}` | Modificar grupo |
| DELETE | `/objects/host_group_config/{name}` | Borrar grupo |

---

## 5. Business Intelligence (BI)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/domain-types/bi_aggregation/actions/aggregation_state/invoke` | Estado de agregaciones BI |
| POST | `/domain-types/bi_aggregation/actions/aggregation_state/invoke` | Estado de agregaciones BI (con filtros) |
| GET | `/domain-types/bi_pack/collections/all` | Listar packs de BI |
| GET | `/objects/bi_aggregation/{aggregation_id}` | Detalle de una agregación |
| PUT | `/objects/bi_aggregation/{aggregation_id}` | Modificar una agregación |
| POST | `/objects/bi_aggregation/{aggregation_id}` | Crear una agregación |

---

## 6. Curls de referencia

```bash
BASE="http://10.18.95.12/monitoring/check_mk/api/1.0"
AUTH="Authorization: Bearer automation TU_SECRET"

# Todos los hosts
curl -s -X GET "$BASE/domain-types/host_config/collections/all" \
  -H "$AUTH" -H "Accept: application/json"

# Servicios NO OK (modo monitor)
curl -s -X POST "$BASE/domain-types/service/collections/all" \
  -H "$AUTH" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"columns":["host_name","description","state","plugin_output"],"query":{"op":"!=","left":"state","right":"0"}}'

# Servicios de un host concreto
curl -s -X POST "$BASE/objects/host/NOMBRE_HOST/collections/services" \
  -H "$AUTH" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{"columns":["description","state","plugin_output"]}'

# Downtimes activos
curl -s -X GET "$BASE/domain-types/downtime/collections/all" \
  -H "$AUTH" -H "Accept: application/json"
```

---

## 7. Operadores disponibles en `query`

| Operador | Significado |
|----------|-------------|
| `=` | Igual |
| `!=` | Distinto |
| `>` | Mayor que |
| `<` | Menor que |
| `>=` | Mayor o igual |
| `<=` | Menor o igual |
| `and` | Y lógico (combina varios filtros) |
| `or` | O lógico (combina varios filtros) |
| `not` | Negación |