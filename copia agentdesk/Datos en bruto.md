---
title: Datos en bruto de Agent Desk
tags:
  - agentdesk
  - copia-seguridad
  - backup
date_created: 2026-10-24
date_modified: 2026-10-24
---

# Datos en bruto de Agent Desk

Respuestas JSON tal cual devolvió Agent Desk el 24/10/2026, para no perder nada. Índice: [[Copia Agent Desk]].

## whoami

```json
{
  "agent": {
    "id": "59d74399-b11f-47b2-96d9-d44113d1ca44",
    "name": "Notis",
    "status": "active",
    "capabilities": [
      "notas",
      "revisiones",
      "trabajo",
      "proyectos"
    ]
  },
  "scopes": [
    "tasks:read",
    "tasks:write",
    "delegations:read",
    "delegations:write",
    "runs:read",
    "runs:write",
    "notes:read",
    "notes:write",
    "projects:read",
    "projects:write",
    "activity:read"
  ],
  "queue": {
    "delegations": 0,
    "tasks": 4
  },
  "serverTime": "2026-10-24T14:41:40.350Z"
}
```

## list_projects

```json
{
  "projects": [
    {
      "id": "df7e5f83-cbb9-4001-8083-205a83709cf1",
      "name": "MaraOs",
      "identifier": "MAOS",
      "status": "active",
      "taskTotal": 0,
      "taskDone": 0
    },
    {
      "id": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "name": "Biavent",
      "identifier": "BIA",
      "status": "active",
      "taskTotal": 5,
      "taskDone": 0
    }
  ]
}
```

## list_tasks (status=backlog,todo,in_progress,review,done,cancelled; limit=200)

```json
{
  "count": 5,
  "tasks": [
    {
      "id": "323216bd-fe41-4651-8739-df8e1ee1930d",
      "title": "Poner en el panel de organizador los encuentros que se han hecho",
      "description": null,
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": null,
      "assigneeId": null,
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "fda9d4b9-dddc-4b04-96bb-55a4d409593a",
      "title": "Mostrar en el panel del organizador el número de chats con conversación",
      "description": "Hay que arreglar que en el panel del organizador del evento se refleje el número de chats en los que se está hablando (chats con conversación activa).",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "84db4bc1-95d6-4367-8092-76e5efe254f2",
      "title": "Poner Perfil como última opción del menú inferior",
      "description": "Mover la opción de Perfil para que aparezca en último lugar del menú de navegación de abajo.",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "7e72f2d4-e1d3-48a7-a8ab-02314c5835c2",
      "title": "Revisar el tamaño del chat y por qué se cierra el teclado al enviar un mensaje",
      "description": "Revisar el tamaño de la ventana del chat y averiguar por qué el teclado se cierra al enviar un mensaje.",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "9f3fb907-cf92-405d-ada8-13dab2ff39e4",
      "title": "Probar la app en un dispositivo sin instalarla (Android e iOS)",
      "description": "Conseguir probar la aplicación en un dispositivo real sin tener que instalarla, tanto en Android como en iOS.",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    }
  ]
}
```

## list_tasks (sin filtro; limit=200)

```json
{
  "count": 5,
  "tasks": [
    {
      "id": "323216bd-fe41-4651-8739-df8e1ee1930d",
      "title": "Poner en el panel de organizador los encuentros que se han hecho",
      "description": null,
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": null,
      "assigneeId": null,
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "fda9d4b9-dddc-4b04-96bb-55a4d409593a",
      "title": "Mostrar en el panel del organizador el número de chats con conversación",
      "description": "Hay que arreglar que en el panel del organizador del evento se refleje el número de chats en los que se está hablando (chats con conversación activa).",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "84db4bc1-95d6-4367-8092-76e5efe254f2",
      "title": "Poner Perfil como última opción del menú inferior",
      "description": "Mover la opción de Perfil para que aparezca en último lugar del menú de navegación de abajo.",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "7e72f2d4-e1d3-48a7-a8ab-02314c5835c2",
      "title": "Revisar el tamaño del chat y por qué se cierra el teclado al enviar un mensaje",
      "description": "Revisar el tamaño de la ventana del chat y averiguar por qué el teclado se cierra al enviar un mensaje.",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "9f3fb907-cf92-405d-ada8-13dab2ff39e4",
      "title": "Probar la app en un dispositivo sin instalarla (Android e iOS)",
      "description": "Conseguir probar la aplicación en un dispositivo real sin tener que instalarla, tanto en Android como en iOS.",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    }
  ]
}
```

