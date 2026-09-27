# Evolución del desplegamiento de páginas web, antes y ahora
La mejor forma de entenderlo es imaginar que tenés una aplicación web y seguir **todo el recorrido desde que alquilás el servidor hasta que un usuario entra al sitio**. La diferencia entre el modelo tradicional y el moderno no es solamente tecnológica: cambia **qué administrás vos, qué automatizás y a qué escala**.

---

# 1. El modelo tradicional: alquilar hosting y subir la página

Durante muchos años, para publicar un sitio web se hacía algo bastante parecido a esto:

```text
Tu computadora
     │
     │ FTP / SFTP / SSH
     ▼
Servidor del hosting
     │
     ├── Apache
     │
     └── /var/www/html
           │
           ├── index.html
           ├── style.css
           ├── script.js
           └── imágenes
```

Supongamos que desarrollaste una página:

```text
mi-sitio/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── app.js
└── images/
```

## Paso 1: alquilar hosting

Contratabas un servicio de hosting.

Podía ser algo como:

> "Hosting Linux — 10 GB — PHP — MySQL"

El proveedor te daba algo parecido a:

```text
Servidor
IP: xxx.xxx.xxx.xxx

Usuario: usuario123
Password: ********
```

Muchas veces **no administrabas el servidor completo**.

El proveedor ya tenía:

```text
Linux
Apache
PHP
MySQL
FTP
DNS
panel de administración
```

configurados.

---

# 2. El proveedor ya había hecho gran parte del trabajo

Esto es importante.

Cuando contratabas un **hosting compartido**, no necesariamente instalabas Apache.

El proveedor ya tenía algo parecido a:

```text
                    SERVIDOR
┌──────────────────────────────────────────┐
│ Linux                                    │
│                                          │
│ Apache                                   │
│                                          │
│ ├── Cliente A                            │
│ ├── Cliente B                            │
│ ├── Cliente C                            │
│ └── Cliente D                            │
│                                          │
└──────────────────────────────────────────┘
```

Es decir, **muchos sitios compartían el mismo servidor Apache**.

Vos simplemente recibías acceso a tu espacio.

---

# 3. Subías los archivos

Por ejemplo mediante FTP/SFTP.

Con un programa como FileZilla podías ver:

```text
LOCAL
─────────────────
mi-sitio/
 index.html
 css/
 js/
 images/


REMOTO
─────────────────
/public_html/
 index.html
 css/
 js/
 images/
```

Arrastrabas los archivos.

Eso era esencialmente el deploy.

---

# 4. ¿Qué ocurría cuando alguien entraba?

El usuario escribía:

```text
https://midominio.com
```

El proceso era:

```text
Usuario
   │
   ▼
DNS
   │
   ▼
Servidor del hosting
   │
   ▼
Apache
   │
   ▼
public_html/index.html
   │
   ▼
Navegador
```

Apache recibía:

```http
GET /
```

y buscaba:

```text
/public_html/index.html
```

Después se lo enviaba al navegador.

---

# 5. ¿Y si había PHP?

Acá empezaba a aparecer algo más interesante.

Supongamos:

```text
index.php
```

con:

```php
<?php
echo "Hola";
?>
```

Apache recibía:

```http
GET /
```

y en vez de simplemente entregar el archivo como texto, lo procesaba mediante PHP.

Conceptualmente:

```text
Navegador
    │
    ▼
Apache
    │
    ▼
PHP
    │
    ▼
HTML generado
    │
    ▼
Navegador
```

Por eso los hostings tradicionales eran muy populares para:

* WordPress
* Joomla
* Drupal
* PHP
* MySQL

---

# 6. ¿Y la base de datos?

El hosting podía darte también:

```text
MySQL
```

Entonces tenías:

```text
              INTERNET
                  │
                  ▼
               Apache
                  │
                  ▼
                PHP
                  │
                  ▼
                MySQL
```

Todo estaba bastante integrado.

Desde un panel podías crear:

```text
Base de datos: tienda
Usuario: tienda_user
Password: ********
```

Y tu aplicación PHP se conectaba.

---

# 7. El modelo tradicional con VPS

