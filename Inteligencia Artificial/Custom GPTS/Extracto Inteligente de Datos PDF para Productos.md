---
tags:
  - IA
  - InteligenciaArtificial
  - CustomGpt
ai_share: "true"
---
Este prompt sirve para generar un extracto de un documento en el que hay productos y servicios para una base de datos vectorial

Version 1: Esta version tiene todos los datos con precio incluido

```markdown
Analiza el contenido del documento PDF proporcionado y extrae información clave para generar un conjunto de datos estructurados que clasifiquen los elementos en categorías como "producto", "clientes", "beneficios", etc. Toda la información debe derivarse directamente del contenido del documento y organizarse en el formato JSON especificado.

Formato de salida: La salida debe tener el siguiente formato:
```json
{
    "id": "[Identificador único del producto o servicio]",
    "categoria": "[Categoría a la que pertenece el elemento, como producto, cliente, evento, etc.]",
    "nombre": "[Nombre del producto, servicio o entidad]",
    "descripcion": "[Descripción detallada del producto o servicio]",
    "caracteristicas": [
        "[Característica 1]",
        "[Característica 2]",
        "[Característica 3]"
    ],
    "beneficios": [
        "[Beneficio 1]",
        "[Beneficio 2]",
        "[Beneficio 3]"
    ],
    "precio": {
        "moneda": "[Moneda en la que se presenta el precio]",
        "monto": "[Monto total del precio]",
        "periodo": "[Periodo de tiempo del precio, como mensual o anual]"
    },
    "clientes": [
        {
            "nombre": "[Nombre del cliente]",
            "sector": "[Sector del cliente]",
            "resultado": "[Resultado obtenido por el cliente utilizando el producto]"
        }
    ],
    "lanzamiento": "[Fecha de lanzamiento del producto o servicio]",
    "version": "[Versión actual del producto]",
    "documentacion": "[Enlace a la documentación técnica del producto]",
    "actualizaciones": [
        {
            "fecha": "[Fecha de actualización]",
            "cambios": "[Descripción de los cambios o mejoras realizadas]"
        }
    ]
}
```

Proceso de extracción:

- Productos y servicios: Extrae la información relacionada con los productos o servicios ofrecidos por la empresa, incluyendo su descripción, características, beneficios, y precio.
- Clientes: Recupera información sobre los clientes que utilizan los productos o servicios, con especial énfasis en los resultados que han obtenido.
- Actualizaciones y lanzamientos: Incluye detalles sobre las versiones del producto, así como cualquier actualización o mejora significativa que se haya implementado.

Reglas:

- La información generada debe ser clara y autónoma, sin hacer referencia explícita al documento PDF.
- Toda la información debe estar derivada directamente del contenido del PDF, sin agregar ningún dato externo.
- Asegúrate de que los campos estén completos y que los elementos dentro de arrays (como características, beneficios, clientes, etc.) sean coherentes y relevantes al contexto.
- Generación proporcional: El número de productos o entradas generadas debe ser proporcional a la cantidad de páginas en el PDF, con al menos 1 producto o entrada principal por página.

```json
{
    "id": "[Identificador único del producto o servicio]",
    "categoria": "[Categoría a la que pertenece el elemento, como producto, cliente, evento, etc.]",
    "nombre": "[Nombre del producto, servicio o entidad]",
    "descripcion": "[Descripción detallada del producto o servicio]",
    "caracteristicas": [
        "[Característica 1]",
        "[Característica 2]",
        "[Característica 3]",
        "[Característica 4]",
        "[Característica 5]"
    ],
    "beneficios": [
        "[Beneficio 1]",
        "[Beneficio 2]",
        "[Beneficio 3]",
        "[Beneficio 4]",
        "[Beneficio 5]"
    ],
    "precio": {
        "moneda": "[Moneda en la que se presenta el precio]",
        "monto": "[Monto total del precio]",
        "periodo": "[Periodo de tiempo del precio, como mensual o anual]"
    },
    "clientes": [
        {
            "nombre": "[Nombre del cliente]",
            "sector": "[Sector del cliente]",
            "resultado": "[Resultado obtenido por el cliente utilizando el producto]"
        }
    ],
    "lanzamiento": "[Fecha de lanzamiento del producto o servicio]",
    "version": "[Versión actual del producto]",
    "documentacion": "[Enlace a la documentación técnica del producto]",
    "actualizaciones": [
        {
            "fecha": "[Fecha de actualización]",
            "cambios": "[Descripción de los cambios o mejoras realizadas]"
        }
    ]
}

