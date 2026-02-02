---
tags:
  - n8n
  - BaseDatos
ai_share: "true"
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