Hay otro modelo tradicional más avanzado: **alquilar un VPS**.

Acá sí tenías control del servidor.

Por ejemplo:

```text
VPS
Ubuntu
2 CPU
4 GB RAM
80 GB SSD
IP pública
```

Entrabas:

```bash
ssh root@IP
```

Y vos instalabas:

```bash
apt install apache2
```

Después:

```bash
apt install php
```

Después:

```bash
apt install mysql-server
```

Y configurabas Apache.

Por ejemplo:

```text
/etc/apache2/
├── apache2.conf
├── ports.conf
└── sites-available/
      └── mi-sitio.conf
```

---

# 8. Virtual Hosts

Apache permitía alojar varios sitios en el mismo servidor.

Por ejemplo:

```text
VPS
│
└── Apache
    │
    ├── sitio1.com
    │
    ├── sitio2.com
    │
    └── sitio3.com
```

Configurabas un **VirtualHost**.

Conceptualmente:

```apache
<VirtualHost *:80>
    ServerName sitio1.com
    DocumentRoot /var/www/sitio1
</VirtualHost>

<VirtualHost *:80>
    ServerName sitio2.com
    DocumentRoot /var/www/sitio2
</VirtualHost>
```

Apache miraba el dominio solicitado y sabía qué directorio debía servir.

---

# 9. El deploy tradicional en un VPS

Podría ser:

```text
1. Escribís código
        ↓
2. Probás localmente
        ↓
3. Te conectás por SSH
        ↓
4. Copiás archivos
        ↓
5. Configurás Apache
        ↓
6. Configurás DNS
        ↓
7. Configurás HTTPS
        ↓
8. Reiniciás Apache
        ↓
9. Sitio publicado
```

Por ejemplo:

```bash
scp -r ./mi-sitio/* usuario@vps:/var/www/mi-sitio/
```

---

# 10. El problema que aparece al crecer

Imaginemos ahora que tu aplicación deja de ser:

```text
HTML + CSS + JS
```

y pasa a ser:

```text
Frontend
+
Node.js / Express
+
MySQL
+
Redis
+
Nginx
```

El VPS empieza a tener:

```text
Ubuntu
├── Nginx
├── Node.js
├── npm
├── MySQL
├── Redis
├── Git
├── certificados
└── aplicación
```

Y después aparece otra aplicación:

```text
Ubuntu
├── Nginx
├── Node.js 22
├── Node.js 20
├── MySQL
├── Redis
├── aplicación A
└── aplicación B
```

Ahora empiezan los problemas de dependencias y configuración.

Ahí Docker resulta especialmente útil.

---

# 11. Docker cambia la unidad de despliegue

Tradicionalmente pensabas:

> "Tengo un servidor y tengo que instalar las cosas que necesita mi aplicación."

Con Docker empezás a pensar:

> "Tengo una aplicación empaquetada en una imagen que puedo ejecutar."

Por ejemplo:

```text
Aplicación
│
├── código
├── dependencias
├── configuración de runtime
└── Dockerfile
```

Construís:

```bash
docker build -t mi-app .
```

y obtenés:

```text
mi-app:latest
```

Después:

```bash
docker run mi-app
```

---

# 12. La diferencia conceptual

### Tradicional

```text
VPS
│
├── Ubuntu
├── Apache
├── PHP
├── Node
├── MySQL
└── aplicación
```

La aplicación depende directamente del entorno del VPS.

### Docker

```text
VPS
│
├── Ubuntu
│
└── Docker
     │
     ├── Container Apache
     │
     ├── Container Node
     │
     └── Container MySQL
```

Cada componente tiene un entorno más aislado.

---

# 13. Docker Compose

Ahora imaginemos que tu aplicación necesita:

```text
Frontend
Backend
MySQL
```

Podrías crear:

```text
docker-compose.yml
```

Por ejemplo conceptualmente:

```yaml
services:

  frontend:
    build: ./frontend

  backend:
    build: ./backend

  database:
    image: mysql
```

Ahora tenés declarada la arquitectura:

```text
          Docker Compose
                │
      ┌─────────┼─────────┐
      ▼         ▼         ▼
 frontend    backend    database
```

