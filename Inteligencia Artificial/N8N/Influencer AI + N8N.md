---
tags:
  - IA
  - n8n
  - InteligenciaArtificial
  - bots
ai_share: "true"
---
![[Pasted image 20250117085739.png]]

### **1. Publicación Programada**

En esta sección configuré la publicación automática de tweets cada 6 horas con minutos aleatorios. 

Quería que mis publicaciones parecieran más naturales, por eso añadí esa variación de tiempo. 

Gracias a esta opción, no tengo que preocuparme por estar pendiente todo el tiempo de publicar.

### **2. Publicación Bajo Demanda**

A veces me interesa publicar algo de manera manual, por lo que he añadido un nodo que me permite ejecutar el flujo cuando yo quiera con solo un clic. 


### **3. Configuración del Perfil de Influencer**

Aquí es donde defino cómo quiero que se genere el contenido. Personalizo varios parámetros para que el tweet se alinee con el tono y el estilo que busco. Estos son los elementos que configuro:

* **Nicho objetivo:** Por ejemplo, hablo de IA, desarrollo web o tecnología en general.
* **Estilo de escritura:** A veces quiero que el tono sea informativo, otras veces prefiero algo más inspirador o humorístico.
* **Inspiración:**  Aqui pongo algunos influencers o redactores que me gustan para que escriba como ellos.


### **4. Generar Tweet**

En esta parte, utilizo  el LLM de OpenAI GPT4o Mini para crear el contenido del tweet. Basándome en los parámetros que configuré antes, se genera un texto que sigue el estilo y tema que definí. 

### **5. Validar Tweet**

Después de generar el tweet, hago que pase por una validación automática. Esto me asegura que el texto cumple con las restricciones de longitud y formato de la plataforma twitter. 

Si el contenido supera el límite de caracteres o contiene errores, se regenera hasta que cumpla con los requisitos. Gracias a este proceso, evito errores que podrían afectar la publicación.

### **6. Publicar el Tweet**

Cuando todo está listo, el flujo publica automáticamente el tweet en mi cuenta de twitter. Este nodo está conectado a la API de la plataforma, por lo que no tengo que hacer nada más que añadir el texto validado del nodo anterior