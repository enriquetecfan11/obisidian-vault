---
type: "resource"
tags:
  - qdrant
  - base-de-datos-vectorial
  - comandos
  - api-rest
project: "none"
status: "pendiente"
date_created: "2026-03-01"
date_modified: "2026-03-01"
related: [] # Array vacío o con [[links]]
---

Para crear una tabla dentro de la base de datos de 1024 caracteres

```bash
 curl -X PUT "<http://localhost:6333/collections/db_name>" \\
   -H "Content-Type: application/json" \\
   -d '{
     "vectors": {
       "size": 1024,
       "distance": "Cosine"
     },
     "shard_number": 1
   }'
```

En una linea mas facil para todo

```bash
curl -X PUT "<http://localhost:6333/collections/db_name>" -H "Content-Type: application/json" -d '{"vectors": {"size": 1024, "distance": "Cosine"}, "shard_number": 1}'
```

Para que funcione en powershell

```bash
 Invoke-RestMethod -Uri "<http://localhost:6333/collections/db_name>" -Method Put -Headers @{"Content-Type"="application/json"} -Body ('{"vectors": {"size": 1024, "distance": "Cosine"}, "shard_number": 1}')
```

### Varios comandos

Para ver las tablas o colecciones que tengo:

```bash
 curl -X GET "<http://localhost:6333/collections>"
```

```bash
 Invoke-RestMethod -Uri "<http://localhost:6333/collections>" -Method Get
```

Para ver los documentos

```bash
 curl -X GET "<http://localhost:6333/documents>"
```

Eliminar una coleccion en QDrant

```bash
curl -X DELETE "<http://localhost:6333/collections/db_name>"
```