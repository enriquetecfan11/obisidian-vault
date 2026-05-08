# TOOLS.md - Notas operativas locales

Las skills explican cómo usar herramientas generales. Este archivo guarda detalles específicos de este entorno.

## Obsidian

- Ruta canónica del vault: `/home/enriquetecfan/Documents/obisidian-vault`.
- Mantener literalmente `obisidian-vault`; no corregirlo a `obsidian-vault`.
- Obsidian es la fuente de verdad por defecto para conocimiento operativo: memoria, decisiones, prompts, procedimientos, arquitectura, contexto reutilizable y documentación viva.
- Si Kike dice “recuerda”, “acuérdate”, “como esta mañana” o pide recuperar contexto anterior, consultar primero Obsidian.
- Si hay notas duplicadas o en conflicto, priorizar la nota canónica del vault.
- Regla práctica: si algo importa mañana, probablemente debe quedar en Obsidian.
- Área operativa principal: `/home/enriquetecfan/Documents/obisidian-vault/MaraOs/`.
- Archivos canónicos del sistema: `/home/enriquetecfan/Documents/obisidian-vault/MaraOs/SystemFiles/`.

## Tareas y calendario

- Tareas y calendario deben usar las integraciones/MCPs configuradas en esta máquina, no sistemas paralelos inventados.
- **Regla fija de Kike:** las tareas que él dicte deben apuntarse **solo en el MCP de `agents-notes`**.
- Al crear tareas en `agents-notes`, usar `Title`, `Notes`, `Due_Date` y `Completion_Date`. `Due_Date` es la fecha de la tarea; `Completion_Date` es la fecha en que debe completarse. Formato verificado: RFC3339, por ejemplo `2026-05-11T00:00:00.000Z`.
- La finalización real se marca con la herramienta `Complete_a_Task`; el sistema registra la fecha de completado.
- No guardar tareas en cron, Obsidian ni listas paralelas salvo que Kike pida explícitamente un recordatorio/programación adicional.
- Para eventos, usar el sistema configurado de calendario.
- Si una integración falla o no está disponible, decirlo claro; no inventar estados.

## GitHub / registro de documentación viva

- Cuando Mara actualice documentos propios importantes (`SOUL.md`, `USER.md`, `TOOLS.md`, `IDENTITY.md`, `AGENTS.md`, memoria operativa o reglas estables), debe dejar copia/registro en Obsidian.
- El vault canónico tiene remote GitHub configurado: `https://github.com/enriquetecfan11/obisidian-vault.git`.
- Después de cambios relevantes en el vault, verificar `git status`, hacer commit con mensaje claro y `git push`, salvo que Kike indique lo contrario o haya riesgo/conflicto que requiera confirmación.
- No afirmar que algo está subido a GitHub sin verificar el resultado del `git push`.
