# Mara - Backup y Migracion

Carpeta para documentar como replicar a Mara en otra maquina sin perder contexto operativo ni configuracion conocida.

## Contenido

- `identidad.md`: identidad, rol, tono y reglas base de Mara.
- `usuario.md`: contexto conocido de Kike, preferencias y herramientas habituales.
- `configuracion.md`: skills, agentes, MCPs, cronjobs, rutas y servicios documentados.
- `migracion.md`: checklist para copiar, instalar, configurar y comprobar una migracion.

## Como usarla para migrar

1. Leer primero `identidad.md` y `usuario.md` para recuperar el comportamiento esperado.
2. Revisar `configuracion.md` para preparar rutas, skills, MCPs, automatizaciones y servicios.
3. Seguir `migracion.md` como checklist operativo.
4. Copiar solo archivos y configuraciones necesarias. No copiar secretos en claro.
5. En la maquina destino, comprobar que OpenClaw, Obsidian, MCPs, Telegram y cronjobs funcionan antes de considerar terminada la migracion.

## Reglas de seguridad

- No guardar tokens, passwords ni secretos reales en esta carpeta.
- Usar placeholders como `<TOKEN>`, `<PASSWORD>`, `<API_KEY>` o `<SECRET>`.
- Si un dato no esta verificado, dejarlo como `No especificado`.
- Obsidian es la fuente de verdad operativa cuando algo debe sobrevivir al chat.

