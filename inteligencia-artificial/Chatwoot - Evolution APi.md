---
tags:
  - chatwoot
  - evolution-api
  - whatsapp
  - crm
  - automatizacion
status: active
updated: 2026-05-13
title: chatwoot-evolution-api
type: nota
project: none
date_created: 2026-05-13
date_modified: 2026-05-13
---
# Cómo conectar Chatwoot con Evolution API

> Tutorial de referencia detallado para conectar una instancia de Chatwoot con Evolution API y centralizar conversaciones de WhatsApp en una bandeja operativa tipo CRM conversacional. Basado en el vídeo **"Cómo Conectar Chatwoot con Evolution API"** de Andy Cruz y en su transcripción completa. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
## Ruta exacta de configuración

Dentro de Evolution Manager, el flujo del vídeo es este:
1. Entrar en la instancia deseada. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
2. Abrir **Settings**. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
3. Ir a **Integraciones**. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
4. Elegir **Chatwoot**. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

En esa pantalla aparecerá el formulario de configuración de la integración. Según se muestra en el vídeo, puede aparecer inicialmente deshabilitado y es necesario activarlo manualmente. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Campos que hay que rellenar

El vídeo enseña varios campos y explica cómo obtenerlos. Esta parte conviene documentarla con cuidado porque es donde suelen ocurrir la mayoría de errores de conexión.

### 1. Chatwoot URL

El campo `Chatwoot URL` debe contener la URL base de la instancia de Chatwoot. En el vídeo, el autor copia la URL desde el navegador y especifica que debe pegarse **solo hasta antes de `/app`**. También advierte que normalmente la URL se copia con una barra final y recomienda quitarla. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

#### Regla práctica

- Correcto: `https://tu-chatwoot.midominio.com`
- Incorrecto: `https://tu-chatwoot.midominio.com/`
- Incorrecto: `https://tu-chatwoot.midominio.com/app`

La intención es entregar a Evolution Manager la raíz de la aplicación, no una ruta interna de la interfaz web. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### 2. Account ID

El `Account ID` es el identificador numérico de la cuenta de Chatwoot. En el vídeo se explica que puede obtenerse de dos formas:

- Observando la URL, en el segmento que contiene `accounts/{id}`. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Consultando la sección de **Settings**, donde también aparece el `Account ID`. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

El autor muestra un ejemplo donde el identificador es `1`, pero señala expresamente que en otros entornos podría ser `2`, `3` u otro valor. Ese número es el que debe copiarse al campo correspondiente de la integración. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### 3. Token de acceso

El token se obtiene desde **Profile Settings** en Chatwoot. El vídeo indica que hay que ir a la parte inferior izquierda, entrar en la configuración del perfil, bajar hasta el final y copiar el **Access Token**. Ese valor se pega en el campo `token` de la integración de Evolution Manager. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

Este paso merece una observación operativa: el vídeo no entra en políticas de seguridad, pero en la práctica este token debe tratarse como una credencial sensible, ya que otorga acceso operativo contra la cuenta configurada. Esa consideración no aparece desarrollada en el vídeo, aunque se deduce por el rol que cumple el token en el proceso. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### 4. Nombre del inbox

El vídeo muestra un campo de nombre que determina cómo aparecerá el inbox creado en Chatwoot. El autor recomienda asignarle el nombre con el que quieres que luego se vea dentro de la interfaz de Chatwoot. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

En su ejemplo, utiliza un nombre específico para el inbox y recomienda mantener coherencia con el identificador del bot o integración. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### 5. Identificador o nombre interno del bot

El autor comenta que conviene poner el mismo nombre, pero en minúsculas, para el bot que realizará la conexión. Esto parece una recomendación de consistencia para reconocer fácilmente la integración y evitar discrepancias entre el nombre visual y el identificador operativo. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### 6. Logo

El vídeo indica expresamente que el logo puede dejarse vacío. No es un requisito para que la integración funcione. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### 7. Conversación pendiente

La opción de conversación pendiente se deja activada en el ejemplo del vídeo. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### 8. Reabrir conversación

El autor recomienda **no activar** la opción de reabrir conversación. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### 9. Importar contactos

La importación de contactos se activa en el vídeo, por lo que forma parte de la configuración recomendada por el autor. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### 10. Importar mensajes

También se activa la importación de mensajes. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### 11. Ventana o rango de importación

El vídeo menciona dejar por defecto un rango de **7 días**, con la justificación de que si se amplía demasiado podría cargar demasiada información. Esto sugiere que el campo controla la cantidad de histórico a importar o sincronizar inicialmente. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### 12. Números excluidos

Existe un campo para indicar números que no se desean importar. En el vídeo se deja en blanco. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### 13. Auto create

La opción `auto create` debe activarse. El vídeo lo marca como parte del proceso antes de guardar. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Guardar y validar la integración

