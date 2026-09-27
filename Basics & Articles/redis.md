# Qué es [Redis](https://en.wikipedia.org/wiki/Redis)?
**Redis** (*RE*mote *DI*ctionary *S*erver) es un almacén de datos **NoSQL en memoria** de código abierto, basado en pares **clave-valor**, que funciona como base de datos, caché de aplicaciones y broker de mensajes. Al mantener los datos en **RAM** en vez de en disco, ofrece latencia de microsegundos/milisegundos y cientos de miles de operaciones por segundo.

Creado en 2009 por Salvatore Sanfilippo y escrito en C, soporta estructuras de datos como cadenas, hashes, listas, sets, sorted sets, bitmaps, HyperLogLog, índices geoespaciales y streams. Sus usos principales son **caching** (aliviar la carga de una base de datos relacional), administración de **sesiones**, **pub/sub**, colas de mensajes, rankings y análisis en tiempo real. Incluye persistencia opcional en disco (RDB/AOF), replicación, y escalabilidad vía Redis Sentinel y Redis Cluster. Su licencia actual es dual: RSALv2 y SSPLv1.


---


**Redis** es una base de datos que trabaja principalmente **en memoria RAM**, diseñada para guardar y recuperar datos extremadamente rápido.

El nombre viene originalmente de **REmote DIctionary Server**.

La idea más sencilla es:

> **Redis = un almacén de datos muy rápido que normalmente se usa como complemento de una base de datos tradicional.**

### ¿Por qué hace falta Redis?

Imaginá una aplicación web tradicional:

```text
Usuario
   ↓
Node.js / Express
   ↓
MySQL
   ↓
Respuesta
```

Cada vez que necesitás un dato, Node consulta MySQL.

Por ejemplo:

```sql
SELECT * FROM products WHERE id = 25;
```

Esto funciona perfectamente, pero si ese dato se solicita **miles de veces**, estás haciendo miles de consultas a MySQL.

Con Redis podés hacer:

```text
Usuario
   ↓
Node.js
   ↓
Redis
   ↓
¿Está el dato?
   ├── Sí → devolverlo inmediatamente
   └── No → consultar MySQL → guardar en Redis → devolverlo
```

Esto se llama **caché**.

---

## 1. Redis como caché

Supongamos que tu aplicación tiene:

```text
GET /api/products
```

Y la consulta a MySQL tarda 50 ms.

La primera vez:

```text
Node → Redis
          ↓
        vacío
          ↓
       MySQL
          ↓
       productos
          ↓
       Redis
          ↓
       Usuario
```

Redis guarda temporalmente el resultado.

La siguiente petición:

```text
Node → Redis → productos → Usuario
```

Como Redis mantiene los datos en RAM, la respuesta puede ser muchísimo más rápida.

Podés establecer además un tiempo de expiración:

```text
productos → Redis → 60 segundos
```

Después de 60 segundos desaparece y la aplicación vuelve a consultar MySQL.

---

# 2. Redis no reemplaza necesariamente a MySQL

Esta distinción es importante.

Podrías tener:

```text
              ┌── Redis
              │
Node.js ──────┤
              │
              └── MySQL
```

Cada uno cumple una función diferente.

**MySQL:**

* datos permanentes
* usuarios
* productos
* pedidos
* facturas
* relaciones entre tablas
* transacciones

**Redis:**

* caché
* sesiones
* datos temporales
* contadores
* colas
* información que necesita acceso muy rápido

Por ejemplo:

```text
MySQL
└── Usuario #152
    ├── nombre
    ├── email
    └── dirección

Redis
└── sesión del usuario #152
    ├── userId = 152
    └── expira en 30 minutos
```

Si Redis se reinicia y perdés una sesión o una caché, normalmente no perdés el registro permanente del usuario porque ese está en MySQL.

---

# 3. Redis también puede guardar sesiones

Esto es particularmente interesante para lo que venís estudiando con **Express y `express-session`**.

Podés tener:

```text
Usuario
   ↓
POST /login
   ↓
Express
   ↓
express-session
   ↓
Redis
```

Redis almacena algo como:

```text
session:abc123
    userId: 25
    loggedIn: true
```

Y cuando el usuario hace:

```text
GET /profile
```

Express obtiene la sesión desde Redis y sabe:

```text
userId = 25
```

Esto se vuelve especialmente útil cuando tenés **varios servidores**:

```text
                    ┌── Node #1
                    │
Load Balancer ──────┼── Node #2
                    │
                    └── Node #3
                         │
                         ↓
                       Redis
```

