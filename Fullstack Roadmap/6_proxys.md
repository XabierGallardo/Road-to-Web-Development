# Reverse proxy 
Un **reverse proxy** es un servidor que se coloca **delante de tus aplicaciones** y recibe las peticiones de Internet para después decidir **a qué aplicación interna enviarlas**.

Es uno de esos conceptos que parece complicado hasta que ves el recorrido.

---

# 1. Primero: ¿qué es un proxy?

Un **proxy** es, en términos generales, un intermediario.

Por ejemplo:

```text
Cliente
   │
   ▼
 Proxy
   │
   ▼
Servidor
```

El cliente no se comunica directamente con el servidor final. El proxy recibe la petición y la reenvía.

Un **reverse proxy** hace algo parecido, pero está pensado desde el punto de vista del servidor:

```text
                    INTERNET
                       │
                       ▼
                Reverse Proxy
                       │
              ┌────────┼────────┐
              ▼        ▼        ▼
             App 1    App 2    App 3
```

---

# 2. Un ejemplo muy sencillo

Supongamos que tenés tres aplicaciones en tu VPS:

```text
VPS
│
├── Landing → puerto 3000
├── API     → puerto 3001
└── Panel   → puerto 3002
```

Sin reverse proxy, podrías acceder mediante:

```text
http://IP:3000
http://IP:3001
http://IP:3002
```

Pero eso no es muy cómodo.

Queremos:

```text
https://midominio.com
https://api.midominio.com
https://admin.midominio.com
```

Entonces ponemos un reverse proxy delante:

```text
                         INTERNET
                            │
                            ▼
                    ┌──────────────┐
                    │ Nginx        │
                    │ Reverse Proxy│
                    └───────┬──────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
          :3000           :3001         :3002
        Landing            API           Panel
```

---

# 3. ¿Qué hace Nginx?

Nginx recibe:

```http
GET /
Host: midominio.com
```

y dice:

> "Esta petición es para `midominio.com`, así que la mando a la aplicación que está en `localhost:3000`."

Entonces:

```text
Navegador
    │
    │ https://midominio.com
    ▼
  Nginx
    │
    │ http://localhost:3000
    ▼
 Landing
```

El navegador **no sabe necesariamente que existe el puerto 3000**.

Para él:

```text
https://midominio.com
```

es el sitio.

---

# 4. Otro ejemplo: una API Node/Express

Supongamos que tu aplicación Express escucha:

```javascript
app.listen(3000);
```

Eso significa:

```text
Node.js
   │
   └── localhost:3000
```

Podrías tener Nginx delante:

```text
Internet
    │
    │ https://midominio.com
    ▼
  Nginx
    │
    │ http://localhost:3000
    ▼
Node/Express
```

Nginx recibe la petición y la **proxyfica** hacia Node.

Por ejemplo:

```text
GET /api/products
```

llega a Nginx:

```text
Nginx
  │
  ▼
http://localhost:3000/api/products
  │
  ▼
Express
```

---

# 5. ¿Por qué no conectar directamente el usuario con Node?

Podrías hacerlo.

Por ejemplo:

```text
Internet
   │
   ▼
Node.js :3000
```

Para una aplicación pequeña puede funcionar perfectamente.

Pero Nginx puede encargarse de muchas tareas que no necesariamente querés que maneje directamente tu aplicación Node.

Por ejemplo:

* HTTPS/TLS;
* certificados;
* redirecciones;
* múltiples dominios;
* servir archivos estáticos;
* compresión;
* límites de tamaño;
* balanceo de carga;
* caching;
* routing;
* headers;
* protección básica frente a determinadas solicitudes.

Entonces tenés:

```text
Internet
   │
   ▼
Nginx
   │
   ▼
Node.js
```

---

# 6. HTTPS es una de las razones más importantes

Supongamos que tu Node/Express escucha:

```text
HTTP :3000
```

Podés hacer:

```text
                   HTTPS
Internet ─────────────────────► Nginx
                                  │
                                  │ HTTP
                                  ▼
                               Node.js
```

Nginx se encarga de la conexión HTTPS externa.

Node puede trabajar internamente mediante HTTP.

Esto se conoce como **TLS termination**.

Por ejemplo:

```text
Internet
https://midominio.com
       │
       ▼
     Nginx
     HTTPS
       │
       │ HTTP interno
       ▼
 Node :3000
```

---

