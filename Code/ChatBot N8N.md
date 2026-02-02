---
tags:
  - angular
  - Programación
  - IA
  - n8n
ai_share: "true"
---
## Componente ts angular

```js

ngAfterViewInit(): void {  
    createChat({  
        webhookUrl: 'https://rational-glorious-bedbug.ngrok-free.app/webhook/4b3b1838-d6b3-447e-9d79-d0931eddb9f8/chat',  
        target: '#n8n-chat',  
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