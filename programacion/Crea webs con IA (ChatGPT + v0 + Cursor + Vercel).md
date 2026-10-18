---
title: "Crea webs con IA — ChatGPT + v0 + Cursor + Vercel"
type: article
tags:
  - ia
  - frontend
  - desarrollo
status: active
project: none
date_created: 2026-10-17
date_modified: 2026-10-17
source: https://www.javiggil.com/0d3763dddd65
---
# Crea webs con IA — ChatGPT + v0 + Cursor + Vercel

> Guía de javiggil (recurso, 28-ago-2026) para sacar una web real online y con dominio propio sin saber programar. Encadena ChatGPT (contenido), v0.dev (diseño), Cursor (código), Vercel (publicar) y Hostinger (dominio), con los prompts exactos de cada paso.

## Resumen ejecutivo

El proceso es siempre el mismo: **contenido con ChatGPT → diseño con v0 → preparar y desplegar con Cursor → publicar en Vercel → comprar y conectar dominio en Hostinger**. Lo diferencial no es crear un diseño bonito (eso lo enseñan todos), sino convertirlo en una web con link funcional y dominio propio. La guía incluye truco para usar el propio documento como tutor: subirlo a ChatGPT y pedirle que guíe paso a paso.

## Herramientas y coste

| Herramienta | Para qué | Coste |
| --- | --- | --- |
| ChatGPT | Generar el contenido | Gratis |
| v0.dev | Crear el diseño visual | Gratis (con límite) |
| Cursor | Preparar el código | Gratis (incluye tokens) |
| Vercel | Publicar | Gratis |
| Hostinger | Dominio (.com, .es) | ~10 €/año (al final) |

## Los pasos

0. **Decidir la web.** Tres preguntas en una nota: qué es, qué debe hacer el visitante (una sola acción) y con qué datos reales se llena. Sin datos reales la IA rellena con humo.
1. **Contenido (ChatGPT).** Prompt de copywriter: titular, subtítulo, 3 secciones de servicios, «Sobre nosotros», prueba (reseñas literales, sin inventar), CTA y pie con contacto.
2. **Diseño (v0.dev).** Prompt de landing moderna y responsive, pegando el contenido de ChatGPT debajo; se itera escribiendo cambios en el chat.
3. **Descargar el proyecto.** «Add to Codebase» da un comando `npx`; antes hay que instalar Node.js (versión LTS) y comprobar `node --version`.
4. **Preparar con Cursor.** Abrir la carpeta y pedir (con un modelo Claude) que revise `package.json`, configure `build`, añada lo que falte para Vercel, ejecute `npm install` y haga un build de prueba.
5. **Publicar en Vercel.** Vía Cursor (Vercel CLI, login y deploy) o vía web importando el repo de GitHub; queda un link `proyecto.vercel.app`.
6. **Dominio.** Comprar en Hostinger y conectarlo en Vercel (Settings → Domains): apuntar el registro **A** (`@`) y añadir un **CNAME** para `www` con lo que indique Vercel; la propagación DNS tarda de 10 min a 48 h.

## Funcionalidades complejas

Un sistema de reservas, un formulario que manda email o pagos: el circuito es siempre el mismo — pedir a ChatGPT un informe detallado de lo que conlleva, y pegarlo en Cursor para que lo implemente paso a paso.

## Problemas comunes

| Problema | Solución |
| --- | --- |
| «npm no se reconoce como comando» | Node.js no está instalado |
| Error de build en Vercel | Copiar el error completo a ChatGPT o Cursor |
| El dominio no conecta | Esperar hasta 48 h; revisar que los DNS coincidan con Vercel |
| Cursor no responde | Comprobar tokens; continuar con ChatGPT |
| v0 sin usos gratis | Generar HTML/CSS con ChatGPT y abrirlo en Cursor |

## Relacionado

- [[MOC Programacion]] — índice del área
- [[Cómo construir una landing premium con Claude Code]] — landing hecha con Claude Code (enfoque código)
- [[OpenCode - Orquestador de agentes]] — orquestar agentes para trabajar código
