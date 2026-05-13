---
title: qdrant-referencia-completa
type: code
tags:
  - qdrant
  - base-de-datos-vectorial
  - api-rest
  - embeddings
  - comandos
  - ia
  - code
  - dev
status: active
created: 2026-03-01
updated: 2026-04-06
source: "https://qdrant.tech/documentation/"
---

# QDrant — Referencia Completa

[[QDrant]] es una base de datos vectorial optimizada para búsquedas de similitud y recuperación de información a gran escala. Sus comandos y funcionalidades se gestionan principalmente a través de una API REST y un SDK disponible en varios lenguajes como Python, Node.js y Rust.

---

## 0. Comandos rápidos (cURL / PowerShell)

### Crear colección (1024 dimensiones, Cosine)

```bash
# cURL — formato extendido
curl -X PUT "http://localhost:6333/collections/db_name" \
  -H "Content-Type: application/json" \
  -d '{
    "vectors": { "size": 1024, "distance": "Cosine" },
    "shard_number": 1
  }'

# cURL — una línea
curl -X PUT "http://localhost:6333/collections/db_name" -H "Content-Type: application/json" -d '{"vectors": {"size": 1024, "distance": "Cosine"}, "shard_number": 1}'

# PowerShell
Invoke-RestMethod -Uri "http://localhost:6333/collections/db_name" -Method Put -Headers @{"Content-Type"="application/json"} -Body ('{"vectors": {"size": 1024, "distance": "Cosine"}, "shard_number": 1}')
```

### Listar colecciones

```bash
# cURL
curl -X GET "http://localhost:6333/collections"
# PowerShell
Invoke-RestMethod -Uri "http://localhost:6333/collections" -Method Get
```

### Ver documentos

```bash
curl -X GET "http://localhost:6333/documents"
```

### Eliminar colección

```bash
curl -X DELETE "http://localhost:6333/collections/db_name"
```

---

## 1. Gestión de Colecciones (Collections)

### Crear una colección

```http
PUT /collections/{collection_name}
{
    "vectors": {
      "size": 1024,
      "distance": "Cosine"
    }
}
```

Permite crear una nueva colección con una configuración específica, como el tamaño del vector y la métrica de distancia.

### Listar todas las colecciones

```http
GET /collections
```

Devuelve un listado de todas las colecciones existentes en la base de datos.

### Obtener detalles de una colección

```http
GET /collections/{collection_name}
```

Proporciona información sobre una colección específica, como la configuración y el estado.

### Eliminar una colección

```http
DELETE /collections/{collection_name}
```

Elimina completamente una colección y todos sus vectores.

---

## 2. Gestión de Puntos (Vectors)

### Insertar puntos (vectores)

```http
PUT /collections/{collection_name}/points
```

Permite agregar nuevos vectores a la colección.

```json
{
  "points": [
    { "id": 1, "vector": [0.12, 0.5, 0.9] }
  ]
}
```

### Buscar vectores similares (Vector Search)

```http
POST /collections/{collection_name}/points/search
```

```json
{
  "vector": [0.12, 0.5, 0.9],
  "limit": 5
}
```

### Filtrar vectores por metadatos

```http
POST /collections/{collection_name}/points/search
```

```json
{
  "vector": [0.12, 0.5, 0.9],
  "limit": 5,
  "filter": {
    "must": [
      { "key": "category", "match": { "value": "technology" } }
    ]
  }
}
```

### Actualizar un vector existente

```http
PATCH /collections/{collection_name}/points
```

### Eliminar vectores por ID

```http
DELETE /collections/{collection_name}/points
```

```json
{ "points": [1, 2, 3] }
```

---

## 3. Índices y Optimización

### Actualizar configuración de una colección

```http
PATCH /collections/{collection_name}
```

### Optimizar (scroll)

```http
POST /collections/{collection_name}/points/scroll
```

---

## 4. Snapshots y Backups

### Crear un snapshot

```http
POST /collections/{collection_name}/snapshots
```

### Restaurar un snapshot

```http
PUT /collections/{collection_name}/snapshots/{snapshot_name}
```

---

## 5. Administración del Servidor

### Estado del cluster

```http
GET /cluster
```

### Métricas del sistema

```http
GET /metrics
```

---

## Extras

Qdrant soporta WebSockets para streaming en tiempo real y tiene SDKs oficiales en **Python**, **Node.js** y **Rust**.
