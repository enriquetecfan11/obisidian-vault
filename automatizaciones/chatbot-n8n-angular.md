---
title: "Chatbot con n8n y Angular"
type: "nota"
tags:
  - angular
  - automatizacion
  - chatbot
  - frontend
  - n8n
project: "N8N Automation"
status: "pendiente"
date_created: "2026-03-01"
date_modified: "2026-03-01"
updated: 2026-04-06
---
## Componente ts angular

```js

ngAfterViewInit(): void {  
    createChat({  
        webhookUrl: 'https://rational-glorious-bedbug.ngrok-free.app/webhook/4b3b1838-d6b3-447e-9d79-d0931eddb9f8/chat',  
        target: '#n8n',  
        mode: 'window',  
        chatInputKey: 'chatInput',  
        chatSessionKey: 'sessionId',  
        showWelcomeScreen: false,  
        defaultLanguage: 'en',  
        initialMessages: [  
            'Hola, escribe tu pregunta para ayudarte.',  
        ],  
        i18n: {  
            en: {  
                title: 'Hola! 👋',  
                subtitle: "Si tienes alguna duda sobre el portal, no dudes en preguntar.",  
                footer: '',  
                getStarted: 'Nueva conversacion',  
                inputPlaceholder: 'Escribe tu pregunta..',  
                closeButtonTooltip: 'Cerrar chat',  
            },  
        },  
    });  
}

```

## Relacionado
- [[n8n-api-endpoints]] — API n8n
- [[Tablas PostgreSQL N8N]] — memoria de chat en Postgres
- [[MOC Automatizaciones]] — índice
