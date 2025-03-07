# **Los objetos `req` y `res` en Express.js**  

En Express.js, `req` (request) y `res` (response) son dos objetos fundamentales que representan la **solicitud del cliente** y la **respuesta del servidor** respectivamente. Estos objetos permiten gestionar la comunicación entre el cliente y el servidor dentro de una aplicación web.

---

## **1. ¿Qué es `req` (Request)?**  
El objeto `req` representa la solicitud HTTP que realiza un cliente al servidor. Contiene información clave como:  
- **Método HTTP usado** (`GET`, `POST`, `PUT`, `DELETE`, etc.).  
- **Cabeceras de la solicitud**.  
- **Parámetros en la URL**.  
- **Datos enviados en el cuerpo de la solicitud (body)**.  
- **Cookies y autenticación**.  

### **Ejemplo de uso de `req`**
```javascript
app.get('/usuario/:id', (req, res) => {
    console.log(req.method);       // "GET"
    console.log(req.params.id);    // ID de usuario en la URL
    console.log(req.query.role);   // Parámetro de consulta en la URL
    console.log(req.headers);      // Cabeceras de la solicitud
    res.send('Solicitud recibida');
});
```

### **Propiedades principales de `req`**
| Propiedad | Descripción | Ejemplo |
|-----------|------------|---------|
| `req.params` | Obtiene los parámetros en la URL. | `/usuario/:id → req.params.id` |
| `req.query` | Obtiene los parámetros en la URL después de `?`. | `/usuario?id=5 → req.query.id` |
| `req.body` | Obtiene los datos enviados en el cuerpo de la solicitud (POST/PUT). | `req.body.nombre` |
| `req.headers` | Contiene las cabeceras HTTP enviadas por el cliente. | `req.headers['user-agent']` |
| `req.method` | Indica el método HTTP utilizado. | `"GET", "POST", "PUT", "DELETE"` |
| `req.url` | Obtiene la URL solicitada. | `/usuario/10?role=admin` |

---

## **2. ¿Qué es `res` (Response)?**  
El objeto `res` representa la **respuesta HTTP** que el servidor enviará de vuelta al cliente. Permite:  
- Enviar datos como **JSON, HTML o texto**.  
- Configurar el código de estado HTTP (`200`, `404`, `500`, etc.).  
- Redirigir a otras páginas.  
- Enviar cabeceras personalizadas.  

### **Ejemplo de uso de `res`**
```javascript
app.get('/usuario/:id', (req, res) => {
    const usuarioId = req.params.id;
    
    if (!usuarioId) {
        return res.status(400).send('ID de usuario requerido');
    }
    
    res.status(200).json({ id: usuarioId, nombre: 'Juan Pérez' });
});
```

### **Métodos principales de `res`**
| Método | Descripción | Ejemplo |
|--------|------------|---------|
| `res.send()` | Envía una respuesta en formato texto o HTML. | `res.send('Hola Mundo')` |
| `res.json()` | Envía una respuesta en formato JSON. | `res.json({ mensaje: 'OK' })` |
| `res.status()` | Establece el código de estado HTTP. | `res.status(404).send('No encontrado')` |
| `res.redirect()` | Redirige a otra URL. | `res.redirect('/login')` |
| `res.setHeader()` | Establece una cabecera HTTP personalizada. | `res.setHeader('Content-Type', 'application/json')` |

---

## **3. Ejemplo Completo en Express.js**
```javascript
const express = require('express');
const app = express();

app.use(express.json()); // Middleware para parsear JSON en req.body

app.post('/login', (req, res) => {
    const { username, password } = req.body;

    if (username === 'admin' && password === '1234') {
        res.status(200).json({ mensaje: 'Login exitoso' });
    } else {
        res.status(401).send('Credenciales incorrectas');
    }
});

app.listen(3000, () => console.log('Servidor en http://localhost:3000'));
```
🔹 **Explicación**:  
- Se recibe una solicitud `POST` con `username` y `password` en `req.body`.  
- Si las credenciales son correctas, se envía un **código 200** con un mensaje JSON.  
- Si son incorrectas, se envía un **código 401 (No autorizado)**.

