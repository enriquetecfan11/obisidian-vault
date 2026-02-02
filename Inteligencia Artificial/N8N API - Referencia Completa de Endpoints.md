---
tags:
  - n8n
  - api
  - documentacion
  - inteligenciartificial
ai_share: "true"
---
## 🔐 Autenticación

La API requiere autenticación mediante **API Key** o **JWT**, según la configuración del servidor.

### Cabecera de Seguridad

```http
Authorization: Bearer <API_KEY>
```

**Ejemplo:**

```bash
curl -H "Authorization: Bearer n8n_api_1234567890abcdef" \
     https://tu-n8n-instance.com/api/v1/workflows
```

---

## 👥 Users

Operaciones sobre usuarios del sistema.

### Endpoints Disponibles

|Método|Endpoint|Descripción|
|---|---|---|
|`GET`|`/users`|Obtener todos los usuarios|
|`POST`|`/users`|Crear múltiples usuarios|
|`GET`|`/users/{id}`|Obtener usuario por ID/Email|
|`DELETE`|`/users/{id}`|Eliminar un usuario|
|`PATCH`|`/users/{id}/role`|Cambiar rol global de un usuario|

### Ejemplos de Uso

**Obtener todos los usuarios:**

```bash
GET /users
```

**Crear usuarios:**

```bash
POST /users
Content-Type: application/json

{
  "users": [
    {
      "email": "usuario@ejemplo.com",
      "firstName": "Juan",
      "lastName": "Pérez",
      "role": "global:member"
    }
  ]
}
```

**Cambiar rol de usuario:**

```bash
PATCH /users/{id}/role
Content-Type: application/json

{
  "newRoleName": "global:admin"
}
```

---

## 🔍 Audit

Operaciones de auditoría de seguridad.

### Endpoints Disponibles

|Método|Endpoint|Descripción|
|---|---|---|
|`POST`|`/audit`|Generar un reporte de auditoría|

### Ejemplo de Uso

```bash
POST /audit
Content-Type: application/json

{
  "startDate": "2026-01-01",
  "endDate": "2026-02-01",
  "eventTypes": ["workflow.created", "user.login"]
}
```

---

## ▶️ Executions

Operaciones sobre ejecuciones de workflows.

### Endpoints Disponibles

|Método|Endpoint|Descripción|
|---|---|---|
|`GET`|`/executions`|Obtener todas las ejecuciones|
|`GET`|`/executions/{id}`|Obtener una ejecución específica|
|`DELETE`|`/executions/{id}`|Eliminar una ejecución|

### Ejemplos de Uso

**Listar ejecuciones:**

```bash
GET /executions?limit=50&status=success
```

**Obtener detalles de una ejecución:**

```bash
GET /executions/12345
```

**Eliminar una ejecución:**

```bash
DELETE /executions/12345
```

---

## 🔄 Workflows

Operaciones sobre workflows (flujos de trabajo).

### Endpoints Disponibles

|Método|Endpoint|Descripción|
|---|---|---|
|`POST`|`/workflows`|Crear un workflow|
|`GET`|`/workflows`|Obtener todos los workflows|
|`GET`|`/workflows/{id}`|Obtener un workflow|
|`DELETE`|`/workflows/{id}`|Eliminar un workflow|
|`PUT`|`/workflows/{id}`|Actualizar un workflow|
|`POST`|`/workflows/{id}/activate`|Activar un workflow|
|`POST`|`/workflows/{id}/deactivate`|Desactivar un workflow|
|`PUT`|`/workflows/{id}/transfer`|Transferir workflow a otro proyecto|
|`GET`|`/workflows/{id}/tags`|Obtener etiquetas de un workflow|
|`PUT`|`/workflows/{id}/tags`|Actualizar etiquetas de un workflow|

### Ejemplos de Uso

**Crear un workflow:**

```bash
POST /workflows
Content-Type: application/json

{
  "name": "Mi Workflow",
  "nodes": [...],
  "connections": {...},
  "active": false
}
```

**Activar un workflow:**

```bash
POST /workflows/123/activate
```

**Transferir workflow a otro proyecto:**

```bash
PUT /workflows/123/transfer
Content-Type: application/json

{
  "destinationProjectId": "456"
}
```

**Actualizar etiquetas:**

```bash
PUT /workflows/123/tags
Content-Type: application/json

{
  "tags": ["producción", "clientes", "automático"]
}
```

---

## 🔑 Credentials

Operaciones sobre credenciales de autenticación.

### Endpoints Disponibles

|Método|Endpoint|Descripción|
|---|---|---|
|`POST`|`/credentials`|Crear credencial|
|`DELETE`|`/credentials/{id}`|Eliminar credencial|
|`GET`|`/credentials/schema/{credentialTypeName}`|Obtener esquema de credencial|
|`PUT`|`/credentials/{id}/transfer`|Transferir credencial a otro proyecto|

### Ejemplos de Uso

**Crear credencial:**

```bash
POST /credentials
Content-Type: application/json

{
  "name": "API Telegram Bot",
  "type": "telegramApi",
  "data": {
    "accessToken": "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
  }
}
```

