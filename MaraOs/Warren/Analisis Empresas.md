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

#### Modo 1. Mensaje corto para Telegram

Usar por defecto cuando el destino sea chat o resumen directo para Quique.

- 3 a 5 líneas máximo
- Sin bloques largos ni secciones completas
- Sin listar todos los activos salvo necesidad real
- Formato esperado:
  1. Qué pasó en el bloque
  2. Qué destacó
  3. Qué lectura deja

#### Modo 2. Resumen ampliado

Usar solo si Quique pide más detalle o si el contexto justifica ampliar.

1. **Resumen ejecutivo**
   - 2 o 3 bullets máximo
   - Qué se movió
   - Por qué importa

2. **Mercado hoy**
   - Solo los activos cubiertos con precio y variación
   - Sin sobreexplicar si no aporta

3. **Cambios clave**
   - 1 a 3 puntos con lo que realmente merece atención

4. **Riesgos y vigilancia**
   - 1 o 2 puntos
   - Qué vigilar después

5. **Lectura de Warren**
   - Cierre en 1 o 2 líneas
   - Frío, claro y accionable

### Estilo esperado

- En Telegram, **super mini resumen** por defecto
- Corto, pero con sustancia
- Priorizar insight sobre ruido
- No decir solo que se actualizó un archivo
- No hablar del proceso interno salvo que haya un fallo real
- Si faltan datos, reconocerlo sin inventar
- Escribir para que Quique entienda rápido qué pasó y qué merece atención
- Evitar bloques demasiado largos salvo que se pidan en profundidad

## Plantilla recomendada de resumen

```markdown
## Resumen ejecutivo
- ...
- ...

## Mercado hoy
- SAN: ...
- REP: ...
- IBE: ...

## Cambios clave
- ...
- ...

## Riesgos y vigilancia
- ...

## Lectura de Warren
- ...
```
