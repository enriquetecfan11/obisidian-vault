---
type: "resource"
tags:
  - raspberry-pi
  - networking
  - vpn
  - wireguard
  - pi-hole
  - tailscale
project: "none"
status: "pendiente"
date_created: "2026-03-01"
date_modified: "2026-03-01"
related: [] # Array vacío o con [[links]]
---

# Guía Completa - Raspberry Pi Gateway con Tailscale, WireGuard y Pi-hole

## 📋 Tabla de Contenidos

1. [Introducción](#introducción)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Requisitos Previos](#requisitos-previos)
4. [Fase 1: Preparación de la Raspberry Pi](#fase-1-preparación-de-la-raspberry-pi)
5. [Fase 2: Instalación de Tailscale](#fase-2-instalación-de-tailscale)
6. [Fase 3: Instalación de Pi-hole](#fase-3-instalación-de-pi-hole)
7. [Fase 4: Instalación de WireGuard](#fase-4-instalación-de-wireguard)
8. [Fase 5: Configuración de Enrutamiento](#fase-5-configuración-de-enrutamiento)
9. [Configuración de Clientes](#configuración-de-clientes)
10. [Verificación y Pruebas](#verificación-y-pruebas)
11. [Solución de Problemas](#solución-de-problemas)
12. [Mantenimiento](#mantenimiento)

---

## Introducción

Esta guía te ayudará a configurar una Raspberry Pi 5 como gateway de red completo con las siguientes capacidades:

- **Tailscale**: Acceso remoto seguro mediante VPN mesh
- **Pi-hole**: Bloqueo de anuncios y DNS personalizado para toda la red
- **WireGuard**: VPN local para dispositivos de confianza
- **Gateway/Router**: Enrutamiento entre todas las redes

### ¿Qué lograremos?

```
Internet
   ↓
[Router Principal]
   ↓
[Raspberry Pi 5 Gateway]
   ├─→ Tailscale (Acceso remoto desde cualquier lugar)
   ├─→ Pi-hole (Bloqueo de anuncios para toda la red)
   ├─→ WireGuard (VPN local para dispositivos móviles)
   └─→ LAN (192.168.1.0/24)
```

---

## Arquitectura del Sistema

### Rangos de Red

| Red | Rango | Propósito |
|-----|-------|-----------|
| LAN Local | 192.168.1.0/24 | Red doméstica principal |
| WireGuard | 10.0.0.0/24 | VPN local para clientes |
| Tailscale | 100.x.x.x/32 | Red mesh automática de Tailscale |

### Puertos Utilizados

| Servicio | Puerto | Protocolo |
|----------|--------|-----------|
| WireGuard | 51820 | UDP |
| Pi-hole Web | 80/443 | TCP |
| Pi-hole DNS | 53 | TCP/UDP |
| Tailscale | 41641 | UDP |

---

## Requisitos Previos

### Hardware

- ✅ Raspberry Pi 5 (4GB RAM mínimo recomendado)
- ✅ Tarjeta microSD de 32GB o superior
- ✅ Fuente de alimentación oficial (27W para Pi 5)
- ✅ Cable Ethernet
- ✅ Acceso al router principal

### Software

- ✅ Raspberry Pi OS (64-bit) instalado
- ✅ Acceso SSH habilitado
- ✅ Conexión a Internet funcional
- ✅ Cuenta de Tailscale (gratuita en https://tailscale.com)

### Conocimientos

- Conocimientos básicos de Linux/terminal
- Acceso al panel de administración del router
- Editor de texto básico (nano/vim)

---

## Fase 1: Preparación de la Raspberry Pi

### 1.1 Conexión Inicial

Conéctate a tu Raspberry Pi por SSH:

```bash
ssh pi@192.168.1.X
# Reemplaza X con la IP de tu Raspberry Pi
```

### 1.2 Actualización del Sistema

```bash
# Actualizar lista de paquetes
sudo apt update

# Actualizar todos los paquetes instalados
sudo apt upgrade -y

# Limpiar paquetes antiguos
sudo apt autoremove -y
sudo apt autoclean
```

### 1.3 Instalación de Herramientas Esenciales

```bash
# Instalar herramientas necesarias
sudo apt install -y \
    iptables-persistent \
    curl \
    git \
    net-tools \
    dnsutils \
    htop \
    vim \
    qrencode
```

**Explicación de cada herramienta:**

- `iptables-persistent`: Guarda las reglas de firewall entre reinicios
- `curl`: Descarga archivos desde Internet
- `git`: Control de versiones (útil para scripts)
- `net-tools`: Herramientas de red (ifconfig, netstat, etc.)
- `dnsutils`: Herramientas DNS (dig, nslookup)
- `htop`: Monitor de procesos mejorado
- `vim`: Editor de texto avanzado
- `qrencode`: Genera códigos QR para configuraciones de WireGuard

### 1.4 Habilitar IP Forwarding

El IP forwarding permite que la Raspberry Pi actúe como router, reenviando paquetes entre interfaces de red.

```bash
# Editar el archivo de configuración del kernel
sudo nano /etc/sysctl.conf
```

Busca la línea:
```
#net.ipv4.ip_forward=1
```

Descoméntala (quita el #):
```
net.ipv4.ip_forward=1
```

Guarda el archivo (`Ctrl+O`, `Enter`, `Ctrl+X`)

Aplica los cambios:

```bash
# Aplicar cambios inmediatamente
sudo sysctl -p

# Verificar que está habilitado (debe mostrar 1)
cat /proc/sys/net/ipv4/ip_forward
```

### 1.5 Configurar IP Estática

Es importante que la Raspberry Pi tenga una IP estática en tu red local.

```bash
# Editar la configuración de red
sudo nano /etc/dhcpcd.conf
```

Añade al final del archivo (ajusta según tu red):

```
# Configuración estática para eth0
interface eth0
static ip_address=192.168.1.10/24
static routers=192.168.1.1
static domain_name_servers=127.0.0.1 1.1.1.1
```

**Explicación:**
- `ip_address`: IP estática de la Pi (elige una fuera del rango DHCP)
- `routers`: IP de tu router principal
- `domain_name_servers`: Primero localhost (Pi-hole), luego Cloudflare como respaldo

Reinicia el servicio de red:

```bash
sudo systemctl restart dhcpcd
```

---

## Fase 2: Instalación de Tailscale

Tailscale crea una red VPN mesh que permite acceder a tu red local desde cualquier lugar de forma segura.

### 2.1 Instalación del Cliente

```bash
# Descargar e instalar Tailscale
curl -fsSL https://tailscale.com/install.sh | sh
```

### 2.2 Configuración como Subnet Router

```bash
# Iniciar Tailscale con opciones avanzadas
sudo tailscale up \
    --advertise-routes=192.168.1.0/24 \
    --advertise-exit-node \
    --accept-dns=false
```

**Explicación de las opciones:**

- `--advertise-routes=192.168.1.0/24`: Anuncia tu red local a Tailscale
- `--advertise-exit-node`: Permite usar la Pi como salida a Internet
- `--accept-dns=false`: No sobrescribir la configuración DNS (usaremos Pi-hole)

El comando te dará una URL como:
```
To authenticate, visit: https://login.tailscale.com/a/XXXXXXXX
```

### 2.3 Autenticación y Configuración Web

1. Abre la URL en tu navegador
2. Inicia sesión con tu cuenta de Tailscale
3. Autoriza el dispositivo
4. Ve a: https://login.tailscale.com/admin/machines
5. Encuentra tu Raspberry Pi en la lista
6. Haz clic en los tres puntos (...) junto al dispositivo
7. **Habilita "Subnet routes"** - marca la casilla de 192.168.1.0/24
8. **Habilita "Exit node"** si quieres usarla como salida a Internet
9. (Opcional) Desactiva la caducidad de claves en "Disable key expiry"

### 2.4 Verificar la Conexión

```bash
# Ver el estado de Tailscale
sudo tailscale status

# Ver la IP de Tailscale asignada
sudo tailscale ip -4

# Probar conectividad
sudo tailscale ping nombre-de-otro-dispositivo
```

### 2.5 Configuración Adicional (Opcional)

**Establecer un hostname personalizado:**

```bash
sudo tailscale up --hostname=raspberry-gateway
```

**Ver logs en caso de problemas:**

```bash
sudo journalctl -u tailscaled -f
```

---

## Fase 3: Instalación de Pi-hole

Pi-hole actúa como servidor DNS que bloquea dominios de publicidad y rastreadores.

### 3.1 Instalación Automática

```bash
# Descargar e instalar Pi-hole
curl -sSL https://install.pi-hole.net | bash
```

### 3.2 Opciones Durante la Instalación

Durante el proceso interactivo, selecciona:

1. **Upstream DNS Provider**: Selecciona Cloudflare (1.1.1.1) o Google (8.8.8.8)
2. **Blocklists**: Deja las predeterminadas marcadas
3. **Admin Web Interface**: ✅ Sí
4. **Web Server**: ✅ Instalar lighttpd
5. **Logging**: ✅ Habilitar
6. **Privacy Mode**: Selecciona según tu preferencia (Show everything recomendado)
7. **Interface**: Selecciona `eth0` (tu interfaz principal)

### 3.3 Guardar Credenciales

Al finalizar, Pi-hole mostrará:

```
  [✓] Configure Pi-hole
  [✓] Install packages
  [✓] Configure firewall
  
  Web Interface: http://192.168.1.10/admin
  Password: XXXXXXXXXX
```

**⚠️ IMPORTANTE: Guarda esta contraseña**

### 3.4 Cambiar la Contraseña (Opcional)

```bash
# Establecer una nueva contraseña
pihole -a -p

# O sin contraseña (no recomendado)
pihole -a -p ""
```

### 3.5 Configuración Inicial del Panel Web

1. Accede a: `http://192.168.1.10/admin`
2. Haz clic en "Login" e ingresa tu contraseña
3. Ve a **Settings** → **DNS**
4. Configura:
   - **Upstream DNS Servers**: Cloudflare (1.1.1.1 y 1.0.0.1)
   - **Interface listening behavior**: Listen on all interfaces
   - **Advanced DNS settings**: Habilita DNSSEC

### 3.6 Añadir Listas de Bloqueo Adicionales

Ve a **Group Management** → **Adlists** y añade:

```
https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
https://v.firebog.net/hosts/AdguardDNS.txt
https://v.firebog.net/hosts/Easylist.txt
https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt
```

Luego actualiza:

```bash
pihole -g
```

### 3.7 Configurar Pi-hole como DNS de la Red

**Opción A: Configurar en el router (Recomendado)**

1. Accede al panel de tu router (usualmente 192.168.1.1)
2. Busca la configuración DHCP/DNS
3. Establece el DNS primario como: `192.168.1.10`
4. Guarda y reinicia el router

**Opción B: Configurar en cada dispositivo manualmente**

En cada dispositivo, configura DNS como `192.168.1.10`

### 3.8 Verificar Funcionamiento

```bash
# Ver estadísticas
pihole -c

# Ver logs en tiempo real
pihole -t

# Probar resolución DNS
dig @192.168.1.10 google.com

# Probar bloqueo de anuncios
dig @192.168.1.10 doubleclick.net
# Debe responder con 0.0.0.0
```

---

## Fase 4: Instalación de WireGuard

WireGuard es una VPN moderna, rápida y segura para conectar dispositivos a tu red local.

### 4.1 Instalación de WireGuard

```bash
# Instalar WireGuard
sudo apt install -y wireguard wireguard-tools

# Crear directorio de configuración
sudo mkdir -p /etc/wireguard
cd /etc/wireguard
```

### 4.2 Generar Claves del Servidor

```bash
# Generar par de claves del servidor
umask 077
wg genkey | sudo tee /etc/wireguard/server_private.key | wg pubkey | sudo tee /etc/wireguard/server_public.key

# Ver las claves generadas
sudo cat /etc/wireguard/server_private.key
UNZYOmaqbnTI0a7DlBMa2pdEOuMqumyZOZXwioGa9mU=

sudo cat /etc/wireguard/server_public.key
MqCSj/kXanWPXiiz29Dn0H6QLowr0qk5hnfzjFGTwzM=
```

**⚠️ Guarda estas claves en un lugar seguro**

### 4.3 Configurar el Servidor WireGuard

```bash
# Crear el archivo de configuración
sudo nano /etc/wireguard/wg0.conf
```

Pega la siguiente configuración:

```ini
[Interface]
# Dirección IP del servidor dentro de la VPN
Address = 10.0.0.1/24

# Puerto de escucha
ListenPort = 51820

# Clave privada del servidor (reemplaza con la tuya)
PrivateKey = UNZYOmaqbnTI0a7DlBMa2pdEOuMqumyZOZXwioGa9mU=

# Reglas que se ejecutan al levantar la VPN
PostUp = iptables -A FORWARD -i wg0 -j ACCEPT; iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE; iptables -A FORWARD -o wg0 -j ACCEPT
PostDown = iptables -D FORWARD -i wg0 -j ACCEPT; iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE; iptables -D FORWARD -o wg0 -j ACCEPT

# DNS para los clientes (Pi-hole)
DNS = 192.168.1.10

# MTU óptimo (ajustar si hay problemas de conectividad)
MTU = 1420
```

**Reemplaza `CONTENIDO_DE_server_private.key`** con tu clave privada:

```bash
# Obtener la clave privada
sudo cat /etc/wireguard/server_private.key

# Editamos de nuevo el archivo
sudo nano /etc/wireguard/wg0.conf
# Y pegamos la clave privada en la línea PrivateKey
```

Establece permisos correctos:

```bash
sudo chmod 600 /etc/wireguard/wg0.conf
sudo chmod 600 /etc/wireguard/server_private.key
```

### 4.4 Generar Configuraciones de Clientes

Vamos a crear un script para generar configuraciones de clientes fácilmente:

```bash
sudo nano /etc/wireguard/add-client.sh
```

Pega este script:

```bash
#!/bin/bash

# Script para generar configuración de cliente WireGuard

if [ -z "$1" ]; then
    echo "Uso: $0 nombre-cliente"
    exit 1
fi

CLIENT_NAME=$1
SERVER_PUBLIC_KEY=$(sudo cat /etc/wireguard/server_public.key)
SERVER_ENDPOINT="TU_IP_PUBLICA:51820"  # Reemplaza con tu IP pública o dominio
CLIENT_NUMBER=$(ls /etc/wireguard/clients/ 2>/dev/null | wc -l)
CLIENT_IP="10.0.0.$((CLIENT_NUMBER + 2))"

# Crear directorio de clientes
sudo mkdir -p /etc/wireguard/clients

# Generar claves del cliente
cd /etc/wireguard/clients
umask 077
wg genkey | sudo tee ${CLIENT_NAME}_private.key | wg pubkey | sudo tee ${CLIENT_NAME}_public.key

CLIENT_PRIVATE_KEY=$(sudo cat ${CLIENT_NAME}_private.key)
CLIENT_PUBLIC_KEY=$(sudo cat ${CLIENT_NAME}_public.key)

# Crear archivo de configuración del cliente
cat > ${CLIENT_NAME}.conf <<EOF
[Interface]
PrivateKey = ${CLIENT_PRIVATE_KEY}
Address = ${CLIENT_IP}/24
DNS = 192.168.1.10

[Peer]
PublicKey = ${SERVER_PUBLIC_KEY}
Endpoint = ${SERVER_ENDPOINT}
AllowedIPs = 192.168.1.0/24, 10.0.0.0/24
PersistentKeepalive = 25
EOF

echo ""
echo "✅ Configuración generada para: ${CLIENT_NAME}"
echo "📁 Archivo: /etc/wireguard/clients/${CLIENT_NAME}.conf"
echo "🔑 IP asignada: ${CLIENT_IP}"
echo ""
echo "Añade este peer al servidor:"
echo ""
echo "[Peer]"
echo "PublicKey = ${CLIENT_PUBLIC_KEY}"
echo "AllowedIPs = ${CLIENT_IP}/32"
echo ""

# Generar código QR para móviles
echo "📱 Código QR para dispositivos móviles:"
qrencode -t ansiutf8 < ${CLIENT_NAME}.conf
```

Haz el script ejecutable:

```bash
sudo chmod +x /etc/wireguard/add-client.sh
```

### 4.5 Obtener tu IP Pública

Antes de generar clientes, necesitas tu IP pública:

```bash
88.27.113.238
curl ifconfig.me
```

O usa un servicio de DNS dinámico (DuckDNS, No-IP, etc.) si tu IP cambia.

Edita el script y reemplaza `TU_IP_PUBLICA`:

```bash
sudo nano /etc/wireguard/add-client.sh
# Busca la línea SERVER_ENDPOINT y reemplaza TU_IP_PUBLICA
```

### 4.6 Crear tu Primer Cliente

```bash
# Generar configuración para un cliente (ejemplo: tu móvil)
sudo /etc/wireguard/add-client.sh movil-personal
```

El script te mostrará:
1. La configuración del peer que debes añadir al servidor
2. Un código QR para escanear con tu móvil

### 4.7 Añadir el Peer al Servidor

Copia la sección `[Peer]` que mostró el script y añádela al servidor:

```bash
sudo nano /etc/wireguard/wg0.conf
```

Añade al final:

```ini
[Peer]
# Móvil Personal
PublicKey = CLAVE_PUBLICA_DEL_CLIENTE
AllowedIPs = 10.0.0.2/32
```

### 4.8 Iniciar WireGuard

```bash
# Habilitar WireGuard para que inicie con el sistema
sudo systemctl enable wg-quick@wg0

# Iniciar WireGuard
sudo systemctl start wg-quick@wg0

# Verificar estado
sudo systemctl status wg-quick@wg0

# Ver información de WireGuard
sudo wg show
```

Public key WJviQuDLuP1rDg5ZYRjn01hxUBMMX7vb5paTRVgGozI=
### 4.9 Abrir Puerto en el Router

**⚠️ IMPORTANTE**: Debes hacer port forwarding en tu router:

1. Accede al panel de tu router (192.168.1.1)
2. Busca "Port Forwarding" o "NAT"
3. Crea una regla:
   - **Puerto externo**: 51820
   - **Puerto interno**: 51820
   - **Protocolo**: UDP
   - **IP destino**: 192.168.1.10 (tu Raspberry Pi)
4. Guarda la configuración

### 4.10 Configurar Cliente en Móvil

**Android/iOS:**

1. Instala la app "WireGuard" desde Play Store o App Store
2. Toca el botón "+"
3. Selecciona "Crear desde código QR"
4. Escanea el código QR que generó el script
5. Activa la conexión

**Windows/Linux/Mac:**

1. Copia el archivo `.conf` al dispositivo
2. Instala WireGuard: https://www.wireguard.com/install/
3. Importa el archivo de configuración
4. Activa la conexión

---

## Fase 5: Configuración de Enrutamiento

Ahora configuraremos las reglas de firewall para que todo funcione correctamente.

### 5.1 Reglas de iptables

```bash
# Crear script de firewall
sudo nano /etc/firewall-rules.sh
```

Pega estas reglas:

```bash
#!/bin/bash

# Limpiar reglas existentes
iptables -F
iptables -X
iptables -t nat -F
iptables -t nat -X

# Políticas por defecto
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT

# Permitir tráfico de loopback
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Permitir conexiones establecidas
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Permitir SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Permitir Pi-hole (DNS y Web)
iptables -A INPUT -p tcp --dport 53 -j ACCEPT
iptables -A INPUT -p udp --dport 53 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Permitir WireGuard
iptables -A INPUT -p udp --dport 51820 -j ACCEPT

# Permitir Tailscale
iptables -A INPUT -p udp --dport 41641 -j ACCEPT

# NAT para WireGuard
iptables -t nat -A POSTROUTING -s 10.0.0.0/24 -o eth0 -j MASQUERADE

# Permitir forwarding entre interfaces
iptables -A FORWARD -i wg0 -o eth0 -j ACCEPT
iptables -A FORWARD -i eth0 -o wg0 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Permitir forwarding para Tailscale
iptables -A FORWARD -i tailscale0 -j ACCEPT
iptables -A FORWARD -o tailscale0 -j ACCEPT

# Permitir tráfico entre WireGuard y LAN
iptables -A FORWARD -i wg0 -d 192.168.1.0/24 -j ACCEPT
iptables -A FORWARD -s 192.168.1.0/24 -o wg0 -j ACCEPT

# Logging (opcional, para debug)
# iptables -A INPUT -j LOG --log-prefix "INPUT DROP: "
# iptables -A FORWARD -j LOG --log-prefix "FORWARD DROP: "

echo "✅ Reglas de firewall aplicadas"
```

Haz el script ejecutable:

```bash
sudo chmod +x /etc/firewall-rules.sh
```

### 5.2 Aplicar Reglas al Inicio

```bash
# Ejecutar el script
sudo /etc/firewall-rules.sh

# Guardar las reglas para que persistan
sudo netfilter-persistent save

# Crear servicio systemd para aplicar reglas al inicio
sudo nano /etc/systemd/system/firewall-rules.service
```

Pega:

```ini
[Unit]
Description=Apply custom firewall rules
Before=network-pre.target
Wants=network-pre.target

[Service]
Type=oneshot
ExecStart=/etc/firewall-rules.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Habilitar el servicio:

```bash
sudo systemctl daemon-reload
sudo systemctl enable firewall-rules.service
sudo systemctl start firewall-rules.service
```

### 5.3 Configurar DNS Conditional Forwarding

Esto permite que Pi-hole resuelva nombres de dispositivos en tu red local:

1. Accede al panel de Pi-hole: `http://192.168.1.10/admin`
2. Ve a **Settings** → **DNS** → **Advanced DNS settings**
3. En **Conditional Forwarding**:
   - ✅ Habilita conditional forwarding
   - **Local network**: 192.168.1.0/24
   - **Router IP**: 192.168.1.1
   - **Local domain name**: home.local (o el que uses)

### 5.4 Configurar Split DNS para Tailscale

```bash
# Editar configuración de Tailscale
sudo nano /etc/default/tailscaled
```

Añade:

```
TS_ACCEPT_DNS=false
```

Reinicia Tailscale:

```bash
sudo systemctl restart tailscaled
```

---

## Configuración de Clientes

### Cliente WireGuard - Windows

1. Descarga WireGuard: https://www.wireguard.com/install/
2. Instala la aplicación
3. Haz clic en "Añadir túnel" → "Añadir túnel vacío"
4. Pega la configuración del cliente
5. Guarda con un nombre descriptivo
6. Activa el túnel

**Verificación:**

```cmd
# En PowerShell
ping 192.168.1.10
ping 10.0.0.1
```

### Cliente WireGuard - Android/iOS

1. Instala WireGuard desde la tienda de apps
2. Toca "+" → "Crear desde código QR"
3. Escanea el código QR generado
4. Activa el túnel

**Verificación:**
- Abre un navegador y visita: http://192.168.1.10/admin
- Deberías ver el panel de Pi-hole

### Cliente Tailscale - Todos los Dispositivos

**Windows/Mac/Linux:**

1. Descarga desde: https://tailscale.com/download
2. Instala y ejecuta
3. Inicia sesión con tu cuenta
4. El dispositivo aparecerá en tu panel de Tailscale

**Android/iOS:**

1. Descarga la app "Tailscale"
2. Inicia sesión
3. Activa la conexión

**Acceder a tu red local desde Tailscale:**

Una vez conectado a Tailscale, puedes acceder a cualquier dispositivo en tu red local:

```bash
# Ejemplo: acceder a Pi-hole desde cualquier lugar
http://192.168.1.10/admin

# O usar ping
ping 192.168.1.1
```

---

## Verificación y Pruebas

### Verificar Pi-hole

```bash
# Ver estadísticas
pihole -c

# Probar consulta DNS
dig @192.168.1.10 google.com

# Verificar que bloquea anuncios
dig @192.168.1.10 ads.google.com
# Debe responder con 0.0.0.0
```

### Verificar WireGuard

```bash
# Ver estado de WireGuard
sudo wg show

# Ver logs
sudo journalctl -u wg-quick@wg0 -f

# Verificar interfaz
ip addr show wg0
```

**Salida esperada de `sudo wg show`:**

```
interface: wg0
  public key: (clave pública del servidor)
  private key: (hidden)
  listening port: 51820

peer: (clave pública del cliente)
  endpoint: XX.XX.XX.XX:XXXXX
  allowed ips: 10.0.0.2/32
  latest handshake: 1 minute, 23 seconds ago
  transfer: 15.23 KiB received, 48.71 KiB sent
```

### Verificar Tailscale

```bash
# Ver estado
sudo tailscale status

# Ver rutas anunciadas
sudo tailscale status --json | grep AdvertisedRoutes

# Probar conectividad
sudo tailscale ping nombre-otro-dispositivo
```

### Verificar Enrutamiento

```bash
# Ver tabla de enrutamiento
ip route show

# Ver reglas de iptables
sudo iptables -L -v -n
sudo iptables -t nat -L -v -n

# Verificar forwarding
cat /proc/sys/net/ipv4/ip_forward
# Debe mostrar: 1
```

### Test de Conectividad Completo

**Desde un cliente WireGuard:**

```bash
# Ping al servidor WireGuard
ping 10.0.0.1

# Ping a un dispositivo en la LAN
ping 192.168.1.1

# Consulta DNS a Pi-hole
nslookup google.com 192.168.1.10

# Traceroute
traceroute 192.168.1.1
```

**Desde un cliente Tailscale:**

```bash
# Ping a la Raspberry Pi
ping 192.168.1.10

# Ping a otros dispositivos de la LAN
ping 192.168.1.1

# Verificar que puedes acceder a Pi-hole
curl http://192.168.1.10/admin
```

---

## Solución de Problemas

### Pi-hole no bloquea anuncios

**Problema:** Los anuncios siguen apareciendo

**Soluciones:**

```bash
# Verificar que Pi-hole está ejecutándose
pihole status

# Actualizar listas de bloqueo
pihole -g

# Verificar que el dispositivo usa Pi-hole como DNS
nslookup google.com
# Debe mostrar "Server: 192.168.1.10"

# Limpiar caché de Pi-hole
pihole restartdns reload-lists

# Ver logs en tiempo real
pihole -t
```

### WireGuard no conecta

**Problema:** El cliente no puede conectarse

**Soluciones:**

```bash
# Verificar que WireGuard está ejecutándose
sudo systemctl status wg-quick@wg0

# Ver logs
sudo journalctl -u wg-quick@wg0 -n 50

# Verificar que el puerto está abierto
sudo ss -tulpn | grep 51820

# Reiniciar WireGuard
sudo systemctl restart wg-quick@wg0

# Verificar configuración
sudo wg show wg0

# Probar desde el cliente con verbose
wg-quick up cliente1 # En el cliente
```

**Verificar port forwarding:**

Usa una herramienta online como: https://www.yougetsignal.com/tools/open-ports/

Ingresa tu IP pública y puerto 51820 (UDP)

### Tailscale no puede acceder a la LAN

**Problema:** Conectado a Tailscale pero no puedo acceder a 192.168.1.x

**Soluciones:**

1. Verifica que las subnet routes están habilitadas en el panel de Tailscale
2. Comprueba que están anunciadas:

```bash
sudo tailscale status --json | grep AdvertisedRoutes
```

3. Reinicia Tailscale:

```bash
sudo systemctl restart tailscaled
sudo tailscale up --advertise-routes=192.168.1.0/24
```

4. Verifica reglas de iptables:

```bash
sudo iptables -L FORWARD -v -n
# Debe haber reglas que permitan tráfico desde tailscale0
```

### No hay conectividad entre redes

**Problema:** No puedo hacer ping entre WireGuard y LAN

**Soluciones:**

```bash
# Verificar IP forwarding
cat /proc/sys/net/ipv4/ip_forward
# Debe ser 1

# Verificar reglas de NAT
sudo iptables -t nat -L -v -n

# Verificar reglas de FORWARD
sudo iptables -L FORWARD -v -n

# Recargar reglas
sudo /etc/firewall-rules.sh
sudo netfilter-persistent reload

# Ver tabla de enrutamiento
ip route show table all
```

### Rendimiento lento

**Problema:** Las conexiones son lentas

**Soluciones:**

```bash
# Monitorear uso de CPU y memoria
htop

# Ver estadísticas de red
sudo iftop

# Ajustar MTU en WireGuard
sudo nano /etc/wireguard/wg0.conf
# Cambiar MTU = 1420 a MTU = 1380

# Reiniciar WireGuard
sudo systemctl restart wg-quick@wg0

# Verificar temperatura de la Raspberry Pi
vcgencmd measure_temp

# Si está caliente, considerar refrigeración adicional
```

### DNS no resuelve correctamente

**Problema:** Los nombres de dominio no se resuelven

**Soluciones:**

```bash
# Verificar que Pi-hole está corriendo
pihole status

# Probar DNS manualmente
dig @192.168.1.10 google.com
nslookup google.com 192.168.1.10

# Verificar configuración del cliente
# En el cliente, ver qué DNS está usando:

# Linux/Mac:
cat /etc/resolv.conf

# Windows:
ipconfig /all

# Reiniciar servicio DNS de Pi-hole
pihole restartdns

# Ver logs de Pi-hole
tail -f /var/log/pihole.log
```

---

## Mantenimiento

### Actualizaciones Regulares

Crea un script de mantenimiento semanal:

```bash
sudo nano /usr/local/bin/maintenance.sh
```

```bash
#!/bin/bash

echo "=== Iniciando mantenimiento ==="
date

# Actualizar sistema
echo "Actualizando sistema..."
sudo apt update && sudo apt upgrade -y

# Actualizar Pi-hole
echo "Actualizando Pi-hole..."
pihole -up

# Actualizar listas de bloqueo
echo "Actualizando listas de bloqueo..."
pihole -g

# Limpiar logs antiguos
echo "Limpiando logs antiguos..."
sudo journalctl --vacuum-time=30d

# Limpiar paquetes
echo "Limpiando paquetes..."
sudo apt autoremove -y
sudo apt autoclean

# Verificar servicios
echo "Verificando servicios..."
sudo systemctl status pihole-FTL --no-pager
sudo systemctl status wg-quick@wg0 --no-pager
sudo systemctl status tailscaled --no-pager

# Reiniciar servicios si es necesario
# sudo systemctl restart pihole-FTL
# sudo systemctl restart wg-quick@wg0
# sudo systemctl restart tailscaled

echo "=== Mantenimiento completado ==="
date
```

Haz el script ejecutable:

```bash
sudo chmod +x /usr/local/bin/maintenance.sh
```

Programa ejecución semanal con cron:

```bash
sudo crontab -e
```

Añade:

```
# Mantenimiento cada domingo a las 3 AM
0 3 * * 0 /usr/local/bin/maintenance.sh >> /var/log/maintenance.log 2>&1
```

### Backups

Crea backups de las configuraciones importantes:

```bash
sudo nano /usr/local/bin/backup-config.sh
```

```bash
#!/bin/bash

BACKUP_DIR="/home/pi/backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/config_backup_$DATE.tar.gz"

# Crear directorio de backups
mkdir -p $BACKUP_DIR

# Hacer backup
sudo tar -czf $BACKUP_FILE \
    /etc/wireguard/ \
    /etc/pihole/ \
    /etc/dnsmasq.d/ \
    /etc/sysctl.conf \
    /etc/dhcpcd.conf \
    /etc/firewall-rules.sh \
    /var/lib/tailscale/

echo "Backup creado: $BACKUP_FILE"

# Mantener solo los últimos 7 backups
ls -t $BACKUP_DIR/config_backup_*.tar.gz | tail -n +8 | xargs -r rm

echo "Backups antiguos eliminados"
```

Haz el script ejecutable:

```bash
sudo chmod +x /usr/local/bin/backup-config.sh
```

Ejecutar backup semanal:

```bash
sudo crontab -e
```

Añade:

```
# Backup cada domingo a las 2 AM
0 2 * * 0 /usr/local/bin/backup-config.sh
```

### Monitoreo

**Instalar Netdata (opcional):**

```bash
bash <(curl -Ss https://my-netdata.io/kickstart.sh)
```

Accede a: `http://192.168.1.10:19999`

**Scripts de monitoreo básico:**

```bash
sudo nano /usr/local/bin/status-check.sh
```

```bash
#!/bin/bash

echo "=== Estado del Sistema ==="
date
echo ""

echo "--- CPU y Memoria ---"
top -bn1 | head -5
echo ""

echo "--- Temperatura ---"
vcgencmd measure_temp
echo ""

echo "--- Espacio en Disco ---"
df -h | grep -v tmpfs
echo ""

echo "--- Servicios ---"
systemctl is-active pihole-FTL && echo "✅ Pi-hole: OK" || echo "❌ Pi-hole: ERROR"
systemctl is-active wg-quick@wg0 && echo "✅ WireGuard: OK" || echo "❌ WireGuard: ERROR"
systemctl is-active tailscaled && echo "✅ Tailscale: OK" || echo "❌ Tailscale: ERROR"
echo ""

echo "--- WireGuard ---"
sudo wg show wg0 | head -10
echo ""

echo "--- Pi-hole Stats ---"
pihole -c -e
```

Haz ejecutable:

```bash
sudo chmod +x /usr/local/bin/status-check.sh
```

Ejecútalo cuando quieras ver el estado:

```bash
sudo /usr/local/bin/status-check.sh
```

### Rotación de Claves (Recomendado cada 6-12 meses)

**Para WireGuard:**

```bash
# Generar nuevas claves del servidor
cd /etc/wireguard
sudo wg genkey | sudo tee server_private_new.key | wg pubkey | sudo tee server_public_new.key

# Backup de configuración actual
sudo cp wg0.conf wg0.conf.backup

# Actualizar configuración con nueva clave
sudo nano wg0.conf
# Reemplaza PrivateKey con el contenido de server_private_new.key

# Reiniciar WireGuard
sudo systemctl restart wg-quick@wg0

# Actualizar clientes con la nueva clave pública
# (Regenerar configuraciones de clientes con el script add-client.sh)
```

---

## Anexos

### Anexo A: Comandos Útiles

```bash
# Pi-hole
pihole status                    # Estado de Pi-hole
pihole -g                        # Actualizar listas de bloqueo
pihole -up                       # Actualizar Pi-hole
pihole -t                        # Tail logs en tiempo real
pihole -c                        # Cronómetro de consultas
pihole restartdns                # Reiniciar DNS
pihole arpflush                  # Limpiar tabla ARP
pihole -q dominio.com            # Consultar si un dominio está bloqueado
pihole -w dominio.com            # Añadir a whitelist
pihole -b dominio.com            # Añadir a blacklist

# WireGuard
sudo wg show                     # Mostrar información de WireGuard
sudo wg show wg0                 # Info de interfaz específica
sudo wg showconf wg0             # Mostrar configuración
sudo systemctl restart wg-quick@wg0    # Reiniciar WireGuard
sudo wg set wg0 peer PUBLICKEY remove  # Eliminar peer

# Tailscale
sudo tailscale status            # Estado de Tailscale
sudo tailscale ip                # Ver IPs asignadas
sudo tailscale ping hostname     # Ping a otro dispositivo
sudo tailscale netcheck          # Verificar conectividad
sudo tailscale bugreport         # Generar reporte de bug
sudo tailscale logout            # Cerrar sesión
sudo tailscale down              # Desconectar
sudo tailscale up                # Conectar

# Red
ip addr show                     # Ver interfaces de red
ip route show                    # Ver tabla de enrutamiento
sudo iptables -L -v -n           # Ver reglas de firewall
sudo iptables -t nat -L -v -n    # Ver reglas de NAT
ss -tulpn                        # Ver puertos abiertos
netstat -rn                      # Ver tabla de enrutamiento
tcpdump -i wg0                   # Capturar tráfico en WireGuard

# Sistema
sudo systemctl status servicio   # Estado de un servicio
sudo journalctl -u servicio -f   # Logs de un servicio
htop                             # Monitor de procesos
vcgencmd measure_temp            # Temperatura de la Pi
df -h                            # Espacio en disco
free -h                          # Memoria RAM
```

### Anexo B: Estructura de Archivos

```
/etc/
├── wireguard/
│   ├── wg0.conf                    # Configuración del servidor WireGuard
│   ├── server_private.key          # Clave privada del servidor
│   ├── server_public.key           # Clave pública del servidor
│   └── clients/                    # Configuraciones de clientes
│       ├── movil-personal.conf
│       ├── movil-personal_private.key
│       └── movil-personal_public.key
├── pihole/
│   ├── pihole-FTL.conf            # Configuración de Pi-hole
│   ├── adlists.list               # Listas de bloqueo
│   ├── whitelist.txt              # Dominios permitidos
│   └── blacklist.txt              # Dominios bloqueados
├── firewall-rules.sh              # Script de reglas de firewall
├── sysctl.conf                    # Configuración del kernel
└── dhcpcd.conf                    # Configuración de red

/usr/local/bin/
├── maintenance.sh                 # Script de mantenimiento
├── backup-config.sh               # Script de backup
└── status-check.sh                # Script de verificación de estado

/var/log/
├── pihole.log                     # Logs de Pi-hole
├── maintenance.log                # Logs de mantenimiento
└── syslog                         # Logs del sistema

/home/pi/
└── backups/                       # Directorio de backups
    └── config_backup_*.tar.gz
```

### Anexo C: Puertos y Protocolos

| Servicio | Puerto | Protocolo | Propósito |
|----------|--------|-----------|-----------|
| SSH | 22 | TCP | Acceso remoto |
| DNS | 53 | TCP/UDP | Resolución de nombres |
| HTTP | 80 | TCP | Panel web de Pi-hole |
| HTTPS | 443 | TCP | Panel web seguro |
| WireGuard | 51820 | UDP | VPN |
| Tailscale | 41641 | UDP | VPN mesh |
| Netdata | 19999 | TCP | Monitoreo (opcional) |

### Anexo D: Recursos y Referencias

**Documentación Oficial:**
- Pi-hole: https://docs.pi-hole.net/
- WireGuard: https://www.wireguard.com/quickstart/
- Tailscale: https://tailscale.com/kb/
- Raspberry Pi: https://www.raspberrypi.com/documentation/

**Comunidades:**
- Reddit r/pihole: https://reddit.com/r/pihole
- Reddit r/WireGuard: https://reddit.com/r/WireGuard
- Tailscale Community: https://tailscale.com/community/

**Herramientas Útiles:**
- Test de DNS: https://www.dnsleaktest.com/
- Test de puerto abierto: https://www.yougetsignal.com/tools/open-ports/
- Generador de configuraciones WireGuard: https://www.wireguardconfig.com/

### Anexo E: Seguridad Adicional

**Fail2Ban para SSH:**

```bash
# Instalar Fail2Ban
sudo apt install -y fail2ban

# Crear configuración personalizada
sudo nano /etc/fail2ban/jail.local
```

```ini
[sshd]
enabled = true
port = 22
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
bantime = 3600
findtime = 600
```

```bash
# Iniciar Fail2Ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban

# Ver estado
sudo fail2ban-client status sshd
```

**Cambiar puerto SSH (opcional):**

```bash
sudo nano /etc/ssh/sshd_config
# Cambia: Port 22
# Por: Port 2222

sudo systemctl restart ssh
```

**Deshabilitar login root por SSH:**

```bash
sudo nano /etc/ssh/sshd_config
# Cambia: PermitRootLogin yes
# Por: PermitRootLogin no

sudo systemctl restart ssh
```

---

## Conclusión

¡Felicidades! Has configurado exitosamente una Raspberry Pi como gateway completo con:

✅ **Tailscale** - Acceso remoto seguro desde cualquier lugar
✅ **Pi-hole** - Bloqueo de anuncios en toda tu red
✅ **WireGuard** - VPN rápida y moderna para dispositivos móviles
✅ **Enrutamiento completo** - Conectividad entre todas las redes

### Próximos Pasos Recomendados:

1. Configurar más clientes WireGuard para todos tus dispositivos
2. Personalizar las listas de bloqueo de Pi-hole
3. Configurar backups automáticos en la nube
4. Instalar Netdata para monitoreo en tiempo real
5. Explorar funciones avanzadas de Tailscale (MagicDNS, etc.)

### Recuerda:

- Mantén tu sistema actualizado regularmente
- Haz backups de tus configuraciones
- Monitorea el rendimiento y logs
- Cambia las contraseñas periódicamente
- Mantén el firmware de tu router actualizado

---

**Fecha de creación:** $(date +%Y-%m-%d)
**Versión:** 1.0
**Sistema:** Raspberry Pi 5 con Raspberry Pi OS
**Red:** 192.168.1.0/24

---

## Notas Personales

<!-- Añade aquí tus notas personales, IPs específicas, contraseñas (¡en un gestor seguro!), etc. -->