---

## **Conclusión**
- `req` contiene **los datos que el cliente envía** al servidor.  
- `res` se usa para **devolver una respuesta** al cliente.  
- Ambos objetos permiten manejar la comunicación entre el cliente y el servidor en Express.js. 🚀

---

# Callbacks `request` y `response`
En el contexto de **JavaScript** y **Node.js**, los **callbacks de `request` y `response`** son funciones que se utilizan en aplicaciones web para manejar las solicitudes (requests) y las respuestas (responses) entre el cliente y el servidor. Estas funciones son fundamentales en los servidores HTTP, como los creados con el módulo `http` de Node.js o con el framework **Express.js**.


---


# **Los objetos `req` y `res` en Express.js**  
En **JavaScript Vanilla** (JavaScript puro, sin frameworks como Express.js), no existen directamente los objetos `req` y `res` como en Express. Sin embargo, podemos trabajar con objetos equivalentes en el contexto de **solicitudes y respuestas HTTP** usando la API de **Fetch** o la API de **XMLHttpRequest**.

---

## **1. ¿Cómo se manejan las solicitudes HTTP en JavaScript Vanilla?**
Cuando una página web necesita enviar o recibir datos de un servidor, utiliza funciones como `fetch()` para hacer peticiones HTTP. En este contexto:

- **El objeto `req` (request)** equivale a la solicitud que enviamos al servidor.
- **El objeto `res` (response)** equivale a la respuesta que el servidor devuelve.

### **Ejemplo de una solicitud HTTP con `fetch()`**
```javascript
fetch('https://jsonplaceholder.typicode.com/users/1')
    .then(response => response.json()) // Convierte la respuesta en JSON
    .then(data => console.log(data))   // Muestra los datos en consola
    .catch(error => console.error('Error en la solicitud:', error));
```
🔹 **Explicación**:  
1. `fetch()` envía una solicitud HTTP `GET` a la URL.  
2. `response.json()` convierte la respuesta en un objeto JSON.  
3. Se imprimen los datos en la consola.  
4. Si hay un error, se captura en el `catch()`.  

---

## **2. ¿Qué es `Request` en JavaScript Vanilla?**
El objeto `Request` en la API Fetch representa la solicitud HTTP que se enviará al servidor.

### **Ejemplo de creación de un objeto `Request`**
```javascript
const request = new Request('https://jsonplaceholder.typicode.com/users', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: 'Juan', email: 'juan@email.com' })
});

fetch(request)
    .then(response => response.json())
    .then(data => console.log('Usuario creado:', data))
    .catch(error => console.error('Error:', error));
```
🔹 **Explicación**:  
- Creamos un objeto `Request` con la URL, método `POST`, cabeceras y un `body` con datos en JSON.  
- Luego usamos `fetch(request)` para enviar la solicitud.  

### **Propiedades principales de `Request`**
| Propiedad | Descripción |
|-----------|------------|
| `request.url` | URL de la solicitud. |
| `request.method` | Método HTTP (`GET`, `POST`, etc.). |
| `request.headers` | Cabeceras de la solicitud. |
| `request.body` | Cuerpo de la solicitud (para `POST` y `PUT`). |

---

## **3. ¿Qué es `Response` en JavaScript Vanilla?**
El objeto `Response` en Fetch representa la respuesta HTTP recibida del servidor.

### **Ejemplo de uso del objeto `Response`**
```javascript
fetch('https://jsonplaceholder.typicode.com/users/1')
    .then(response => {
        console.log(response.status);  // Código de estado HTTP
        console.log(response.ok);      // `true` si el estado es 200-299
        return response.json();
    })
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
```

### **Propiedades principales de `Response`**
| Propiedad | Descripción |
|-----------|------------|
| `response.status` | Código de estado HTTP (ej. 200, 404, 500). |
| `response.ok` | `true` si el código de estado es 200-299. |
| `response.headers` | Cabeceras de la respuesta. |
| `response.json()` | Convierte la respuesta en JSON. |
| `response.text()` | Convierte la respuesta en texto. |

---