# 7. Reverse proxy con Docker

Esto conecta directamente con lo que veníamos hablando.

Podrías tener:

```text
                    INTERNET
                       │
                       ▼
                Nginx container
                Reverse Proxy
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
       frontend container    API container
             │                   │
          Nginx              Node.js
```

Por ejemplo:

```text
Docker
│
├── nginx
│
├── frontend
│
└── backend
```

Nginx podría recibir:

```text
midominio.com
```

y enviarlo a:

```text
frontend
```

mientras:

```text
api.midominio.com
```

va hacia:

```text
backend
```

---

# 8. Incluso podés hacerlo por rutas

No necesitás necesariamente distintos subdominios.

Podrías tener:

```text
https://midominio.com/
```

→ frontend

y:

```text
https://midominio.com/api/
```

→ backend.

Visualmente:

```text
                         Nginx
                           │
              ┌────────────┴────────────┐
              │                         │
       /                           /api/*
              │                         │
              ▼                         ▼
        Frontend                    Backend
```

Por ejemplo:

```text
GET /
```

va a:

```text
frontend
```

pero:

```text
GET /api/products
```

va a:

```text
backend
```

---

# 9. ¿Por qué se llama "reverse"?

Esta parte es más conceptual.

Un **forward proxy** suele representar al **cliente**:

```text
Cliente
   │
   ▼
Forward Proxy
   │
   ▼
Internet
   │
   ▼
Servidor
```

Por ejemplo, una empresa podría tener un proxy para que sus empleados accedan a Internet.

El proxy actúa en nombre del cliente.

En un **reverse proxy**:

```text
Cliente
   │
   ▼
Internet
   │
   ▼
Reverse Proxy
   │
   ▼
Servidor/aplicación
```

El reverse proxy está del lado de los servidores y actúa como puerta de entrada a ellos.

---

# 10. Un ejemplo con tus aplicaciones

Imaginemos que tenés:

```text
Frontend
HTML/CSS/JS

Backend
Node/Express

Database
MySQL
```

Podrías tener:

```text
                         INTERNET
                             │
                             ▼
                     ┌──────────────┐
                     │    Nginx     │
                     │ reverse proxy│
                     └───────┬──────┘
                             │
                   ┌─────────┴──────────┐
                   │                    │
                   ▼                    ▼
             Frontend                Backend
              :80                     :3000
                                        │
                                        ▼
                                      MySQL
                                      :3306
```

Y algo importante:

**MySQL no debería estar expuesto públicamente simplemente porque el backend necesita utilizarlo.**

El backend puede acceder a MySQL por la red interna:

```text
Backend ─────► MySQL
```

mientras que Internet solamente llega a:

```text
Internet ─────► Nginx
```

---

# 11. Esto es muy común con Docker Compose

Por ejemplo:

```text
docker-compose.yml

services:

  nginx:
    ...

  frontend:
    ...

  backend:
    ...

  mysql:
    ...
```

La red interna podría ser:

```text
Docker network
│
├── nginx
├── frontend
├── backend
└── mysql
```

Nginx puede comunicarse con:

```text
http://frontend
```

y:

```text
http://backend:3000
```

sin que necesariamente esos servicios tengan que estar publicados directamente a Internet.

---

# 12. Reverse proxy también permite balancear carga

Acá se vuelve todavía más interesante.

Supongamos que tenés tres instancias de tu API:

```text
API 1
API 2
API 3
```

Nginx puede recibir:

```text
                  Nginx
                    │
             ┌──────┼──────┐
             ▼      ▼      ▼
           API 1  API 2  API 3
```

Y distribuir las solicitudes:

```text
Request 1 → API 1
Request 2 → API 2
Request 3 → API 3
Request 4 → API 1
...
```

Esto es **load balancing**.

---

# 13. Reverse proxy + microservicios

Ahora se conecta con tu pregunta anterior.

Supongamos:

```text
users-service
products-service
orders-service
payments-service
```

Podrías tener:

```text
                         INTERNET
                            │
                            ▼
                      Reverse Proxy
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
          users          products         orders
          service         service         service
                                             │
                                             ▼
                                          payments
```

El reverse proxy puede actuar como una especie de **puerta de entrada**.

Sin embargo, no necesariamente todas las comunicaciones internas entre microservicios pasan por el reverse proxy público. Muchas veces los servicios se comunican directamente por la red interna, o mediante un API gateway/service mesh según la arquitectura.

