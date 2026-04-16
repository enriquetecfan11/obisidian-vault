---
title: Analisis Empresas
type: resource
tags:
  - mara-os
  - warren
  - finanzas
  - renta-variable
  - analisis
project: MaraOS
status: active
date_created: 2026-03-01
date_modified: 2026-04-16
---
# Análisis de Empresas

Plantilla de seguimiento de activos que usa Warren para sus informes diarios y para los resúmenes que envía por cron.

## Universo de seguimiento

### Acciones EEUU
- AMZN, NVDA, AAPL, ASML
- Precio actual
- Porcentaje de cambio en las últimas 24 horas
- Fundamentales acciones: PER, crecimiento ingresos/beneficios, márgenes, deuda/equity, ROE, EPS, tendencia 1–3 años
- Noticias y eventos: earnings, splits, guidance, M&A, regulación sector, cambios directiva, lanzamientos de producto

### Crypto
- BTC, ETH, XRP, SOL
- Precio actual
- Porcentaje de cambio en las últimas 24 horas
- Métricas cripto: market cap, volumen 24h, oferta circulante/total, direcciones activas, transacciones, fees, TVL (en SOL/ETH), tokenomics básica
- Noticias y eventos: upgrades/hard forks, hacks, regulación, partnerships clave, movimientos grandes on-chain hacia/desde exchanges

### Acciones España
- SAN, REP, IBE
- Precio actual
- Porcentaje de cambio en las últimas 24 horas
- Fundamentales acciones: PER, crecimiento ingresos/beneficios, márgenes, deuda/equity, ROE, EPS, tendencia 1–3 años
- Noticias y eventos: earnings, splits, guidance, M&A, regulación sector, cambios directiva, lanzamientos de producto

## Formato de salida para crons de Warren

Objetivo: que el cron entregue un resumen útil para decisión, no un log técnico ni una nota de mantenimiento.

### Estructura obligatoria

1. **Resumen ejecutivo**
   - 2 a 4 bullets con lo más importante del bloque analizado
   - Qué se movió
   - Por qué importa

2. **Mercado hoy**
   - Precio y variación de los activos cubiertos
   - Separar por España, EEUU y Crypto cuando aplique

3. **Ganadores y perdedores**
   - Qué destacó al alza
   - Qué destacó a la baja
   - Si no hubo movimientos relevantes, decirlo claro

4. **Cambios clave**
   - Noticias, earnings, regulación, flujos, on-chain, guidance, rotaciones o eventos relevantes

5. **Riesgos y vigilancia**
   - Niveles a vigilar
   - Eventos próximos
   - Señales de deterioro o confirmación

6. **Lectura de Warren**
   - Cierre en 2 o 3 líneas
   - Interpretación fría, estructurada y accionable
   - Sin hype ni frases vacías

### Estilo esperado

- Priorizar insight sobre ruido
- No decir solo que se actualizó un archivo
- No hablar del proceso interno salvo que haya un fallo real
- Si faltan datos, reconocerlo sin inventar
- Escribir para que Quique entienda rápido qué pasó y qué merece atención

## Plantilla recomendada de resumen

```markdown
## Resumen ejecutivo
- ...
- ...

## Mercado hoy
### España
- SAN: ...
- REP: ...
- IBE: ...

### EEUU
- AMZN: ...
- NVDA: ...
- AAPL: ...
- ASML: ...

### Crypto
- BTC: ...
- ETH: ...
- XRP: ...
- SOL: ...

## Ganadores y perdedores
- Ganadores: ...
- Perdedores: ...

## Cambios clave
- ...
- ...

## Riesgos y vigilancia
- ...
- ...

## Lectura de Warren
- ...
```
