# ¿Qué significa hacer deploy?

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
