---
type: "resource"
tags: ["#proyecto-SaaS", "#area-devops", "#status-pendiente", "#topic-ia", "#topic-db"] # Siempre array con 2-5 tags específicos
project: "none"
status: "pendiente"
date_created: "2026-03-01"
date_modified: "2026-03-01"
related: [] # Array vacío o con [[links]]
---

Qdrant es una base de datos vectorial optimizada para búsquedas de similitud y recuperación de información a gran escala. Sus comandos y funcionalidades se gestionan principalmente a través de una API REST y un SDK disponible en varios lenguajes como Python, Node.js y Rust.

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

```json

GET /collections

```

Devuelve un listado de todas las colecciones existentes en la base de datos.
### Obtener detalles de una colección

```json

GET /collections/{collection_name}

```

Proporciona información sobre una colección específica, como la configuración y el estado.
### Eliminar una colección

```json

DELETE /collections/{collection_name}

```

Elimina completamente una colección y todos sus vectores.
## 2. Gestión de Puntos (Vectors)

### Insertar puntos (vectores)

```json

PUT /collections/{collection_name}/points

```

Permite agregar nuevos vectores a la colección. Los datos deben incluir la identificación del vector y el array de valores.

Ejemplo en JSON:
```json

{

  "points": [

    {

      "id": 1,

      "vector": [0.12, 0.5, 0.9]

    }

  ]

}

```

### Buscar vectores similares (Vector Search)

```json

POST /collections/{collection_name}/points/search

```

Busca los vectores más similares al proporcionado.

Ejemplo:

```json

{

  "vector": [0.12, 0.5, 0.9],

  "limit": 5

}

```

### Filtrar vectores por metadatos

```json

POST /collections/{collection_name}/points/search

```

Incluye un filtro para buscar solo vectores que cumplan ciertas condiciones.

Ejemplo:

```json

{

  "vector": [0.12, 0.5, 0.9],

  "limit": 5,

  "filter": {

    "must": [

      {

        "key": "category",

        "match": {

          "value": "technology"

        }

      }

    ]

  }

}

```

### Actualizar un vector existente
```json

PATCH /collections/{collection_name}/points

```

Permite modificar el contenido de un vector.
### Eliminar un vector por ID

```json

DELETE /collections/{collection_name}/points

```

Ejemplo:

```json

{

  "points": [1, 2, 3]

}

```

Borra los vectores con los identificadores proporcionados.
## 3. Índices y Optimización

### Actualizar la configuración de una colección

```json

PATCH /collections/{collection_name}

```

Se usa para cambiar parámetros como el número de shards o la métrica de distancia.
### Optimizar una colección

```json

POST /collections/{collection_name}/points/scroll

```

Recorre los vectores y los reorganiza para mejorar el rendimiento.
## 4. Snapshots y Backups

### Crear un snapshot de la base de datos

```json

POST /collections/{collection_name}/snapshots

```

Genera un backup de la colección.
### Restaurar un snapshot

```json

PUT /collections/{collection_name}/snapshots/{snapshot_name}

```

Restaura la base de datos a un estado anterior.
## 5. Administración del Servidor

### Ver el estado del servidor

```json

GET /cluster

```

Muestra información sobre los nodos y el estado del cluster.
### Ver métricas del sistema

```json

GET /metrics

```

Devuelve estadísticas sobre el rendimiento del servidor.
## Extras

Qdrant también soporta WebSockets para streaming de datos en tiempo real y tiene SDKs en Python, Node.js y Rust para facilitar su uso en aplicaciones.