# Callbacks `request` y `response`
En el contexto de **JavaScript** y **Node.js**, los **callbacks de `request` y `response`** son funciones que se utilizan en aplicaciones web para manejar las solicitudes (requests) y las respuestas (responses) entre el cliente y el servidor. Estas funciones son fundamentales en los servidores HTTP, como los creados con el módulo `http` de Node.js o con el framework **Express.js**.

---

## **1. ¿Qué son los Callbacks en General?**

Un **callback** es una función que se pasa como argumento a otra función y que se ejecutará más tarde, ya sea de manera síncrona o asíncrona. En el caso de servidores HTTP, los callbacks permiten manejar eventos, como recibir una solicitud o enviar una respuesta, de manera estructurada.

---

## **2. Callbacks de Request y Response**

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