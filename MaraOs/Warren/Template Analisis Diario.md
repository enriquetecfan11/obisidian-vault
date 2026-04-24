---
title: Template Analisis Diario
type: template
tags:
  - mara-os
  - warren
  - template
  - analisis-diario
project: MaraOS
status: active
date_created: 2026-04-16
date_modified: 2026-04-16
---
# Template — Análisis Diario Warren

Objetivo: normalizar los archivos generados por Warren para que sean útiles tanto como archivo histórico como para extraer un resumen corto y accionable para Quique.

## Problemas detectados en el formato actual

- España sale demasiado crudo y orientado a ficha por activo.
- Crypto tiene mejor señal, pero mezcla insight con demasiado detalle operativo.
- No hay una estructura homogénea entre bloques.
- El archivo sirve como dump de datos, pero no siempre como lectura rápida.

## Principios del nuevo template

- El archivo diario debe servir para dos usos a la vez:
  1. **archivo canónico de análisis**
  2. **base para resumen corto enviado a Quique**
- Primero insight, luego detalle.
- El dato completo puede existir, pero no debe tapar la lectura.
- Todos los bloques deben compartir la misma estructura base.

## Estructura recomendada por archivo diario

### 1. Cabecera
```yaml
---
title: <Mercado> · Análisis diario
source: Mara / Warren
date: YYYY-MM-DD
market: <España|EEUU|Crypto>
window: <09:00|13:30|15:30>
status: generated
---
```

### 2. Resumen ejecutivo
- 2 o 3 bullets máximo
- Qué se movió
- Qué importa
- Qué lectura deja el bloque

### 3. Mercado hoy
Lista corta de los activos cubiertos con:
- ticker
- precio
- variación 24h

Ejemplo:
```markdown
## Mercado hoy
- SAN: €10.53 (-1.31%)
- REP: €20.93 (+2.05%)
- IBE: €19.86 (-0.10%)
```

### 4. Cambios clave
- 1 a 3 bullets
- Noticias, earnings, regulación, flujos, on-chain o catalizadores que realmente explican el movimiento

### 5. Riesgos y vigilancia
- 1 o 2 bullets
- Qué vigilar en la siguiente ventana o sesión

### 6. Lectura de Warren
- 1 o 2 líneas
- Interpretación final, fría y accionable

### 7. Apéndice por activo
Solo después del resumen útil.
Aquí sí se puede volcar la ficha más completa por activo:
- fundamentales
- noticias
- métricas on-chain
- TVL
- tendencias 1–3 años

## Plantilla canónica de salida

```markdown
---
title: <Mercado> · Análisis diario
source: Mara / Warren
date: YYYY-MM-DD
market: <España|EEUU|Crypto>
window: <09:00|13:30|15:30>
status: generated
---

# <MERCADO>

## Resumen ejecutivo
- ...
- ...

## Mercado hoy
- ...
- ...

## Cambios clave
- ...
- ...

## Riesgos y vigilancia
- ...

## Lectura de Warren
- ...

---

## Apéndice por activo

### <Ticker> · <Nombre>
- Precio actual: ...
- % 24h: ...
- Fundamentales / métricas: ...
- Noticias y eventos: ...
```

## Regla de calidad

Si Warren solo pudiera enviar las primeras 5 secciones, el análisis debería seguir siendo útil por sí mismo.

## Uso recomendado en cron

- El cron genera primero el bloque corto canónico.
- Después añade el apéndice detallado.
- El mensaje para Quique debe salir del bloque corto, no del apéndice.
- Si el destino es Telegram o chat directo, el mensaje enviado debe reducirse aún más a un microresumen de 3 a 5 líneas.
- El archivo puede ser más completo, pero el mensaje no.