---

# 14. Reverse proxy vs API Gateway

Son conceptos relacionados pero no idénticos.

Un reverse proxy básico puede hacer:

```text
/api → backend
```

Un **API Gateway** suele añadir lógica específica para APIs, como:

* autenticación;
* autorización;
* rate limiting;
* routing;
* transformación de requests;
* versionado;
* métricas.

Podrías tener:

```text
Internet
    │
    ▼
API Gateway
    │
    ├── users
    ├── products
    ├── orders
    └── payments
```

Un API Gateway puede implementarse usando tecnologías que también funcionan como reverse proxies.

---

# 15. Una analogía

Imaginá un edificio de oficinas.

```text
                    CALLE
                      │
                      ▼
                RECEPCIÓN
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Oficina A   Oficina B   Oficina C
```

La persona que llega no necesita conocer todos los detalles del edificio.

Le dice a recepción:

> "Vengo a ver a Productos."

Recepción sabe:

> "Productos está en la oficina B."

Y lo dirige allí.

El **reverse proxy es parecido a esa recepción**.

---

# 16. Lo que realmente conviene recordar

Cuando veas:

```text
Internet
   ↓
Nginx
   ↓
Node.js
```

pensá:

> **Nginx está recibiendo las peticiones externas y actuando como intermediario hacia Node.**

Cuando veas:

```text
Internet
   ↓
Nginx
   ├──→ frontend
   └──→ backend
```

pensá:

> **Nginx está haciendo routing.**

Cuando veas:

```text
Internet
   ↓
Nginx
   ├──→ API 1
   ├──→ API 2
   └──→ API 3
```

pensá:

> **Nginx puede estar funcionando además como balanceador de carga.**

Y cuando veas:

```text
Internet
   ↓
Nginx
   ↓
Docker
   ├── frontend
   ├── backend
   └── ...
```

pensá:

> **Nginx es la puerta de entrada; Docker proporciona los entornos donde viven las aplicaciones.**

Esa separación es clave: **Nginx no es Docker, Docker no es un reverse proxy y Node/Express tampoco es un reverse proxy**. Son piezas distintas que pueden trabajar juntas.



---



# EXTRA / Captive Portal, Proxies y Redis
La página de login del Wi-Fi de una facultad suele formar parte de un sistema llamado **captive portal (portal cautivo)**. Puede utilizar un proxy, pero **el portal cautivo y el proxy no son exactamente lo mismo**.

Y Redis es otra cosa: es un **almacén de datos en memoria**, muy utilizado como caché, almacenamiento temporal, sesiones, colas y otros usos.

Vamos por partes.

---

# 1. El Wi-Fi de la facultad

Imaginá que te conectás a:

```text
Wi-Fi Facultad
      │
      ▼
   tu PC
```

Intentás entrar a:

```text
https://google.com
```

pero en lugar de Google aparece:

```text
┌──────────────────────────────┐
│                              │
│      Universidad             │
│                              │
│ Usuario: [____________]      │
│ Password: [____________]     │
│                              │
│          ENTRAR              │
│                              │
└──────────────────────────────┘
```

Eso normalmente es un **portal cautivo**.

---

# 2. ¿Qué hace un portal cautivo?

La idea es:

> "Estás conectado a nuestra red, pero todavía no estás autorizado a salir libremente a Internet."

El flujo puede ser:

```text
Tu computadora
      │
      ▼
Wi-Fi Facultad
      │
      ▼
Sistema de autenticación
      │
      ├── ¿Usuario autenticado?
      │
      │ NO
      ▼
Portal de login
```

Después de autenticarte:

```text
Usuario
   │
   ▼
Login correcto
   │
   ▼
Red autorizada
   │
   ▼
Internet
```

---

# 3. ¿Es un proxy?

**Puede haber un proxy involucrado, pero no necesariamente.**

Un proxy tradicional funciona así:

```text
Tu PC
  │
  ▼
Proxy
  │
  ▼
Internet
```

El proxy recibe las solicitudes y las reenvía.

Por ejemplo:

```text
Tu navegador
     │
     │ GET https://ejemplo.com
     ▼
Proxy de la universidad
     │
     ▼
ejemplo.com
```

La universidad podría utilizar el proxy para:

* controlar acceso;
* registrar tráfico;
* aplicar políticas;
* filtrar sitios;
* autenticar usuarios;
* almacenar caché;
* etc.