Y podés levantar todo:

```bash
docker compose up -d
```

En vez de hacer manualmente:

```bash
docker run ...
docker run ...
docker run ...
```

---

# 14. Compose es principalmente "orquestación local/simple"

Docker Compose es muy útil para:

* desarrollo;
* servidores pequeños;
* proyectos personales;
* aplicaciones pequeñas/medianas;
* entornos de staging.

Por ejemplo:

```text
VPS
│
└── Docker Compose
     │
     ├── nginx
     ├── frontend
     ├── backend
     ├── mysql
     └── redis
```

Pero todavía estás administrando **un servidor**.

---

# 15. ¿Dónde aparece Kubernetes?

Kubernetes aparece cuando la infraestructura empieza a ser mucho más grande.

Supongamos que ya no tenés:

```text
1 VPS
```

sino:

```text
Servidor 1
Servidor 2
Servidor 3
Servidor 4
Servidor 5
...
```

Y necesitás ejecutar muchas instancias de tu aplicación.

Kubernetes puede encargarse de cosas como:

* ejecutar containers;
* reiniciarlos si fallan;
* distribuirlos;
* escalar replicas;
* realizar actualizaciones;
* balancear tráfico;
* gestionar configuración;
* administrar servicios entre múltiples máquinas.

Conceptualmente:

```text
                 Kubernetes
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
    Node 1         Node 2        Node 3
       │             │             │
    ┌──────┐       ┌──────┐      ┌──────┐
    │ API  │       │ API  │      │ API  │
    └──────┘       └──────┘      └──────┘
       │             │             │
    ┌──────┐       ┌──────┐      ┌──────┐
    │ API  │       │ API  │      │ API  │
    └──────┘       └──────┘      └──────┘
```

Ahora ya no estás pensando simplemente:

> "¿En qué directorio pongo `index.html`?"

Estás pensando:

> "¿Cómo mantengo funcionando 20 instancias de mi aplicación distribuidas entre varios servidores?"

Es un problema completamente distinto.

---

# 16. Y después aparece CI/CD

Hay otra evolución importante.

Supongamos que modificás:

```javascript
app.js
```

En el modelo tradicional:

```text
Modificar código
      ↓
FTP/SSH
      ↓
Copiar archivos
      ↓
Reiniciar aplicación
```

Con CI/CD podés tener:

```text
Modificar código
      ↓
git push
      ↓
GitHub
      ↓
CI/CD
      ↓
Tests
      ↓
Build
      ↓
Docker image
      ↓
Deploy
      ↓
Producción
```

La gran diferencia es la **automatización del proceso**.

---

# 17. ¿Qué significa CI?

**CI = Continuous Integration.**

La idea básica:

> Cada vez que incorporás cambios al código, un sistema automático los verifica.

Por ejemplo:

```text
git push
   ↓
Tests
   ↓
Lint
   ↓
Build
   ↓
OK / ERROR
```

Si rompiste algo:

```text
Tests
   ↓
ERROR
   ↓
Deploy NO
```

---

# 18. ¿Qué significa CD?

Puede significar **Continuous Delivery** o **Continuous Deployment**, dependiendo del contexto.

Una vez que el código pasa las verificaciones:

```text
Código
 ↓
Tests
 ↓
Build
 ↓
Deploy
```

El sistema puede publicar automáticamente.

Por ejemplo:

```text
git push main
       ↓
GitHub Actions
       ↓
npm test
       ↓
docker build
       ↓
docker push
       ↓
VPS
       ↓
docker compose pull
       ↓
docker compose up -d
```

Entonces vos prácticamente hacés:

```bash
git push
```

y el resto ocurre automáticamente.

---

# 19. Comparación completa

Podemos visualizar las cuatro generaciones así.

## A. Hosting tradicional

```text
         INTERNET
             │
             ▼
       Hosting
             │
           Apache
             │
       public_html
             │
       index.html
```

Vos básicamente subís archivos.

**Complejidad:** baja.

**Control:** bajo.

**Automatización:** baja.

---

# 20. B. VPS tradicional

