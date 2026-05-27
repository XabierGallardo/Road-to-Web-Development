# 1 / El protocolo HTTP
El **protocolo HTTP (Hypertext Transfer Protocol)** es uno de los pilares fundamentales de la comunicación en la web. Fue diseñado para transferir información en la World Wide Web, permitiendo la comunicación entre clientes (como navegadores) y servidores web. A continuación, te explico en detalle cada aspecto de este protocolo.

---

## 1. Estructura de una peticion HTTP
Estructura de Petición HTTP

La estructura de una petición HTTP se compone de varias partes:

1. **Línea de solicitud**: La primera línea de la petición, que indica el método HTTP utilizado (por ejemplo, GET, POST, PUT, DELETE, etc.), la ruta del recurso solicitado (URL) y la versión del protocolo HTTP (por ejemplo, HTTP/1.1).
	* Ejemplo: `GET /index.html HTTP/1.1`
2. **Cabeceras**: Las cabeceras se encuentran después de la línea de solicitud y proporcionan información adicional sobre la petición. Algunas cabeceras comunes son:
	* `Host`: La dirección del servidor al que se dirige la petición.
	* `User-Agent`: La información del cliente (navegador, sistema operativo, etc.).
	* `Accept-Language`: El idioma preferido por el cliente.
	* `Accept-Encoding`: El tipo de codificación o compresión que el cliente puede procesar.
	* `Connection`: Indica si la conexión debe mantenerse viva o cerrarse después de la respuesta.
3. **Cuerpo**: El cuerpo de la petición contiene los datos que se envían con la petición, como un formulario de envío o un archivo adjunto. El cuerpo es opcional y solo se utiliza con métodos como POST, PUT y PATCH.

Estructura general:
```
Línea de solicitud
Cabeceras
Cuerpo (opcional)

GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept-Language: en-US
Accept-Encoding: gzip, deflate
Connection: Keep-Alive

[Cuerpo opcional]
```
En el ejemplo anterior, la petición GET solicita el recurso `/index.html` del servidor `www.example.com`. Las cabeceras proporcionan información adicional sobre el cliente y la conexión. No hay cuerpo en este ejemplo, ya que el método GET solo devuelve información y no envía datos.

Es importante destacar que la estructura de una petición HTTP puede variar dependiendo del método utilizado y de la implementación del servidor web. Sin embargo, la estructura básica descrita anteriormente se aplica a la mayoría de las peticiones HTTP.

---

## 2. **Definición y Propósito**
HTTP es un protocolo de nivel de aplicación que sigue un modelo de solicitud-respuesta. Su principal función es facilitar la transferencia de recursos, como archivos HTML, imágenes, videos y datos estructurados, entre un cliente (generalmente un navegador) y un servidor web.

HTTP está basado en texto y es **sin estado** (stateless), lo que significa que cada solicitud es independiente y no guarda información sobre las interacciones anteriores.

---


## 3. **Estructura de una Transacción HTTP**
Una transacción HTTP consta de dos componentes principales: **la solicitud** y **la respuesta**.

### 3.1. **Solicitud HTTP**
La solicitud HTTP es el mensaje que el cliente envía al servidor para solicitar un recurso.

#### Componentes de una Solicitud:
1. **Línea de solicitud:**
   - Especifica el método HTTP, la URL del recurso y la versión del protocolo.
   - Ejemplo: `GET /index.html HTTP/1.1`

2. **Encabezados de solicitud:**
   - Contienen información adicional sobre la solicitud.
   - Ejemplo:
     ```
     Host: www.ejemplo.com
     User-Agent: Mozilla/5.0
     Accept: text/html
     ```

3. **Cuerpo de la solicitud (opcional):**
   - Incluye datos adicionales, como formularios enviados con el método POST.

#### Métodos Comunes:
- **GET:** Solicita un recurso sin modificarlo.
- **POST:** Envía datos al servidor.
- **PUT:** Carga o reemplaza un recurso.
- **DELETE:** Elimina un recurso.
- **HEAD:** Similar a GET, pero solo recupera los encabezados.
- **OPTIONS:** Describe las opciones de comunicación disponibles.

---

### 3.2. **Respuesta HTTP**
La respuesta HTTP es el mensaje que el servidor envía al cliente tras procesar la solicitud.

#### Componentes de una Respuesta:
1. **Línea de estado:**
   - Indica la versión de HTTP, un código de estado y una frase descriptiva.
   - Ejemplo: `HTTP/1.1 200 OK`

2. **Encabezados de respuesta:**
   - Proporcionan metadatos sobre la respuesta.
   - Ejemplo:
     ```
     Content-Type: text/html
     Content-Length: 348
     ```

3. **Cuerpo de la respuesta (opcional):**
   - Contiene el contenido del recurso solicitado, como HTML o JSON.

