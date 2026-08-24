---
type: nota
tags:
  - wazuh
  - geek
  - api-rest
  - devops
status: active
created: 2026-05-13
updated: 2026-05-13
title: wazuh-indexer-api-alerts
project: none
date_created: 2026-05-13
date_modified: 2026-05-13
---
# Wazuh - Indexer API (alertas)

La **Wazuh Indexer API** (puerto 9200) es la que se usa para leer y explotar alertas, porque los documentos de alertas viven en índices como `wazuh-alerts-*` o `wazuh-alerts-4.x-*`. [web:58][web:148][web:86]

## 1. Variables base

```bash
export INDEXER_HOST="https://IP_O_HOSTNAME:9200"
export INDEXER_USER="admin"
export INDEXER_PASS="tu_password"
export ALERT_INDEX="wazuh-alerts-*"
```

Las credenciales suelen ser las mismas que usas para entrar al dashboard (`admin` / contraseña generada en instalación). [web:86][web:58]

## 2. Búsqueda básica de alertas

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 10,
    "sort": [
      { "timestamp": { "order": "desc" } }
    ],
    "query": {
      "match_all": {}
    }
  }'
```

Devuelve las últimas alertas (10 por defecto), ordenadas por `timestamp` descendente. [web:86][web:58]

## 3. Contar alertas (métrica rápida)

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

Es útil para tener contadores de alertas sin traer todo el payload a tu script. [web:60][web:58]

## 4. Últimas alertas de la última hora

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 50,
    "sort": [
      { "timestamp": { "order": "desc" } }
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

Clásico para ver actividad reciente o alimentar dashboards en tiempo casi real. [web:12][web:83]

## 5. Alertas por severidad (`rule.level`)

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 25,
    "sort": [
      { "timestamp": { "order": "desc" } }
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

Filtra alertas de nivel alto (por ejemplo ≥ 12), que suelen corresponder a eventos importantes/críticos según la clasificación de reglas de Wazuh. [web:82][web:150][web:152]

## 6. Alertas por `rule.id`

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 20,
    "sort": [
      { "timestamp": { "order": "desc" } }
    ],
    "query": {
      "term": {
        "rule.id": "5710"
      }
    }
  }'
```

Sirve para investigar una regla concreta (propia o de Wazuh) y ver qué está generando. [web:83][web:147]

## 7. Alertas por agente (`agent.id` / `agent.name`)

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 20,
    "sort": [
      { "timestamp": { "order": "desc" } }
    ],
    "query": {
      "term": {
        "agent.id": "001"
      }
    }
  }'
```

Puedes cambiar a `agent.name` si te resulta más cómodo, depende de cómo etiquetes los agentes. [web:60][web:58]

## 8. Alertas por origen, servicio o grupo

Ejemplo filtrando por `decoder.name` (por ejemplo, sshd):

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

También puedes usar campos como `data.srcip`, `rule.groups`, `manager.name` o etiquetas de agente (`agent.labels.*`). [web:58][web:149]

## 9. Top reglas (agregación)

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

Devuelve un top‑10 de reglas más disparadas, muy útil para tuning y para detectar ruido. [web:12][web:81][web:151]

## 10. Seleccionar solo algunos campos (`_source`)

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search?pretty" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 10,
    "_source": [
      "timestamp",
      "rule.id",
      "rule.level",
      "rule.description",
      "agent.id",
      "agent.name"
    ],
    "sort": [
      { "timestamp": { "order": "desc" } }
    ],
    "query": {
      "match_all": {}
    }
  }'
```

Ayuda a reducir tamaño de respuesta cuando solo quieres campos clave para logs, dashboards o notificaciones. [web:60][web:151]

## 11. Obtener una alerta por `_id` de documento

```bash
curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X GET "$INDEXER_HOST/$ALERT_INDEX/_doc/ID_DEL_DOCUMENTO?pretty"
```

Útil cuando desde un dashboard ves un `_id` concreto y quieres resolverlo vía API. [web:58][web:60]

## 12. Casos de uso típicos
v

| Caso                              | Endpoint / patrón                          | Descripción |
|----------------------------------|--------------------------------------------|------------|
| Últimas alertas                  | `POST /wazuh-alerts-*/_search` [web:86]    | Listado general ordenado por fecha. |
| Alertas críticas                 | `range` sobre `rule.level` [web:82]        | Solo eventos de alta severidad. |
| Actividad de un agente           | `term` sobre `agent.id` [web:83]           | Ver qué le pasa a un host concreto. |
| Top reglas / ruido               | `aggs` por `rule.id` [web:81]              | Reglas más disparadas. |
| Volumen de alertas               | `POST /_count` [web:60]                    | Métrica rápida para dashboards. |

## 13. Notas rápidas

- Piensa en el indexer como tu capa de **analytics** en tiempo casi real para alertas y eventos. [web:148][web:81]
- Estos patrones se pueden enchufar fácilmente a scripts, n8n o servicios propios para enviar notificaciones, generar informes o alimentar Grafana. [web:89][web:151]
- Ajusta `ALERT_INDEX` según tu versión: en muchos despliegues es `wazuh-alerts-4.x-*`. [web:86][web:12]