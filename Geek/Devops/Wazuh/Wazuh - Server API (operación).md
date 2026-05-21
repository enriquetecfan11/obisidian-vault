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


Esta nota resume los endpoints de la **Wazuh Server API** (puerto 55000) que son útiles para operación: estado de agentes, manager y cluster, más algunos patrones de automatización. [web:53][web:66]

## 1. Variables base

```bash
export WAZUH_HOST="https://IP_O_HOSTNAME:55000"
export WAZUH_USER="tu_usuario"
export WAZUH_PASS="tu_password"
export TOKEN=$(curl -sku "$WAZUH_USER:$WAZUH_PASS" \
  -X GET "$WAZUH_HOST/security/user/authenticate?raw=true")
```

Comprueba que `TOKEN` no está vacío y tiene pinta de JWT (tres bloques separados por puntos). [web:3][web:66]

## 2. Health check básico de la API

```bash
curl -sk -H "Authorization: Bearer $TOKEN" \
  "$WAZUH_HOST/?pretty=true"
```

Devuelve información general de la API y confirma que autenticación + conectividad funcionan. [web:3][web:53]

## 3. Agentes

### 3.1 Listar todos los agentes

```bash
curl -sk -X GET "$WAZUH_HOST/agents?pretty=true&limit=500" \
  -H "Authorization: Bearer $TOKEN"
```

### 3.2 Agentes por estado

```bash
# Activos
curl -sk -X GET "$WAZUH_HOST/agents?status=active&pretty=true" \
  -H "Authorization: Bearer $TOKEN"

# Desconectados
curl -sk -X GET "$WAZUH_HOST/agents?status=disconnected&pretty=true" \
  -H "Authorization: Bearer $TOKEN"
```

Patrón típico para scripts de health check de agentes. [web:66][web:92]

### 3.3 Detalle de un agente

```bash
curl -sk -X GET "$WAZUH_HOST/agents/001?pretty=true" \
  -H "Authorization: Bearer $TOKEN"
```

### 3.4 Último keepalive de un agente

```bash
curl -sk -X GET "$WAZUH_HOST/agents/001?pretty=true" \
  -H "Authorization: Bearer $TOKEN" \
  | jq '.data.affected_items.lastKeepAlive'
```

Útil para detectar agentes “zombies” que llevan tiempo sin reportar. [web:92][web:66]

## 4. Manager

### 4.1 Estado del manager

```bash
curl -sk -X GET "$WAZUH_HOST/manager/status?pretty=true" \
  -H "Authorization: Bearer $TOKEN"
```

### 4.2 Estadísticas de daemons

```bash
curl -sk -X GET "$WAZUH_HOST/manager/daemons/stats?pretty=true" \
  -H "Authorization: Bearer $TOKEN"
```

### 4.3 Información de configuración del manager

```bash
curl -sk -X GET "$WAZUH_HOST/manager/configuration?pretty=true" \
  -H "Authorization: Bearer $TOKEN"
```

Estos endpoints son la base para health checks y dashboards de estado de la plataforma. [web:66][web:74]

## 5. Cluster

Si tienes un despliegue con cluster, estos endpoints te permiten ver la salud de master y workers. [web:66][web:74]

```bash
# Info general del cluster
curl -sk -X GET "$WAZUH_HOST/cluster/status?pretty=true" \
  -H "Authorization: Bearer $TOKEN"

# Nodos del cluster
curl -sk -X GET "$WAZUH_HOST/cluster/nodes?pretty=true" \
  -H "Authorization: Bearer $TOKEN"
```

## 6. Información de reglas y configuración

No es “operación” pura, pero ayuda a documentar qué está cargado en el manager. [web:53][web:3]

```bash
# Listar reglas (paginado)
curl -sk -X GET "$WAZUH_HOST/rules?pretty=true&limit=50" \
  -H "Authorization: Bearer $TOKEN"
```

## 7. Patrones de automatización

### 7.1 Script de check rápido de agentes desconectados

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

Este patrón es ideal para enganchar en n8n, cronjobs o tu sistema multi‑agente y generar alertas operativas cuando haya muchos agentes desconectados. [web:66][web:92]

### 7.2 Health check del manager para monitorización externa

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

Puedes usar esta salida como métrica simple para Prometheus, Zabbix o cualquier sistema de monitorización externo. [web:66][web:107]