## **4. Comparación entre JavaScript Vanilla y Express.js**
| Característica | JavaScript Vanilla (`fetch()`) | Express.js (`req`, `res`) |
|--------------|---------------------------------|--------------------------|
| Manejo de solicitudes | `fetch()` para hacer solicitudes al servidor. | `req` representa la solicitud entrante del cliente. |
| Manejo de respuestas | `Response` representa la respuesta del servidor. | `res` se usa para enviar respuestas al cliente. |
| Servidor necesario | No, solo realiza peticiones a servidores existentes. | Sí, Express.js maneja solicitudes y respuestas en el servidor. |

---

## **5. Ejemplo completo de cliente-servidor en JavaScript Vanilla + Express.js**
**Cliente (JavaScript en el navegador)**:
```javascript
fetch('http://localhost:3000/users')
    .then(response => response.json())
    .then(data => console.log('Usuarios:', data))
    .catch(error => console.error('Error:', error));
```

**Servidor (Express.js en Node.js)**:
```javascript
const express = require('express');
const app = express();

app.get('/users', (req, res) => {
    res.json([{ id: 1, name: 'Juan' }, { id: 2, name: 'Ana' }]);
});

app.listen(3000, () => console.log('Servidor en http://localhost:3000'));
```

---

## **Conclusión**
- En **JavaScript Vanilla**, `fetch()` gestiona las solicitudes y respuestas HTTP, usando `Request` y `Response`.
- En **Express.js**, `req` y `res` manejan las solicitudes y respuestas del lado del servidor.
- Ambos permiten la comunicación entre cliente y servidor en aplicaciones web. 🚀


---


# **1. ¿Qué son los Callbacks en General?**

Un **callback** es una función que se pasa como argumento a otra función y que se ejecutará más tarde, ya sea de manera síncrona o asíncrona. En el caso de servidores HTTP, los callbacks permiten manejar eventos, como recibir una solicitud o enviar una respuesta, de manera estructurada.

---

## **2. Callbacks de Request y Response**
`req` y `res` son objetos de solicitud y respuesta

### **Request (req):**
El objeto `request` contiene toda la información sobre la solicitud que el cliente envió al servidor. Esto incluye:
- Método HTTP (`GET`, `POST`, `PUT`, `DELETE`, etc.).
- Encabezados de la solicitud (headers).
- Parámetros de consulta (query params).
- Cuerpo de la solicitud (en métodos como `POST` o `PUT`).
- URL solicitada.

### **Response (res):**
El objeto `response` se utiliza para enviar la respuesta del servidor al cliente. Permite:
- Especificar el estado HTTP (`200`, `404`, `500`, etc.).
- Enviar datos al cliente (texto, JSON, HTML, etc.).
- Configurar encabezados de respuesta.

### **Callback entre `req` y `res`:**
El callback es la función que se ejecuta cada vez que el servidor recibe una solicitud. Esta función recibe los objetos `req` y `res` como parámetros, lo que permite procesar la solicitud y enviar una respuesta.

---

## **3. Ejemplo Básico con el Módulo `http` de Node.js**

En Node.js, se utiliza el módulo `http` para crear un servidor básico. Aquí, el callback maneja el flujo entre `request` y `response`.

### **Código:**
```javascript
const http = require('http');

// Crear el servidor
const server = http.createServer((req, res) => {
    // Manejar la solicitud (request)
    console.log(`Método: ${req.method}`); // Método HTTP
    console.log(`URL solicitada: ${req.url}`); // URL de la solicitud

    // Configurar y enviar la respuesta
    res.statusCode = 200; // Código de estado
    res.setHeader('Content-Type', 'text/plain'); // Encabezado de respuesta
    res.end('Hola desde Node.js'); // Enviar respuesta
});

// Iniciar el servidor
server.listen(3000, () => {
    console.log('Servidor ejecutándose en http://localhost:3000');
});
```

### **Explicación:**
1. El método `http.createServer` recibe un **callback** con los objetos `req` y `res`.
2. `req` contiene información sobre la solicitud entrante:
   - Método HTTP (`GET`, `POST`, etc.).
   - URL solicitada.
