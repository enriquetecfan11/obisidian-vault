---
type: "resource"
tags: ["#proyecto-SaaS", "#area-devops", "#status-pendiente", "#topic-n8n", "#topic-ia"] # Siempre array con 2-5 tags específicos
project: "N8N Automation"
status: "pendiente"
date_created: "2026-03-01"
date_modified: "2026-03-01"
related: [] # Array vacío o con [[links]]
---

## 🔗 Endpoint Base

```
https://www.builderbot.cloud/api/v2/aXMuiiBizI30Kl-Hwi_k2/messages
```

---
## 🔐 Autenticación

### Headers Requeridos

```http
Content-Type: application/json
x-api-builderbot: TU_API_KEY
```

**API Key actual:**

```
bb-ygmc9zTq68gvx0e7A6XPLM6U426rbr-dCtl
```

---
## 📤 Enviar Mensajes

### Método HTTP

```
POST
```

### Estructura del Body

#### Mensaje de Texto Simple

```json
{
    "messages": {
        "content": "Hola, este es un mensaje de prueba"
    },
    "number": "34727788459"
}
```

#### Mensaje con Multimedia

```json
{
    "messages": {
        "content": "Mira esta imagen",
        "mediaUrl": "https://ejemplo.com/imagen.jpg"
    },
    "number": "34727788459"
}
```

---

## 💻 Ejemplos de Implementación

### cURL - Mensaje de Texto

```bash
curl --location 'https://www.builderbot.cloud/api/v2/aXMuiiBizI30Kl-Hwi_k2/messages' \
--header 'Content-Type: application/json' \
--header 'x-api-builderbot: bb-ygmc9zTq68gvx0e7A6XPLM6U426rbr-dCtl' \
--data '{
    "messages": {
        "content": "Hola, este es un mensaje de prueba"
    },
    "number": "34727788459"
}'
```

### cURL - Mensaje con Imagen

```bash
curl --location 'https://www.builderbot.cloud/api/v2/aXMuiiBizI30Kl-Hwi_k2/messages' \
--header 'Content-Type: application/json' \
--header 'x-api-builderbot: bb-ygmc9zTq68gvx0e7A6XPLM6U426rbr-dCtl' \
--data '{
    "messages": {
        "content": "Mira esta imagen",
        "mediaUrl": "https://ejemplo.com/imagen.jpg"
    },
    "number": "34727788459"
}'
```

---

## 🔄 Respuesta de la API

### Respuesta Exitosa

```json
{
    "number": "34727788459",
    "message": "Hola, este es un mensaje de prueba",
    "waited": true
}
```

### Campos de la Respuesta

|Campo|Tipo|Descripción|
|---|---|---|
|`number`|String|Número de teléfono destinatario|
|`message`|String|Contenido del mensaje enviado|
|`waited`|Boolean|Indica si el mensaje fue procesado|

---

## 🔧 Integración con N8N

### Configuración del Nodo HTTP Request

#### 1️⃣ Configuración Básica

```
Method: POST
URL: https://www.builderbot.cloud/api/v2/aXMuiiBizI30Kl-Hwi_k2/messages
Authentication: None (usar Headers)
```

#### 2️⃣ Headers

|Header|Value|
|---|---|
|`Content-Type`|`application/json`|
|`x-api-builderbot`|`bb-ygmc9zTq68gvx0e7A6XPLM6U426rbr-dCtl`|

#### 3️⃣ Body (JSON)

**Mensaje Simple:**

```json
{
    "messages": {
        "content": "{{ $json.mensaje }}"
    },
    "number": "{{ $json.telefono }}"
}
```

**Mensaje con Multimedia:**

```json
{
    "messages": {
        "content": "{{ $json.mensaje }}",
        "mediaUrl": "{{ $json.urlImagen }}"
    },
    "number": "{{ $json.telefono }}"
}
```

---

## 📋 Workflow N8N Completo

### Ejemplo: Enviar Mensaje desde Webhook

```json
{
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "enviar-mensaje",
        "responseMode": "responseNode",
        "options": {}
      },
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "position": [250, 300]
    },
    {
      "parameters": {
        "url": "https://www.builderbot.cloud/api/v2/aXMuiiBizI30Kl-Hwi_k2/messages",
        "sendHeaders": true,
        "headerParameters": {
          "parameters": [
            {
              "name": "Content-Type",
              "value": "application/json"
            },
            {
              "name": "x-api-builderbot",
              "value": "bb-ygmc9zTq68gvx0e7A6XPLM6U426rbr-dCtl"
            }
          ]
        },
        "sendBody": true,
        "bodyParameters": {
          "parameters": [
            {
              "name": "messages",
              "value": "={{ { content: $json.body.mensaje } }}"
            },
            {
              "name": "number",
              "value": "={{ $json.body.telefono }}"
            }
          ]
        },
        "options": {}
      },
      "name": "HTTP Request - BuilderBot",
      "type": "n8n-nodes-base.httpRequest",
      "position": [450, 300]
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ $json }}"
      },
      "name": "Respond to Webhook",
      "type": "n8n-nodes-base.respondToWebhook",
      "position": [650, 300]
    }
  ],
  "connections": {
    "Webhook": {
      "main": [
        [
          {
            "node": "HTTP Request - BuilderBot",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "HTTP Request - BuilderBot": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

### Probar el Workflow

```bash
curl -X POST https://tu-n8n.com/webhook/enviar-mensaje \
-H "Content-Type: application/json" \
-d '{
  "mensaje": "Hola desde N8N",
  "telefono": "34727788459"
}'
```

---

## 🐍 Ejemplo con Python

```python
import requests
import json

