# Repositorios y Operación

## `obisidian-vault`
- Vault canónico local: `/home/enriquetecfan/Documents/obisidian-vault`.
- Remote esperado: `https://github.com/enriquetecfan11/obisidian-vault.git`.
- Área operativa principal: `MaraOs/`.
- Archivos canónicos del sistema: `MaraOs/SystemFiles/`.
- Diarios nuevos: `MaraOs/diario/diario/diario-DD-MM-YYYY.md`.
- Resúmenes Atlas, changelogs y resúmenes semanales: `MaraOs/diario/...`, salvo instrucción explícita distinta.
- `MaraOs/daily/` es histórico/legacy.
- Tras cambios relevantes en documentos propios de Mara, verificar `git status`, commit claro y `git push`, salvo conflicto o instrucción distinta de Kike.

## `mara-os`
- Contiene Mission Control / dashboard y lógica operativa.
- Remotos:
  - `origin`: `https://github.com/tecfandeveloper/mara-os.git`
  - `upstream`: `https://github.com/carlosazaustre/tenacitOS.git`

## Estructura de conocimiento en Obsidian
- Contiene conocimiento estructurado de Mara dentro de `MaraOs/SystemFiles/` y `MaraOs/diario/...`.
- Estructura base en SystemFiles:
  - `inbox/` entrada rápida
  - `skills/draft` y `skills/approved`
  - `knowledge-base/`
  - `datasets/`
  - `prompts/{mara,atlas,arvis,warren}`
  - `archive/`

## Flujo recomendado
1. Kike sube contenido a `inbox/`.
2. Mara clasifica y mueve.
3. Commit con mensaje claro.
4. Push a `main`.
