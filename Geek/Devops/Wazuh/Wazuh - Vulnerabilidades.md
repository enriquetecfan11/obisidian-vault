---
type:
tags:
  - geek
  - devops
  - automation
  - wazuh
status: active
updated: 2026-05-13
---
## Autenticación (JWT)

```bash
TOKEN=$(curl -sk -u admin:PASSWORD \
  -X POST "https://localhost:55000/security/user/authenticate?raw=true")
```

---

## REST API (puerto 55000)
> ⚠️ Disponible principalmente en Wazuh < 4.7

### Listar vulnerabilidades de un agente

```bash
curl -sk -H "Authorization: Bearer ${TOKEN}" \
  "https://localhost:55000/vulnerability/001?limit=500&severity=Critical" \
  | jq '.data.affected_items[] | {cve, name, severity, version}'
```

### Resumen de vulnerabilidades por campo

```bash
curl -sk -H "Authorization: Bearer ${TOKEN}" \
  "https://localhost:55000/vulnerability/001/summary/severity"
```

---

## Indexer API (puerto 9200)
> ✅ Recomendado desde Wazuh v4.7+

### Todas las vulnerabilidades

```bash
curl -k -u admin:PASSWORD \
  "https://<INDEXER_IP>:9200/wazuh-states-vulnerabilities/_search?pretty" \
  -H "Content-Type: application/json" \
  -d '{
    "query": { "match_all": {} },
    "size": 5000
  }'
```

### Filtrar por severidad (Critical / High)

```bash
curl -k -u admin:PASSWORD \
  "https://<INDEXER_IP>:9200/wazuh-states-vulnerabilities/_search?pretty" \
  -H "Content-Type: application/json" \
  -d '{
    "query": {
      "terms": {
        "vulnerability.severity": ["Critical", "High"]
      }
    },
    "sort": [{ "vulnerability.score.base": { "order": "desc" } }]
  }'
```

### Vulnerabilidades de un agente específico

```bash
curl -k -u admin:PASSWORD \
  "https://<INDEXER_IP>:9200/wazuh-states-vulnerabilities-*/_search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": {
      "bool": {
        "must": [{ "match": { "agent.id": "001" } }]
      }
    },
    "_source": [
      "package.name",
      "package.version",
      "vulnerability.severity",
      "vulnerability.score.base",
      "vulnerability.id",
      "vulnerability.published_at"
    ]
  }'
```

### Resumen por severidad (aggregation)

```bash
curl -k -u admin:PASSWORD \
  "https://<INDEXER_IP>:9200/wazuh-states-vulnerabilities/_search" \
  -H "Content-Type: application/json" \
  -d '{
    "size": 0,
    "aggs": {
      "by_severity": {
        "terms": { "field": "vulnerability.severity" }
      }
    }
  }'
```

### Top 10 CVEs más frecuentes

```bash
curl -k -u admin:PASSWORD \
  "https://<INDEXER_IP>:9200/wazuh-states-vulnerabilities/_search" \
  -H "Content-Type: application/json" \
  -d '{
    "size": 0,
    "aggs": {
      "top_cves": {
        "terms": {
          "field": "vulnerability.id",
          "size": 10
        }
      }
    }
  }'
```
