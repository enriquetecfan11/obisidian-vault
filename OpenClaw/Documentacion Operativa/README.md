---
title: readme
type: index
tags:
  - openclaw
  - documentacion-operativa
project: none
status: active
date_created: 2026-08-13
date_modified: 2026-08-23
---
# Documentacion Operativa de OpenClaw

Carpeta canonica para centralizar la documentacion operativa de OpenClaw dentro de MaraOS.

## Fuente de verdad

- Este vault es la fuente persistente de verdad.
- Todo lo que se genere para OpenClaw debe guardarse aqui primero.
- La carpeta esta pensada para sincronizarse con Git/GitHub sin depender del chat.

## Estructura

- `identidad.md`: identidad y rol operativo de Mara.
- `usuario.md`: contexto de Kike, preferencias y herramientas habituales.
- `configuracion.md`: rutas, MCPs, agentes, sincronizacion y notas de sistema.
- `migracion.md`: checklist para replicar el entorno en otra maquina.
- `agentes.md`: definicion funcional de Mara, Atlas, Arvis y Warren.
- `prompts.md`: prompts y reglas base de cada agente.
- `memoria.md`: decisiones y aprendizajes operativos que deben persistir.

## Archivos espejo

Los archivos `AGENTS-ARCHITECTURE.md` e `IDENTITY.md` se conservan tambien como espejo de compatibilidad dentro de esta carpeta.

## Regla de uso

1. Si algo cambia en OpenClaw, se actualiza primero aqui.
2. Si cambia un agente, se actualiza su doc y su prompt asociado.
3. Si cambia una ruta, MCP o flujo operativo, se refleja en `configuracion.md` y `migracion.md`.
4. Si hay una leccion estable, se anota en `memoria.md`.