Los tres servidores pueden acceder al mismo almacenamiento de sesiones.

---

# 4. Redis también puede funcionar como contador

Por ejemplo, visitas:

```text
views:article:123 = 1542
```

Cada visita puede hacer:

```text
INCR views:article:123
```

y Redis aumenta:

```text
1542
1543
1544
1545
...
```

Esto es muy rápido y resulta útil para:

* cantidad de visitas
* likes
* intentos de login
* límites de solicitudes
* estadísticas temporales

---

# 5. Redis y los límites de solicitudes

Por ejemplo, querés evitar que una IP haga 1 millón de peticiones:

```text
IP 200.10.20.30
↓
100 requests/minuto
```

Redis puede mantener:

```text
rate_limit:200.10.20.30 = 73
```

y aumentar ese contador con cada petición.

Después de un minuto, puede expirar.

Esto se utiliza para implementar **rate limiting**.

---

# 6. Redis también puede funcionar como cola

Otra utilización importante es:

```text
Usuario
   ↓
Node.js
   ↓
Redis Queue
   ↓
Worker
   ↓
Enviar email
```

Por ejemplo, alguien compra un producto.

En lugar de hacer que la petición HTTP espere mientras tu servidor envía el email:

```text
POST /purchase
        ↓
Guardar compra
        ↓
Enviar email
        ↓
Esperar...
        ↓
Respuesta
```

podés hacer:

```text
POST /purchase
        ↓
Guardar compra
        ↓
Agregar "enviar email" a una cola
        ↓
Respuesta inmediata
```

Y otro proceso se encarga del email.

```text
Redis Queue
     ↓
   Worker
     ↓
Email
```

Esto es muy común en arquitecturas más grandes.

---

# 7. ¿Por qué es tan rápido?

Principalmente porque trabaja en **RAM**.

Una comparación conceptual:

```text
SSD / disco
     ↓
más lento

RAM
     ↓
muchísimo más rápida
```

Pero hay una consecuencia:

> **La RAM es un recurso limitado y más caro que el almacenamiento en disco.**

Por eso no tiene mucho sentido decir:

> "Voy a guardar toda mi aplicación en Redis."

Normalmente se guarda allí aquello que necesita acceso rápido o que puede reconstruirse.

---

# 8. Redis tiene estructuras de datos interesantes

No es solamente un simple:

```text
clave → valor
```

Puede trabajar con diferentes estructuras.

Por ejemplo:

### String

```text
user:25:name → "Juan"
```

### Lista

```text
queue:emails
    ↓
[email1, email2, email3, ...]
```

### Set

Un conjunto de elementos sin duplicados:

```text
online_users
    ↓
{15, 28, 43, 72}
```

### Hash

Parecido a un pequeño objeto:

```text
user:25
    name → Juan
    age  → 30
    city → Buenos Aires
```

### Sorted Set

Elementos asociados a una puntuación:

```text
leaderboard

Juan     → 950
Pedro    → 870
Ana      → 820
```

Muy útil para rankings, puntuaciones, etc.

---

# Redis dentro de una arquitectura moderna

Si continuamos con lo que veníamos hablando de **Docker, microservicios y reverse proxy**, podrías terminar teniendo algo así:

```text
                         Internet
                            │
                            ↓
                     Reverse Proxy
                      (Nginx/Traefik)
                            │
                     ┌──────┴──────┐
                     ↓             ↓
                Frontend       Backend API
                                  │
                     ┌────────────┼────────────┐
                     ↓            ↓            ↓
                   Redis        MySQL        Servicio
                     │                         │
                     │                         ↓
                     │                       ...
                     ↓
               caché / sesiones /
               colas / contadores
```

Y Docker podría levantar cada componente:

```text
docker
├── nginx
├── node-api
├── mysql
└── redis
```

Aunque **Redis no es exclusivo de microservicios**. También podés usarlo perfectamente en una aplicación monolítica de Node/Express.

### En una frase

Si **MySQL es el archivo permanente de tu aplicación**, Redis es más parecido a una **memoria de trabajo ultrarrápida** que la aplicación utiliza para no tener que hacer determinadas operaciones una y otra vez.

Y una diferencia importante con lo que preguntabas antes sobre los proxies: **Redis no es un proxy**. Un proxy está en el medio de una comunicación entre clientes y servidores; Redis es un **servicio de almacenamiento de datos en memoria**.
