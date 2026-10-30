# Hermes API — Referencia de curls

> `hermes serve` · REST + WebSocket · Puerto: **9119** · IP: **192.168.1.196**

## Servidor

El servidor corre como servicio systemd permanente con `--host 0.0.0.0`, accesible desde toda la red local. Se gestiona con:

```bash
systemctl --user status hermes-serve   # estado
systemctl --user restart hermes-serve  # reiniciar
systemctl --user stop hermes-serve     # parar
```

## Autenticación

El servidor usa **HTTP Basic Auth**. Credenciales:

| Campo | Valor |
|---|---|
| Usuario | `admin` |
| Contraseña | `3_QE_PwIymuVs9bI8Iomlg` |

Todos los curls llevan `-u "admin:3_QE_PwIymuVs9bI8Iomlg"`. Define la variable una vez:

```bash
HERMES_HOST="http://192.168.1.196:9119"
AUTH="admin:3_QE_PwIymuVs9bI8Iomlg"

# Prueba rápida:
curl -s -u "$AUTH" $HERMES_HOST/api/health
# → {"ok":true,...}
```

---

## 🔑 Auth & Token

### `GET /api/auth/me` — Identidad del usuario actual
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/auth/me" | python3 -m json.tool
```
> En modo loopback devuelve `provider: "loopback"`. Sin token válido → 401.

### `POST /api/auth/ws-ticket` — Ticket de un solo uso para WebSocket
```bash
curl -s -X POST \
  -u "$AUTH" \
  "$HERMES_HOST/api/auth/ws-ticket" | python3 -m json.tool
```
> Expira en ~30 s. Úsalo como `?ticket=…` al conectar por WebSocket en modo gated.

---

## 📡 Estado del servidor

### `GET /api/health` — Health check básico
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/health"
```

### `GET /api/status` — Estado completo (gateway, plataformas, agentes)
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/status" | python3 -m json.tool
```

### `GET /api/system/stats` — Estadísticas del sistema (CPU, RAM, disco)
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/system/stats" | python3 -m json.tool
```

### `GET /api/host/identity` — Identidad del host
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/host/identity" | python3 -m json.tool
```

---

## 💬 Sesiones

### `GET /api/sessions` — Listar sesiones
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/sessions?profile=default&order=recent" | python3 -m json.tool
```
> Parámetros: `profile`, `order=created|recent`, `source`.

### `GET /api/sessions/search` — Buscar sesiones por texto
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/sessions/search?q=mi+consulta&profile=default" | python3 -m json.tool
```

### `GET /api/sessions/{id}` — Obtener sesión por ID
```bash
SESSION_ID="tu-session-id"

curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/sessions/$SESSION_ID" | python3 -m json.tool
```

### `GET /api/sessions/{id}/messages` — Mensajes de una sesión
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/sessions/$SESSION_ID/messages" | python3 -m json.tool
```

### `GET /api/sessions/{id}/timeline` — Timeline (herramientas, tokens, costes)
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/sessions/$SESSION_ID/timeline" | python3 -m json.tool
```

### `GET /api/sessions/{id}/export` — Exportar sesión como Markdown
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/sessions/$SESSION_ID/export" \
  -o "sesion-$SESSION_ID.md"
```

### `PATCH /api/sessions/{id}` — Renombrar o archivar una sesión
```bash
curl -s -X PATCH \
  -u "$AUTH" \
  -H "Content-Type: application/json" \
  -d '{"title": "Nuevo nombre", "archived": false}' \
  "$HERMES_HOST/api/sessions/$SESSION_ID" | python3 -m json.tool
```

### `DELETE /api/sessions/{id}` — Eliminar una sesión
```bash
curl -s -X DELETE \
  -u "$AUTH" \
  "$HERMES_HOST/api/sessions/$SESSION_ID"
```

### `GET /api/sessions/stats` — Estadísticas globales de sesiones
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/sessions/stats?profile=default" | python3 -m json.tool
```

### `POST /api/sessions/bulk-delete` — Eliminar varias sesiones
```bash
curl -s -X POST \
  -u "$AUTH" \
  -H "Content-Type: application/json" \
  -d '{"session_ids": ["id1", "id2", "id3"]}' \
  "$HERMES_HOST/api/sessions/bulk-delete"
```

### `POST /api/sessions/prune` — Limpiar sesiones vacías
```bash
curl -s -X POST \
  -u "$AUTH" \
  -H "Content-Type: application/json" \
  -d '{}' \
  "$HERMES_HOST/api/sessions/prune" | python3 -m json.tool
```

---

## 🧠 Modelos

### `GET /api/model/info` — Modelo activo y proveedor
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/model/info?profile=default" | python3 -m json.tool
```

### `GET /api/model/options` — Modelos disponibles
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/model/options?profile=default&include_unconfigured=1" | python3 -m json.tool
```

### `GET /api/model/recommended-default` — Modelo recomendado
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/model/recommended-default?profile=default" | python3 -m json.tool
```