def enviar_mensaje_builderbot(telefono, mensaje, media_url=None):
    """
    Envía un mensaje a través de BuilderBot
    
    Args:
        telefono (str): Número de teléfono (formato: 34XXXXXXXXX)
        mensaje (str): Contenido del mensaje
        media_url (str, optional): URL de imagen/video/audio
    
    Returns:
        dict: Respuesta de la API
    """
    url = "https://www.builderbot.cloud/api/v2/aXMuiiBizI30Kl-Hwi_k2/messages"
    
    headers = {
        "Content-Type": "application/json",
        "x-api-builderbot": "bb-ygmc9zTq68gvx0e7A6XPLM6U426rbr-dCtl"
    }
    
    payload = {
        "messages": {
            "content": mensaje
        },
        "number": telefono
    }
    
    # Añadir mediaUrl si se proporciona
    if media_url:
        payload["messages"]["mediaUrl"] = media_url
    
    response = requests.post(url, headers=headers, json=payload)
    
    return response.json()

# Ejemplo de uso
if __name__ == "__main__":
    # Mensaje simple
    resultado = enviar_mensaje_builderbot(
        telefono="34727788459",
        mensaje="Hola desde Python!"
    )
    print(resultado)
    
    # Mensaje con imagen
    resultado_media = enviar_mensaje_builderbot(
        telefono="34727788459",
        mensaje="Mira esta imagen",
        media_url="https://ejemplo.com/imagen.jpg"
    )
    print(resultado_media)
```

---

## 🌐 Ejemplo con JavaScript/Node.js

```javascript
const axios = require('axios');

async function enviarMensajeBuilderBot(telefono, mensaje, mediaUrl = null) {
    const url = 'https://www.builderbot.cloud/api/v2/aXMuiiBizI30Kl-Hwi_k2/messages';
    
    const headers = {
        'Content-Type': 'application/json',
        'x-api-builderbot': 'bb-ygmc9zTq68gvx0e7A6XPLM6U426rbr-dCtl'
    };
    
    const data = {
        messages: {
            content: mensaje
        },
        number: telefono
    };
    
    // Añadir mediaUrl si se proporciona
    if (mediaUrl) {
        data.messages.mediaUrl = mediaUrl;
    }
    
    try {
        const response = await axios.post(url, data, { headers });
        return response.data;
    } catch (error) {
        console.error('Error:', error.response?.data || error.message);
        throw error;
    }
}

// Ejemplo de uso
(async () => {
    // Mensaje simple
    const resultado = await enviarMensajeBuilderBot(
        '34727788459',
        'Hola desde Node.js!'
    );
    console.log(resultado);
    
    // Mensaje con imagen
    const resultadoMedia = await enviarMensajeBuilderBot(
        '34727788459',
        'Mira esta imagen',
        'https://ejemplo.com/imagen.jpg'
    );
    console.log(resultadoMedia);
})();
```

---

## 📝 Formatos de Número Soportados

### Formato Correcto

```
34727788459    ✅ (Código país + número sin espacios)
```

### Formatos Incorrectos

```
+34 727 788 459   ❌ (Espacios no permitidos)
727788459          ❌ (Falta código país)
+34727788459       ❌ (Símbolo + no permitido)
```

---

## 🎯 Tipos de Media Soportados

|Tipo|Extensiones|Ejemplo URL|
|---|---|---|
|**Imágenes**|`.jpg`, `.jpeg`, `.png`, `.gif`|`https://ejemplo.com/foto.jpg`|
|**Videos**|`.mp4`, `.avi`, `.mov`|`https://ejemplo.com/video.mp4`|
|**Audio**|`.mp3`, `.ogg`, `.wav`|`https://ejemplo.com/audio.mp3`|
|**Documentos**|`.pdf`, `.doc`, `.docx`|`https://ejemplo.com/doc.pdf`|

---

## 🛠️ Troubleshooting

### Error: "Invalid API Key"

**Solución:** Verifica que el header `x-api-builderbot` contenga la API key correcta.

```bash
# Verificar header
curl -v https://www.builderbot.cloud/api/v2/aXMuiiBizI30Kl-Hwi_k2/messages \
--header 'x-api-builderbot: bb-ygmc9zTq68gvx0e7A6XPLM6U426rbr-dCtl'
```

### Error: "Invalid phone number"

**Solución:** Asegúrate de usar el formato correcto (código país + número sin espacios).

```json
{
    "number": "34727788459"  // ✅ Correcto
}
```

### Media no se envía

**Solución:** Verifica que la URL de media sea accesible públicamente.

```bash
# Probar acceso a la URL
curl -I https://ejemplo.com/imagen.jpg
```

---

## 📊 Códigos de Respuesta HTTP

| Código | Significado       | Acción                        |
| ------ | ----------------- | ----------------------------- |
| `200`  | Éxito             | Mensaje enviado correctamente |
| `400`  | Bad Request       | Verificar formato del body    |
| `401`  | Unauthorized      | Verificar API key             |
| `404`  | Not Found         | Verificar endpoint            |
| `429`  | Too Many Requests | Implementar rate limiting     |
| `500`  | Server Error      | Reintentar más tarde          |
