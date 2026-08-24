---
title: tornos-de-acceso-acceso-al-terminal-de-tornos-por-ip
type: nota
tags:
  - work
  - origen
project: none
status: active
date_created: 2026-08-13
date_modified: 2026-08-23
---
> NOTA: Este procedimiento asume que el terminal de tornos expone una interfaz web o de administración accesible por IP. Adapta IP, puerto y credenciales a tu entorno.

---

## 1. Datos necesarios

Antes de acceder al terminal por IP, asegúrate de tener:
- **Dirección IP del terminal** (por ejemplo: `192.168.1.50`).  
- **Puerto de acceso**, si no es el 80 o 443 (por ejemplo: `8080`).  
- **Tipo de acceso**:
  - Interfaz web (HTTP/HTTPS).
  - SSH o similar (solo para personal técnico).  
- **Usuario y contraseña** de acceso, según tu rol.  
Pide estos datos a sistemas/IT o al responsable del sistema de tornos.

---

## 2. Comprobar conectividad con el terminal

Desde un equipo conectado a la misma red:
1. Abre una **terminal** o **símbolo del sistema**.  
2. Ejecuta un ping básico (si está permitido):

   ```bash
   ping 192.168.1.50
   ```

3. Si recibes respuesta, hay conectividad IP básica.  
4. Si no hay respuesta, revisa:
   - Que estés en la **misma red/VLAN**.
   - Que no haya **cortafuegos** bloqueando el tráfico.
   - Que el terminal esté **encendido** (comprueba también que se puede usar físicamente con QR/pulsera). [file:1]

---

## 3. Acceso por navegador web (HTTP/HTTPS)

Si el terminal expone una **web de gestión**:

1. Abre tu navegador (Chrome, Firefox, etc.).  
2. En la barra de direcciones, escribe:

   - Para HTTP:  
     `http://192.168.1.50`  
   - Para HTTP con puerto específico:  
     `http://192.168.1.50:8080`  
   - Para HTTPS:  
     `https://192.168.1.50`  

3. Pulsa Enter y espera a que cargue la página.  
4. Si aparece una advertencia de certificado (en HTTPS), confirma con el responsable si puedes continuar.  

---

## 4. Inicio de sesión en la interfaz

Una vez cargada la página del terminal:

1. Introduce tu **usuario** y **contraseña** facilitados por sistemas.  
2. Haz clic en **Iniciar sesión** / **Login**.  
3. Si las credenciales son correctas, accederás al panel de administración correspondiente a tu rol (solo lectura, operador, admin, etc.).  

Si falla el login:
- Verifica mayúsculas/minúsculas.  
- Comprueba si tu cuenta tiene permisos de acceso remoto.  
- Contacta con el responsable para resetear credenciales o permisos.

---

## 5. Operaciones habituales (ejemplos)

Dependiendo de cómo esté implementado el sistema, desde la interfaz por IP podrías:
- Ver el **estado** del terminal (online, errores, logs básicos).  
- Consultar **eventos de acceso** (lecturas de QR y pulseras). [file:1]  
- Forzar un **reinicio remoto** del dispositivo (equivalente al reset con C + D en el propio terminal). [file:1]  
- Gestionar usuarios y asociaciones de pulseras (si esa parte no está delegada a otra aplicación central). [file:1]

Documenta aquí, con capturas y pasos, las acciones reales que se hagan desde la interfaz una vez la tengas definida.

---

## 6. Acceso por terminal (SSH) – Solo personal técnico

Si el acceso es por **SSH**:

1. Abre una terminal en tu equipo.  
2. Ejecuta:

   ```bash
   ssh usuario@192.168.1.50
   ```

   O, si usa un puerto no estándar:

   ```bash
   ssh -p 2222 usuario@192.168.1.50
   ```

3. Introduce la **contraseña** cuando te la pida.  
4. Una vez dentro, sigue los procedimientos internos (por ejemplo, ver logs, reiniciar servicios, actualizar software, etc.).

> Importante: No modifiques configuraciones críticas sin seguir el procedimiento interno documentado. Cambios erróneos pueden dejar el torno inaccesible tanto por IP como físicamente.

---

## 7. Problemas frecuentes y soluciones

- **No carga la web**:
  - Comprueba IP, puerto y conexión de red.
  - Prueba otro navegador.
  - Verifica si hay un firewall bloqueando.  

- **No puedo hacer ping**:
  - Puede estar bloqueado ICMP.
  - Verifica que el terminal esté encendido y operativo físicamente. [file:1]  
  - Consulta a redes/sistemas.  

- **Credenciales incorrectas**:
  - Revisa teclado (bloq mayús, idioma).
  - Solicita reset de contraseña.  

- **Cambios no aplican al terminal**:
  - Puede requerir un **reinicio del servicio** o del propio dispositivo.
  - Coordínalo con sistemas para no interrumpir el uso con QR/pulsera. [file:1]

---

## 8. Buenas prácticas

- Usa siempre **HTTPS** cuando esté disponible.  
- No compartas tus **credenciales** con terceros.  
- Registra en la documentación interna cualquier cambio relevante que hagas en la configuración.  
- Si el terminal no responde ni físicamente (QR/pulsera) ni por IP, aplica el **reset físico** (C y luego D) y vuelve a probar. [file:1]