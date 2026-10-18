---
title: "Índice de clippings"
type: indice
tags:
  - documentacion
  - indice
status: active
project: none
date_created: 2026-10-18
date_modified: 2026-10-18
---

# Índice de clippings

Registro de la bandeja de entrada `Clippings/`. No es un MOC ni una nota de
conocimiento: son recortes web en bruto a la espera de convertirse en nota propia.
Cuando un recorte se convierte, se marca `status: procesado` y `promoted_to:` apunta
a la nota creada.

## Pendientes de procesar

```dataview
TABLE published AS Publicado, source AS Fuente
FROM "Clippings"
WHERE file.name != "INDEX" AND status != "procesado"
SORT published DESC
```

## Procesados

```dataview
TABLE promoted_to AS Nota, published AS Publicado
FROM "Clippings"
WHERE file.name != "INDEX" AND status = "procesado"
SORT published DESC
```

## Cómo se marca cada recorte

- `status: pendiente` — recorte sin nota propia todavía (o en duda).
- `status: procesado` + `promoted_to: "[[Nota]]"` — ya convertido en nota.

Nota: un recorte nuevo sin campo `status` aparece igualmente en «Pendientes»
(`status != "procesado"`), así que no hace falta tocar la plantilla del Web Clipper.

## Ver también

- [[MOC Inteligencia Artificial]]
- [[MOC Programacion]]
- [[Informes/INDEX|Informes del vault]] — ejemplo del mismo patrón de índice (sin ser MOC)
