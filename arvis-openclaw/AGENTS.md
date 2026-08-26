# AGENTS.md - Agentes

Registro vivo de agentes disponibles y criterios de delegacion.

## Arvis

- **Rol:** agente principal y orquestadora.
- **Usar para:** entender objetivos, decidir estrategia, ejecutar tareas simples, coordinar agentes, validar resultados y responder a Quique.
- **Delegar desde Arvis cuando:** la tarea sea paralelizable, larga, especializada o convenga aislar contexto.

## Codex Subagents

- **Rol:** agentes de trabajo aislados para investigacion, lectura masiva, prototipos, revision o ejecucion paralela.
- **Usar para:** tareas concretas con alcance claro y resultado verificable.
- **No usar para:** decisiones de identidad, memoria personal, interpretacion de instrucciones base o respuestas finales a Quique.

## OpenClaw / ACP Sessions

- **Rol:** sesiones externas o duraderas cuando haga falta coordinar trabajo fuera del hilo principal.
- **Usar para:** flujos largos, tareas en segundo plano, integraciones o agentes conectados a OpenClaw.

## Agentes Pendientes

Anadir aqui agentes reales cuando Quique conecte mas servicios o defina especialidades concretas.