```text
             INTERNET
                 │
                 ▼
                VPS
                 │
               Linux
                 │
              Apache
                 │
        ┌────────┴────────┐
        │                 │
     sitio A           sitio B
```

Vos administrás:

* Linux;
* Apache;
* firewall;
* usuarios;
* certificados;
* actualizaciones;
* aplicaciones;
* bases de datos.

**Complejidad:** media.

**Control:** alto.

**Automatización:** normalmente manual.

---

# 21. C. VPS + Docker Compose

```text
                 INTERNET
                     │
                     ▼
                    VPS
                     │
                   Docker
                     │
              Docker Compose
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     Nginx         Node         MySQL
    container     container     container
```

Ahora empaquetás las aplicaciones.

**Complejidad:** media.

**Control:** alto.

**Reproducibilidad:** mucho mayor.

---

# 22. D. CI/CD + Docker

Ahora agregás automatización:

```text
                   Git
                    │
                    ▼
                 GitHub
                    │
                    ▼
                  CI/CD
                    │
             ┌──────┴──────┐
             ▼             ▼
           Tests          Build
                           │
                           ▼
                     Docker image
                           │
                           ▼
                         Deploy
                           │
                           ▼
                          VPS
```

Vos hacés:

```bash
git push
```

y el pipeline se ocupa del resto.

---

# 23. E. Kubernetes

Y si necesitás escalar mucho:

```text
                     INTERNET
                         │
                         ▼
                    Kubernetes
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       Node 1          Node 2          Node 3
          │              │              │
       containers      containers      containers
```

Ahora Kubernetes puede gestionar:

```text
replicas
scaling
networking
health checks
rolling updates
service discovery
```

etc.

---

# 24. Pero hay algo muy importante

Estas tecnologías **no forman necesariamente una escalera donde una reemplaza a la anterior**.

Podés tener:

```text
CI/CD
  │
  ▼
Docker
  │
  ▼
Docker Compose
  │
  ▼
VPS
```

O:

```text
CI/CD
  │
  ▼
Docker
  │
  ▼
Kubernetes
  │
  ▼
varios servidores
```

Y también:

```text
VPS
│
└── Apache
    └── sitio web
```

que sigue siendo perfectamente válido.

---

# 25. Un ejemplo concreto: tu aplicación Node/Express

Supongamos que desarrollás:

```text
mi-app/
├── package.json
├── src/
│   ├── server.js
│   ├── routes/
│   └── controllers/
└── views/
```

### Tradicionalmente

En el VPS:

```bash
sudo apt install nodejs
```

Después:

```bash
git clone ...
npm install
```

Y arrancás:

```bash
node src/server.js
```

Quizás usás PM2:

```bash
pm2 start src/server.js
```

Y Apache/Nginx hace **reverse proxy** (`6_proxys.md`):

```text
Internet
   ↓
Apache
   ↓
Node.js
```

---

# 26. Con Docker

Creás:

```text
Dockerfile
```

que define cómo construir la aplicación.

Entonces:

```text
Código
 ↓
Dockerfile
 ↓
Docker image
 ↓
Container
 ↓
Node.js
```

El VPS ya no necesita tener necesariamente Node.js instalado directamente para esa aplicación.

Lo tiene dentro del entorno de la imagen/container.

---

# 27. Con Compose

Si además tenés MySQL:

```text
Node.js
   │
   ▼
MySQL
```

podés declarar ambos:

```text
docker-compose.yml
```

y ejecutar:

```bash
docker compose up -d
```

Queda:

```text
VPS
│
└── Docker
    │
    ├── node-container
    │
    └── mysql-container
```

---

# 28. Con CI/CD

Después conectás GitHub:

```text
                         GitHub
                           │
                       git push
                           │
                           ▼
                       CI/CD
                           │
                    ┌──────┴──────┐
                    │             │
                  Tests          Build
                                  │
                                  ▼
                            Docker image
                                  │
                                  ▼
                                VPS
                                  │
                                  ▼
                            New container
```

Ahora publicar una nueva versión puede ser simplemente:

```bash
git push origin main
```

---

# 29. Con Kubernetes

Finalmente, si tu aplicación crece muchísimo:

