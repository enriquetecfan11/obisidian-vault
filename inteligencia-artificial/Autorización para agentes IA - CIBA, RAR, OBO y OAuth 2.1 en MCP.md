---
title: Autorización para agentes IA - CIBA, RAR, OBO y OAuth 2.1 en MCP
tags:
  - ia
  - agentes-ia
  - mcp
  - ciberseguridad
  - documentacion
date_created: 2026-11-12
date_modified: 2026-11-12
status: active
---

# Autorización para agentes IA: CIBA, RAR, OBO y OAuth 2.1 en MCP

Los agentes de IA no solo conversan: llaman a herramientas, APIs y datos. Hace falta autenticar a la persona, limitar qué puede hacer el agente y, cuando hay varios servicios en cadena, dejar claro en nombre de quién actúa. Estos cuatro conceptos cubren ese recorrido: cómo se aprueba (CIBA), con qué detalle (RAR), con qué delegación (OBO) y cómo se aplica en MCP (OAuth 2.1).

## CIBA (Client-Initiated Backchannel Authentication)

Autenticación mediante un canal independiente, como la aprobación desde el móvil.

Es una extensión de OpenID Connect (especificada en *OpenID Connect Client-Initiated Backchannel Authentication Core*). El cliente inicia el flujo por un canal de backchannel, no por el navegador del usuario. El usuario autentica o aprueba en otro dispositivo (por ejemplo, una app en el móvil). El grant type es `urn:openid:params:grant-type:ciba`.

**Caso típico:** un agente o un cajero pide consentimiento y la persona confirma en el teléfono, sin introducir credenciales en la máquina que inició la petición.

## RAR (Rich Authorization Requests)

Autorización granular para definir exactamente qué operaciones puede realizar una aplicación.

Está definido en el [RFC 9396](https://www.rfc-editor.org/rfc/rfc9396.html). En lugar de limitarse a *scopes* generales, la petición incluye el parámetro `authorization_details`: un array JSON que describe, con tipos y campos (acciones, recursos, etc.), qué se pide autorizar.

**Caso típico:** en vez de un alcance amplio como «acceso a pagos», se autoriza solo «transferir hasta 50 € a esta cuenta, una vez».

## OBO (On-Behalf-Of)

Delegación de identidad y permisos para que una aplicación o servicio actúe en nombre de un usuario.

Hay dos referencias habituales, relacionadas pero no idénticas:

- El [RFC 8693](https://www.rfc-editor.org/rfc/rfc8693.html) (*OAuth 2.0 Token Exchange*) permite canjear un token por otro, con una identidad o un conjunto de permisos distintos.
- El flujo *On-Behalf-Of* de Microsoft Identity Platform es un caso concreto de ese patrón: un API intermedio canjea el token del usuario por otro token para llamar a un API posterior actuando en su nombre.

**Caso típico:** el usuario autoriza a un agente; ese agente llama a un servicio intermedio, y este obtiene un token para consultar un API interno como si fuera el usuario, sin pedirle de nuevo la contraseña.

## OAuth 2.1 para MCP (Model Context Protocol)

Autorización segura para que agentes de IA accedan a herramientas, APIs y recursos mediante tokens y permisos controlados.

La especificación de autorización de MCP se apoya en OAuth 2.1. Incluye PKCE (el cliente no usa un secreto compartido de forma insegura), metadatos del recurso protegido ([RFC 9728](https://www.rfc-editor.org/rfc/rfc9728.html), para que el servidor MCP anuncie su servidor de autorización) e indicadores de recurso ([RFC 8707](https://www.rfc-editor.org/rfc/rfc8707.html), para restringir el *audience* del token al recurso concreto).

**Caso típico:** un agente se conecta a un servidor MCP (correo, calendario, base de datos); el usuario autoriza y el agente opera solo con el token y los permisos concedidos, no con credenciales guardadas en el prompt.

## Comparación

| Concepto | Qué resuelve | Referencia principal | En un agente, para qué sirve |
|---|---|---|---|
| CIBA | Aprobar en un canal distinto al que inició la petición | OpenID Connect CIBA | Confirmar una acción sensible en el móvil mientras el agente espera |
| RAR | Pedir permiso con detalle, no solo con un *scope* amplio | RFC 9396 (`authorization_details`) | Limitar la operación (recurso, acción, importe, vigencia) |
| OBO | Actuar en nombre del usuario a través de varios servicios | RFC 8693; flujo OBO de Microsoft | Encadenar APIs sin reautenticar ni mezclar identidades |
| OAuth 2.1 en MCP | Autorizar el acceso de un agente a herramientas MCP | Especificación de autorización de MCP; PKCE; RFC 9728; RFC 8707 | Conectar el agente a servidores MCP con tokens acotados |

## Relacionado

- [[MOC Inteligencia Artificial]]
- [[MCP y skills]]
- [[ejercito-empleados-digitales]]
- [[Post LinkedIn - MCP es el enchufe - 2026-10-28]]
- [[Documentación MCP Linear — ClawdBot]]
- [[CAI Framework - Inteligencia Artificial Seguridad]]
