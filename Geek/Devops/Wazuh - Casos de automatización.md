---
type: nota
tags:
  - wazuh
  - devops
  - geek
  - ordenador
  - api-rest
status: active
pipeline: raw
updated: 2026-05-13
source:
---
Esta nota recoge patrones prácticos para automatizar operación y seguridad con la Wazuh Server API e Indexer API (scripts, n8n, agentes, etc.). [web:66][web:58][web:81]

## 1. Health checks automáticos

### 1.1 Comprobar estado del manager

```bash
#!/usr/bin/env bash
set -euo pipefail

WAZUH_HOST="https://IP_O_HOSTNAME:55000"
WAZUH_USER="tu_usuario"
WAZUH_PASS="tu_password"

TOKEN=$(curl -sku "$WAZUH_USER:$WAZUH_PASS" \
  -X GET "$WAZUH_HOST/security/user/authenticate?raw=true")

STATUS=$(curl -sk -X GET "$WAZUH_HOST/manager/status" \
  -H "Authorization: Bearer $TOKEN" \
  | jq -r '.data.affected_items.status')

if [[ "$STATUS" != "running" ]]; then
  echo "WAZUH_MANAGER_STATUS{status=\"$STATUS\"} 0"
  exit 1
fi

echo "WAZUH_MANAGER_STATUS{status=\"$STATUS\"} 1"
```

Puedes llamar a este script desde cron, n8n o un exporter para Prometheus. [web:66][web:138]

### 1.2 Detectar agentes desconectados

```bash
#!/usr/bin/env bash
set -euo pipefail

WAZUH_HOST="https://IP_O_HOSTNAME:55000"
WAZUH_USER="tu_usuario"
WAZUH_PASS="tu_password"

TOKEN=$(curl -sku "$WAZUH_USER:$WAZUH_PASS" \
  -X GET "$WAZUH_HOST/security/user/authenticate?raw=true")

curl -sk -X GET "$WAZUH_HOST/agents?status=disconnected&pretty=true" \
  -H "Authorization: Bearer $TOKEN" \
  | jq '.data.affected_items[] | {id, name, lastKeepAlive}'
```

A partir de esta salida puedes disparar correos, mensajes a Teams/Slack o tickets. [web:92][web:140]

## 2. Automatización sobre alertas (Indexer API)

### 2.1 Alertas críticas recientes → webhook

```bash
#!/usr/bin/env bash
set -euo pipefail

INDEXER_HOST="https://IP_O_HOSTNAME:9200"
INDEXER_USER="admin"
INDEXER_PASS="tu_password"
ALERT_INDEX="wazuh-alerts-*"
WEBHOOK_URL="https://tu-servicio-webhook"

PAYLOAD=$(curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_search" \
  -H 'Content-Type: application/json' \
  -d '{
    "size": 20,
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
      "range": {
        "rule.level": {
          "gte": 12
        }
      }
    }
  }')

curl -X POST "$WEBHOOK_URL" \
  -H 'Content-Type: application/json' \
  -d "$PAYLOAD"
```

Patrón base para notificar alertas críticas a otro sistema (SOAR, Teams, n8n, etc.). [web:81][web:82][web:155]

### 2.2 Métrica de volumen de alertas

```bash
INDEXER_HOST="https://IP_O_HOSTNAME:9200"
INDEXER_USER="admin"
INDEXER_PASS="tu_password"
ALERT_INDEX="wazuh-alerts-*"

COUNT=$(curl -sku "$INDEXER_USER:$INDEXER_PASS" \
  -X POST "$INDEXER_HOST/$ALERT_INDEX/_count" \
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
  }' | jq '.count')

echo "WAZUH_ALERTS_LAST_5M $COUNT"
```

Puedes usar el valor como métrica simple para dashboards de carga o detección de picos. [web:60][web:58]

## 3. Integraciones con ticketing / SOAR

Wazuh permite integrar alertas con sistemas externos usando scripts (integrator) o directamente desde tus pipelines. [web:155][web:158]

Patrón típico (pseudo‑flujo):

1. Filtro de alertas en el indexer (por nivel/condiciones).
2. Script Python/Bash que mapea alerta → ticket (campos, prioridad).
3. POST contra la API de tu sistema de tickets (Jira, Teams “ticketing as a service”, etc.). [web:155][web:161]

Ejemplo mínimo de POST genérico (pseudo‑código curl):

```bash
curl -X POST "https://ticketing/api/tickets" \
  -H "Authorization: Bearer TU_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Alerta Wazuh crítica",
    "severity": "high",
    "source": "wazuh",
    "payload": { ... }
  }'
```

## 4. Active Response vía API (respuesta)

Si quieres ir más allá de la alerta y ejecutar acciones (bloquear IP, limpiar iptables, etc.) puedes usar Active Response. [web:103][web:160]

Ejemplo de llamada API (simplificado; asume que ya tienes el comando configurado y script desplegado):

```bash
curl -sk -X PUT "$WAZUH_HOST/active-response?agents_list=001&pretty=true" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "command": "!flushIpTables",
    "custom": true,
    "alert": {
      "data": {
        "srcip": "1.2.3.4"
      }
    }
  }'
```

Aquí `flushIpTables` es un script de ejemplo que limpia reglas de iptables, registrado en `ossec.conf` y con permisos correctos. [web:154][web:160][web:163]

## 5. Ideas concretas para tu stack

- **n8n / agentes**: Encadenar health check de agentes + query de alertas críticas + envío de resumen diario a Obsidian o a un canal de chat. [web:66][web:81]
- **Mara/OpenClaw**: Agente que, al pedirle “estado de seguridad”, llame a tus scripts de indexer y server API y escriba un resumen en una nota diaria en Obsidian. [web:58][web:159]
- **Tuning continuo**: Job semanal que calcula top reglas y top agentes ruidosos y abre una “tarea de tuning” con la lista de reglas a revisar. [web:81][web:150]