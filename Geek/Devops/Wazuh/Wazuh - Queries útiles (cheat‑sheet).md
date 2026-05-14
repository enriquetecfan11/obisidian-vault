---
type: nota
tags:
  - wazuh
  - devops
  - geek
  - ordenador
  - api-rest
status: active
created: 2026-05-13
---
Resumen de comandos rápidos (Server API + Indexer API) para consulta de estado y alertas desde terminal o scripts. [web:3][web:58][web:55]

---

## 1. Server API (operación)

```bash
export WAZUH_HOST="https://IP_O_HOSTNAME:55000"
export WAZUH_USER="tu_usuario"
export WAZUH_PASS="tu_password"
export TOKEN=$(curl -sku "$WAZUH_USER:$WAZUH_PASS" \
  -X GET "$WAZUH_HOST/security/user/authenticate?raw=true")
```

### 1.1 Health check API

```bash
curl -sk -H "Authorization: Bearer $TOKEN" \
  "$WAZUH_HOST/?pretty=true"
```

### 1.2 Listar agentes

```bash
curl -sk -X GET "$WAZUH_HOST/agents?pretty=true&limit=500" \
  -H "Authorization: Bearer $TOKEN"
```

### 1.3 Agentes activos / desconectados

```bash
curl -sk -X GET "$WAZUH_HOST/agents?status=active&pretty=true" \
  -H "Authorization: Bearer $TOKEN"

curl -sk -X GET "$WAZUH_HOST/agents?status=disconnected&pretty=true" \
  -H "Authorization: Bearer $TOKEN"
```

### 1.4 Detalle rápido de un agente

```bash
curl -sk -X GET "$WAZUH_HOST/agents/001?pretty=true" \
  -H "Authorization: Bearer $TOKEN"
```

### 1.5 Estado del manager

```bash
curl -sk -X GET "$WAZUH_HOST/manager/status?pretty=true" \
  -H "Authorization: Bearer $TOKEN"
```

### 1.6 Estado del cluster

```bash
curl -sk -X GET "$WAZUH_HOST/cluster/status?pretty=true" \
  -H "Authorization: Bearer $TOKEN"
```

---

## 2. Indexer API (alertas)

```bash
export INDEXER_HOST="https://IP_O_HOSTNAME:9200"
export INDEXER_USER="admin"
export INDEXER_PASS="tu_password"
export ALERT_INDEX="wazuh-alerts-*"
```

### 2.1 Últimas alertas

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 10,
    "sort": [ { "timestamp": { "order": "desc" } } ],
    "query": { "match_all": {} }
  }'
```

### 2.2 Alertas de la última hora

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 50,
    "sort": [ { "timestamp": { "order": "desc" } } ],
    "query": {
      "range": {
        "timestamp": {
          "gte": "now-1h",
          "lte": "now"
        }
      }
    }
  }'
```

### 2.3 Alertas críticas (por nivel)

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 25,
    "sort": [ { "timestamp": { "order": "desc" } } ],
    "query": {
      "range": {
        "rule.level": { "gte": 12 }
      }
    }
  }'
```

### 2.4 Alertas de una regla concreta

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 20,
    "sort": [ { "timestamp": { "order": "desc" } } ],
    "query": {
      "term": { "rule.id": "5710" }
    }
  }'
```

### 2.5 Alertas de un agente

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 20,
    "sort": [ { "timestamp": { "order": "desc" } } ],
    "query": {
      "term": { "agent.id": "001" }
    }
  }'
```

### 2.6 Top reglas más disparadas

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 0,
    "aggs": {
      "top_rules": {
        "terms": { "field": "rule.id", "size": 10 }
      }
    }
  }'
```

### 2.7 Contar alertas en los últimos 5 minutos

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_count?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "query": {
      "range": {
        "timestamp": {
          "gte": "now-5m",
          "lte": "now"
        }
      }
    }
  }'
```

---

## 3. Mini tabla de referencia

| Tema            | Query clave                         | Notas |
|----------------|-------------------------------------|-------|
| Agents health  | `/agents?status=disconnected`       | Ver agentes caídos. [web:75] |
| Manager health | `/manager/status`                   | Estado del manager. [web:3] |
| Cluster health | `/cluster/status`                   | Solo si tienes cluster. [web:130] |
| Últimas alertas| `_search` + `sort timestamp desc`   | Lista rápida. [web:83] |
| Críticas       | `range rule.level gte 12`           | Afinar umbral según ruleset. [web:82] |
| Volumen        | `_count` con rango de tiempo        | Métrica para dashboards. [web:86][web:60] |

Para ampliar o afinar cualquier query, la referencia completa está en la documentación oficial de la Server API y de la Indexer API. [web:53][web:58]