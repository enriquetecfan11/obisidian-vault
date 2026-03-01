---
type: "resource"
tags: ["#proyecto-SaaS", "#area-devops", "#status-pendiente", "#topic-ia", "#topic-db"] # Siempre array con 2-5 tags específicos
project: "none"
status: "pendiente"
date_created: "2026-03-01"
date_modified: "2026-03-01"
related: [] # Array vacío o con [[links]]
---

# CAI Framework - Guía de Instalación y Configuración

## 📦 Instalación Inicial

```bash
# Actualizar sistema e instalar dependencias
sudo apt-get update && \
    sudo apt-get install -y git python3-pip python3.12-venv

# Crear entorno virtual
python3.12 -m venv cai_env

# Activar entorno e instalar CAI
source cai_env/bin/activate && pip install cai-framework
```

## ⚙️ Configuración del Archivo `.env`

### Configuración Básica (Inicial)

```bash
OPENAI_API_KEY="sk-1234"
ANTHROPIC_API_KEY=""
OLLAMA=""
PROMPT_TOOLKIT_NO_CPR=1
CAI_STREAM=false
```

### Configuración para Ollama (Recomendada)

```bash
OPENAI_API_KEY="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"
ANTHROPIC_API_KEY=""
OLLAMA="http://192.168.1.104:11434"
CAI_MODEL=ollama/qwen3:latest
CAI_LLM_PROVIDER=ollama
PROMPT_TOOLKIT_NO_CPR=1
CAI_STREAM=false
```

> **Nota:** Ajusta `OLLAMA` a la IP de tu servidor Ollama y `CAI_MODEL` al modelo que desees usar.

## 🚀 Iniciar CAI

### Paso 1: Activar el Entorno Virtual

```bash
source cai_env/bin/activate
```

### Paso 2: Lanzar CAI con Ollama

```bash
OLLAMA_API_BASE="http://127.0.0.1:11434/v1" cai
```

> ⏱️ **Importante:** El primer lanzamiento puede tardar hasta 30 segundos.

## 🤖 Modelos Optimizados para Ollama

- **Qwen2.5 72B**
- **Qwen2.5 14B**
- **Qwen3:latest** (configurado por defecto)

## 🔍 Prompt para Auditoría Web

### Caso de Uso: Auditoría de Seguridad y Análisis Técnico

```
You are running on Kali Linux with full privileges and access to all tools (nmap, curl, whatweb, whois, dig, wget, etc.) and external APIs (ipinfo.io, ipapi.com, etc.).

Your task is to audit the website: https://nundusoft.com/

If accessible, extract all useful information: technologies, headers, structure, endpoints.
If unreachable, resolve its IP and analyze it: geolocation, ASN, hosting provider, open ports.

Do not explain your actions. Just execute. Output only the findings. End with a concise summary of the key results.

If you have problems with any tool, ignore it and use another one.
```

### Personalización del Prompt

Para auditar otro sitio web, simplemente cambia la URL:

```
Your task is to audit the website: https://tu-sitio-web.com/
```

## 📝 Notas Adicionales

- **Permisos:** CAI requiere acceso a herramientas del sistema (nmap, curl, etc.)
- **Networking:** Asegúrate de que el servidor Ollama esté accesible desde la IP configurada
- **Primera ejecución:** El sistema puede tardar en cargar el modelo la primera vez
- **Modelos:** Puedes cambiar el modelo editando `CAI_MODEL` en el archivo `.env`

## 🛠️ Troubleshooting

### Error al conectar con Ollama

Verifica que el servidor Ollama esté corriendo:

```bash
curl http://192.168.1.104:11434/api/tags
```

### CAI no encuentra el modelo

Lista los modelos disponibles:

```bash
ollama list
```

E instala el modelo si es necesario:

```bash
ollama pull qwen3:latest
```

---

**Última actualización:** Febrero 2026  