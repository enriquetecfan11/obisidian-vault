---
type: home
tags:
  - index
  - home
status: active
created: 2026-04-06
updated: 2026-04-06
---
# Vault — Segundo cerebro

Entrada principal al sistema de conocimiento. Navega por los MOCs para acceder a cualquier área del vault.

---

## Maps of Content

| MOC | Propósito |
|-----|-----------|
| [[moc-agentesia]] | IA, modelos, Custom GPTs, tooling |
| [[moc-maraos]] | Sistema de agentes personales MaraOs |
| [[moc-n8n]] | Automatizaciones y workflows N8N |
| [[moc-rrss]] | Estrategia y contenido en redes sociales |
| [[moc-proyectos]] | Proyectos activos, trabajo, inversiones |

---

## Acceso rápido

- **Diario hoy →** `MaraOs/diario/diario/`
- **Kanban →** [[kanban-workflow]]
- **Perfil personal →** [[Perfil Personal]]
- **Templates →** [[nota-base]]

---

## Pipeline de conocimiento

Este vault sigue el patrón **raw → wiki → Q&A → write-back**. Ver [[pipeline]] para la guía completa.

| Etapa | Tipo de nota | Dónde |
|-------|-------------|-------|
| Raw | `type: diario`, `pipeline: raw` | `MaraOs/diario/diario/`, borradores RRSS |
| Wiki | `type: resource/nota/ia/agent` | `IA/`, `Code/`, `N8N/`, `Work/`, agentes |
| Q&A | `type: analisis` | `MaraOs/diario/warren/`, `diario/viajes/` |
| Write-back | promover con `promotes_to` | cualquier carpeta wiki |

---

## Cómo navegar este vault

Empieza siempre por un MOC. Cada MOC es un índice curado, no una lista de todo lo que existe. Si buscas algo concreto, usa la búsqueda de Obsidian (`Cmd+O`) o el grafo para descubrir conexiones no evidentes.

- Captura ideas en el **diario** (`pipeline: raw`); promuévelas a wiki cuando tienen valor duradero.
- Cuando una síntesis Q&A responde la misma pregunta varias veces, escríbela de vuelta como nota wiki permanente (write-back).
- Los MOCs enlazan entre sí cuando los temas se solapan — sigue esos enlaces cruzados.
- No todo necesita un MOC: las notas operativas de MaraOs viven en su carpeta y se accede a ellas desde [[moc-maraos]].