#### Códigos de Estado Comunes:
- **1xx (Informativos):** Indican que la solicitud está en curso.
  - Ejemplo: 100 Continue.
- **2xx (Éxito):** Indican que la solicitud fue exitosa.
  - Ejemplo: 200 OK.
- **3xx (Redirección):** Indican que es necesario realizar otra acción para completar la solicitud.
  - Ejemplo: 301 Moved Permanently.
- **4xx (Errores del cliente):** Indican problemas en la solicitud enviada por el cliente.
  - Ejemplo: 404 Not Found.
- **5xx (Errores del servidor):** Indican fallos en el servidor.
  - Ejemplo: 500 Internal Server Error.

---

## 4. **Características Clave**
### 4.1. **Sin Estado:**
HTTP no guarda información de las transacciones previas. Esto simplifica su diseño pero requiere el uso de cookies o sesiones para rastrear usuarios.

### 4.2. **Conexiones Persistentes:**
Desde HTTP/1.1, se permite reutilizar conexiones TCP, mejorando la eficiencia.

### 4.3. **Flexibilidad:**
Es extensible y soporta diferentes tipos de contenido, gracias al uso de encabezados como `Content-Type`.

### 4.4. **Caché:**
Soporta estrategias de almacenamiento en caché para reducir el tiempo de carga, usando encabezados como `Cache-Control` y `ETag`.

### 4.5. **Seguridad:**
- **HTTP:** Transmite datos en texto plano.
- **HTTPS (HTTP Secure):** Usa TLS/SSL para cifrar las comunicaciones, garantizando confidencialidad e integridad.

---

## 5. **Ventajas y Desventajas**
### Ventajas:
- Simple y ampliamente adoptado.
- Soporta múltiples tipos de contenido.
- Evoluciona para abordar nuevas necesidades.

### Desventajas:
- La naturaleza sin estado puede ser limitada en ciertas aplicaciones.
- HTTP/1.x puede ser ineficiente en redes lentas debido a la latencia.

---

## 6. **Casos de Uso Comunes**
- Navegación web.
- Comunicación entre aplicaciones a través de APIs RESTful.
- Transferencia de archivos multimedia.

---

## 7. **Cómo Funciona en la Práctica**
Cuando escribes una URL en tu navegador, el proceso se realiza así:
1. El navegador genera una solicitud HTTP y la envía al servidor correspondiente.
2. El servidor procesa la solicitud, recupera el recurso y envía una respuesta HTTP.
3. El navegador procesa la respuesta y muestra el contenido al usuario.

---

El protocolo HTTP es crucial para la web moderna, y aunque simple en su concepto, ha evolucionado para manejar aplicaciones complejas y demandas de alto rendimiento.


---

# 2 / Por que decimos que HTTP es un protocolo sin estado? (stateless)
Decir que **HTTP es un protocolo *sin estado* (*stateless*)** significa que **el servidor no recuerda información de las solicitudes anteriores**.
Cada vez que un cliente (como un navegador) envía una petición, esta es **independiente**, y el servidor la procesa sin saber nada del historial de ese cliente.

* Cada petición HTTP es **autónoma**.
* El servidor **no guarda memoria** de qué hiciste antes.
* Si necesitas que el servidor "recuerde" algo, debes enviar esa información **en cada petición** (cookies, tokens, sesiones, etc.).

---

## 📌 Ejemplo claro

Si un usuario hace:

1. `GET /productos`
2. Luego `GET /carrito`

El servidor **no sabe que es el mismo usuario**, a menos que el navegador envíe algo adicional como:

* una **cookie** de sesión
* un **token JWT**
* un **identificador** en la URL
* etc.

Sin esos datos, para el servidor, cada petición parece venir de un cliente distinto.

---

## 📚 ¿Por qué fue diseñado así?

Porque hacerlo sin estado lo vuelve:

* **más simple**
* **más rápido**
* **más escalable**
* **más fácil de distribuir entre múltiples servidores**

Pero implica que, para funcionalidades como login, carrito de compras, preferencias, etc., se necesite algún mecanismo externo para mantener el estado.

---

## 🎯 Resumen corto

> **HTTP es sin estado porque no almacena ninguna información entre una petición y la siguiente. Cada petición debe contener toda la información necesaria para ser procesada.**


---

# 3. Protocolos basicos para el desarrollo web
Cuando desarrollás aplicaciones web, todo el tiempo están ocurriendo intercambios de información entre distintos sistemas: navegador ↔ servidor, frontend ↔ backend, backend ↔ base de datos, microservicios entre sí, APIs externas, etc.

Los protocolos son las “reglas” que permiten que esa comunicación funcione.

Entenderlos es importante porque:

