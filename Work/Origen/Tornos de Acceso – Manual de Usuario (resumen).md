Documento interno – Nundu Desarrollo de Software (25-03-2026) [file:1]

---

## 1. Descripción general

La aplicación **Tornos de Acceso** controla la entrada y salida de usuarios a instalaciones protegidas mediante lecturas de **QR** o **pulsera NFC**, mostrando siempre en pantalla si el acceso está permitido o denegado. [file:1]

Además, permite **asociar pulseras NFC** a usuarios ya existentes en el sistema, de forma que puedan acceder sin usar QR. [file:1]

---

## 2. Qué puede hacer el usuario

- Pasar un **QR** por el lector para registrar entrada o salida. [file:1]  
- Acercar una **pulsera NFC** al lector para registrar entrada o salida. [file:1]  
- Consultar el resultado en pantalla: permitido / denegado y mensajes asociados. [file:1]  
- Usar los **botones físicos** para:
  - Entrar en el modo registro de pulseras NFC. [file:1]
  - Reiniciar el dispositivo (reset rápido). [file:1]

---

## 3. Primeros pasos

1. Comprobar que el dispositivo está encendido. [file:1]  
2. Esperar a que aparezca la **pantalla de inicio**. [file:1]  
3. Utilizar el lector de QR o el lector de pulseras NFC según el caso. [file:1]

### Elementos de la interfaz (botones físicos)

- **A – OK**: confirmar acción (seleccionar usuario, aceptar). [file:1]  
- **B – Atrás**: cancelar y volver a la pantalla de inicio. [file:1]  
- **C – Arriba**: subir en listas (modo registro NFC) / iniciar reset (C + D). [file:1]  
- **D – Abajo**: bajar en listas (modo registro NFC) / completar reset (C + D). [file:1]

La pantalla principal muestra mensajes como “Acceso permitido”, “Entrada denegada”, etc. [file:1]

---

## 4. Navegación básica

El dispositivo **no tiene menús complejos**: cambia de pantalla automáticamente cuando detecta una lectura de QR o pulsera NFC. [file:1]

Pantallas principales:  
- **Pantalla de inicio**: lista para lecturas, no requiere acción. [file:1]  
- **Pantalla de resultado**: muestra permitido/denegado y vuelve sola al inicio tras unos segundos. [file:1]  
- **Modo registro NFC**: se usa para asociar pulseras a usuarios. [file:1]

---

## 5. Acceso con QR

**Cuándo usarlo**: el usuario dispone de un QR válido para entrar o salir. [file:1]

**Pasos**:  
1. Colocar el QR frente al lector, bien visible. [file:1]  
2. Mantenerlo quieto un instante. [file:1]  
3. Mirar la pantalla para ver el resultado. [file:1]

**Mensajes de éxito**:  
- “Acceso permitido”. [file:1]  
- “Bienvenido” + “Entrada permitida”. [file:1]  
- “Salida registrada” + “Gracias por su visita”. [file:1]

**Mensajes de error / denegación**:  
- “Entrada denegada”. [file:1]  
- “Salida denegada”. [file:1]

Tras unos segundos, el dispositivo vuelve solo a la pantalla de inicio. [file:1]

---

## 6. Acceso con pulsera NFC

**Cuándo usarlo**: el usuario tiene pulsera NFC en lugar de QR. [file:1]

**Pasos**:  
1. Acercar la pulsera al lector NFC. [file:1]  
2. Mantenerla quieta hasta que cambie la pantalla. [file:1]  
3. Consultar el resultado en pantalla. [file:1]

**Mensajes de éxito**:  
- “Bienvenido” (entrada registrada correctamente). [file:1]  
- “Salida registrada” (salida registrada correctamente). [file:1]

**Mensajes de error / denegación**:  
- “Entrada denegada”. [file:1]  
- “Salida denegada”. [file:1]

---

## 7. Modo registro NFC (asociar pulsera a usuario)

**Objetivo**: asociar o reasignar una pulsera NFC a un usuario concreto. [file:1]

### A. Entrar en modo registro