```
¿Cómo funcionaría este prompt?

- El asistente procesará el PDF página por página y extraerá la información relevante, organizándola en las categorías que has especificado.

- Cada producto, cliente o evento tendrá su propia entrada estructurada con los detalles clave. Puedes generar múltiples productos o clientes si el PDF incluye más información.
```

Version 2: Esta version tiene todos los datos pero sin precio, ni clientes, ni lanzamiento, ni version, ni updates

```markdown
Analiza el contenido del documento PDF proporcionado y extrae información clave para generar un conjunto de datos estructurados que clasifiquen los elementos en categorías como "producto", "clientes", "beneficios", etc. Toda la información debe derivarse directamente del contenido del documento y organizarse en el formato JSON especificado.

Formato de salida: La salida debe tener el siguiente formato:
```json
{
    "id": "[Identificador único del producto o servicio]",
    "categoria": "[Categoría a la que pertenece el elemento, como producto, cliente, evento, etc.]",
    "nombre": "[Nombre del producto, servicio o entidad]",
    "descripcion": "[Descripción detallada del producto o servicio]",
    "caracteristicas": [
        "[Característica 1]",
        "[Característica 2]",
        "[Característica 3]"
    ],
    "beneficios": [
        "[Beneficio 1]",
        "[Beneficio 2]",
        "[Beneficio 3]"
    ],
    "paginawebproducto": "[Enlace a la pagina web del producto]",
}
```

Proceso de extracción:

- Productos y servicios: Extrae la información relacionada con los productos o servicios ofrecidos por la empresa, incluyendo su descripción, características, beneficios, y precio.
- Clientes: Recupera información sobre los clientes que utilizan los productos o servicios, con especial énfasis en los resultados que han obtenido.
- Actualizaciones y lanzamientos: Incluye detalles sobre las versiones del producto, así como cualquier actualización o mejora significativa que se haya implementado.

Reglas:

- La información generada debe ser clara y autónoma, sin hacer referencia explícita al documento PDF.
- Toda la información debe estar derivada directamente del contenido del PDF, sin agregar ningún dato externo.
- Asegúrate de que los campos estén completos y que los elementos dentro de arrays (como características, beneficios, clientes, etc.) sean coherentes y relevantes al contexto.
- Generación proporcional: El número de productos o entradas generadas debe ser proporcional a la cantidad de páginas en el PDF, con al menos 1 producto o entrada principal por página.

```json
{
    "id": "[Identificador único del producto o servicio]",
    "categoria": "[Categoría a la que pertenece el elemento, como producto, cliente, evento, etc.]",
    "nombre": "[Nombre del producto, servicio o entidad]",
    "descripcion": "[Descripción detallada del producto o servicio]",
    "caracteristicas": [
        "[Característica 1]",
        "[Característica 2]",
        "[Característica 3]",
        "[Característica 4]",
        "[Característica 5]"
    ],
    "beneficios": [
        "[Beneficio 1]",
        "[Beneficio 2]",
        "[Beneficio 3]",
        "[Beneficio 4]",
        "[Beneficio 5]"
    ],
    "paginawebproducto": "[Enlace a la pagina web del producto]",
}

```
¿Cómo funcionaría este prompt?

- El asistente procesará el PDF página por página y extraerá la información relevante, organizándola en las categorías que has especificado.

- Cada producto, cliente o evento tendrá su propia entrada estructurada con los detalles clave. Puedes generar múltiples productos o clientes si el PDF incluye más información.
```