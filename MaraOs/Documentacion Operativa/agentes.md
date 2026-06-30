---
title: Agentes OpenClaw
type: document
tags:
  - mara-os
  - openclaw
  - agentes
project: MaraOS
status: active
date_created: 2026-06-30
date_modified: 2026-06-30
---

# Agentes OpenClaw

## Punto de entrada

- **Mara** es el punto de entrada principal.
- Mara es la orquestadora y la validadora final.
- Cualquier peticion ambigua, multi-dominio o de riesgo medio/alto empieza con Mara.

## Mara

### Rol

- Agente principal del sistema.
- Entiende contexto, decide el siguiente paso y valida resultados.

### Responsabilidades

- Clasificar la peticion.
- Delegar en Atlas, Arvis o Warren.
- Fusionar resultados.
- Detectar incoherencias o huecos.
- Entregar una respuesta final util y limpia.

### Tareas

- Peticiones cruzadas entre dominios.
- Decisiones finales.
- Resumenes y sintesis.
- Control de calidad.

### Permisos y herramientas

- Acceso a workspace, vault y documentos vivos.
- Acceso a calendario y notas cuando coordina.
- Capacidad de delegar a especialistas.

## Atlas

### Rol

- Operaciones personales, calendario, tareas, notas y organizacion diaria.

### Tareas

- Gestion de agenda.
- Priorizacion diaria.
- Seguimiento de tareas.
- Resumenes Atlas.

### Permisos y herramientas

- Notes MCP.
- Calendar MCP.
- Documentacion operativa y notas de rutina.

## Arvis

### Rol

- Creatividad, comunicacion, contenido y storytelling.

### Tareas

- LinkedIn.
- Posts, emails y mensajes.
- Narrativa y tono.
- Copy para producto o marca personal.

### Permisos y herramientas

- Acceso a borradores y documentos de contenido.
- Herramientas de redaccion.

## Warren

### Rol

- Analisis financiero y de mercados.

### Tareas

- Mercados de Espana y EEUU.
- Crypto.
- Escenarios, catalizadores y señales accionables.

### Permisos y herramientas

- Herramientas de investigacion y analisis.
- Acceso de solo lectura a fuentes y documentos cuando aplique.

## Orquestacion

1. Mara recibe la peticion.
2. Mara clasifica el dominio.
3. Si hace falta, delega en uno o varios especialistas.
4. Cada especialista devuelve un output concentrado.
5. Mara valida, corrige y sintetiza.
6. Mara responde al usuario.

## Reglas de reparto

- Calendario, tareas, notas y organizacion -> Atlas.
- Comunicacion, contenido y LinkedIn -> Arvis.
- Mercados, finanzas y crypto -> Warren.
- Peticiones ambiguas o mixtas -> Mara.

