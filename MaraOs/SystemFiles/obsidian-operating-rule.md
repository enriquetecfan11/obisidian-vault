---
type: wiki
tags:
  - obsidian
  - maraos
  - system
  - knowledge-base
status: active
pipeline: wiki
created: 2026-04-09
updated: 2026-04-09
---
# Obsidian operating rule

Obsidian no es solo un repositorio de notas. En este sistema es la memoria operativa y la base de conocimiento activa de MaraOs.

## Regla principal

El vault ubicado en `/home/enriquetecfan/Documents/obisidian-vault` es el system of record para conocimiento reutilizable, contexto operativo y trabajo que deba sobrevivir al chat o a la sesión.

## Qué debe aterrizar aquí

- decisiones relevantes
- arquitectura y diseño de sistemas
- flujos y procesos
- prompts estables
- integraciones
- procedimientos
- contexto operativo reutilizable
- aprendizajes que vuelvan a servir
- convenciones del sistema y reglas de trabajo

## Regla práctica

Si algo va a importar más tarde, probablemente debe vivir en el vault.

## Ruta y convención

- Ruta canónica del vault en este host Ubuntu: `/home/enriquetecfan/Documents/obisidian-vault`
- Importante: el nombre real de la carpeta es `obisidian-vault`. No corregir automáticamente a `obsidian-vault` en scripts, referencias o documentación mientras esa ruta siga siendo la válida.
- Nota de entrada principal: [[Vault]]
- Flujo de trabajo del conocimiento: [[pipeline]]
- Área operativa principal del sistema: `MaraOs/`

## Criterio de uso

No tratar Obsidian como documentación secundaria. Tratarlo como parte del sistema real de trabajo.

Después de trabajo relevante, hacer write-back en el vault siguiendo el flujo raw → wiki → Q&A → write-back cuando aplique.

## Notas relacionadas

- [[moc-maraos]]
- [[Vault]]
- [[pipeline]]
- [[MEMORY]]

## Write-back de Mara

Los documentos vivos de Mara también forman parte del sistema real de trabajo. Cuando Mara actualice su personalidad, identidad, reglas operativas, memoria, preferencias de Kike o criterios de coordinación, debe:

1. Actualizar el archivo operativo local correspondiente.
2. Registrar o replicar el cambio en Obsidian bajo `MaraOs/SystemFiles/` o `MaraOs/diario/...`.
3. Subir el cambio a GitHub mediante el repositorio del vault cuando proceda y Kike lo haya pedido como parte del flujo.
4. Verificar el push antes de decir que está subido.

Esto permite que Kike pueda revisar la evolución de Mara y mantener un binomio cada vez mejor coordinado.

