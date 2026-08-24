---
Type: reference
Tags:
  - infraestructura-personal
  - topologia-de-red
  - tailscale
  - acceso-remoto
Project: ""
Date Created: 2026-08-24
Date Modified: 2026-08-24
---

# Topología de red

```mermaid
flowchart TB
    TS(["Tailscale<br/>Red privada VPN"])

    subgraph Apple["Dispositivos Apple"]
        MBA["MacBook Air M4<br/>Portátil y acceso remoto"]
        MM["Mac mini M4<br/>Proyectos y trabajo principal"]
    end

    subgraph PCs["PCs — instalaciones desde cero"]
        P1["PC1 MasterRace<br/>Omarchy · IA y desarrollo"]
        P2["PC2 Simulador<br/>Windows 11 · juegos y simulador"]
        P3["PC3 Servidor<br/>Ubuntu Server · Docker y agente"]
    end

    RPI["Raspberry Pi 5<br/>MaraOS"]

    TS --- MBA
    TS --- MM
    TS --- P1
    TS --- P2
    TS --- P3
    TS --- RPI

    MBA -. "Parsec / RustDesk" .-> MM
    MBA -. "Parsec / RustDesk" .-> P1
    MBA -. "Parsec / RustDesk" .-> P2
    MBA -. "RustDesk" .-> P3

    classDef vpn fill:#2563eb,color:#ffffff,stroke:#1d4ed8,stroke-width:2px
    classDef apple fill:#e5e7eb,color:#111827,stroke:#9ca3af
    classDef pc fill:#fef3c7,color:#78350f,stroke:#f59e0b
    classDef pi fill:#dcfce7,color:#14532d,stroke:#22c55e

    class TS vpn
    class MBA,MM apple
    class P1,P2,P3 pc
    class RPI pi
```

## Lectura del esquema

- Las líneas continuas representan la conectividad privada común mediante Tailscale.
- Las líneas discontinuas muestran el acceso gráfico remoto habitual desde el MacBook Air.
- El acceso remoto de la Raspberry Pi está pendiente de decidir.

Ver también: [[01 - Dispositivos Apple]], [[02 - PCs]], [[03 - Raspberry Pi 5 - MaraOS]] y [[04 - Red, acceso remoto y pendientes]].
