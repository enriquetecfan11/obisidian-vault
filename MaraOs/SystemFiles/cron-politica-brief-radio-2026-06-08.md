---
type: policy
tags:
  - maraos
  - cron
  - policy
  - brief-radio
status: active
---
# Politica de crons MaraOS - brief de radio

Fecha: 2026-06-08
Estado: activo

## Regla general

Los crons de MaraOS deben enviar mensajes cortos, tipo brief de radio. No articulos, no tochos, no parrafos largos. Si no hay nada relevante, priorizar silencio o una linea estandar.

## Warren diario

- Unico resumen Warren: lunes a viernes, 22:30 Europe/Madrid.
- Objetivo: Espana + EEUU + Crypto.
- Secciones fijas:
  - Lo importante hoy: maximo 3 bullets.
  - Movimientos clave: solo movimientos relevantes o eventos grandes.
  - Oportunidades / riesgos a vigilar: maximo 3 puntos.
- Prohibido: parrafos largos, contexto historico salvo imprescindible, logs de proceso.

## WatchDog Warren

- Ventana: lunes a viernes, 09:00-21:00 Europe/Madrid.
- Frecuencia actual: 09:00, 11:00, 13:00, 15:00, 17:00, 19:00 y 21:00.
- Rol: solo alertas, nunca informes largos.
- Zona operativa: `Europe/Madrid`.
- Para activos USA (acciones, ETFs e indices), calcular cada dia la apertura/cierre de NYSE/Nasdaq convirtiendo `09:30-16:00 America/New_York` a `Europe/Madrid`; no hardcodear 14:30 ni 15:30.
- Si la hora local Madrid es anterior a la apertura USA calculada para ese dia, etiquetar como `premarket EEUU`.
- Desde la apertura USA calculada hasta el cierre USA calculado, etiquetar como `mercado regular EEUU`.
- Despues del cierre USA calculado, usar `after-hours EEUU` solo si el dato corresponde claramente a after-hours; si no esta claro, omitir etiqueta.
- Crypto, petroleo, futuros y commodities no deben llevar nunca `premarket` porque cotizan casi continuo.
- Las semanas de desfase de cambio horario entre EEUU y Europa quedan cubiertas por la conversion diaria `America/New_York` -> `Europe/Madrid`.
- Si no hay movimiento relevante ni noticia muy grande: silencio o `WatchDog Warren: sin novedades relevantes.`
- Si hay evento: maximo 3 bullets, cada bullet 1 linea, con ticker/activo + porcentaje + motivo corto.
- Debe usar internet y fuentes actuales. Priorizar Reuters, CNBC, MarketWatch, Yahoo Finance, Investing.com, TradingView, Nasdaq/NYSE, CoinMarketCap/CoinGecko y fuentes oficiales.
- No emitir senales concretas sin una fuente razonable. No inventar porcentajes, motivos ni referencias.
- Si hay alerta, cada bullet debe llevar referencia corta y el mensaje debe terminar con una linea `Refs: ...`.
- Umbrales actuales: >=2% en indices/acciones grandes/ETFs; >=5% en crypto/activos volatiles; cualquier noticia muy grande.
- Prohibido: repetir resumen diario, dar vision global o escribir analisis largo.

## Atlas

- Horario: 07:00 Europe/Madrid.
- Resumen de dia en 3-5 bullets maximo.
- Solo tareas, eventos, slots clave o huecos importantes.
- Sin ensayo ni explicacion de proceso salvo fallo real.

## Ubuntu Ops

- Horarios: 08:30, 14:30 y 20:30 Europe/Madrid.
- Si todo OK: `Ubuntu Ops: todo en verde.`
- Si hay error/anomalia: maximo 5 bullets con problema e impacto/accion.
- No detallar metricas normales.

## Obsidian / changelog

- Orientado a archivos y registros, no a mensajes largos.
- Mensaje normal: `Changelog diario actualizado en Obsidian.`
- Solo ampliar si hubo algo especial: maximo 3 bullets.

## Estado de scheduler aplicado

- Warren Crypto 13:30: desactivado, consolidado.
- Warren EEUU 15:30: desactivado, consolidado.
- Ubuntu Ops 11:00/16:00/21:00: desactivado, consolidado en 3 checks diarios.
