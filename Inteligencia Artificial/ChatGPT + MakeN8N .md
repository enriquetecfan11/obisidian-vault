---
type: "nota"
tags: ["#proyecto-SaaS", "#area-devops", "#status-pendiente", "#topic-n8n", "#topic-ia"] # Siempre array con 2-5 tags específicos
project: "N8N Automation"
status: "pendiente"
date_created: "2026-03-01"
date_modified: "2026-03-01"
related: [] # Array vacío o con [[links]]
---

## 📋 Índice

1. [Definir Funcionalidades](https://claude.ai/chat/11c865c3-afc6-4238-8f9b-bbd5735ae48a#1-definir-las-funcionalidades-del-asistente)
2. [Configurar Automatización en Make](https://claude.ai/chat/11c865c3-afc6-4238-8f9b-bbd5735ae48a#2-configurar-la-automatizaci%C3%B3n-en-make-o-n8n)
3. [Crear el Asistente en ChatGPT](https://claude.ai/chat/11c865c3-afc6-4238-8f9b-bbd5735ae48a#3-crear-el-asistente-en-chatgpt)
4. [Configurar Acciones](https://claude.ai/chat/11c865c3-afc6-4238-8f9b-bbd5735ae48a#4-configurar-las-acciones-en-chatgpt)
5. [Probar el Asistente](https://claude.ai/chat/11c865c3-afc6-4238-8f9b-bbd5735ae48a#5-probando-el-asistente)

---

## 1. Definir las Funcionalidades del Asistente

### ¿Qué Automatizar?

Identifica tareas que cumplan estos criterios:

- ✅ **Repetitivas** - Se realizan con frecuencia
- ✅ **Bajo impacto** - No son críticas para el negocio
- ✅ **Consumen tiempo** - Aunque simples, suman horas al mes

### Ejemplos de Tareas Ideales

|Tarea|Descripción|Ahorro de Tiempo|
|---|---|---|
|**Registro de facturas**|Extraer datos de facturas y subirlas a Google Sheets|~15 min/factura|
|**Gestión de tickets**|Clasificar y asignar tickets de soporte|~10 min/ticket|
|**Actualización de CRM**|Registrar interacciones con clientes|~5 min/cliente|
|**Resúmenes de reuniones**|Extraer puntos clave y crear tareas|~20 min/reunión|

---

## 2. Configurar la Automatización en Make o N8N

### Requisitos Previos

- Cuenta en [Make.com](https://www.make.com/) o N8N instalado
- Cuenta Plus de OpenAI (para GPTs personalizados)

### Pasos en Make.com

#### 2.1. Crear un Nuevo Escenario

1. Accede a **Make.com** → **Scenarios**
2. Clic en **Create a new scenario**
3. Asigna un nombre descriptivo (ej: "ChatGPT - Registro de Facturas")

#### 2.2. Configurar el Webhook

1. Añade un módulo **Webhooks** → **Custom Webhook**
2. Clic en **Add** para crear un nuevo webhook
3. Asigna un nombre al webhook (ej: "Webhook ChatGPT Facturas")
4. Copia y guarda la URL generada

**Ejemplo de Webhook generado:**

```
https://hook.eu2.make.com/u63igzuw7ygjmd9m2sp8cpp34h
```

**Desglose de la URL:**

- **Link base:** `https://hook.eu2.make.com`
- **ID del webhook:** `/u63igzuw7ygjmd9m2sp8cpp34h`

#### 2.3. Estructura del Webhook

El webhook recibirá datos en formato JSON desde ChatGPT:

```json
{
  "tipo_documento": "factura",
  "proveedor": "Acme Corp",
  "fecha": "2026-02-01",
  "importe": 450.50,
  "categoria": "servicios",
  "notas": "Servicios de hosting mensual"
}
```

---

## 3. Crear el Asistente en ChatGPT

### Requisitos

> ⚠️ **Importante:** Necesitas una cuenta **ChatGPT Plus** para crear GPTs personalizados.

### 3.1. Iniciar la Creación del GPT

1. Accede a [ChatGPT](https://chat.openai.com/)
2. Ve a **Explore GPTs** → **My GPTs**
3. Clic en **Create** (Crear)

### 3.2. Configurar el Asistente

#### Pestaña "Configure"

**Nombre:**

```
Mi Asistente de Cuentas
```

**Descripción:**

```
Asistente inteligente que procesa facturas, tickets y documentos empresariales, enviando datos estructurados a Make.com para automatización.
```

**Instrucciones (System Prompt):**

```markdown
Eres un asistente personal y ejecutivo especializado en automatización de tareas.

## Tu Misión
Ayudar al usuario a procesar documentos empresariales (facturas, tickets, recibos) extrayendo información relevante y enviándola a sistemas de automatización.

## Cómo Operar
1. Cuando el usuario adjunte un documento, analízalo cuidadosamente
2. Extrae los datos clave según el tipo de documento
3. Estructura la información en formato JSON
4. Envía los datos al webhook de Make.com usando la acción configurada
5. Confirma al usuario que la información se procesó correctamente

## Datos a Extraer (Facturas)
- Proveedor/Emisor
- Fecha de emisión
- Importe total
- Categoría (servicios, productos, suministros, etc.)
- Notas adicionales relevantes

## Tono
Profesional, eficiente y claro. Confirma cada acción realizada.
```

**Conversation Starters (Ejemplos de inicio):**

```
📄 Adjunta una factura para procesarla
🎫 Registra este ticket de soporte
💰 Analiza este recibo de compra
📊 ¿Qué puedes hacer por mí?
```

### 3.3. Configurar Capacidades

- ✅ **Web Browsing** - Desactivado (no es necesario)
- ✅ **DALL·E Image Generation** - Desactivado
- ✅ **Code Interpreter** - Activado (útil para procesar datos)

---

## 4. Configurar las Acciones en ChatGPT

### 4.1. Acceder al Editor de Acciones

1. En la configuración del GPT, ve a la pestaña **Actions**
2. Clic en **Create new action**

### 4.2. Generar el Schema con GPT Especializado

Usa este GPT para generar el schema automáticamente:  
🔗 [Create Make.com Webhook Schema's](https://chatgpt.com/g/g-zVzDlJ8dR-create-make-com-webhook-schema-s)

**Prompt para el GPT generador:**

```
Crea un schema de webhook para Make.com que reciba:
- tipo_documento (string)
- proveedor (string)
- fecha (string en formato YYYY-MM-DD)
- importe (number)
- categoria (string)
- notas (string)

La URL del webhook es: https://hook.eu2.make.com/u63igzuw7ygjmd9m2sp8cpp34h
```

### 4.3. Schema Generado (Ejemplo)

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "Make.com Webhook - Registro de Facturas",
    "description": "Envía datos de facturas a Make.com para procesamiento automático",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "https://hook.eu2.make.com"
    }
  ],
  "paths": {
    "/u63igzuw7ygjmd9m2sp8cpp34h": {
      "post": {
        "operationId": "enviarFactura",
        "summary": "Envía datos de factura a Make.com",
        "requestBody": {
          "required": true,
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "tipo_documento": {
                    "type": "string",
                    "description": "Tipo de documento (factura, ticket, recibo)"
                  },
                  "proveedor": {
                    "type": "string",
                    "description": "Nombre del proveedor o emisor"
                  },
                  "fecha": {
                    "type": "string",
                    "format": "date",
                    "description": "Fecha del documento en formato YYYY-MM-DD"
                  },
                  "importe": {
                    "type": "number",
                    "description": "Importe total del documento"
                  },
                  "categoria": {
                    "type": "string",
                    "description": "Categoría del gasto (servicios, productos, suministros, etc.)"
                  },
                  "notas": {
                    "type": "string",
                    "description": "Notas o comentarios adicionales"
                  }
                },
                "required": ["tipo_documento", "proveedor", "fecha", "importe", "categoria"]
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "Datos recibidos correctamente",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "success": {
                      "type": "boolean"
                    },
                    "message": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### 4.4. Configurar la Acción en ChatGPT

1. **Pega el schema** en el editor de acciones
2. **Verifica que el método sea POST**
3. **Añade la Privacy Policy:**
    
    ```
    https://www.make.com/en/privacy-notice
    ```
    
4. **Guarda la acción**

---

## 5. Probando el Asistente

### 5.1. Preparar Make.com

1. En tu escenario de Make, clic en **Run Once**
2. El webhook quedará en espera de datos

### 5.2. Probar desde ChatGPT

1. Abre un nuevo chat con tu GPT personalizado
2. Adjunta una factura o imagen de documento
3. Pide al asistente que la procese:
    
    ```
    Procesa esta factura y registra los datos
    ```
    

### 5.3. Agregar Módulo de Google Sheets

#### Configuración del Módulo

1. En Make, añade un módulo **Google Sheets** → **Add a Row**
2. Conecta tu cuenta de Google
3. Selecciona tu hoja de cálculo
4. Mapea los campos:

|Campo en Sheets|Dato del Webhook|
|---|---|
|Fecha|`{{fecha}}`|
|Proveedor|`{{proveedor}}`|
|Importe|`{{importe}}`|
|Categoría|`{{categoria}}`|
|Notas|`{{notas}}`|

#### Estructura Sugerida de la Hoja

|Fecha|Proveedor|Importe|Categoría|Notas|
|---|---|---|---|---|
|2026-02-01|Acme Corp|450.50|Servicios|Hosting mensual|

---

## 🔧 Ejemplo Completo de Flujo en Make

```
┌─────────────────┐
│  Custom Webhook │
│  (Recibe datos) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Router         │
│  (Opcional)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Google Sheets   │
│ Add a Row       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Email/Slack    │
│  (Notificación) │
└─────────────────┘
```

---

## 🐛 Troubleshooting

### El webhook no recibe datos

**Solución:**

1. Verifica que el webhook esté en modo **Run Once**
2. Comprueba que la URL en el schema de ChatGPT sea correcta
3. Revisa que el método sea **POST**

### ChatGPT no llama a la acción

**Solución:**

1. Asegúrate de que las instrucciones del GPT mencionen usar la acción
2. Verifica que la acción esté guardada y activa
3. Prueba con un prompt más explícito:
    
    ```
    Usa la acción para enviar estos datos a Make
    ```
    

### Los datos llegan vacíos a Google Sheets

**Solución:**

1. Verifica el mapeo de campos en Make
2. Usa la sintaxis correcta: `{{1.nombre_campo}}`
3. Comprueba que el JSON del webhook contenga los campos esperados

---

## 📊 Casos de Uso Avanzados

### 1. Sistema de Tickets de Soporte

**Campos a extraer:**

- ID del cliente
- Tipo de problema
- Prioridad
- Descripción
- Asignado a

**Acción en Make:**

- Crear ticket en sistema CRM
- Notificar al equipo por Slack
- Registrar en base de datos

### 2. Procesamiento de Recibos de Gastos

**Campos a extraer:**

- Empleado
- Proyecto/Centro de costes
- Tipo de gasto
- Importe
- Adjuntos (URL imagen)

**Acción en Make:**

- Validar límites de gasto
- Aprobar/Rechazar automáticamente
- Generar reporte mensual

### 3. Análisis de Contratos

**Campos a extraer:**

- Cliente
- Fecha inicio/fin
- Valor del contrato
- Términos clave
- Renovación automática

**Acción en Make:**

- Crear recordatorio de renovación
- Actualizar pipeline de ventas
- Notificar al equipo legal

---

## 📝 Mejores Prácticas

### Prompts del GPT

✅ **Hacer:**

- Ser específico sobre qué datos extraer
- Incluir ejemplos de formato esperado
- Definir manejo de errores

❌ **Evitar:**

- Instrucciones vagas o ambiguas
- Demasiadas responsabilidades en un GPT
- No especificar formatos de datos

### Seguridad

- 🔒 No incluyas API keys en el schema
- 🔒 Usa webhooks de Make en lugar de APIs directas
- 🔒 Valida datos en Make antes de escribir en bases de datos
- 🔒 Implementa rate limiting en Make

### Mantenimiento

- 📅 Revisa logs de Make semanalmente
- 📅 Actualiza el schema cuando cambien requisitos
- 📅 Documenta cambios en las instrucciones del GPT

---

## 🔗 Recursos Útiles

- [Documentación oficial de Make](https://www.make.com/en/help)
- [OpenAI GPTs Guide](https://help.openai.com/en/articles/8554397-gpts)
- [GPT generador de schemas](https://chatgpt.com/g/g-zVzDlJ8dR-create-make-com-webhook-schema-s)
- [Make Privacy Notice](https://www.make.com/en/privacy-notice)

---

**Última actualización:** Febrero 2026  
**Autor:** Kike - Nundu Desarrollos