```text
                    Kubernetes
                         │
              ┌──────────┼──────────┐
              │          │          │
             API        API        API
              │          │          │
             API        API        API
```

Kubernetes puede aumentar o disminuir las instancias según la configuración y las necesidades del sistema.

Pero para una pequeña aplicación personal, probablemente sería una infraestructura innecesariamente compleja.

---

# 30. Roadmap conceptual

Para alguien que está aprendiendo **HTML/CSS/JS → Node/Express → MySQL**, podría ordenarse conceptualmente así:

```text
1. HTML/CSS/JS
       ↓
2. Servidor web
   Apache / Nginx
       ↓
3. HTTP
       ↓
4. DNS
       ↓
5. VPS
       ↓
6. Node.js / Express
       ↓
7. Reverse proxy
       ↓
8. Docker
       ↓
9. Docker Compose
       ↓
10. CI/CD
       ↓
11. Kubernetes
```

No porque Kubernetes sea "el siguiente nivel obligatorio", sino porque cada paso resuelve un problema que aparece después.

---

## La evolución en una sola imagen mental

```text
                 MODELO TRADICIONAL
                 ──────────────────

 Internet
    │
    ▼
 Hosting / VPS
    │
    ▼
 Apache
    │
    ▼
 Archivos / PHP / aplicación
```

↓

```text
                 DOCKER

 Internet
    │
    ▼
 VPS
    │
    ▼
 Docker
    │
    ├── Container frontend
    ├── Container backend
    └── Container database
```

↓

```text
                 COMPOSE

 Internet
    │
    ▼
 VPS
    │
    ▼
 Docker Compose
    │
    ├── frontend
    ├── backend
    ├── database
    └── redis
```

↓

```text
                 CI/CD

 git push
    │
    ▼
 GitHub
    │
    ▼
 Tests → Build → Docker image
                    │
                    ▼
                   VPS
                    │
                    ▼
                 Deploy
```

↓

```text
                 KUBERNETES

                    INTERNET
                       │
                       ▼
                  Load Balancer
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       servidor     servidor     servidor
          │            │            │
       containers   containers   containers
```

La transición fundamental es entonces **de "yo entro al servidor y modifico cosas manualmente" hacia "describo mi infraestructura y automatizo cómo se construye, prueba y despliega"**.

Y hay una distinción especialmente importante para tu aprendizaje: **Docker y Kubernetes no son alternativas directas a Apache**. Apache/Nginx son servidores web/reverse proxies; Docker es una tecnología de empaquetado/ejecución de procesos; Compose coordina varios containers; Kubernetes coordina containers a mayor escala; y CI/CD automatiza el camino desde el código fuente hasta una versión desplegada.





---





# Explicacion secundaria / ¿Qué significa hacer deploy?

Hacer deploy consiste en tomar una aplicación que funciona en tu computadora y publicarla en un servidor para que otros usuarios puedan acceder a ella a través de Internet.

Por ejemplo:

* En desarrollo:

  * Frontend: `http://localhost:5173`
  * Backend: `http://localhost:8080`

* En producción:

  * Frontend: `https://miapp.com`
  * Backend: `https://api.miapp.com`

---

# Formas de deployar una aplicación web

## 1. Frontend y backend juntos

Es común en aplicaciones pequeñas o medianas.

### Estructura

```txt
proyecto/
├── frontend/
├── backend/
└── servidor
```

El backend sirve los archivos estáticos del frontend.

Por ejemplo con Express:

```javascript
app.use(express.static("public"));
```

Cuando el usuario entra a:

```txt
https://miapp.com
```

Express entrega el HTML, CSS y JavaScript del frontend.

Y las APIs están en:

```txt
https://miapp.com/api/productos
```

### Ventajas

* Más simple.
* Un solo servidor.
* Un solo dominio.

### Desventajas

* Menos escalable.
* Si el backend cae, también el frontend.

---

# 2. Frontend y backend separados

Es la arquitectura más común actualmente.

### Ejemplo

Frontend:

```txt
https://miapp.com
```

Backend:

```txt
https://api.miapp.com
```

o

```txt
https://backend.onrender.com
```

