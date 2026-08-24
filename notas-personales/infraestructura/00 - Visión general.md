---
Type: reference
Tags:
  - infraestructura-personal
  - homelab
  - tailscale
  - acceso-remoto
Project: ""
Date Created: 2026-08-24
Date Modified: 2026-08-24
---
# Infraestructura personal — visión general

> Nota base para documentar la red y los equipos. Se ampliará con una nota por equipo, servicios, copias de seguridad y procedimientos.

## Esquema general

```text
                         ┌─────────────────────┐
                         │      Tailscale      │
                         │  red privada VPN    │
                         └──────────┬──────────┘
                                    │
 ┌──────────────────┬──────────────┼──────────────┬──────────────────┐
 ▼                  ▼              ▼              ▼                  ▼
MacBook Air      Mac mini M4   PC1 MasterRace  PC2 Simulador    PC3 Servidor
portátil         proyectos    IA y desarrollo  Windows/juegos   servicios/agente
                                                    
                                    ▼
                             Raspberry Pi 5
                                MaraOS
```

Todos los equipos se conectan mediante **Tailscale**, lo que permite comunicarlos por una red privada independientemente de dónde se encuentren. El acceso gráfico remoto se realiza principalmente con **Parsec** y **RustDesk**.

## Roles de los equipos

| Equipo | Función principal | Sistema / notas |
| --- | --- | --- |
| **MacBook Air M4** — 16 GB / 500 GB | Equipo diario y portátil; cliente remoto y desarrollo puntual sin conexión. | Puede administrar el resto de la infraestructura. |
| **Mac mini M4** — 16 GB / 1 TB | Estación principal de trabajo y repositorio de proyectos. | Ejecuta OrcaADE y está accesible por VPN. |
| **PC1 MasterRace** — i5 / 32 GB / 1 TB / RTX 3060 12 GB | Estación Linux para programación y modelos de IA locales. | Migración prevista a Omarchy; buena capacidad CUDA para LLM locales. |
| **PC2 Simulador** — i5 / 32 GB / 1 TB / RTX 3050 8 GB | Equipo dedicado al simulador, juegos y Windows. | Actualmente usa Proxmox para pruebas; se prevé Windows 11 como destino principal. |
| **PC3 Servidor** — i5 / 16 GB / 500 GB / GTX 1050 | Servidor doméstico y entorno de pruebas. | Migración prevista a Ubuntu Server; candidato para Docker y un agente personal (OpenClaw o Hermes Agent). |
| **Raspberry Pi 5** — 4 GB | Nodo ligero dedicado a MaraOS. | Pendiente de detallar los servicios concretos. |

## Conectividad y acceso

- **Tailscale:** capa común de conectividad privada entre todos los nodos. Debe ser el canal preferente para administración y servicios internos.
- **Parsec:** acceso remoto de baja latencia, especialmente útil para los equipos con GPU y el simulador.
- **RustDesk:** acceso remoto alternativo y de soporte para todos los equipos.
- **MacBook Air:** punto de acceso habitual cuando se está fuera de casa.

## Próximas notas

- [[01 - Inventario y direcciones de red]]
- [[02 - Mac mini - estación de trabajo]]
- [[03 - PC1 MasterRace - IA y desarrollo]]
- [[04 - PC2 Simulador - Windows y juegos]]
- [[05 - PC3 Servidor - servicios y agente personal]]
- [[06 - Raspberry Pi 5 - MaraOS]]
- [[07 - Acceso remoto y Tailscale]]
- [[08 - Copias de seguridad y recuperación]]

## Pendiente de decidir

- Nombre definitivo de cada nodo en Tailscale.
- Servicios que vivirán en PC3 y qué funciones tendrá MaraOS.
- Política de copias de seguridad, almacenamiento compartido y actualización de equipos.