### `POST /api/model/set` — Cambiar el modelo activo
```bash
curl -s -X POST \
  -u "$AUTH" \
  -H "Content-Type: application/json" \
  -d '{"model": "anthropic/claude-sonnet-4-6", "provider": "anthropic"}' \
  "$HERMES_HOST/api/model/set?profile=default" | python3 -m json.tool
```

### `GET /api/model/auxiliary` — Modelos auxiliares (resumen, cron…)
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/model/auxiliary?profile=default" | python3 -m json.tool
```

### `GET /api/model/moa` — Configuración Mixture of Agents
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/model/moa?profile=default" | python3 -m json.tool
```

---

## ⚙️ Configuración

### `GET /api/config` — Leer config.yaml
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/config?profile=default" | python3 -m json.tool
```

### `GET /api/config/schema` — Esquema JSON de la configuración
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/config/schema" | python3 -m json.tool
```

### `PUT /api/config` — Actualizar config.yaml (merge parcial)
```bash
curl -s -X PUT \
  -u "$AUTH" \
  -H "Content-Type: application/json" \
  -d '{"agent": {"reasoning_effort": "medium"}}' \
  "$HERMES_HOST/api/config?profile=default" | python3 -m json.tool
```

### `GET /api/env` — Listar variables de entorno del perfil
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/env?profile=default" | python3 -m json.tool
```

### `PUT /api/env` — Añadir o actualizar variable de entorno
```bash
curl -s -X PUT \
  -u "$AUTH" \
  -H "Content-Type: application/json" \
  -d '{"key": "MI_VAR", "value": "mi_valor"}' \
  "$HERMES_HOST/api/env?profile=default"
```

### `DELETE /api/env` — Eliminar variable de entorno
```bash
curl -s -X DELETE \
  -u "$AUTH" \
  -H "Content-Type: application/json" \
  -d '{"key": "MI_VAR"}' \
  "$HERMES_HOST/api/env?profile=default"
```

---

## 🎯 Skills & Tools

### `GET /api/skills` — Listar skills instaladas
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/skills?profile=default" | python3 -m json.tool
```

### `GET /api/tools/toolsets` — Toolsets disponibles y activos
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/tools/toolsets?profile=default" | python3 -m json.tool
```

---

## 🔌 MCP Servers

### `GET /api/mcp` — Listar servidores MCP
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/mcp?profile=default" | python3 -m json.tool
```

---

## 🧩 Memoria

### `GET /api/memory` — Configuración del proveedor de memoria
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/memory?profile=default" | python3 -m json.tool
```

---

## 📨 Gateway & Mensajería

### `GET /api/gateway` — Estado del gateway
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/gateway?profile=default" | python3 -m json.tool
```

### `GET /api/messaging/platforms` — Plataformas de mensajería configuradas
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/messaging/platforms?profile=default" | python3 -m json.tool
```

---

## ⏰ Cron Jobs

### `GET /api/cron` — Listar cron jobs
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/cron" | python3 -m json.tool
```

---

## 🗂️ Curator

### `GET /api/curator` — Estado del curator
```bash
curl -s \
  -u "$AUTH" \
  "$HERMES_HOST/api/curator?profile=default" | python3 -m json.tool
```

### `PUT /api/curator/paused` — Pausar o reanudar el curator
```bash
# Pausar
curl -s -X PUT \
  -u "$AUTH" \
  -H "Content-Type: application/json" \
  -d '{"paused": true}' \
  "$HERMES_HOST/api/curator/paused?profile=default"

# Reanudar
curl -s -X PUT \
  -u "$AUTH" \
  -H "Content-Type: application/json" \
  -d '{"paused": false}' \
  "$HERMES_HOST/api/curator/paused?profile=default"
```

### `POST /api/curator/run` — Lanzar el curator manualmente
```bash
curl -s -X POST \
  -u "$AUTH" \
  -H "Content-Type: application/json" \
  -d '{}' \
  "$HERMES_HOST/api/curator/run?profile=default"
```

---

## ⚡ WebSocket

> Requiere `websocat` (`cargo install websocat`) o `wscat` (`npm i -g wscat`).

### `/api/pty` — Terminal PTY (hermes --tui)
```bash
websocat "ws://${HERMES_HOST#http://}/api/pty?token=$TOKEN"
# o con wscat:
wscat -c "ws://${HERMES_HOST#http://}/api/pty?token=$TOKEN"
```
> Bytes PTY en bruto. El resize viaja como `\x1b[RESIZE:<cols>;<rows>]`.

### `/api/ws` — JSON-RPC sobre WebSocket
```bash
websocat "ws://${HERMES_HOST#http://}/api/ws?token=$TOKEN"
```

### `/api/events` — Feed de eventos del sidebar
```bash
CHANNEL="default"
websocat "ws://${HERMES_HOST#http://}/api/events?token=$TOKEN&channel=$CHANNEL"
```