## list_notes (limit=100, offset=0)

```json
{
  "notes": [],
  "total": 0,
  "limit": 100,
  "offset": 0,
  "nextOffset": null
}
```

## list_notes (projectId=Biavent, limit=100)

```json
{
  "notes": [],
  "total": 0,
  "limit": 100,
  "offset": 0,
  "nextOffset": null
}
```

## list_delegations (sin filtro)

```json
{
  "delegations": []
}
```

## list_delegations (todos los estados)

```json
{
  "delegations": []
}
```

## get_queue

```json
{
  "delegations": [],
  "tasks": [
    {
      "id": "fda9d4b9-dddc-4b04-96bb-55a4d409593a",
      "title": "Mostrar en el panel del organizador el número de chats con conversación",
      "description": "Hay que arreglar que en el panel del organizador del evento se refleje el número de chats en los que se está hablando (chats con conversación activa).",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "84db4bc1-95d6-4367-8092-76e5efe254f2",
      "title": "Poner Perfil como última opción del menú inferior",
      "description": "Mover la opción de Perfil para que aparezca en último lugar del menú de navegación de abajo.",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "7e72f2d4-e1d3-48a7-a8ab-02314c5835c2",
      "title": "Revisar el tamaño del chat y por qué se cierra el teclado al enviar un mensaje",
      "description": "Revisar el tamaño de la ventana del chat y averiguar por qué el teclado se cierra al enviar un mensaje.",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    },
    {
      "id": "9f3fb907-cf92-405d-ada8-13dab2ff39e4",
      "title": "Probar la app en un dispositivo sin instalarla (Android e iOS)",
      "description": "Conseguir probar la aplicación en un dispositivo real sin tener que instalarla, tanto en Android como en iOS.",
      "status": "todo",
      "priority": "none",
      "autonomy": "do_with_approval",
      "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
      "project": "Biavent",
      "parentTaskId": null,
      "labels": [],
      "dueDate": null,
      "dueTime": null,
      "assigneeType": "agent",
      "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
      "claimedByAgentId": null,
      "leaseExpiresAt": null,
      "leaseSecondsLeft": null,
      "claimCount": 0,
      "subtaskTotal": 0,
      "subtaskDone": 0
    }
  ]
}
```

## get_task 323216bd-fe41-4651-8739-df8e1ee1930d

```json
{
  "task": {
    "id": "323216bd-fe41-4651-8739-df8e1ee1930d",
    "title": "Poner en el panel de organizador los encuentros que se han hecho",
    "description": null,
    "status": "todo",
    "priority": "none",
    "autonomy": "do_with_approval",
    "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
    "project": "Biavent",
    "parentTaskId": null,
    "labels": [],
    "dueDate": null,
    "dueTime": null,
    "assigneeType": null,
    "assigneeId": null,
    "claimedByAgentId": null,
    "leaseExpiresAt": null,
    "leaseSecondsLeft": null,
    "claimCount": 0,
    "subtaskTotal": 0,
    "subtaskDone": 0
  },
  "subtasks": [],
  "comments": [],
  "approvals": [],
  "openRun": null
}
```

## get_task fda9d4b9-dddc-4b04-96bb-55a4d409593a

