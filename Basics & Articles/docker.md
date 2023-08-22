# Docker
- Tecnología que nos permite asegurarnos de que nuestra app siempre corre en el mismo entorno
- Todas las dependencias estan metidas ahi mismo, como en una sandbox. Esto evita conflictos entre versiones de nuestra aplicación con otra aplicación en la misma máquina
- Ej. En una misma computadora, podemos correr una app con PHP 7 y otra app con PHP 6. Esos contenedores funcionarán sin colisionar y sin problema
- Es muy fácil de mover nuestro contenedor y funcionará igual (clásico problema de funciona en mi máquina y en la tuya no)
- Docker corre en cualquier sistema operativo de Linux (Ubuntu, Debian, CoreOS, CentOS)

## Diferencias con una Máquina Virtual
A diferencia de una VM, en Docker sólo tenemos
- La Infraestructura (servidor)
- El Host o Sistema Operativo que corre todos los contenedores

## Dockerfiles
Docker corre una imagen, que es una copia de nuestra app con los archivos de la distro de linux

Un dockerfile es una lista de tareas para crear una imagen
```sh
# Dockerfile -> build img -> runs container
FROM ubuntu
run apt-get install apache2

CMD ["apache2"]
```