Después de completar el formulario, el autor pulsa guardar y comenta que aparece un mensaje indicando que Chatwoot ha sido conectado con éxito. Sin embargo, acto seguido observa que aparentemente no pasa nada visible en la interfaz y vuelve a hacer clic en la opción de `auto create`, tras lo cual la integración queda aplicada con éxito y finalmente aparece el nuevo inbox en Chatwoot. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

Este detalle es importante porque sugiere una de estas posibilidades operativas:

- La integración se guarda primero y materializa el inbox en un segundo intento. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- El panel puede tardar un poco en refrescar el estado. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Puede existir un comportamiento algo inconsistente del formulario o del proceso visual de confirmación. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

El vídeo no profundiza en la causa técnica, pero sí deja una pauta práctica útil: si tras guardar no aparece el inbox nuevo, conviene revisar `auto create`, refrescar y repetir la acción antes de asumir que la conexión ha fallado. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Qué debería aparecer en Chatwoot

Si todo ha ido bien, en Chatwoot aparecerá un **nuevo inbox** asociado a la integración recién creada. En el vídeo, el autor muestra cómo ya se ve el inbox nuevo en la interfaz lateral y cómo queda asociado al bot o a la instancia conectada. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

A partir de ese momento, la expectativa es que los mensajes que entren por el número o bot conectado mediante Evolution API puedan visualizarse desde ese inbox dentro de Chatwoot. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Prueba funcional de extremo a extremo

El vídeo realiza una validación simple pero suficiente:

1. Se envía un mensaje de prueba (“hola”) desde WhatsApp al número o bot conectado. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
2. Se revisa el inbox en Chatwoot. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
3. Inicialmente no aparece nada. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
4. Se descubre que el motivo no es un fallo de conexión, sino el filtro de visualización de conversaciones. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

Este punto es probablemente la parte más útil del vídeo para troubleshooting básico, porque evita concluir demasiado pronto que la integración está rota cuando en realidad el problema es puramente de interfaz o filtrado. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Problema típico: “no veo la conversación”

Según el vídeo, Chatwoot estaba mostrando únicamente conversaciones con estado **abierto**. Debido a eso, el mensaje de prueba no se veía, aunque la integración ya estaba funcionando. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### Cómo corregirlo

Hay que entrar en la zona de filtros del inbox y localizar el filtro de estado, que estaba configurado como `open` o `abiertas`. Después hay que quitar ese filtro y cambiarlo por `all`, aplicando el nuevo criterio. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### Resultado esperado

Una vez aplicado el filtro `all`, el mensaje de prueba aparece inmediatamente en el inbox. El vídeo muestra el contacto y el mensaje visible tras ese ajuste. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Respuesta desde Chatwoot

Con el chat ya visible, el autor responde desde Chatwoot con un mensaje de ejemplo. Después comprueba en el canal de destino que la respuesta se ha reflejado correctamente. Esto confirma el flujo bidireccional básico: recepción en Chatwoot y salida desde Chatwoot hacia el otro extremo conectado por Evolution API. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

Aunque el vídeo no hace una batería completa de pruebas, esta verificación sí deja claro que la integración no es solo de consulta, sino también de operación básica sobre mensajes. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Diferencia visual frente a la app oficial

El vídeo menciona una diferencia visual interesante en Chatwoot: cuando el inbox está conectado por la app oficial de WhatsApp, aparece un símbolo de WhatsApp; cuando está conectado a través de Evolution API, aparece un símbolo de nube. El autor lo atribuye a que se trata de una app no oficial. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

Esto no cambia el flujo funcional principal, pero puede servirte para reconocer rápidamente en la interfaz qué inboxes están conectados por la API oficial y cuáles dependen de una integración basada en Evolution API. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Guardar el filtro para no repetir el ajuste

Tras corregir el filtro de conversaciones, el autor recomienda guardar un filtro personalizado para no tener que rehacer este cambio cada vez. La sugerencia del vídeo es crear un filtro con un nombre como `all conversations` o `todas las conversaciones`. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### Qué resuelve este filtro guardado

Con ese filtro persistente, cuando entres a otros inboxes y regreses al inbox conectado por Evolution API, podrás volver rápidamente a la vista que muestra todas las conversaciones, evitando la confusión de pensar que desaparecieron. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### Por qué importa en operación diaria

En un entorno con varios inboxes, agentes o integraciones, es fácil olvidar que la vista actual está filtrada. Guardar el filtro es una mejora de usabilidad pequeña, pero muy relevante para soporte y operación continua. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Procedimiento resumido paso a paso

A continuación queda el proceso reescrito como checklist operativo continuo:

