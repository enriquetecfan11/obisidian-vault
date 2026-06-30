---
title: Migracion OpenClaw
type: document
tags:
  - mara-os
  - openclaw
  - migracion
project: MaraOS
status: active
date_created: 2026-06-30
date_modified: 2026-06-30
---

# Migracion de OpenClaw

Checklist para replicar OpenClaw y MaraOS en otra maquina sin perder contexto operativo.

## Que copiar

- Workspace OpenClaw: `/home/enriquetecfan/.openclaw/workspace`
- Vault Obsidian: `/home/enriquetecfan/Documents/obisidian-vault`
- Carpeta MaraOS completa.
- Documentacion operativa: `MaraOs/Documentacion Operativa`
- Memoria diaria si existe.
- Configuracion viva de agentes y prompts.

## Que verificar

1. Que el vault abre correctamente.
2. Que `MaraOs/Documentacion Operativa` existe.
3. Que los archivos de identidad, usuario, configuracion, agentes, prompts, memoria y migracion estan presentes.
4. Que Git puede hacer pull, commit y push.
5. Que OpenClaw carga el workspace correcto.
6. Que los MCPs de notas y calendario responden.

## Que no copiar

- Secretos en claro.
- Tokens.
- Passwords.
- Credenciales no protegidas.

## Orden recomendado

1. Restaurar el vault.
2. Verificar el repositorio Git.
3. Restaurar OpenClaw.
4. Comprobar que Mara, Atlas, Arvis y Warren siguen la documentacion viva.
5. Sincronizar cambios pendientes.