El frontend consume la API mediante fetch.

```javascript
fetch("https://api.miapp.com/productos")
```

### Ventajas

* Más escalable.
* Más profesional.
* Cada parte puede desplegarse independientemente.

### Desventajas

* Debes configurar CORS.
* Hay más infraestructura.

---

# Métodos sencillos para deployar

Para aprender Node.js y desarrollo web, estas son las opciones más simples.

## Frontend

### [Vercel](https://vercel.com)

Ideal para:

* React
* Next.js
* Vue
* Angular

Pasos:

1. Subir proyecto a GitHub.
2. Conectar GitHub con Vercel.
3. Deploy automático.

Cada push genera una nueva versión.

---

### [Netlify](https://www.netlify.com)

Muy parecido a Vercel.

Ideal para:

* Sitios estáticos.
* React.
* Vue.

---

## Backend

### [Render](https://render.com)

Probablemente la forma más sencilla para Node.js.

Pasos:

1. Subir backend a GitHub.
2. Conectar repositorio.
3. Elegir:

```txt
Web Service
```

4. Definir:

```txt
Build Command:
npm install

Start Command:
npm start
```

Render genera una URL:

```txt
https://mi-api.onrender.com
```

---

### [Railway](https://railway.com)

Muy simple para:

* Node.js
* PostgreSQL
* MongoDB

Automatiza gran parte de la configuración.

---

# ¿Qué se usa profesionalmente?

Depende del tamaño de la empresa.

## Opción 1: VPS

Un servidor virtual privado.

Proveedores populares:

* [DigitalOcean](https://www.digitalocean.com)
* [Hetzner](https://www.hetzner.com)
* [Linode](https://www.linode.com)

Se instala:

```txt
Linux
Node.js
Nginx
PM2
```

Arquitectura típica:

```txt
Internet
    ↓
Nginx
    ↓
Node.js
    ↓
MongoDB/PostgreSQL
```

---

## Opción 2: Docker

Muy utilizado actualmente.

Empaquetas toda la aplicación:

```txt
Aplicación
+
Node.js
+
Dependencias
+
Configuración
```

en una imagen Docker.

Luego esa imagen puede ejecutarse en cualquier servidor.

Ejemplo:

```bash
docker build -t mi-app .
docker run -p 3000:3000 mi-app
```

---

## Opción 3: Cloud Providers

Grandes empresas suelen usar:

* [Amazon Web Services (AWS)](https://aws.amazon.com)
* [Google Cloud](https://cloud.google.com)
* [Microsoft Azure](https://azure.microsoft.com)

Permiten:

* Balanceadores de carga.
* Bases de datos administradas.
* Autoescalado.
* Contenedores.
* Kubernetes.

---

## Opción 4: Kubernetes

Cuando la aplicación es muy grande.

Arquitectura típica:

```txt
Frontend
Backend
Auth Service
Payments Service
Notifications Service
```

Cada servicio corre en contenedores independientes administrados por Kubernetes.

Es habitual en empresas de gran escala, pero excesivo para proyectos personales o de estudio.

---

# ¿Qué aprender primero?

Si estás aprendiendo desarrollo fullstack con Node.js, una progresión razonable sería:

1. Deploy de frontend en Vercel.
2. Deploy de backend en Render.
3. Configurar dominio propio.
4. Aprender Nginx.
5. Aprender PM2.
6. Deploy en un VPS Linux.
7. Aprender Docker.
8. Más adelante Kubernetes y AWS.

Para proyectos de portfolio o práctica, la combinación **Vercel (frontend) + Render (backend)** suele ser la más sencilla y cercana a cómo se trabaja actualmente con aplicaciones frontend y backend separados.


---


# Que pasa con FileZilla y Apache?
Todavía se usan, pero mucho menos para desplegar aplicaciones modernas de Node.js, React o aplicaciones fullstack actuales.

## FileZilla

[FileZilla Project](https://filezilla-project.org)

FileZilla es simplemente un cliente FTP/SFTP. Su función es copiar archivos desde tu computadora a un servidor.

Antes era muy común:

```txt
Mi PC
   ↓ FTP
FileZilla
   ↓
Servidor web
```

Por ejemplo:

1. Comprabas un hosting.
2. Abrías FileZilla.
3. Te conectabas al servidor.
4. Subías los archivos HTML, CSS y JS.

### ¿Se sigue usando?

Sí, pero principalmente para:

* Sitios web estáticos.
* WordPress.
* Modificar archivos de un servidor.
* Acceder a VPS mediante SFTP.

Para aplicaciones Node.js modernas normalmente se usa:

```txt
GitHub
   ↓
Deploy automático
   ↓
Render / Railway / AWS / VPS
```

o directamente:

```bash
git push
```

y el servidor actualiza la aplicación automáticamente.

---

## Apache

[Apache HTTP Server Project](https://httpd.apache.org)

Apache sigue siendo uno de los servidores web más utilizados del mundo.

Su función es recibir peticiones HTTP y responderlas.

```txt
Internet
    ↓
Apache
    ↓
Sitio web
```

Históricamente se usaba mucho con:

```txt
Apache
+
PHP
+
MySQL
```

El famoso stack:

```txt
LAMP
Linux
Apache
MySQL
PHP
```

---

## ¿Apache sirve para Node.js?

Sí.

Por ejemplo:

```txt
Internet
    ↓
Apache
    ↓
Node.js (Express)
```

Apache puede actuar como **reverse proxy**.

Configuración conceptual:

```apache
ProxyPass / http://localhost:3000/
ProxyPassReverse / http://localhost:3000/
```

Cuando un usuario entra a:

```txt
https://miapp.com
```

Apache recibe la petición y la reenvía a tu aplicación Express.

---

## ¿Por qué hoy suele verse más Nginx que Apache?

[NGINX Open Source](https://nginx.org)

En entornos Node.js es muy común:

```txt
Internet
    ↓
Nginx
    ↓
Node.js
```

Porque Nginx suele:

* Consumir menos memoria.
* Manejar mejor muchas conexiones simultáneas.
* Tener configuraciones simples para reverse proxy.
* Ser muy popular en Docker y cloud.

Por eso muchos tutoriales modernos enseñan:

```txt
Ubuntu
+
Nginx
+
PM2
+
Node.js
```

en lugar de:

```txt
Ubuntu
+
Apache
+
Node.js
```

---

## Entonces, ¿qué debería aprender hoy?

Si tu objetivo es ser desarrollador fullstack moderno:

### Muy importante

* Git
* GitHub
* Linux
* Deploy en Render o Railway
* Variables de entorno
* Dominios y DNS

### Importante

* Nginx
* PM2
* Docker

### Útil conocer

* Apache
* FileZilla
* FTP/SFTP

Apache y FileZilla no están muertos; simplemente ya no suelen ser la primera opción para desplegar aplicaciones modernas de React, Vue, Angular, Express o NestJS. En cambio, siguen apareciendo mucho en hosting compartido, WordPress, servidores heredados y mantenimiento de infraestructura existente.



---


# Del Administrador de Sistemas al Devops
Hace 15 o 20 años la separación entre desarrolladores y administradores de sistemas era bastante clara:

### Desarrollo Web / Multiplataforma

Se encargaban de:

* Programar aplicaciones.
* Bases de datos.
* Interfaces.
* Lógica de negocio.
* Testing.

### Administración de Sistemas y Redes

Se encargaban de:

* Servidores.
* Linux.
* Windows Server.
* Redes.
* DNS.
* Firewalls.
* Backups.
* Seguridad.
* Hosting.

En aquella época era habitual que el desarrollador terminara el sistema y luego "se lo pasara" al administrador para que lo instalara en producción.

```txt
Desarrollador
     ↓
Entrega aplicación
     ↓
Administrador de Sistemas
     ↓
Instala en servidor
```

---

# ¿Quién hacía el deploy?

Originalmente, el administrador de sistemas.

Por ejemplo:

1. El desarrollador generaba un ZIP.
2. Lo enviaba al administrador.
3. El administrador lo copiaba al servidor.
4. Configuraba Apache.
5. Reiniciaba servicios.

El desarrollador muchas veces ni siquiera tenía acceso al servidor productivo.

---

# ¿Qué problema tenía ese modelo?

Generaba fricción.

El desarrollador decía:

> "En mi máquina funciona."

El administrador respondía:

> "En producción no."

Y comenzaba una discusión interminable.

Por ejemplo:

```txt
PC del desarrollador
Node 16

Servidor
Node 14
```

o

```txt
PC del desarrollador
Windows

Servidor
Linux
```

o

```txt
Falta una variable de entorno
```

---

# ¿Cuándo aparece DevOps?

El término DevOps empezó a popularizarse alrededor de 2008-2010.

La idea era unir:

```txt
DEV + OPS
```

donde:

* DEV = Development
* OPS = Operations

No nació como un puesto, sino como una filosofía.

La pregunta era:

> ¿Por qué desarrollo y operaciones trabajan como departamentos aislados?

---

# ¿Qué propone DevOps?

Que quienes desarrollan también entiendan cómo se ejecuta el software.

Y que quienes administran infraestructura entiendan las necesidades del desarrollo.

Se busca eliminar el muro entre ambos.

Antes:

```txt
DEV →→→→→ OPS
```

Ahora:

```txt
DEV ↔ OPS
```

---

# ¿Qué hace un DevOps hoy?

Dependiendo de la empresa, puede encargarse de:

### Infraestructura

* Linux
* Redes
* DNS
* Balanceadores de carga
* Seguridad

### Cloud

* [AWS](https://aws.amazon.com)
* [Google Cloud](https://cloud.google.com)
* [Microsoft Azure](https://azure.microsoft.com)

### Contenedores

* Docker
* Kubernetes

### Automatización

* CI/CD
* Pipelines
* Deploys automáticos

### Observabilidad

* Logs
* Métricas
* Monitoreo
* Alertas

---

# ¿Qué es CI/CD?

Uno de los pilares de DevOps.

Supongamos que haces:

```bash
git push origin main
```

Automáticamente ocurre:

```txt
GitHub
   ↓
Tests
   ↓
Build
   ↓
Deploy
   ↓
Producción
```

Sin que nadie copie archivos manualmente.

Herramientas comunes:

* [GitHub Actions](https://github.com/features/actions)
* [GitLab CI/CD](https://about.gitlab.com/features/continuous-integration/)
* [Jenkins](https://www.jenkins.io)

---

# ¿Y hoy quién hace el deploy?

Depende mucho del tamaño de la empresa.

### Startup pequeña

El desarrollador suele hacer todo:

```txt
Programa
+
Docker
+
Deploy
+
Base de datos
```

Un perfil cercano al "fullstack".

---

### Empresa mediana

Suele existir un equipo DevOps.

```txt
Frontend
Backend
DevOps
QA
```

El desarrollador genera el código y DevOps mantiene la plataforma.

---

### Empresa grande

Aparecen equipos especializados:

```txt
Backend
Frontend
Platform
SRE
DevOps
Cloud
Seguridad
```

Un backend puede no tener acceso directo a producción.

---

# ¿Qué es SRE?

Otro concepto importante.

SRE significa:

**Site Reliability Engineering**

Fue impulsado por [Google](https://www.google.com).

Mientras DevOps nació como una cultura, SRE es más una disciplina de ingeniería enfocada en:

* Disponibilidad.
* Rendimiento.
* Escalabilidad.
* Respuesta a incidentes.
* Automatización operativa.

Muchas empresas modernas tienen SRE donde antes hubieran tenido administradores de sistemas tradicionales.

---

# Si vienes de una tecnicatura clásica...

La evolución más o menos fue:

```txt
Administrador de Sistemas
          ↓
SysAdmin
          ↓
DevOps
          ↓
Cloud Engineer
          ↓
Platform Engineer / SRE
```

Mientras que:

```txt
Desarrollador Web
          ↓
Full Stack
          ↓
Full Stack + Docker + Cloud
```

Por eso hoy es común que un desarrollador backend sepa hacer deploy básico en Linux, configurar Nginx, usar Docker y desplegar en la nube. Hace 15 años, muchas de esas tareas habrían sido responsabilidad exclusiva del administrador de sistemas.
