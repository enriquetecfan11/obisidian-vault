# Migracion de Mara

Checklist para replicar a Mara en otra maquina sin perder contexto ni configuracion conocida.

## Que copiar

Copiar:

- Workspace OpenClaw: `/home/enriquetecfan/.openclaw/workspace`.
- Memoria diaria del workspace: `memory/YYYY-MM-DD.md`.
- Memoria curada si existe: `MEMORY.md`.
- Documentos vivos del workspace: `SOUL.md`, `IDENTITY.md`, `USER.md`, `TOOLS.md`, `AGENTS.md`.
- Vault Obsidian: `/home/enriquetecfan/Documents/obisidian-vault`.
- Carpeta principal MaraOS: `MaraOs/`.
- Archivos canonicos: `MaraOs/SystemFiles/`.
- Cronjobs OpenClaw:
  - `/home/enriquetecfan/.openclaw/cron/jobs.json`
  - `/home/enriquetecfan/.openclaw/cron/jobs-state.json`
  - `/home/enriquetecfan/.openclaw/cron/runs/` si se quiere conservar historial.

No copiar:

- Tokens, passwords o secretos en claro.
- Cache temporal no necesaria.
- Archivos locales de sesion si contienen datos sensibles y no son imprescindibles.

## Que instalar

- Ubuntu Desktop o entorno Linux compatible: version exacta No especificado.
- OpenClaw: version exacta No especificado.
- Node.js: version documentada en runtime local, `v22.22.1`.
- Git.
- Obsidian.
- Docker, si se mantiene Ubuntu Ops y servicios asociados.
- Tailscale, si se usa en la maquina destino.
- Dependencias de skills: No especificado.

## Que configurar

1. Restaurar el vault en:
   - `/home/enriquetecfan/Documents/obisidian-vault`
2. Mantener literalmente el nombre `obisidian-vault`.
3. Restaurar workspace en:
   - `/home/enriquetecfan/.openclaw/workspace`
4. Configurar OpenClaw y Telegram para el chat directo de Kike.
5. Configurar MCPs:
   - Calendario: `https://core-n8n.832gky.easypanel.host/mcp/calendar`
   - Tareas/notas: `https://core-n8n.832gky.easypanel.host/mcp/agents-notes`
   - Linear: `https://core-n8n.832gky.easypanel.host/mcp/agents-linear` si aplica.
6. Restaurar cronjobs desde `jobs.json`.
7. Revisar que los cronjobs apunten a `Europe/Madrid`.
8. Configurar Git remoto del vault:
   - `https://github.com/enriquetecfan11/obisidian-vault.git`
9. Configurar secretos mediante el mecanismo seguro del sistema, nunca en Markdown:
   - `<OPENCLAW_TOKEN>`
   - `<GITHUB_TOKEN>`
   - `<MCP_AUTH_TOKEN>`
   - `<TELEGRAM_TOKEN>`
   - `<N8N_SECRET>`

## Como comprobar que todo funciona

### Obsidian

- Abrir el vault en `/home/enriquetecfan/Documents/obisidian-vault`.
- Comprobar que existe `MaraOs/SystemFiles/`.
- Comprobar que existe `MaraOs/diario/diario/`.
- Crear una nota de prueba y verificar que Git la detecta.

### Git/GitHub

- Ejecutar `git status` dentro del vault.
- Verificar remoto con `git remote -v`.
- Hacer `git pull` si procede.
- Hacer commit y push de una prueba no sensible.

### OpenClaw

- Confirmar que Mara arranca con el workspace correcto.
- Confirmar que carga `SOUL.md`, `IDENTITY.md`, `USER.md`, `TOOLS.md` y `AGENTS.md`.
- Confirmar que puede enviar respuesta visible por Telegram.
- Confirmar que puede leer y escribir en el vault.

### MCPs

- Calendario: listar eventos y crear un evento de prueba recuperable.
- Tareas/notas: listar tareas y crear una tarea de prueba recuperable.
- Completar o borrar las pruebas despues de verificarlas.

### Cronjobs

- Listar cronjobs activos.
- Verificar que existen:
  - Atlas 07:00.
  - Diario Obsidian 00:05.
  - Changelog 20:00.
  - Resumen semanal domingo 20:00.
  - WatchDog Warren 09-21.
  - Warren 22:30.
  - Ubuntu Ops 08:30/14:30/20:30.
- Ejecutar manualmente un cron no destructivo o esperar al siguiente run.
- Comprobar que la entrega por Telegram funciona.

### Seguridad

- Buscar secretos accidentalmente guardados en Markdown.
- Verificar que esta carpeta solo contiene placeholders.
- Confirmar que acciones externas sensibles siguen pidiendo confirmacion.

## Criterio de migracion completa

La migracion se considera completa cuando:

- Mara responde con su tono y reglas correctas.
- Obsidian esta disponible y es escribible.
- MCPs de calendario y tareas responden.
- Telegram envia y recibe correctamente.
- Cronjobs principales estan restaurados y activos.
- Git del vault puede hacer commit y push.
- No hay secretos reales guardados en archivos Markdown.