1. En la pantalla de inicio, pulsar **A (OK)**. [file:1]  
2. Justo después, pulsar **B (Atrás)**. [file:1]  
3. Aparece la pantalla “Modo registro NFC” con la lista de usuarios (ej. “1/5”). [file:1]

### B. Elegir usuario

- Pulsar **C (Arriba)** para subir en la lista. [file:1]  
- Pulsar **D (Abajo)** para bajar en la lista. [file:1]  
- El usuario seleccionado queda marcado en pantalla. [file:1]

### C. Confirmar usuario

1. Con el usuario correcto seleccionado, pulsar **A (OK)**. [file:1]  
2. El dispositivo muestra “Acerque la pulsera” / “Esperando lectura para asociar”. [file:1]

### D. Asociar la pulsera

1. Acercar la pulsera al lector NFC. [file:1]  
2. Mantenerla quieta hasta que cambie la pantalla. [file:1]  
3. Aparece “Pulsera asociada”. [file:1]  
4. Tras unos segundos, el sistema vuelve a la pantalla de inicio. [file:1]

### E. Cancelar modo registro

- Pulsar **B (Atrás)** para salir sin asociar. [file:1]  
- El dispositivo cierra el modo registro y vuelve a inicio. [file:1]

Si no hay usuarios disponibles se muestra “No hay usuarios”; el dispositivo vuelve solo al inicio y se debe avisar al responsable para revisar la lista. [file:1]

---

## 8. Reset del dispositivo (reinicio rápido)

**Cuándo usarlo**: dispositivo bloqueado, sin respuesta o comportamiento anómalo. [file:1]

Pasos:  
1. Pulsar **C (Arriba)**. [file:1]  
2. Justo después, pulsar **D (Abajo)**. [file:1]  
3. Aparece la pantalla de reset y el dispositivo se reinicia. [file:1]

---

## 9. Acciones comunes

- **Confirmar acción**: botón **A (OK)**. [file:1]  
- **Cancelar y volver a inicio**: botón **B (Atrás)**. [file:1]  
- **Moverse por listas (modo registro)**: botones **C / D**. [file:1]  
- **Reintentar lectura QR**: mejorar enfoque, evitar reflejos, buena iluminación. [file:1]  
- **Reintentar lectura pulsera**: acercarla más y no moverla hasta que cambie la pantalla. [file:1]  
- **Reiniciar dispositivo**: combinación **C + D** (reset rápido). [file:1]

---

## 10. Mensajes y estados del sistema

### Mensajes de éxito

- “Acceso permitido”. [file:1]  
- “Bienvenido” + “Entrada permitida”. [file:1]  
- “Salida registrada” + “Gracias por su visita”. [file:1]  
- “Pulsera asociada”. [file:1]

### Mensajes de error / denegación

- “Entrada denegada” (reintentar o contactar responsable). [file:1]  
- “Salida denegada” (reintentar o contactar responsable). [file:1]  
- “No hay usuarios” (lista de usuarios no disponible, avisar al responsable). [file:1]

### Estados del modo registro NFC

- “Modo registro NFC” / “Seleccione usuario”: elegir usuario con C/D. [file:1]  
- “Acerque la pulsera” / “Esperando lectura…”: acercar la pulsera al lector. [file:1]  
- “Pulsera asociada”: asociación completada, vuelta a inicio. [file:1]  
- “No hay usuarios”: sin lista disponible, vuelve a inicio automáticamente. [file:1]

---

## 11. Consejos de uso

- **Para QR**: evitar reflejos, mantener el código quieto y buena iluminación. [file:1]  
- **Para pulsera NFC**: acercarla al máximo y mantenerla inmóvil hasta cambio de pantalla. [file:1]  
- **Si algo va lento**: esperar a que vuelva a la pantalla de inicio antes de repetir. [file:1]  
- **En modo registro**: revisar bien el nombre del usuario antes de pulsar A (OK). [file:1]  
- **Si el dispositivo no responde**: hacer reset con C y luego D. [file:1]

Si los mensajes de error se repiten varias veces, se debe indicar al usuario que contacte con el responsable o soporte interno del centro. [file:1]