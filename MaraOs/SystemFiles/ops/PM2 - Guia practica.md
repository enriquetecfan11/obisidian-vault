# PM2 - Guia practica

Fecha: 12-06-2026
Tags: #nodejs #pm2 #produccion #servidores #ops

## Para que sirve

PM2 es un gestor de procesos para aplicaciones Node.js. Sirve para ejecutar apps en servidores, mantenerlas vivas, reiniciarlas si fallan, consultar logs, monitorizar consumo y restaurarlas automaticamente despues de un reinicio del sistema.

Usarlo cuando una app Node.js deba quedar corriendo en produccion, staging, VPS, hosting con SSH/cPanel o cualquier servidor donde no baste con lanzar `node app.js` manualmente.

## Instalacion

Instalacion global:

```bash
npm install pm2 -g
```

Comprobar version:

```bash
pm2 -v
```

## Arrancar una aplicacion

Desde el directorio de la app:

```bash
pm2 start app.js
```

Con nombre explicito:

```bash
pm2 start app.js --name mi-app
```

Con variables de entorno inline:

```bash
NODE_ENV=production PORT=3000 pm2 start app.js --name mi-app
```

Para apps con `npm start`, suele ser mejor:

```bash
pm2 start npm --name mi-app -- start
```

## Ver procesos activos

```bash
pm2 list
```

La tabla muestra datos importantes:

- `id`: identificador numerico para acciones rapidas.
- `name`: nombre del proceso.
- `mode`: modo de ejecucion, normalmente `fork` o `cluster`.
- `pid`: proceso del sistema.
- `uptime`: tiempo activo.
- `status`: `online`, `stopped`, `errored`, etc.
- `cpu` y `mem`: consumo actual.
- `restarts`: numero de reinicios.

## Gestion diaria

```bash
pm2 stop mi-app
pm2 restart mi-app
pm2 reload mi-app
pm2 delete mi-app
```

Tambien se puede usar el `id`:

```bash
pm2 restart 0
```

Acciones sobre todo:

```bash
pm2 restart all
pm2 reload all
pm2 stop all
```

`restart` reinicia el proceso. `reload` intenta recargar con menos interrupcion, especialmente util en apps preparadas para ello o en modo cluster.

## Logs

Ver logs en directo:

```bash
pm2 logs
```

Ver logs de una app concreta:

```bash
pm2 logs mi-app
```

Formatos utiles:

```bash
pm2 logs --json
pm2 logs --format
```

Limpiar logs:

```bash
pm2 flush
```

Recargar archivos de logs:

```bash
pm2 reloadLogs
```

PM2 separa normalmente dos tipos de log:

- `nombre-error.log`: errores de la aplicacion.
- `nombre-out.log`: salida normal, `console.log`, mensajes de arranque, etc.

Ubicacion habitual:

```bash
~/.pm2/logs/
```

## Monitorizacion

Panel interactivo en terminal:

```bash
pm2 monit
```

Informacion detallada de una app:

```bash
pm2 show mi-app
```

Informacion del sistema PM2:

```bash
pm2 report
```

## Persistencia tras reinicio del servidor

PM2 no queda automaticamente restaurado tras reiniciar el servidor si no se configura el startup.

Generar script de arranque:

```bash
pm2 startup
```

PM2 suele devolver un comando con `sudo`. Hay que copiarlo y ejecutarlo exactamente como lo muestra.

Guardar la lista actual de procesos:

```bash
pm2 save
```

Flujo recomendado tras desplegar o cambiar procesos:

```bash
pm2 list
pm2 save
```

Eliminar startup si ya no se quiere autoinicio:

```bash
pm2 unstartup
```

## Debug de una app con PM2

Cuando una app falla en PM2, no empieces reiniciando a ciegas. Flujo recomendado:

1. Revisar logs:

```bash
pm2 logs mi-app
```

2. Ver estado e id:

```bash
pm2 list
```

3. Parar temporalmente la app:

```bash
pm2 stop mi-app
```

4. Ejecutarla manualmente fuera de PM2:

```bash
node app.js
```

Si la app arranca con npm:

```bash
npm start
```

Esto suele mostrar errores mas directos: stack traces, variables de entorno faltantes, errores de sintaxis, puertos ocupados, permisos, dependencias rotas o problemas de conexion.

5. Corregir el problema.

6. Volver a levantar con PM2:

```bash
pm2 start app.js --name mi-app
```

O si ya existia:

```bash
pm2 restart mi-app
```

7. Confirmar estado:

```bash
pm2 list
pm2 logs mi-app
```

8. Si el cambio debe sobrevivir a reinicios:

```bash
pm2 save
```

## Despliegue rapido recomendado

Para una app Node.js simple:

```bash
cd /ruta/de/la/app
npm install --production
NODE_ENV=production pm2 start app.js --name mi-app
pm2 list
pm2 logs mi-app
pm2 save
```

Si es la primera vez en ese servidor:

```bash
pm2 startup
```

Despues ejecutar el comando con `sudo` que PM2 indique y terminar con:

```bash
pm2 save
```

## Comandos de chuleta

```bash
pm2 start app.js --name mi-app
pm2 start npm --name mi-app -- start
pm2 list
pm2 monit
pm2 logs
pm2 logs mi-app
pm2 show mi-app
pm2 restart mi-app
pm2 reload mi-app
pm2 stop mi-app
pm2 delete mi-app
pm2 flush
pm2 startup
pm2 save
pm2 unstartup
```

## Problemas comunes

### La app aparece como `errored`

Revisar:

```bash
pm2 logs mi-app
pm2 show mi-app
```

Despues probar fuera de PM2:

```bash
node app.js
```

### La app funciona manualmente pero no con PM2

Posibles causas:

- Variables de entorno no cargadas.
- Directorio de trabajo incorrecto.
- Ruta relativa mal resuelta.
- Usuario distinto al esperado.
- Puerto ocupado.
- Dependencias no instaladas en el entorno correcto.

### El servidor reinicio y la app no volvio

Revisar si se hizo:

```bash
pm2 startup
pm2 save
```

Si no, configurar startup y guardar la lista actual.

### Hay demasiados logs

Limpiar:

```bash
pm2 flush
```

Para produccion real, valorar rotacion de logs con `pm2-logrotate`.

## Buenas practicas

- Usar nombres claros con `--name`.
- Revisar `pm2 list` despues de cada cambio.
- Usar `pm2 logs mi-app` antes de reiniciar sin diagnostico.
- Ejecutar la app manualmente cuando el error no sea claro.
- Hacer `pm2 save` despues de cambios que deban persistir.
- Documentar ruta de la app, puerto, usuario del sistema y comando de arranque.
- No depender solo de PM2 para seguridad, backups, firewall o observabilidad.

## Referencias

- WNPower Help: [Como hacer debug de aplicaciones que corren en PM2](https://help.wnpower.com/hc/es/articles/6791777427981-C%C3%B3mo-hacer-debug-de-aplicaciones-que-corren-en-PM2)
- DEV Community: [Utilizando PM2 (Basico)](https://dev.to/migpsi/utilizando-pm2-basico-110b)

