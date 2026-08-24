---
type: agent
tags:
  - scrum
  - mara
  - prompt
  - linear
status: active
pipeline: raw
created: 2026-04-09
updated: 2026-04-09
source:
promotes_to:
title: documentacion-mcp-linear-clawdbot
project: none
date_created: 2026-04-09
date_modified: 2026-04-09
---
## Contexto

Este documento explica cómo funciona la integración de Linear a través de MCP (Model Context Protocol) en el sistema de agentes. Existen **dos conectores distintos** para Linear, con capacidades y orígenes diferentes.

---

## Workspace

- **Organización:** `tecfan-os`
- **Team:** `QuiqueOS` (key: `QQ`)
- **URL base:** `https://linear.app/tecfan-os`

### Proyectos activos

| Emoji | Nombre     | Estado  | Descripción                                                |
| ----- | ---------- | ------- | ---------------------------------------------------------- |
| 🚗    | **CarApp** | Backlog | PWA de gestión financiera del coche con N8N y bot Telegram |
| 📅    | **MaraOS** | Planned | Donde tu escribes                                          |

---

## Conectores disponibles

### 1. `linear-mara` (conector custom vía N8N)

Conector simple construido sobre N8N. Tiene **3 operaciones** básicas y actúa sobre el team `QQ` por defecto.

**URL MCP:** `https://core-n8n.832gky.easypanel.host/mcp/agents-linear`

#### Operaciones

##### `Get_many_issues_in_Linear`

Devuelve todas las issues del workspace.

```
Parámetros:
  Return_All: boolean  → true para traer todas
```

> ⚠️ No filtra por proyecto ni por team. Devuelve todas las issues del workspace mezcladas.

##### `Create_an_issue_in_Linear`

Crea una nueva issue en Linear.

```
Parámetros:
  Title:       string  → Título de la issue (requerido)
  Description: string  → Descripción de la issue (requerido)
```

> ⚠️ No permite especificar proyecto, estado, asignado ni prioridad. La issue se crea en el team por defecto del conector.

##### `Update_an_issue_in_Linear`

Actualiza una issue existente por su ID.

```
Parámetros:
  Issue_ID:    string  → ID de la issue (ej: "QQ-15")
  Title:       string  → Nuevo título (requerido)
  Description: string  → Nueva descripción (requerido)
```

---

### 2. `Linear` (conector oficial MCP de Linear)

Conector oficial con acceso completo a la API de Linear. Ofrece muchas más operaciones y filtros avanzados.

**URL MCP:** `https://mcp.linear.app/mcp`

#### Operaciones principales utilizadas

##### `list_projects`

Lista todos los proyectos del workspace.

```
Parámetros opcionales:
  query:           string   → Buscar por nombre
  team:            string   → Filtrar por team
  state:           string   → Estado del proyecto
  includeArchived: boolean  → Incluir archivados
  includeMembers:  boolean  → Incluir miembros
  limit:           number   → Máx resultados (default 50)
```

##### `list_issues`

Lista issues con filtros avanzados.

```
Parámetros opcionales:
  project:         string   → Nombre o ID del proyecto (ej: "MaraOS")
  team:            string   → Nombre o ID del team
  assignee:        string   → "me" para issues propias
  state:           string   → Estado (Todo, In Progress, Done...)
  priority:        number   → 0=None, 1=Urgent, 2=High, 3=Normal, 4=Low
  includeArchived: boolean  → Incluir archivadas (default true)
  limit:           number   → Máx resultados
```

##### `get_project`

Detalle completo de un proyecto.

```
Parámetros:
  query:             string   → Nombre o ID del proyecto (requerido)
  includeMembers:    boolean
  includeMilestones: boolean
  includeResources:  boolean
```

##### `list_issue_statuses`

Lista los estados disponibles de un team.

```
Parámetros:
  team: string  → Nombre o ID del team (requerido)
```

##### `research`

Consulta en lenguaje natural. Útil para queries complejas.

```
Parámetros:
  message:        string  → Pregunta en lenguaje natural (requerido)
  conversationId: string  → Para conversaciones multi-turno (opcional)
```

Ejemplos:

- `"List all issues in the MaraOS project"`
- `"What issues are blocking CarApp?"`
- `"Create a bug for the QuiqueOS team"`

---

## Estructura de datos — Issue

Una issue devuelta por el conector oficial tiene esta forma:

```json
{
  "id": "QQ-15",
  "title": "Revisar Origen funcionamiento",
  "description": "...",
  "status": "Todo",
  "priority": 0,
  "project": "MaraOS",
  "team": "QuiqueOS",
  "assignee": "Kike Rodriguez Vela",
  "createdAt": "2026-03-02T07:42:57.919Z",
  "updatedAt": "2026-03-02T07:42:57.919Z",
  "archivedAt": null,
  "completedAt": null,
  "url": "https://linear.app/tecfan-os/issue/QQ-15/...",
  "gitBranchName": "kikerodrivela/qq-15-..."
}
```

---

## Estados disponibles en QuiqueOS

|Nombre|Tipo|
|---|---|
|Backlog|backlog|
|Todo|unstarted|
|In Progress|started|
|Done|completed|
|Cancelled|cancelled|

---

## Cuándo usar cada conector

|Necesidad|Conector recomendado|
|---|---|
|Crear una issue rápida|`linear-mara` → `Create_an_issue_in_Linear`|
|Listar todas las issues sin filtros|`linear-mara` → `Get_many_issues_in_Linear`|
|Actualizar título/descripción de una issue|`linear-mara` → `Update_an_issue_in_Linear`|
|Listar issues de un proyecto concreto|`Linear` → `list_issues` con `project`|
|Ver proyectos del workspace|`Linear` → `list_projects`|
|Consultas complejas o cruzadas|`Linear` → `research`|
|Detalle completo de un proyecto|`Linear` → `get_project`|

---

## Limitaciones conocidas

- `linear-mara` **no filtra por proyecto**: devuelve todas las issues del workspace mezcladas.
- `linear-mara` al crear issues **no permite asignar proyecto, estado ni asignado**.
- El conector `Linear` oficial requiere autenticación OAuth configurada en Claude.ai.
- Las issues archivadas se incluyen por defecto en `list_issues` (`includeArchived: true`).

---

## Ejemplos de uso para el agente

### Listar issues de un proyecto

```
Usar: Linear → list_issues
  project: "CarApp"
  includeArchived: false
```

### Crear una issue nueva

```
Usar: linear-mara → Create_an_issue_in_Linear
  Title: "Implementar login con Google"
  Description: "Añadir OAuth con Google como método de autenticación alternativo."
```

### Actualizar una issue

```
Usar: linear-mara → Update_an_issue_in_Linear
  Issue_ID: "QQ-20"
  Title: "Configurar proyecto: Next.js PWA + FastAPI + Supabase"
  Description: "Descripción actualizada..."
```

### Ver todos los proyectos

```
Usar: Linear → list_projects
```

---

_Documentación generada el 09/04/2026 — Workspace: tecfan-os / QuiqueOS_