```json
{
  "task": {
    "id": "fda9d4b9-dddc-4b04-96bb-55a4d409593a",
    "title": "Mostrar en el panel del organizador el número de chats con conversación",
    "description": "Hay que arreglar que en el panel del organizador del evento se refleje el número de chats en los que se está hablando (chats con conversación activa).",
    "status": "todo",
    "priority": "none",
    "autonomy": "do_with_approval",
    "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
    "project": "Biavent",
    "parentTaskId": null,
    "labels": [],
    "dueDate": null,
    "dueTime": null,
    "assigneeType": "agent",
    "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
    "claimedByAgentId": null,
    "leaseExpiresAt": null,
    "leaseSecondsLeft": null,
    "claimCount": 0,
    "subtaskTotal": 0,
    "subtaskDone": 0
  },
  "subtasks": [],
  "comments": [],
  "approvals": [],
  "openRun": null
}
```

## get_task 84db4bc1-95d6-4367-8092-76e5efe254f2

```json
{
  "task": {
    "id": "84db4bc1-95d6-4367-8092-76e5efe254f2",
    "title": "Poner Perfil como última opción del menú inferior",
    "description": "Mover la opción de Perfil para que aparezca en último lugar del menú de navegación de abajo.",
    "status": "todo",
    "priority": "none",
    "autonomy": "do_with_approval",
    "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
    "project": "Biavent",
    "parentTaskId": null,
    "labels": [],
    "dueDate": null,
    "dueTime": null,
    "assigneeType": "agent",
    "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
    "claimedByAgentId": null,
    "leaseExpiresAt": null,
    "leaseSecondsLeft": null,
    "claimCount": 0,
    "subtaskTotal": 0,
    "subtaskDone": 0
  },
  "subtasks": [],
  "comments": [],
  "approvals": [],
  "openRun": null
}
```

## get_task 7e72f2d4-e1d3-48a7-a8ab-02314c5835c2

```json
{
  "task": {
    "id": "7e72f2d4-e1d3-48a7-a8ab-02314c5835c2",
    "title": "Revisar el tamaño del chat y por qué se cierra el teclado al enviar un mensaje",
    "description": "Revisar el tamaño de la ventana del chat y averiguar por qué el teclado se cierra al enviar un mensaje.",
    "status": "todo",
    "priority": "none",
    "autonomy": "do_with_approval",
    "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
    "project": "Biavent",
    "parentTaskId": null,
    "labels": [],
    "dueDate": null,
    "dueTime": null,
    "assigneeType": "agent",
    "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
    "claimedByAgentId": null,
    "leaseExpiresAt": null,
    "leaseSecondsLeft": null,
    "claimCount": 0,
    "subtaskTotal": 0,
    "subtaskDone": 0
  },
  "subtasks": [],
  "comments": [],
  "approvals": [],
  "openRun": null
}
```

## get_task 9f3fb907-cf92-405d-ada8-13dab2ff39e4

```json
{
  "task": {
    "id": "9f3fb907-cf92-405d-ada8-13dab2ff39e4",
    "title": "Probar la app en un dispositivo sin instalarla (Android e iOS)",
    "description": "Conseguir probar la aplicación en un dispositivo real sin tener que instalarla, tanto en Android como en iOS.",
    "status": "todo",
    "priority": "none",
    "autonomy": "do_with_approval",
    "projectId": "b62c14ae-cf0f-4d19-9923-76cab46c68c9",
    "project": "Biavent",
    "parentTaskId": null,
    "labels": [],
    "dueDate": null,
    "dueTime": null,
    "assigneeType": "agent",
    "assigneeId": "59d74399-b11f-47b2-96d9-d44113d1ca44",
    "claimedByAgentId": null,
    "leaseExpiresAt": null,
    "leaseSecondsLeft": null,
    "claimCount": 0,
    "subtaskTotal": 0,
    "subtaskDone": 0
  },
  "subtasks": [],
  "comments": [],
  "approvals": [],
  "openRun": null
}
```