Pero el hecho de que aparezca una página de login **no significa automáticamente que estés utilizando un proxy**.

---

# 4. Portal cautivo vs proxy

Esta diferencia te va a servir mucho.

### Portal cautivo

Su función principal es:

> **"Antes de darte acceso a Internet, autenticá o aceptá las condiciones."**

```text
Wi-Fi
  ↓
Portal de login
  ↓
Internet
```

### Proxy

Su función principal es:

> **"Las comunicaciones hacia Internet pasan a través de mí."**

```text
Cliente
  ↓
Proxy
  ↓
Internet
```

Podrían utilizarse conjuntamente:

```text
             Facultad
                 │
        ┌────────┴────────┐
        │                 │
 Portal cautivo        Proxy
        │                 │
        └────────┬────────┘
                 ▼
              Internet
```

---

# 5. ¿Y qué tiene que ver esto con el reverse proxy?

Acá se vuelve interesante porque son conceptos relacionados.

### Proxy normal / forward proxy

Está del lado del **cliente**:

```text
TU PC
  │
  ▼
FORWARD PROXY
  │
  ▼
INTERNET
  │
  ▼
SERVIDOR
```

El proxy representa al cliente.

---

### Reverse proxy

Está del lado del **servidor**:

```text
TU PC
  │
  ▼
INTERNET
  │
  ▼
REVERSE PROXY
  │
  ▼
APLICACIÓN
```

El reverse proxy representa/protege a los servidores.

Una forma de recordarlo:

```text
Forward proxy:

CLIENTE → PROXY → INTERNET


Reverse proxy:

CLIENTE → INTERNET → PROXY → SERVIDOR
```

---

# 6. Ahora: ¿qué es Redis?

Redis es completamente diferente.

**Redis es un sistema de almacenamiento de datos en memoria.**

Su nombre originalmente viene de:

> **REmote DIctionary Server**

Es muy rápido porque normalmente mantiene los datos principalmente en **RAM**.

Podés imaginarlo como una especie de diccionario gigantesco:

```text
clave → valor
```

Por ejemplo:

```text
usuario:123 → "Juan"
```

o:

```text
session:abc123 → datos de la sesión
```

---

# 7. Redis comparado con MySQL

Esto es importante para entender por qué existen ambos.

### MySQL

Pensalo como una base de datos tradicional:

```text
MySQL
│
├── users
├── products
├── orders
└── payments
```

Está pensado para almacenar información de forma persistente y estructurada.

Por ejemplo:

```text
users

id | name  | email
---|-------|----------------
1  | Juan  | juan@email.com
2  | Ana   | ana@email.com
```

---

### Redis

Redis se parece más a:

```text
Redis
│
├── "user:1"       → ...
├── "session:abc"  → ...
├── "cart:123"     → ...
└── "counter"      → 42
```

Su fortaleza está en acceder rápidamente a datos pequeños o estructuras que necesitan mucha velocidad.

---

# 8. Un ejemplo muy sencillo

Supongamos que tu aplicación tiene:

```http
GET /products/123
```

Tu backend podría hacer:

```text
Usuario
   │
   ▼
Node/Express
   │
   ▼
Redis
```

Si Redis ya tiene:

```text
product:123 → { ... }
```

el backend puede devolverlo rápidamente.

Si no:

```text
Node
 │
 ▼
Redis
 │
 └── "no lo tengo"
       │
       ▼
     MySQL
       │
       ▼
     producto
       │
       ▼
     Redis
       │
       ▼
     Usuario
```

Esto se llama **caching**.

---

# 9. ¿Por qué Redis puede ser útil como caché?

Supongamos que tenés:

```text
MySQL
```

y una consulta tarda:

```text
50 ms
```

Pero esa misma información se solicita:

```text
100.000 veces
```

No necesariamente querés consultar MySQL 100.000 veces.

Podés hacer:

```text
             ┌── Redis ──► respuesta rápida
             │
Usuario → API
             │
             └── MySQL ──► solamente si Redis no tiene el dato
```

La idea:

```text
Primera petición:
API → Redis → no está
          ↓
        MySQL
          ↓
        Redis
          ↓
        Usuario

Siguientes peticiones:

API → Redis → dato
             ↓
           Usuario
```

---

# 10. Redis también puede almacenar sesiones