1. Verifica que Chatwoot está desplegado y accesible por URL. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
2. Verifica que Evolution API está desplegado y accesible. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
3. En la configuración o variables de entorno de Evolution API, localiza `chatwoot enable` y ponlo en `true` si estaba en `false`. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
4. Guarda los cambios y redepliega el servicio para que la configuración quede aplicada. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
5. Abre Evolution Manager. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
6. Selecciona la instancia que quieras conectar a Chatwoot. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
7. Entra en `Settings -> Integraciones -> Chatwoot`. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
8. Activa la integración si aparece deshabilitada. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
9. Rellena `Chatwoot URL` con la raíz de tu instancia, sin `/app` y sin barra final. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
10. Obtén el `Account ID` de Chatwoot y pégalo en el campo correspondiente. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
11. Obtén el `Access Token` desde `Profile Settings` en Chatwoot y pégalo en el campo de token. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
12. Define el nombre visible del inbox. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
13. Opcionalmente usa el mismo nombre en minúsculas para el identificador del bot o conexión. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
14. Deja el logo vacío si no necesitas personalizarlo. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
15. Mantén activadas las opciones de conversación pendiente, importar contactos e importar mensajes, tal como muestra el vídeo. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
16. No actives la reapertura automática de conversaciones, siguiendo la recomendación del autor. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
17. Mantén el rango de importación en 7 días salvo que tengas un motivo concreto para cambiarlo. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
18. Deja vacía la lista de números excluidos si no necesitas excepciones. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
19. Activa `auto create`. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
20. Guarda la integración. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
21. Si el inbox no aparece a la primera, refresca, revisa `auto create` y repite la acción tal como se ve en el vídeo. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
22. Abre Chatwoot y comprueba que el inbox nuevo ya existe. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
23. Envía un mensaje de prueba desde el WhatsApp o bot conectado. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
24. Si no ves la conversación, revisa el filtro del inbox. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
25. Cambia el estado de `open` a `all`. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
26. Verifica que el mensaje aparece y responde desde Chatwoot. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
27. Guarda un filtro persistente de “todas las conversaciones” para simplificar la operación diaria. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Explicación detallada de cada dato necesario

### URL base de Chatwoot

La URL base es el dominio principal por el que accedes a la interfaz de Chatwoot. Debe representar el host del servicio y no una ruta interna de navegación. El vídeo enfatiza que copiar la URL completa del navegador puede inducir a pegar `/app` o una barra final, y ambos detalles conviene limpiarlos antes de guardar. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### Account ID

El `Account ID` es el identificador lógico de tu cuenta dentro de Chatwoot. No es el usuario, no es el inbox y no es el token. Si se coloca un valor equivocado en este punto, la integración puede no asociarse correctamente a la cuenta deseada. El vídeo enseña claramente que este dato puede consultarse desde la URL o desde ajustes. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### Access Token

El `Access Token` es la credencial que Evolution Manager usará para autenticarse contra Chatwoot. El tutorial lo toma desde la configuración del perfil y no desde un apartado de desarrollador independiente. Eso significa que la integración está apoyándose en una credencial de usuario con permisos sobre la cuenta. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

### Nombre del inbox

Este nombre no es un simple adorno. En la práctica, será la referencia visual que usarás después dentro de Chatwoot para distinguir el canal. Si vas a trabajar con varios bots, varias líneas o varios clientes, conviene adoptar una convención de nombres estable desde el principio, aunque el vídeo solo muestre el ejemplo básico. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Qué capacidades menciona el vídeo una vez conectado

El vídeo abre con una promesa funcional bastante clara: una vez enlazado Chatwoot con Evolution API, se pueden gestionar conversaciones desde un único lugar y operar acciones como etiquetas, transferencias a agentes humanos y colaboración con más usuarios. Esa descripción sitúa la integración no solo como un puente técnico, sino como un punto de consolidación operativa. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

Dicho de otra forma, la ventaja no es únicamente “ver mensajes”, sino mover la operación a una interfaz más adecuada para atención, seguimiento y trabajo de equipo. El vídeo lo enmarca específicamente como un uso de Chatwoot de estilo CRM conversacional. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Limitaciones del vídeo

Aunque el tutorial es útil y directo, conviene entender lo que **no** cubre para que este documento no se use con expectativas incorrectas. El vídeo no entra en configuración de webhooks avanzados, no trata autenticación endurecida, no explica políticas de reintento, no documenta logs ni diagnóstico a nivel de contenedor y tampoco cubre automatizaciones complejas o interoperabilidad con flujos ya existentes. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

Tampoco entra en diferencias de versiones entre instancias de Chatwoot o Evolution API, ni en consideraciones de producción como persistencia, backup, proxy inverso, seguridad TLS, rate limits o problemas de compatibilidad. Por tanto, este documento debe entenderse como una guía de conexión funcional basada estrictamente en el contenido mostrado por el autor. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Problemas y comprobaciones útiles

