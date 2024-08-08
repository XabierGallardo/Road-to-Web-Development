# [Express.js](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Introduction)
Express es el framework backend más popular para Node.js
Está diseñado para construir SPAs y desarrollar aplicaciones backend con Node.js. Entre sus características destacan:

1. **Flexibilidad y personalización**: Express.js es un framework minimalista que permite una gran flexibilidad y personalización para adaptarse a cada proyecto.

2. **Rendimiento**: Express.js tiene una gran rapidez, rendimiento y capacidad para manejar un gran número de solicitudes simultáneas.

3. **Simplicidad**: La API de Express.js es sencilla y fácil de aprender.

4. **Soporte para Middleware**: Express.js admite el uso de middleware, lo que permite agregar funcionalidades adicionales a la aplicación como *autenticación, autorización, manejo de errores, etc.*

5. **Rutas y controladores**: Express.js proporciona un sistema de rutas y controladores que facilita la roganización y el manejo de solicitudes HTTP.

6. **Integración con BBDD**: Express se puede integrar fácilmente con MongoDB, MySQL, PostgreSQL, etc

7. **Seguridad**: Express.js proporciona características de seguridad como manejo de CORS, protección contra ataques CSRF, etc

## Ejemplo básico de un servidor con Express.js
```sh
# Instalar Express.js
npm install express
```

```js
const express = require('express');
const app = express();
const port = 3200;

// Defining a route for index page
app.get('/', (req, res) => {
	res.send('Hola mundo con Express!');
});

// Starting server
app.listen(port, () => {
	console.log(`Servidor escuchando peticiones en http://localhost:${port}`);
});

// Al navegar a http://127.0.0.1:3200/ la pagina nos devuelve:
// Hola mundo con Express!
```

## Cómo funciona Express.js
Express.js utiliza el modelo cliente-servidor para aceptar las peticiones de los usuarios y devolver las respuestas al cliente.

1. Cuando un usuario envía una petición desde su navegador escribiendo la dirección de un sitio web, el navegador envía una petición HTTP a la aplicación cliente servidor.

2. El servidor recibirá la petición a través de una de sus rutas y la procesará utilizando el controlador que coincida con la ruta solicitada.

3. Tras el procesamiento, el servidor enviará una respuesta al cliente utilizando HTTP, la respuesta al cliente puede ser un texto, una página HTML o datos JSON que los desarrolladores del frontend manejarán para mostrar la información en la página web.