---
type: "resource"
tags: ["#proyecto-SaaS", "#area-devops", "#status-pendiente", "#topic-devops", "#topic-n8n"] # Siempre array con 2-5 tags específicos
project: "N8N Automation"
status: "pendiente"
date_created: "2026-03-01"
date_modified: "2026-03-01"
related: [] # Array vacío o con [[links]]
---

# 🐋 Ollama - Configuración para Docker y Redes

## 🔌 Exponer Ollama en Contenedores Docker

### Paso 1: Iniciar Ollama en Todas las Interfaces

```bash
OLLAMA_HOST=0.0.0.0 ollama serve
```

> ⚠️ **Nota:** Esto permite que Ollama sea accesible desde contenedores Docker y otras máquinas en la red.

---

### Paso 2: Obtener la IP del Bridge de Docker

```bash
ip -4 addr show docker0 | grep -Po 'inet \K[\d.]+'
```

**Salida esperada:**

```
172.17.0.1
```

---

### Paso 3: Configurar N8N con la IP de Docker Bridge

Usa la IP obtenida seguida del puerto **11434**:

```
http://172.17.0.1:11434
```

> 💡 **Tip:** Esta es la forma más común de conectar contenedores Docker con servicios del host.

---

### Paso 4: Ollama Dentro de un Contenedor Docker

Si Ollama también está corriendo dentro de Docker, usa el nombre del servicio:

```
http://ollama:11434
```

> 📦 **Requisito:** Los contenedores deben estar en la misma red Docker.

---

### Paso 5: Usar Ollama con CAI

```bash
OLLAMA_API_BASE="http://127.0.0.1:11434/v1" cai
```

---

## 🌐 Exponer Ollama en Toda la Red Local

### Configuración Permanente con Systemd

#### 1️⃣ Detener el Servicio

```bash
sudo systemctl stop ollama
```

#### 2️⃣ Verificar el Estado

```bash
sudo systemctl status ollama
```

**Salida esperada:**

```
● ollama.service - Ollama Service
   Loaded: loaded (/etc/systemd/system/ollama.service; enabled)
   Active: inactive (dead)
```

#### 3️⃣ Editar el Archivo de Servicio

```bash
sudo nano /etc/systemd/system/ollama.service
```

#### 4️⃣ Agregar la Variable de Entorno

Añade esta línea en la sección `[Service]`:

```ini
[Service]
Environment="OLLAMA_HOST=0.0.0.0:11434"
```

**Ejemplo completo:**

```ini
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/local/bin/ollama serve
Environment="OLLAMA_HOST=0.0.0.0:11434"
User=ollama
Group=ollama
Restart=always
RestartSec=3

[Install]
WantedBy=default.target
```

#### 5️⃣ Recargar y Reiniciar el Servicio

```bash
# Recargar la configuración de systemd
sudo systemctl daemon-reload

# Reiniciar Ollama
sudo systemctl restart ollama
```

#### 6️⃣ Verificar el Estado

```bash
sudo systemctl status ollama
```

**Salida esperada:**

```
● ollama.service - Ollama Service
   Loaded: loaded (/etc/systemd/system/ollama.service; enabled)
   Active: active (running)
```

---

## 🧪 Verificar la Conexión

### Desde el Host

```bash
curl http://localhost:11434/api/tags
```

### Desde Otro Dispositivo en la Red

```bash
curl http://192.168.1.104:11434/api/tags
```

> 🔄 **Cambia** `192.168.1.104` por la IP de tu servidor Ollama.

### Desde un Contenedor Docker

```bash
docker run --rm curlimages/curl:latest http://172.17.0.1:11434/api/tags
```

---

## 📊 Tabla de Direcciones según el Contexto

|Contexto|Dirección|Puerto|
|---|---|---|
|**Local (mismo host)**|`http://127.0.0.1`|`11434`|
|**Contenedor Docker → Host**|`http://172.17.0.1`|`11434`|
|**Contenedor → Contenedor**|`http://ollama`|`11434`|
|**Otra máquina en red**|`http://192.168.1.104`|`11434`|
|**CAI (local)**|`http://127.0.0.1`|`11434/v1`|

---

## 🔒 Consideraciones de Seguridad

> ⚠️ **Advertencia:** Exponer Ollama en `0.0.0.0` permite el acceso desde cualquier dispositivo en la red.

### Recomendaciones

1. **Firewall:** Configura reglas para limitar el acceso
2. **Red privada:** Usa solo en redes confiables
3. **Reverse proxy:** Considera usar Nginx con autenticación
4. **VPN:** Para acceso remoto seguro

---

## 🛠️ Troubleshooting

### Error: "Connection refused"

```bash
# Verificar que Ollama está escuchando
sudo netstat -tlnp | grep 11434

# Verificar logs
sudo journalctl -u ollama -f
```

### Error: "No route to host"

```bash
# Verificar firewall
sudo ufw status

# Permitir puerto 11434
sudo ufw allow 11434/tcp
```

### Docker no puede conectar

```bash
# Verificar la red bridge
docker network inspect bridge

# Probar conectividad
docker run --rm alpine ping -c 4 172.17.0.1
```

---

**Última actualización:** Febrero 2026  