Esto conecta directamente con algo que venís estudiando en Express.

Supongamos:

```javascript
req.session.user = {
    id: 123
};
```

La sesión podría almacenarse en Redis.

Entonces:

```text
Usuario
   │
   │ Cookie
   ▼
Node/Express
   │
   ▼
Redis
   │
   └── session:abc123
```

Redis puede contener algo como:

```text
session:abc123
        ↓
{
   userId: 123,
   role: "admin"
}
```

---

# 11. ¿Por qué no guardar la sesión simplemente en Node?

Porque imaginá que tenés tres instancias de tu backend:

```text
              Load Balancer
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
        Node 1   Node 2   Node 3
```

Si Node 1 guarda las sesiones solamente en su memoria:

```text
Node 1
└── session ABC
```

el usuario podría hacer otra petición y terminar en Node 2:

```text
Usuario
   │
   ▼
Load Balancer
   │
   ▼
Node 2
   │
   └── "No conozco esa sesión"
```

Redis permite tener un almacenamiento compartido:

```text
              Load Balancer
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
        Node 1   Node 2   Node 3
          │        │        │
          └────────┼────────┘
                   ▼
                 Redis
```

Todos pueden consultar las mismas sesiones.

---

# 12. Redis también puede funcionar como cola

Por ejemplo, tu aplicación necesita enviar 50.000 emails.

En lugar de hacer:

```text
Usuario
  ↓
API
  ↓
Enviar email
  ↓
esperar
  ↓
respuesta
```

podés hacer:

```text
Usuario
  ↓
API
  ↓
Redis / cola
  ↓
"Email pendiente"
```

La API responde rápidamente.

Después un worker procesa:

```text
Redis
  │
  ▼
Worker
  │
  ▼
Servidor de email
```

Por ejemplo:

```text
API
 │
 ▼
Redis Queue
 │
 ├── email 1
 ├── email 2
 ├── email 3
 └── email 4
       │
       ▼
    Worker
       │
       ▼
     Email
```

---

# 13. Redis tiene más estructuras que un simple "diccionario"

Una de las cosas interesantes de Redis es que proporciona estructuras de datos.

Por ejemplo:

### Strings

```text
name → "Juan"
```

### Lists

```text
queue → [job1, job2, job3]
```

### Sets

```text
online_users → {123, 456, 789}
```

### Sorted sets

Muy útiles para rankings:

```text
ranking
Juan → 1500
Ana  → 1200
Luis → 1000
```

También existen hashes, streams y otras estructuras.

---

# 14. ¿Redis reemplaza a MySQL?

Normalmente **no**.

Una arquitectura podría ser:

```text
              Node.js
                 │
        ┌────────┴────────┐
        ▼                 ▼
      Redis              MySQL
   datos rápidos       datos persistentes
```

Cada uno cumple funciones diferentes.

Una analogía:

**MySQL** sería tu archivo permanente.

**Redis** sería una mesa de trabajo donde tenés a mano las cosas que necesitás constantemente.

No querés guardar absolutamente todo en la mesa de trabajo, pero tampoco querés ir al archivo cada cinco segundos.

---

# 15. Y ahora podemos juntar todos los conceptos que venimos viendo

Una aplicación moderna podría tener:

```text
                         INTERNET
                            │
                            ▼
                     Reverse Proxy
                         Nginx
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
             Frontend                API
                                      │
                           ┌──────────┼──────────┐
                           ▼          ▼          ▼
                        Redis       MySQL      Worker
```

Y todo esto podría ejecutarse en Docker:

```text
VPS
│
└── Docker Compose
     │
     ├── nginx
     ├── frontend
     ├── backend
     ├── redis
     ├── mysql
     └── worker
```

Si el sistema creciera mucho:

```text
VPS 1 ──┐
VPS 2 ──┼── Kubernetes
VPS 3 ──┘
```

Y CI/CD podría encargarse de desplegar nuevas versiones:

```text
git push
   ↓
CI/CD
   ↓
tests
   ↓
Docker build
   ↓
deploy
   ↓
Kubernetes
```

Así que ya podés empezar a ver cómo encajan las piezas:

Y **Redis es probablemente el siguiente concepto que te conviene estudiar después de entender HTTP, Node/Express, bases de datos y Docker**, porque aparece constantemente cuando empezás a trabajar con sesiones distribuidas, caché, colas y aplicaciones que necesitan escalar.