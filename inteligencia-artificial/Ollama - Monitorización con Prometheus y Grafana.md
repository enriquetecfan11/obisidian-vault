---
title: "Ollama — Monitorización con Prometheus y Grafana"
type: resource
tags:
  - devops
  - grafana
  - ia
  - ia-local
  - monitorizacion
  - ollama
  - prometheus
status: active
project: none
date_created: 2026-10-30
date_modified: 2026-10-30
source: https://localaimaster.com/blog/ollama-prometheus-grafana
---
# Ollama — Monitorización con Prometheus y Grafana

> Resumen de la guía de **Local AI Master** (Barsha Mohapatra, 23-abr-2026): montar un stack de observabilidad open-source (Prometheus, DCGM exporter, sidecar de métricas, log-tail y Grafana) para Ollama en producción. Fuente: [Monitor Ollama with Prometheus & Grafana](https://localaimaster.com/blog/ollama-prometheus-grafana).

> Nota: nombres de imágenes Docker, IDs de dashboard de Grafana y el sidecar `ghcr.io/localaimaster/ollama-prom-sidecar` se toman tal cual del artículo; no verificados aquí de forma independiente.

## Resumen

Cuando Ollama «sigue respondiendo» pero va mucho más lento (throttling térmico, presión de memoria/KV cache, cola de peticiones), no se ve con un `ollama run` puntual. La guía monta dashboards de tokens/s, temperatura GPU, VRAM y errores, más alertas que saltan antes de que se queje el usuario. Arranque rápido: `docker compose up -d` → Prometheus `:9090`, Grafana `:3000` (admin/admin), DCGM `:9400`, sidecar Ollama `:9778`; importar dashboard Grafana **19628** para GPU.

## Por qué monitorizar

Tres fallos típicos (según el artículo) invisibles desde `ollama run`:

1. **Throttling térmico silencioso** — 4090 ~83 °C, A6000 ~88 °C; throughput cae 40–60 % hasta que enfría.
2. **Presión de memoria con contexto largo** — un 70B cómodo a 4K puede empezar a usar RAM de CPU a 16K; `free -h` engaña por la caché de archivos. Hay que mirar tamaño de KV cache y swap.
3. **Cola en ráfagas** — Ollama atiende por defecto en serie por modelo; sin profundidad de cola en el proxy no sabes si hace falta otra instancia o `OLLAMA_NUM_PARALLEL`.

## Las cuatro métricas que importan

| Métrica | Origen | Para qué |
| --- | --- | --- |
| `ollama_tokens_per_second` | custom / log-tail | Salud del modelo; caída ≥30 % vs baseline → throttle, cambio de modelo o de contexto |
| `DCGM_FI_DEV_GPU_TEMP` | DCGM | Temperatura del die (°C); sostenida >83 °C (consumer) / >88 °C (workstation) = problema |
| `DCGM_FI_DEV_FB_USED` (vs `_TOTAL`) | DCGM | VRAM usada; >95 % → OOM inminente con el siguiente prompt largo |
| `nginx_http_requests_total` + `nginx_upstream_response_time_seconds` | nginx-exporter | Rate, errores y latencia en el proxy; cola implícita cuando la latencia sube sin que baje el tok/s |

El resto (CPU, RAM, disco, red) es contexto de apoyo.

## Arquitectura

```
Grafana (:3000)
    │ PromQL
Prometheus (:9090)
    ├── DCGM exporter (:9400)     — GPU
    ├── node_exporter (:9100)     — host CPU/RAM/disco
    ├── nginx exporter (:9113)    — rate / latencia / errores
    ├── Ollama sidecar (:9778)    — modelos cargados y estado de cola vía API
    └── log-tail collector (:9779)— tokens/s por request desde /var/log/ollama.log
```

## Setup paso a paso

### 1. Layout del proyecto

```bash
mkdir -p ollama-monitoring/{prometheus,grafana,grafana/provisioning/dashboards,grafana/provisioning/datasources}
cd ollama-monitoring
```

### 2. `docker-compose.yml`

```yaml
version: '3.9'

services:
  prometheus:
    image: prom/prometheus:v2.51.2
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - ./prometheus/alerts.yml:/etc/prometheus/alerts.yml:ro
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.retention.time=30d'
      - '--web.enable-lifecycle'
    restart: unless-stopped

  grafana:
    image: grafana/grafana:10.4.2
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana-data:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
      - GF_USERS_ALLOW_SIGN_UP=false
    restart: unless-stopped

  dcgm-exporter:
    image: nvcr.io/nvidia/k8s/dcgm-exporter:3.3.5-3.4.1-ubuntu22.04
    container_name: dcgm-exporter
    ports:
      - "9400:9400"
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
    cap_add:
      - SYS_ADMIN
    restart: unless-stopped

  node-exporter:
    image: prom/node-exporter:v1.7.0
    container_name: node-exporter
    ports:
      - "9100:9100"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.rootfs=/rootfs'
      - '--path.sysfs=/host/sys'
    restart: unless-stopped

  ollama-sidecar:
    image: ghcr.io/localaimaster/ollama-prom-sidecar:0.4
    container_name: ollama-sidecar
    ports:
      - "9778:9778"
    environment:
      - OLLAMA_URL=http://host.docker.internal:11434
      - SCRAPE_INTERVAL=10
    extra_hosts:
      - "host.docker.internal:host-gateway"
    restart: unless-stopped

volumes:
  prometheus-data:
  grafana-data:
```

### 3. `prometheus/prometheus.yml`

```yaml
# prometheus/prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: ollama-prod

rule_files:
  - /etc/prometheus/alerts.yml

scrape_configs:
  - job_name: prometheus
    static_configs:
      - targets: ['localhost:9090']

  - job_name: dcgm
    static_configs:
      - targets: ['dcgm-exporter:9400']

  - job_name: node
    static_configs:
      - targets: ['node-exporter:9100']

  - job_name: ollama
    static_configs:
      - targets: ['ollama-sidecar:9778']

  - job_name: nginx
    static_configs:
      - targets: ['host.docker.internal:9113']
```

### 4. Colector de tokens/s desde el log

El sidecar cubre estado básico. Para tok/s por request (Ollama lo escribe como `eval rate` en el log, no en `/api/tags`), el artículo propone un colector en `/usr/local/bin/ollama-token-collector.sh` escuchando en `:9779`, y añadir el target a Prometheus:

```
- targets: ['host.docker.internal:9779']
```

Script (tal cual en la guía):

```bash
# /usr/local/bin/ollama-token-collector.sh
#!/usr/bin/env bash
set -euo pipefail

LOG=/var/log/ollama.log
PORT=9779

# Tiny Prometheus textfile collector that parses Ollama "eval rate" lines
exec python3 - <<'PY'
import http.server, re, threading, time
from collections import defaultdict, deque

EVAL_RE = re.compile(r'eval rate:\s+([0-9.]+)\s+tokens/s.*model=(\S+)')
samples = defaultdict(lambda: deque(maxlen=512))

def tail():
    with open('/var/log/ollama.log') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.2); continue
            m = EVAL_RE.search(line)
            if m:
                samples[m.group(2)].append(float(m.group(1)))

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain'); self.end_headers()
        out = ['# TYPE ollama_tokens_per_second gauge']
        for model, vals in samples.items():
            if vals:
                avg = sum(vals)/len(vals)
                out.append(f'ollama_tokens_per_second{{model="{model}"}} {avg}')
        self.wfile.write(('\n'.join(out) + '\n').encode())

threading.Thread(target=tail, daemon=True).start()
http.server.HTTPServer(('0.0.0.0', 9779), Handler).serve_forever()
PY
```

### 5. Arrancar y verificar

```bash
docker compose up -d
docker compose ps
```

Abrir `http://localhost:9090/targets`: todos `UP` en ~30 s. Si falta `dcgm-exporter`, comprobar NVIDIA Container Toolkit con:

```bash
docker run --rm --gpus all nvidia/cuda:12.4.0-base-ubuntu22.04 nvidia-smi
```

## Dashboards en Grafana

Datasource Prometheus → `http://prometheus:9090`.

**Overview Ollama** (queries del artículo):

```promql
avg by (model) (ollama_tokens_per_second)
```

```promql
(DCGM_FI_DEV_FB_USED / DCGM_FI_DEV_FB_TOTAL) * 100
```

```promql
DCGM_FI_DEV_GPU_TEMP
```

Umbrales sugeridos en temperatura: 75 (amarillo) y 83 (rojo) en tarjetas consumer.

```promql
sum(rate(nginx_http_requests_total[1m])) by (status)
```

```promql
histogram_quantile(0.95, sum by (le) (rate(nginx_http_request_duration_seconds_bucket[5m])))
```

**GPU deep dive:** importar dashboard comunitario Grafana ID **19628** (utilización, memoria, temperatura, potencia, PCIe, NVLink).

## Alertas (`prometheus/alerts.yml`)

```yaml
groups:
  - name: ollama
    interval: 30s
    rules:
      - alert: OllamaGpuTemperatureHigh
        expr: DCGM_FI_DEV_GPU_TEMP > 83
        for: 5m
        labels: { severity: warning }
        annotations:
          summary: GPU {{ $labels.gpu }} hot
          description: "{{ $labels.gpu }} at {{ $value }}C for 5+ minutes — throttling likely."

      - alert: OllamaGpuMemoryNearFull
        expr: (DCGM_FI_DEV_FB_USED / DCGM_FI_DEV_FB_TOTAL) > 0.95
        for: 2m
        labels: { severity: critical }
        annotations:
          summary: GPU {{ $labels.gpu }} VRAM > 95%
          description: "OOM imminent on the next long prompt."

      - alert: OllamaThroughputDegraded
        expr: |
          (
            avg_over_time(ollama_tokens_per_second[10m])
            /
            avg_over_time(ollama_tokens_per_second[24h] offset 1h)
          ) < 0.5
        for: 10m
        labels: { severity: warning }
        annotations:
          summary: Ollama throughput halved vs 24h baseline
          description: "Likely thermal throttle, contention, or quantization mismatch."

      - alert: OllamaErrorRateHigh
        expr: |
          sum(rate(nginx_http_requests_total{status=~"5.."}[5m]))
          / sum(rate(nginx_http_requests_total[5m]))
          > 0.01
        for: 10m
        labels: { severity: critical }
        annotations:
          summary: Ollama 5xx rate > 1%
          description: "Reverse proxy is returning errors — check upstream Ollama."

      - alert: OllamaQueueBacklog
        expr: avg_over_time(nginx_upstream_active_connections[5m]) > 20
        for: 5m
        labels: { severity: warning }
        annotations:
          summary: Ollama queue > 20 concurrent
          description: "Consider raising OLLAMA_NUM_PARALLEL or scaling out."
```

Recargar sin reiniciar:

```bash
curl -X POST http://localhost:9090/-/reload
```

Alertmanager para email / Slack / PagerDuty (detalle en la doc oficial de Alertmanager).

## Comparativa de stacks (según el artículo)

| Stack | Setup | Coste storage | GPU | Mejor para |
| --- | --- | --- | --- | --- |
| Prometheus + Grafana + DCGM | 30–60 min | $0 self-hosted | Excelente | Self-hosted, un equipo |
| Datadog | 10 min | $$$$ | Bueno | SaaS, equipos grandes sin SRE |
| New Relic | 15 min | $$$ | Decente | Multi-app, stack mixto |
| OpenTelemetry + Tempo + Loki + Mimir | 2–4 h | $0 self-hosted | Bueno | Pipeline OTel ya existente |
| Netdata | 5 min | $0 | Básico | Solo / un host |

Prometheus + Grafana gana para quien autoalojá Ollama (gratis + mejor integración GPU vía DCGM + dashboard 19628).

## Pitfalls / anti-patrones

1. **Scrape demasiado frecuente** — 15 s está bien; <5 s genera mucho más dato y apenas aporta.
2. **Alertar en una sola muestra** — sin `for: 5m` un pico de 91 °C al cargar el modelo te pagina en falso.
3. **Calcular tok/s desde `/api/tags`** — solo lista modelos; el timing de eval va en el payload de respuesta o en el log → usar el log-tail o instrumentar el cliente.
4. **TSDB de Prometheus en el mismo NVMe que los modelos** — Prometheus ~10 MB/min; cargar modelos lee decenas de GB → stalls. Separar disco/host.
5. **No versionar dashboards** — sin provisioning en `grafana/provisioning/dashboards`, se pierden al resetear el volumen.

## Relacionado

- [[Ollama Docker]] — exponer Ollama a contenedores / n8n
- [[MOC IA Local]] — mapa de IA local (llama.cpp / Ollama)
- [[MOC DevOps]] — monitorización e infraestructura
- [[Docker]] — cheatsheet Docker
- [[Mara OS]] — Mara OS usa Ollama como backend LLM
- [[Ornith en tu homelab - instalar y conectar a n8n y Hermes]] — modelo local servido a n8n/Hermes
