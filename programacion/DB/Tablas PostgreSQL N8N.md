---
title: tablas-postgresql-n8n
type: "nota"
tags:
  - postgresql
  - n8n
  - sql
  - automatizacion
  - chatbot
  - code
  - dev
  - pending
project: "N8N Automation"
status: "pendiente"
date_created: "2026-03-01"
date_modified: "2026-03-01"
updated: 2026-04-06
---

Para crear tablas para almacenar chat de los usuarios:

```sql
CREATE TABLE n8n_chat_pro (
	id SERIAL PRIMARY KEY,
	session_id VARCHAR(255) NOT NULL,
	message JSONB NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```