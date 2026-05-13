---
type: nota
tags:
  - wazuh
  - devops
  - geek
  - ordenador
  - api-rest
status: active
updated: 2026-05-13
---
Este documento recoge los endpoints y patrones de consulta que sí sirven para **ver alertas** en Wazuh desde terminal, pensados para documentarlos en Obsidian y reutilizarlos con `curl`.[1][2]

## Aclaración importante

La **Wazuh Server API** no ofrece un endpoint específico para leer alertas directamente; las alertas se almacenan indexadas en el Wazuh Indexer, por lo que para consultarlas hay que usar la **Wazuh Indexer API** sobre índices como `wazuh-alerts-4.x-*` o `wazuh-alerts-*`.[3][4][5]

## Variables base

```bash
export INDEXER_HOST="https://IP_O_HOSTNAME:9200"
export INDEXER_USER="admin"
export INDEXER_PASS="tu_password"
export ALERT_INDEX="wazuh-alerts-*"
```

## Endpoints clave para ver alertas

### 1. Buscar alertas

El endpoint principal para leer alertas es `POST /<indice>/_search`, que permite listar alertas, filtrar, ordenar y paginar resultados sobre el índice de alertas.[6][2]

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 10,
    "sort": [
      {"timestamp": {"order": "desc"}}
    ],
    "query": {
      "match_all": {}
    }
  }'
```

### 2. Contar alertas

`POST /<indice>/_count` sirve para saber cuántas alertas cumplen una condición sin traer todos los documentos, útil para métricas rápidas o comprobaciones.[1][2]

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_count?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "query": {
      "match_all": {}
    }
  }'
```

### 3. Últimas alertas de la última hora

Puedes limitar por tiempo usando un filtro `range` sobre `timestamp`, que es la forma más habitual de consultar actividad reciente.[7][6]

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 50,
    "sort": [
      {"timestamp": {"order": "desc"}}
    ],
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

### 4. Alertas por severidad

El campo `rule.level` permite filtrar por nivel de severidad, por ejemplo para sacar solo alertas altas o críticas.[8][6]

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 25,
    "sort": [
      {"timestamp": {"order": "desc"}}
    ],
    "query": {
      "range": {
        "rule.level": {
          "gte": 12
        }
      }
    }
  }'
```

### 5. Alertas por `rule.id`

Este patrón sirve para localizar alertas generadas por una regla concreta.[6]

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 20,
    "sort": [
      {"timestamp": {"order": "desc"}}
    ],
    "query": {
      "term": {
        "rule.id": "5710"
      }
    }
  }'
```

### 6. Alertas por agente

Permite consultar alertas de un agente concreto usando `agent.id` o `agent.name`.[2][1]

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 20,
    "sort": [
      {"timestamp": {"order": "desc"}}
    ],
    "query": {
      "term": {
        "agent.id": "001"
      }
    }
  }'
```

### 7. Alertas por grupo o campo concreto

Puedes filtrar por cualquier campo indexado, por ejemplo `rule.groups`, `data.srcip`, `manager.name` o `decoder.name`, según el tipo de alerta.[1][2]

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 20,
    "query": {
      "term": {
        "decoder.name": "sshd"
      }
    }
  }'
```

### 8. Top alertas agregadas

Las agregaciones permiten sacar resúmenes, como las reglas más disparadas, agentes con más alertas o IPs con más eventos.[7][1]

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 0,
    "aggs": {
      "top_rules": {
        "terms": {
          "field": "rule.id",
          "size": 10
        }
      }
    }
  }'
```

### 9. Buscar solo campos concretos

Para reducir payload, puedes pedir solo algunos campos con `_source`, por ejemplo timestamp, regla, descripción y agente.[2][1]

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 10,
    "_source": ["timestamp", "rule.id", "rule.level", "rule.description", "agent.id", "agent.name"],
    "sort": [
      {"timestamp": {"order": "desc"}}
    ],
    "query": {
      "match_all": {}
    }
  }'
```

### 10. Obtener una alerta por ID de documento

Si conoces el `_id` del documento, puedes recuperar una alerta concreta con `GET /<indice>/_doc/<id>`.[1][2]

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X GET "$INDEXER_HOST/$ALERT_INDEX/_doc/ID_DEL_DOCUMENTO?pretty"
```

## Consultas recomendadas para operación diaria

| Caso | Endpoint | Uso |
|---|---|---|
| Ver últimas alertas | `POST /wazuh-alerts-*/_search` [6] | Listado general ordenado por fecha. |
| Saber volumen | `POST /wazuh-alerts-*/_count` [2] | Conteo sin descargar documentos. |
| Filtrar críticas | `POST /wazuh-alerts-*/_search` [8] | Alertas con `rule.level` alto. |
| Revisar una regla | `POST /wazuh-alerts-*/_search` [6] | Búsqueda por `rule.id`. |
| Revisar un agente | `POST /wazuh-alerts-*/_search` [2] | Búsqueda por `agent.id` o `agent.name`. |
| Sacar top reglas | `POST /wazuh-alerts-*/_search` [7] | Agregaciones para reporting. |

## Notas prácticas

- Si consultas alertas, piensa en el **Indexer API**, no en el **Server API**, porque ahí es donde realmente viven los documentos de alertas.[3][4]
- En muchos despliegues el índice se llama `wazuh-alerts-4.x-*`, aunque `wazuh-alerts-*` suele ser una forma cómoda de documentarlo de manera genérica.[6][7]
- Para certificados autofirmados, `curl` suele necesitar `-k`.[7][1]
- Si quieres explorar más campos disponibles, primero lanza una búsqueda corta con `_source` completo y luego ajusta filtros y agregaciones.[2][7]