**Obtener esquema de credencial:**

```bash
GET /credentials/schema/telegramApi
```

**Transferir credencial:**

```bash
PUT /credentials/789/transfer
Content-Type: application/json

{
  "destinationProjectId": "456"
}
```

---

## 🏷️ Tags

Operaciones sobre etiquetas (tags).

### Endpoints Disponibles

|Método|Endpoint|Descripción|
|---|---|---|
|`POST`|`/tags`|Crear etiqueta|
|`GET`|`/tags`|Obtener todas las etiquetas|
|`GET`|`/tags/{id}`|Obtener etiqueta por ID|
|`DELETE`|`/tags/{id}`|Eliminar etiqueta|
|`PUT`|`/tags/{id}`|Actualizar etiqueta|

### Ejemplos de Uso

**Crear etiqueta:**

```bash
POST /tags
Content-Type: application/json

{
  "name": "Producción",
  "color": "#FF5733"
}
```

**Listar todas las etiquetas:**

```bash
GET /tags
```

**Actualizar etiqueta:**

```bash
PUT /tags/123
Content-Type: application/json

{
  "name": "Producción V2",
  "color": "#00FF00"
}
```

---

## 📁 Projects

Operaciones sobre proyectos (organización de workflows).

### Endpoints Disponibles

|Método|Endpoint|Descripción|
|---|---|---|
|`POST`|`/projects`|Crear proyecto|
|`GET`|`/projects`|Obtener proyectos|
|`DELETE`|`/projects/{projectId}`|Eliminar proyecto|
|`PUT`|`/projects/{projectId}`|Actualizar proyecto|
|`POST`|`/projects/{projectId}/users`|Añadir usuarios a un proyecto|
|`DELETE`|`/projects/{projectId}/users/{userId}`|Eliminar usuario de un proyecto|
|`PATCH`|`/projects/{projectId}/users/{userId}`|Cambiar rol de usuario en proyecto|

### Ejemplos de Uso

**Crear proyecto:**

```bash
POST /projects
Content-Type: application/json

{
  "name": "Automatizaciones Clientes",
  "type": "team"
}
```

**Añadir usuario a proyecto:**

```bash
POST /projects/123/users
Content-Type: application/json

{
  "userId": "456",
  "role": "project:editor"
}
```

**Cambiar rol de usuario en proyecto:**

```bash
PATCH /projects/123/users/456
Content-Type: application/json

{
  "role": "project:admin"
}
```

---

## 📊 Roles Disponibles

### Roles Globales

- `global:owner` - Propietario del sistema
- `global:admin` - Administrador global
- `global:member` - Miembro estándar

### Roles de Proyecto

- `project:admin` - Administrador del proyecto
- `project:editor` - Editor (puede modificar workflows)
- `project:viewer` - Visualizador (solo lectura)

---

## 🔧 Ejemplos Completos con cURL

### Crear Workflow y Activarlo

```bash
# 1. Crear workflow
WORKFLOW_ID=$(curl -X POST https://n8n.ejemplo.com/api/v1/workflows \
  -H "Authorization: Bearer n8n_api_xxxxx" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Webhook Test",
    "nodes": [...],
    "active": false
  }' | jq -r '.id')

# 2. Activar workflow
curl -X POST https://n8n.ejemplo.com/api/v1/workflows/$WORKFLOW_ID/activate \
  -H "Authorization: Bearer n8n_api_xxxxx"
```

### Gestión Completa de Proyecto

```bash
# 1. Crear proyecto
PROJECT_ID=$(curl -X POST https://n8n.ejemplo.com/api/v1/projects \
  -H "Authorization: Bearer n8n_api_xxxxx" \
  -H "Content-Type: application/json" \
  -d '{"name": "Automatizaciones"}' | jq -r '.id')

# 2. Añadir usuario al proyecto
curl -X POST https://n8n.ejemplo.com/api/v1/projects/$PROJECT_ID/users \
  -H "Authorization: Bearer n8n_api_xxxxx" \
  -H "Content-Type: application/json" \
  -d '{"userId": "user_123", "role": "project:editor"}'

# 3. Transferir workflow al proyecto
curl -X PUT https://n8n.ejemplo.com/api/v1/workflows/$WORKFLOW_ID/transfer \
  -H "Authorization: Bearer n8n_api_xxxxx" \
  -H "Content-Type: application/json" \
  -d "{\"destinationProjectId\": \"$PROJECT_ID\"}"
```

---

## 📝 Notas Importantes

### Límites de Rate Limiting

- **Por defecto:** 120 peticiones/minuto por API Key
- **Recomendación:** Implementar retry logic con backoff exponencial

### Versionado de API

- **URL base:** `https://tu-instancia.com/api/v1/`
- **Versión actual:** v1

### Formatos Soportados

- **Request:** `application/json`
- **Response:** `application/json`

---

**Última actualización:** Febrero 2026  
**Documentación oficial:** [N8N API Docs](https://docs.n8n.io/api/)