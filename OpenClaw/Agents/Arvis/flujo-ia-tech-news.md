---
type:
tags:
  - ia
  - agentes
  - noticias
  - arvis
status: active
created: 2026-04-06
updated: 2026-04-06
source:
---
# Flujo Arvis ↔ IA / Tech News ↔ Obsidian

## Roles
- **Mara**: diseña y supervisa el sistema.
- **Arvis**: agente de noticias IA/Tech y borradores para redes.
- **Kike**: decide qué noticias se convierten en contenido y revisa borradores en Obsidian.

## Flujo operativo

### 1) Arvis alimenta IA / Tech News
- Arvis lee feeds IA/Tech y etiqueta por categoría.
- Publica noticias en panel:
  - **Panel A**: filtros y contadores.
  - **Panel B**: lista (título, fuente, fecha, resumen, temas).

### 2) Decisión de Kike (Panel B)
Para cada noticia:
- **Marcar para contenido X**
- **Marcar para contenido LinkedIn**
- **Ambos**
- **Descartar**

Esto actualiza el **Panel C** (estado de borradores).

### 3) Arvis crea/actualiza borradores (Panel C + Obsidian)

#### Si se marca "contenido X"
- Panel C: canal = X, estado = `pendiente_redacción`.
- Crear/actualizar nota en: `redes sociales/twitter/`
- Contenido mínimo:
  - Título
  - Resumen noticia
  - Borrador tweet
- Al terminar: estado = `borrador_en_obsidian`.

#### Si se marca "contenido LinkedIn"
- Panel C: canal = LinkedIn, estado = `pendiente_redacción`.
- Crear/actualizar nota en: `redes sociales/linkedin/`
- Contenido mínimo:
  - Título
  - Resumen noticia
  - Borrador LinkedIn
- Al terminar: estado = `borrador_en_obsidian`.

#### Si se marca "Ambos"
- Panel C: canal = `Ambos` (o dos filas separadas X/LinkedIn).
- Crear/actualizar dos notas:
  - `redes sociales/twitter/...`
  - `redes sociales/linkedin/...`
- Cada una pasa a `borrador_en_obsidian` cuando esté lista.

#### Si se marca "Descartar"
- Noticia = `descartada` en IA / Tech News.
- No crear contenido en Obsidian.

### 4) Revisión en Obsidian (Kike)
- Kike revisa/edita borradores en:
  - `redes sociales/twitter/`
  - `redes sociales/linkedin/`
- Cuando la nota esté revisada, marcar para que Arvis actualice Panel C a `revisado_por_kike`.

## Estados estándar Panel C
1. `pendiente_redacción`
2. `borrador_en_obsidian`
3. `revisado_por_kike`

## Regla de supervisión (Mara)
- Mara no redacta por defecto; supervisa calidad y coherencia del flujo.
- Mara ajusta categorías/feeds/criterios cuando cambie la estrategia.
