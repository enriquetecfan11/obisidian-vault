---
type: "resource"
tags:
  - docker
  - contenedores
  - devops
  - infraestructura
  - linux
project: "none"
status: "pendiente"
date_created: "2026-03-01"
date_modified: "2026-03-01"
related: [] # Array vacío o con [[links]]
---

| Acción                         | Comando                                                     |
| ------------------------------ | ----------------------------------------------------------- |
| Parar y eliminar contenedores  | `docker stop $(docker ps -q) && docker rm $(docker ps -aq)` |
| Eliminar volúmenes             | `docker volume rm $(docker volume ls -q)`                   |
| Eliminar imágenes              | `docker rmi $(docker images -q)`                            |
| Eliminar redes                 | `docker network rm $(docker network ls -q)`                 |
| Limpiar todo                   | `docker system prune -a --volumes -f`                       |
| Reiniciar Docker               | `docker restart id-contendor`                               |
| Reinciar todos los contendores | `docker restart $(docker ps -q)`                            |
|                                |                                                             |
## Contendores Útiles

Para monitorizar los routers de la zona → [https://hub.docker.com/r/techantidote/aircrack](https://hub.docker.com/r/techantidote/aircrack)

## Paginas con tutoriales

¿Que es docker? y comandos → [https://ciberninjas.com/que-es-docker/](https://ciberninjas.com/que-es-docker/)

## Para poder buscar una imagen en docker

1. docker login con sudo
2. sudo docker search [nombre de la imagen]

## Para poder descargarte una imagen y entrar en ella

1. docker pull kalilinux/kali-rolling
2. docker run --name kali_linux --net="host" --privileged -e DISPLAY=$DISPLAY -it -v /tmp/.X11-unix:/tmp/.X11-unix kalilinux/kali-rolling /bin/bash
3. docker exec -i -t [Container ID] /bin/bash

## Comandos Útiles

Para eliminar los contendores que se estan ejecutando → docker image prune

Para listar contenendores → docker ps -a

Para ejecutar Alpine → docker run -it --rm alpine /bin/ash

Docker Container run bakcground → docker container run -it -d [nombre maquina] /bin/sh -platform linux/arm/v7

Eliminar todo lo que no se usa → docker system prune

## En Parrot de docker ejecutar

1. apt-get update && apt-cache search kali-linux
2. apt-get install kali-tools-top10 // para las herramientas
3. apt-get install net-tools && apt-get install iputils-ping // ifconfig

## Interfaz gráfica Portainer

1. Poner este comando

***sudo docker run -d -p 8000:8000 -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce***

1.  En el navegador

 https://ip:9000/

## Para poder instalar WordPress en docker

docker run -e MYSQL_ROOT_PASSWORD=mondejar -e MYSQL_DATABASE=wordpress --name wordpressdb -v "$PWD/database":/var/lib/mysql -d mariadb:latest

docker run -e WORDPRESS_DB_USER=root -e WORDPRESS_DB_PASSWORD=mondejar --name wordpress --link wordpressdb:mysql -p 80:80 -v "$PWD/html":/var/www/html -d wordpress

## Node + PostgreSQL

[https://codewithhugo.com/node-postgres-express-docker-compose/](https://codewithhugo.com/node-postgres-express-docker-compose/)