3. `res` se utiliza para enviar una respuesta:
   - Se establece el código de estado (`statusCode`).
   - Se configuran los encabezados.
   - Se envía el cuerpo de la respuesta con `res.end()`.

---

## **4. Uso en Express.js**

Express.js, un framework para Node.js, simplifica la gestión de solicitudes y respuestas. El callback de cada ruta recibe `req` y `res`.

### **Código con Express:**
```javascript
const express = require('express');
const app = express();

// Ruta de ejemplo
app.get('/', (req, res) => {
    console.log('Solicitud recibida en /');
    console.log(`Encabezados: ${JSON.stringify(req.headers)}`); // Headers
    console.log(`Método: ${req.method}`); // Método HTTP

    // Enviar respuesta
    res.status(200).send('Hola desde Express!');
});

// Iniciar el servidor
app.listen(3000, () => {
    console.log('Servidor ejecutándose en http://localhost:3000');
});
```

### **Explicación:**
1. `app.get('/', callback)` define una ruta para solicitudes `GET` a `/`.
2. El callback maneja la solicitud (`req`) y construye la respuesta (`res`).
3. `req.headers` proporciona los encabezados de la solicitud.
4. `res.status(200).send()` establece el código de estado y envía un mensaje al cliente.

---

## **5. Desglose de las Funcionalidades de `req` y `res`**

### **5.1. Propiedades del Objeto `req`:**
| **Propiedad**         | **Descripción**                                                | **Ejemplo**                                   |
|------------------------|---------------------------------------------------------------|-----------------------------------------------|
| `req.method`          | Método HTTP de la solicitud.                                  | `GET`, `POST`, etc.                           |
| `req.url`             | URL solicitada.                                               | `/ruta/ejemplo`                               |
| `req.headers`         | Encabezados HTTP enviados por el cliente.                     | `{ "host": "localhost:3000", ... }`           |
| `req.query`           | Parámetros de consulta (query string) en la URL (Express.js). | `{ name: "Juan" }` para `/ruta?name=Juan`.    |
| `req.body`            | Cuerpo de la solicitud (necesita middleware en Express.js).   | `{ "nombre": "Juan" }` en un `POST`.          |

---

### **5.2. Métodos del Objeto `res`:**
| **Método**             | **Descripción**                                                | **Ejemplo**                                   |
|-------------------------|---------------------------------------------------------------|-----------------------------------------------|
| `res.status(code)`     | Establece el código de estado HTTP.                           | `res.status(404)`                             |
| `res.setHeader(key, value)` | Configura un encabezado HTTP.                            | `res.setHeader('Content-Type', 'application/json')` |
| `res.send(data)`       | Envía una respuesta al cliente.                              | `res.send('Hola!')`                           |
| `res.json(data)`       | Envía una respuesta en formato JSON.                         | `res.json({ mensaje: 'Hola!' })`             |
| `res.end()`            | Finaliza la respuesta.                                       | `res.end('Adiós')`                            |

---

## **6. Ejemplo Avanzado: Manejo de Métodos HTTP**

```javascript
const http = require('http');

const server = http.createServer((req, res) => {
    if (req.method === 'GET') {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Solicitud GET recibida');
    } else if (req.method === 'POST') {
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString(); // Acumula los datos del cuerpo
        });
        req.on('end', () => {
            res.statusCode = 200;
            res.setHeader('Content-Type', 'application/json');
            res.end(JSON.stringify({ mensaje: 'Datos recibidos', datos: body }));
        });
    } else {
        res.statusCode = 405; // Método no permitido
        res.end('Método no permitido');
    }
});

server.listen(3000, () => {
    console.log('Servidor ejecutándose en http://localhost:3000');
});
```

---

## **7. Conclusión**

Los callbacks de `request` y `response` son fundamentales en Node.js y JavaScript para manejar el flujo de datos en aplicaciones web. A través de estos objetos, puedes:
- Analizar las solicitudes enviadas por el cliente (`req`).
- Construir respuestas personalizadas y enviar datos al cliente (`res`).

Su correcta comprensión es clave para el desarrollo de aplicaciones web eficientes y bien estructuradas.