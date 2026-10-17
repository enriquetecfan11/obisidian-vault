---
title: "Notis casero — bot de Telegram que convierte notas de voz en tareas de Notion"
type: article
tags:
  - automatizacion
  - telegram
  - notion
  - ia
  - bots
status: active
project: none
date_created: 2026-10-17
date_modified: 2026-10-17
source: https://www.javiggil.com/e83ee63f7f13
---
# Notis casero — bot de Telegram que convierte notas de voz en tareas de Notion

> Guía de javiggil (serie «Sistema E», día 56 de 100) para montar un bot que recibe notas de voz por Telegram, las transcribe, decide qué tarea son con *function calling* y las crea solas en Notion, sin abrir la app. Incluye petición por etapas para un agente de IA, código real de cada pieza, coste por mensaje y cómo venderlo a consultores de Notion.

## Resumen ejecutivo

Todo lo que hace el bot son tres pasos encadenados: **transcribir** (el audio va a una API como Whisper o `gpt-4o-mini-transcribe` y vuelve texto), **decidir qué tarea es** (*function calling*: se le describe al modelo el esquema exacto de la base de Notion y el modelo rellena campos concretos en vez de escribir prosa) y **ejecutar** (POST a la API de Notion con esos campos). No hace falta modelo propio ni equipo: son tres APIs existentes y se monta en un fin de semana con un agente tipo Claude Code. El coste real vive en la transcripción; decidir y escribir en Notion son casi gratis.

## Las tres piezas

1. **Transcribir** — audio → API de transcripción → texto.
2. **Decidir qué tarea es** — function calling: se definen los campos exactos de la base de Notion (nombre y tipo) como una herramienta JSON y el modelo rellena esos argumentos.
3. **Ejecutar** — `POST https://api.notion.com/v1/pages` con los campos, crea la página.

## Flujo técnico (piezas y código)

1. **Recibir la nota de voz.** El `Update` de Telegram trae `message.voice.file_id`; se pide con `getFile`, se descarga con la ruta devuelta.
2. **Transcribir.** `POST https://api.openai.com/v1/audio/transcriptions` con `model: whisper-1` o `gpt-4o-mini-transcribe`.
3. **Decidir con tool calling.** Se declara una herramienta `crear_tarea_notion` con `properties` (título string, estado enum, fecha_limite string ISO) y `required`; el modelo devuelve los argumentos ya rellenos.
4. **Crear la página en Notion.** `POST https://api.notion.com/v1/pages` con `Authorization: Bearer <token de integración>` y `Notion-Version: 2022-06-28`.

**Dónde corre:** no hace falta servidor propio; una función serverless (Vercel, Cloudflare Workers) que reciba el webhook de Telegram y encadene las cuatro piezas basta para empezar.

## Coste de operar

| Pieza | Coste aproximado |
| --- | --- |
| Transcripción (Whisper / gpt-4o-mini-transcribe) | 0,003-0,006 $/minuto de audio |
| Decidir la tarea (modelo barato tipo gpt-5-nano) | Fracción de céntimo por mensaje |
| Crear la página en Notion | Gratis |

Una nota de voz de 20-30 s sale por bastante menos de un céntimo. **Dónde se dispara:** audios largos y volumen alto sin control; no por decidir ni por escribir.

## Por qué empieza en Telegram y no en WhatsApp

- La puerta oficial de WhatsApp está **cerrada a asistentes de IA desde el 15 de enero de 2026** (política de negocio de Meta cuando la IA es la funcionalidad primaria).
- El atajo del número personal + QR usa librerías no oficiales (Baileys): fuera de términos y con riesgo real de bloqueo del número.
- Telegram no tiene ninguna de las dos restricciones: Bot API oficial, gratuita y sin política que prohíba un asistente de IA encima.

El punto real donde se abandona el montaje no es este, es hacer que el modelo rellene **exactamente** el esquema de tu base sin inventar campos ni duplicar filas: se prueba con notas reales y se ajusta.

## Más canales y más herramientas

- **Más canales:** Telegram (base), WhatsApp por QR con cautelas (canal de segunda, número personal), email (reenviar a `tareas@tudominio.com` y procesar con un webhook; el texto ya hace de transcripción).
- **Más herramientas:** el mismo patrón de tool calling escala dando al modelo varias funciones (`crear_evento_calendar`, `crear_contacto_crm`, `enviar_email`) y deja que elija según lo que se dijo en la nota de voz.

## Cobro y primeros clientes

- **Suscripción con tope de uso:** plan mensual con N mensajes incluidos y aviso/tope al superar; con Stripe `usage-based billing` registrando un evento por nota procesada.
- **Dónde buscar clientes:** el directorio de consultores certificados de Notion (`notion.com/explore-consultants`), gente que ya cobra por Notion y puede revender el bot como añadido. Escaparate secundario: Product Hunt.

## Advertencia del autor (frontera honesta)

El «cómo montarlo» es **recomendación suya**, no una radiografía del stack de Notis (que no publica). Datos del caso que da por verificados: Notis conecta cinco canales y más de 1.000 herramientas, cobra por suscripción y factura del orden de 16.700 $/mes con 529 clientes. Los precios de APIs y modelos son del 2026-08-19 y cambian; hay que reconfirmarlos al montar.

## Relacionado

- [[MOC Automatizaciones]] — índice del área
- [[builderbot-whatsapp-n8n]] — otra vía de bots de mensajería
- [[chatgpt-make-n8n-integracion]] — conectar ChatGPT con Make/n8n
- [[Evolution-API]] — WhatsApp vía Evolution API
