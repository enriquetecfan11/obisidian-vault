# Actualización SystemFiles 2026-06-08

## Objetivo

Actualizar documentos propios/importantes de Mara dentro de `MaraOs/SystemFiles` para reflejar el estado operativo actual en Ubuntu y la política consolidada de crons.

## Actualizado

- Rutas canónicas: vault `/home/enriquetecfan/Documents/obisidian-vault`, área `MaraOs/`, sistema `MaraOs/SystemFiles/`.
- Diarios nuevos: `MaraOs/diario/diario/diario-DD-MM-YYYY.md`.
- `MaraOs/daily/` marcado como histórico/legacy.
- Resúmenes Atlas, changelogs y resúmenes semanales bajo `MaraOs/diario/...`.
- Política de crons breves tipo brief de radio y consolidaciones de Warren/Ubuntu Ops.
- Modelo actual de agentes: Mara, Atlas, Arvis y Warren activos; Scout legacy/no vivo.
- Reglas de tareas/calendario por MCP, tareas dictadas solo en `agents-notes`, viajes en Obsidian.
- Registro GitHub del vault esperado: `https://github.com/enriquetecfan11/obisidian-vault.git`.

## Archivos tocados

- `AGENTS.md`
- `TOOLS.md`
- `MEMORY.md`
- `README.md`
- `USER.md`
- `cron-principales.md`
- `team-operating-model.md`
- `knowledge-base/README.md`
- `knowledge-base/system/00-overview.md`
- `knowledge-base/system/01-agent-architecture.md`
- `knowledge-base/system/02-mcp-integrations.md`
- `knowledge-base/system/03-repos-and-ops.md`
- `knowledge-base/system/04-governance.md`
- `systemfiles-update-2026-06-08.md`

## Limitaciones

- No se han tocado cambios previos ajenos fuera de `MaraOs/SystemFiles`.
- `cron-principales.md` documenta el estado operativo consolidado, no conserva todos los Job ID antiguos porque algunos crons fueron desactivados/consolidados.
- Durante el rebase, el remoto ya había eliminado `MaraOs/SystemFiles/prompts/README.md`; se respetó ese borrado y no se reintrodujo.