* te ayuda a debuggear errores reales,
* mejora cómo diseñás APIs,
* permite optimizar rendimiento,
* ayuda con seguridad,
* y hace que muchas herramientas “dejen de ser mágicas”.

---

# ¿Qué es un protocolo?

Un protocolo es un conjunto de reglas para que dos sistemas puedan comunicarse.

Por ejemplo:

* cómo iniciar una conexión,
* cómo enviar datos,
* cómo responder,
* cómo detectar errores,
* cómo cerrar la comunicación.

Internet funciona porque miles de protocolos trabajan juntos.

---

# TCP/IP: la base de Internet

Cuando hablamos de Internet, normalmente hablamos del conjunto de protocolos TCP/IP.

No es un único protocolo:

* IP se encarga de direccionar paquetes.
* TCP se encarga de que lleguen correctamente.

---

# ¿Qué es IP?

IP significa Internet Protocol.

Su trabajo principal es:

* identificar dispositivos,
* y mover paquetes entre redes.

Cada dispositivo tiene una dirección IP.

Ejemplo:

```txt
192.168.0.10
```

o IPv6:

```txt
2001:0db8:85a3::8a2e:0370:7334
```

IP funciona parecido al correo postal:

* necesitás una dirección origen,
* una dirección destino,
* y los datos viajan por distintos caminos.

## Problema:

IP NO garantiza:

* orden,
* entrega,
* ni integridad.

Ahí entra TCP.

---

# ¿Qué es TCP?

TCP significa Transmission Control Protocol.

TCP agrega confiabilidad.

Se asegura de:

* que los datos lleguen,
* lleguen completos,
* lleguen ordenados,
* y se reenvíen si algo falla.

---

# Cómo funciona TCP (simplificado)

## 1. Handshake (inicio de conexión)

Antes de enviar datos:

* cliente y servidor establecen conexión.

Se llama “three-way handshake”.

```txt
Cliente → SYN
Servidor → SYN-ACK
Cliente → ACK
```

Después de eso:

* ambos quedan conectados.

---

## 2. Envío de datos

TCP divide la información en paquetes.

Cada paquete:

* tiene número de secuencia,
* puede reenviarse,
* y debe confirmarse.

---

## 3. Cierre de conexión

Cuando termina:

```txt
FIN → ACK
```

La conexión se cierra correctamente.

---

# ¿Por qué TCP es importante para web?

Porque HTTP normalmente viaja sobre TCP.

La cadena real es:

```txt
HTTP → TCP → IP
```

Es decir:

* HTTP define cómo hablan navegador y servidor,
* TCP garantiza la conexión,
* IP mueve los paquetes.

---

# HTTP: el protocolo más importante del desarrollo web

HTTP significa HyperText Transfer Protocol.

Es el protocolo que usa la web.

Permite:

* pedir recursos,
* enviar datos,
* recibir respuestas.

---

# Cómo funciona HTTP

El cliente (browser/frontend) hace una request.

El servidor responde.

Ejemplo:

```txt
Cliente:
GET /productos HTTP/1.1

Servidor:
200 OK
```

---

# Request y Response

## Request

Tiene:

* método,
* URL,
* headers,
* body (a veces).

Ejemplo:

```http
POST /users HTTP/1.1
Content-Type: application/json

{
  "nombre": "Juan"
}
```

---

## Response

El servidor responde con:

* status code,
* headers,
* body.

Ejemplo:

```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1
}
```

---

# Métodos HTTP importantes

## GET

Obtiene datos.

```txt
GET /products
```

---

## POST

Crea recursos.

```txt
POST /products
```

---

## PUT

Reemplaza completamente.

---

## PATCH

Actualiza parcialmente.

---

## DELETE

Elimina recursos.

---

# Status codes importantes

## 2xx → éxito

```txt
200 OK
201 Created
204 No Content
```

---

## 3xx → redirecciones

```txt
301 Moved Permanently
302 Found
```

---

## 4xx → error del cliente

```txt
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
```

---

## 5xx → error del servidor

```txt
500 Internal Server Error
502 Bad Gateway
```

---

# Headers HTTP

Los headers agregan metadata.

Ejemplo:

```http
Content-Type: application/json
Authorization: Bearer token
Cookie: sessionId=123
```

Son fundamentales para:

* autenticación,
* CORS,
* cache,
* compresión,
* cookies,
* APIs REST.

---

# HTTP es stateless

HTTP no recuerda nada entre requests.

Cada request es independiente.

Por eso existen:

* cookies,
* sessions,
* JWT,
* tokens,
* almacenamiento en frontend.

---

# HTTPS

HTTPS = HTTP + TLS/SSL.

Agrega:

* cifrado,
* autenticación,
* seguridad.

Evita:

* robo de contraseñas,
* sniffing,
* ataques MITM.

Hoy prácticamente toda la web usa HTTPS.

---

# HTTP/1.1 vs HTTP/2 vs HTTP/3

## HTTP/1.1

* una request por conexión,
* más lento.

---

## HTTP/2

* multiplexing,
* varias requests simultáneas,
* mejor rendimiento.

---

## HTTP/3

* usa QUIC en vez de TCP,
* más rápido,
* mejor tolerancia a pérdida de paquetes.

---

# ¿Por qué entender HTTP es tan importante?

Porque TODO en web depende de HTTP.

Cuando hacés:

* fetch(),
* axios,
* APIs REST,
* autenticación,
* cookies,
* SSR,
* Next.js,
* Express,
* uploads,
* microservicios,
* GraphQL,

estás usando HTTP.

---

# Ejemplo práctico real

Cuando escribís:

```javascript
fetch("/api/users")
```

ocurre algo así:

1. El navegador resuelve DNS.
2. Obtiene IP del servidor.
3. Abre conexión TCP.
4. Negocia HTTPS/TLS.
5. Envía request HTTP.
6. El servidor responde.
7. El navegador interpreta la respuesta.

Entender eso ayuda muchísimo al debug.

---

# DNS: otro protocolo clave

DNS = Domain Name System.

Traduce dominios a IPs.

Ejemplo:

```txt
google.com → 142.250.x.x
```

Sin DNS tendrías que recordar IPs.

---

# ¿Por qué es importante DNS?

Porque muchos errores reales vienen de:

* DNS caído,
* mala configuración,
* propagación,
* problemas de hosting.

---

# TLS/SSL

TLS cifra conexiones HTTPS.

Permite:

* cifrado,
* certificados,
* autenticación.

Cuando ves el candado del navegador:

* estás usando TLS.

---

# WebSocket

HTTP normalmente funciona:

* request → response.

Pero algunas apps necesitan conexión persistente:

* chats,
* videojuegos,
* trading,
* colaboración en tiempo real.

Ahí aparece WebSocket.

Permite:

* comunicación bidireccional en tiempo real.

---

# REST

REST no es exactamente un protocolo:

* es un estilo arquitectónico sobre HTTP.

Usa:

* URLs,
* métodos HTTP,
* status codes.

Ejemplo:

```txt
GET /users
POST /users
DELETE /users/1
```

---

# GraphQL

Alternativa a REST.

Permite pedir exactamente los datos necesarios.

Muy usado en:

* APIs modernas,
* frontend complejos.

---

# SMTP, IMAP y POP3

Importantes si trabajás con emails.

## SMTP

Envía emails.

## IMAP

Lee emails manteniendo sincronización.

## POP3

Descarga emails localmente.

---

# FTP y SFTP

Transferencia de archivos.

## FTP

Viejo y poco seguro.

## SFTP

Seguro, basado en SSH.

Muchos deploys todavía usan SFTP.

---

# SSH

Muy importante para backend/devops.

Permite:

* conectarte a servidores,
* deployar apps,
* ejecutar comandos remotos.

Ejemplo:

```bash
ssh usuario@servidor
```

---

# CORS

Muy importante en frontend/backend.

El navegador restringe requests entre distintos dominios.

Ejemplo:

```txt
frontend.com → api.com
```

El servidor debe permitirlo mediante headers HTTP.

---

# Cookies y sesiones

Las cookies:

* guardan información en el navegador.

Muy usadas para:

* login,
* autenticación,
* sesiones.

Headers involucrados:

```http
Set-Cookie
Cookie
```

---

# JWT

JSON Web Token.

Muy usado para autenticación moderna.

El backend genera un token:

```txt
header.payload.signature
```

El frontend lo envía en:

```http
Authorization: Bearer token
```

---

# Protocolos y capas

Todo esto trabaja en capas.

Modelo simplificado:

```txt
Aplicación → HTTP, DNS, SMTP
Transporte → TCP, UDP
Internet → IP
Red física → WiFi, Ethernet
```

---

# ¿Qué protocolos debería dominar un fullstack?

## Fundamentales

* HTTP/HTTPS
* TCP/IP
* DNS
* TLS/SSL

## Muy importantes

* WebSocket
* SSH
* REST
* GraphQL

## Dependiendo del trabajo

* SMTP
* SFTP
* OAuth
* gRPC

---

# ¿Qué cambia cuando entendés esto?

Dejás de ver:

```javascript
fetch("/api")
```

como “magia”.

Y empezás a entender:

* qué viaja,
* cómo viaja,
* por qué falla,
* dónde optimizar,
* y cómo asegurar la aplicación.

Ese conocimiento marca bastante diferencia entre:

* usar herramientas,
* y realmente comprender cómo funciona la web.
