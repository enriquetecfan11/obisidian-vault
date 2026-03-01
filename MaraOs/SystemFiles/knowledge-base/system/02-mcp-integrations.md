# Integraciones MCP

## Atlas — MCPs principales

### Calendar MCP
- Endpoint: `https://core-n8n.832gky.easypanel.host/mcp/agents-calendar`
- Uso: crear, consultar, editar y borrar eventos.
- Estado: operativo.

### Notes MCP
- Endpoint: `https://core-n8n.832gky.easypanel.host/mcp/agents-notes`
- Uso: gestión de tareas/notas (crear, listar, completar, borrar).
- Estado: operativo.

## Convención de uso
- Todo calendario/notas se enruta a **Atlas** por defecto.
- Mara interviene solo para coordinación, conflictos o decisiones.

## Troubleshooting rápido
- Si un MCP devuelve `404`: endpoint incorrecto.
- Si devuelve `Tool not found`: refrescar schema con `mcporter list <server> --schema`.
- Si falla memoria de n8n (`No session ID found`): revisar workflow/nodo de memoria en backend.