A partir de lo que enseña el vídeo, estos son los puntos de revisión más importantes si algo falla:

| Problema observado | Revisión recomendada | Base en el vídeo |
|---|---|---|
| La opción de Chatwoot no funciona o aparece deshabilitada | Comprobar que `chatwoot enable` está en `true` y redeplegar Evolution API |  [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM) |
| La integración parece guardarse pero no aparece el inbox | Revisar `auto create`, refrescar y volver a aplicar |  [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM) |
| Los mensajes no se ven en Chatwoot | Revisar el filtro de estado y cambiar de `open` a `all` |  [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM) |
| No se sabe qué poner en Chatwoot URL | Usar la raíz del dominio, sin `/app` y sin barra final |  [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM) |
| No se encuentra el Account ID | Buscarlo en la URL de Chatwoot o en Settings |  [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM) |
| No se encuentra el token | Ir a Profile Settings y copiar el Access Token |  [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM) |

## Recomendaciones prácticas para documentarlo en tu stack

Si vas a conservar esta integración como parte estable de tu infraestructura, tiene sentido ampliar el procedimiento del vídeo con documentación interna propia. Aunque esto ya no se explica en detalle en el material original, sí encaja con la forma en que el proceso está planteado y con los puntos delicados que el propio vídeo revela. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

Conviene anotar al menos:

- La URL base exacta del Chatwoot productivo. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- El nombre de la instancia de Evolution API que está enlazada. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- El criterio de naming usado para el inbox. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Dónde está definida la variable `chatwoot enable`. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Qué usuario o perfil generó el token de acceso en Chatwoot. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Qué filtro guardado debe usar el equipo para ver todas las conversaciones. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Ejemplo conceptual de configuración

El vídeo no da un bloque literal exportable, pero sí permite construir un ejemplo conceptual como referencia documental:

```text
Instancia Evolution API: bot-ventas
Integración: Chatwoot
Chatwoot URL: https://chatwoot.midominio.com
Account ID: 1
Access Token: <token-del-perfil-chatwoot>
Inbox Name: ventas
Bot/Internal Name: ventas
Logo: vacío
Pending Conversation: activado
Reopen Conversation: desactivado
Import Contacts: activado
Import Messages: activado
Import Window: 7 días
Excluded Numbers: vacío
Auto Create: activado
```

Este ejemplo no sustituye los valores reales de tu entorno; solo organiza en formato legible los campos que el vídeo va configurando de forma visual. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Interpretación operativa del flujo

Si se mira el vídeo desde una perspectiva de operación real, la integración tiene tres ideas clave. La primera es que la habilitación por variable de entorno en Evolution API manda sobre el resto de la experiencia de configuración. La segunda es que Evolution Manager es el punto más simple para declarar la unión con Chatwoot. La tercera es que, una vez creada la integración, la percepción de “funciona o no funciona” puede depender simplemente del filtro de conversaciones aplicado dentro de Chatwoot. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

Este tercer punto es especialmente importante para equipos pequeños o instalaciones autogestionadas, porque un falso negativo en la interfaz puede llevar a perder tiempo depurando contenedores, tokens o credenciales cuando el problema real es solo una vista filtrada. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Tutorial operativo rápido

Para tener una referencia breve dentro de Obsidian, aquí queda una versión ultraejecutable del procedimiento:

- Poner `chatwoot enable=true` en Evolution API y redeplegar. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Ir a Evolution Manager, seleccionar la instancia y abrir `Settings -> Integraciones -> Chatwoot`. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Activar la integración. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Pegar la URL base de Chatwoot sin `/app` y sin barra final. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Copiar `Account ID` desde Chatwoot. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Copiar `Access Token` desde `Profile Settings`. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Definir nombre de inbox, activar importaciones y `auto create`, luego guardar. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Confirmar que aparece el inbox en Chatwoot. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Enviar un mensaje de prueba. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Si no se ve, cambiar el filtro de conversaciones a `all`. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
- Guardar un filtro persistente de “todas las conversaciones”. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

## Notas finales de uso

Este documento está deliberadamente centrado en el contenido real del vídeo y en su transcripción, por lo que sirve bien como manual de referencia rápida para repetir exactamente el proceso mostrado por el autor. La parte más importante para recordar al volver a este tutorial dentro de Obsidian es que la conexión depende primero de la variable de entorno en Evolution API y, después, de un filtrado correcto en Chatwoot para visualizar lo ya conectado. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)

Si replicando estos pasos el inbox se crea pero la operación no fluye, el siguiente nivel razonable de revisión ya no aparece cubierto en el vídeo y requeriría inspeccionar versión de servicios, logs, credenciales, compatibilidad de la instancia y comportamiento específico de la integración desplegada. [youtube](https://www.youtube.com/watch?v=M2tG1LAodZM)
