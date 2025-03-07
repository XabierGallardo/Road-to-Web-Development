# Node.js & Express.js
# Basics
## `package.json`
El `package.json` es un archivo esencial en proyectos de **Node.js** y **JavaScript** que almacena metadatos sobre el proyecto, sus dependencias y scripts. Es clave para gestionar paquetes y automatizar tareas.

### **¿Qué contiene?**
Algunas de las secciones más comunes en un `package.json` son:

1. **Metadatos del proyecto**  
   - `"name"`: Nombre del proyecto.  
   - `"version"`: Versión del proyecto.  
   - `"description"`: Descripción breve.  
   - `"author"`: Nombre del creador.  
   - `"license"`: Licencia del proyecto.  

2. **Dependencias**  
   - `"dependencies"`: Librerías necesarias para que la aplicación funcione.  
   - `"devDependencies"`: Librerías necesarias solo para desarrollo (como herramientas de prueba o compilación).  
   
   Ejemplo:
   ```json
   "dependencies": {
     "express": "^4.18.2"
   },
   "devDependencies": {
     "nodemon": "^3.0.2"
   }
   ```

3. **Scripts**  
   Son comandos que se pueden ejecutar con `npm run nombre-del-script`.  
   
   Ejemplo:
   ```json
   "scripts": {
     "start": "node index.js",
     "dev": "nodemon index.js"
   }
   ```

4. **Configuraciones adicionales**  
   Puede incluir opciones como:  
   - `"main"`: El archivo de entrada principal del proyecto.  
   - `"engines"`: Versiones de Node.js requeridas.  
   - `"keywords"`: Palabras clave para facilitar la búsqueda del paquete.  

### **¿Cómo se genera?**  
Puedes crear un `package.json` con el siguiente comando en la terminal:  
```sh
npm init
```
o si quieres generarlo rápidamente con valores predeterminados:  
```sh
npm init -y
```

---

## ///////////////////

---


## Que es Node.js?
Node es un entorno de ejecución de JavaScript que permite ejecutar JavaScript en el servidor.

Si bien el navegador es un entorno de ejecución limitado y controlado para ejecutar JavaScript, Node.js nos permite construir apps del lado del servidor y herramientas de desarrollo. Entre sus características destacan

1. Node.js está construido sobre el rapidísimo **motor V8 de Google Chrome**, que compila JS a código máquina nativo, por lo que la ejecución es muy rápida

2. Node.js utiliza un **modelo I/O asíncrono y no bloqueante**, por lo que las operaciones de entrada y salida (leer archivos, consultar BBDD, etc) no detienen la ejecución dle programa y por tanto permite manejar muchas operaciones concurrentes eficientemnete

3. Node.js utiliza una **arquitectura de eventos**, cuando una operación asíncrona se completa, se emite un evento con una función callback asociada, lo que permite construír apps escalables que manejen muchas conexiones concurrentes

4. Node.js trabaja con NPM, Node Package Manager, el gestor de paquetes más grande del mundo para JavaScript. NPM permite instalar, compartir y gestionar dependencias de código de manera sencilla.


## Ejemplo básico de un servidor con Node.js
```js
// nodeServer.js
const http = require('http');
const hostname = '127.0.0.1';
const port = 3100;

const server = http.createServer((req, res) => {
	res.statusCode = 200;
	res.setHeader('Content-Type', 'text/plain');
	res.end('Hola mundo desde Node.js!');
});

server.listen(port, hostname, () => {
	console.log(`Servidor corriendo en http://${hostname}:${port}/`);
});

// Al navegar a http://127.0.0.1:3100/ la pagina nos devuelve:
// Hola mundo desde Node.js!
```

## Ejemplo básico de un servidor con el framework Express.js
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

---

## Modulos en Node.js
En **Node.js**, los módulos son bloques de código reutilizables que encapsulan funcionalidades específicas. Node.js proporciona un sistema de módulos para importar y exportar funcionalidades entre archivos. Este sistema permite organizar proyectos, dividir la lógica en partes más manejables y promover la reutilización del código.

### **1. Sistemas de Módulos en Node.js**
Node.js soporta dos sistemas de módulos principales:

1. **CommonJS (CJS):** Es el sistema de módulos predeterminado de Node.js.
2. **ECMAScript Modules (ESM):** Introducido oficialmente en la especificación ES6, soportado en Node.js a partir de la versión 12 (estable desde la 14).

Ambos sistemas tienen diferencias clave en sintaxis y comportamiento. A continuación, se explican detalladamente cada uno.

---

## **2. CommonJS (CJS)**

El sistema de módulos **CommonJS** usa las funciones `require()` para importar y `module.exports` o `exports` para exportar.

### **2.1 Exportar Módulos con CommonJS**

1. **Exportación de una única funcionalidad:**
   ```javascript
   // archivo: math.js
   function sumar(a, b) {
       return a + b;
   }

   module.exports = sumar;
   ```

2. **Exportación de múltiples funcionalidades (objeto):**
   ```javascript
   // archivo: math.js
   function sumar(a, b) {
       return a + b;
   }

   function restar(a, b) {
       return a - b;
   }

   module.exports = {
       sumar,
       restar
   };
   ```

3. **Exportación incremental con `exports`:**
   ```javascript
   // archivo: math.js
   exports.sumar = (a, b) => a + b;
   exports.restar = (a, b) => a - b;
   ```

---

### **2.2 Importar Módulos con CommonJS**

1. **Importar una funcionalidad única:**
   ```javascript
   // archivo: app.js
   const sumar = require('./math');

   console.log(sumar(5, 3)); // 8
   ```

2. **Importar múltiples funcionalidades:**
   ```javascript
   // archivo: app.js
   const { sumar, restar } = require('./math');

   console.log(sumar(5, 3)); // 8
   console.log(restar(5, 3)); // 2
   ```

3. **Importar un módulo completo:**
   ```javascript
   // archivo: app.js
   const math = require('./math');

   console.log(math.sumar(5, 3)); // 8
   console.log(math.restar(5, 3)); // 2
   ```

---

## **3. ECMAScript Modules (ESM)**

El sistema **ECMAScript Modules** usa las palabras clave `import` y `export`.

### **3.1 Exportar Módulos con ESM**

1. **Exportación nombrada:**
   ```javascript
   // archivo: math.js
   export function sumar(a, b) {
       return a + b;
   }

   export function restar(a, b) {
       return a - b;
   }
   ```

2. **Exportación por defecto:**
   ```javascript
   // archivo: math.js
   export default function multiplicar(a, b) {
       return a * b;
   }
   ```

3. **Exportación combinada:**
   ```javascript
   // archivo: math.js
   export function sumar(a, b) {
       return a + b;
   }

   export function restar(a, b) {
       return a - b;
   }

   export default function multiplicar(a, b) {
       return a * b;
   }
   ```

---

### **3.2 Importar Módulos con ESM**

1. **Importación de exportaciones nombradas:**
   ```javascript
   // archivo: app.js
   import { sumar, restar } from './math.js';

   console.log(sumar(5, 3)); // 8
   console.log(restar(5, 3)); // 2
   ```

2. **Importación de exportación por defecto:**
   ```javascript
   // archivo: app.js
   import multiplicar from './math.js';

   console.log(multiplicar(5, 3)); // 15
   ```

3. **Importación combinada:**
   ```javascript
   // archivo: app.js
   import multiplicar, { sumar, restar } from './math.js';

   console.log(sumar(5, 3)); // 8
   console.log(restar(5, 3)); // 2
   console.log(multiplicar(5, 3)); // 15
   ```

4. **Importar todo como un objeto:**
   ```javascript
   // archivo: app.js
   import * as math from './math.js';

   console.log(math.sumar(5, 3)); // 8
   console.log(math.restar(5, 3)); // 2
   console.log(math.default(5, 3)); // 15
   ```

---

## **4. Configuración de ESM o CommonJS en Node.js**

### **4.1. CommonJS**
Es el sistema predeterminado en Node.js. No requiere configuración adicional.

### **4.2. ECMAScript Modules**
Para usar ESM en Node.js, necesitas una configuración específica:

1. **Activar ESM mediante el archivo `package.json`:**
   ```json
   {
     "type": "module"
   }
   ```

2. **Usar la extensión `.mjs`:**
   Archivos con esta extensión son tratados como módulos ESM sin necesidad de modificar el `package.json`.

---

## **5. Diferencias entre CommonJS y ESM**

| Aspecto                | CommonJS                     | ESM                          |
|-------------------------|------------------------------|------------------------------|
| **Importación**         | `require()`                 | `import`                    |
| **Exportación**         | `module.exports` / `exports`| `export` / `export default` |
| **Cargar dinámicamente**| Sí, con `require()`         | Sí, con `import()`          |
| **Sincronía**           | Sincrónico                  | Asíncrónico                 |
| **Compatibilidad**      | Nativo en Node.js           | Soporte moderno, depende de configuración. |

---

## **6. Casos de Uso Combinados**

Si necesitas combinar módulos CommonJS con ESM (por ejemplo, usando librerías externas que aún usan CommonJS), Node.js permite interoperabilidad mediante:

1. **Importar CommonJS en ESM:**
   ```javascript
   // archivo: app.js (ESM)
   import sumar from './math.cjs';

   console.log(sumar(5, 3)); // 8
   ```

2. **Importar ESM en CommonJS:**
   ```javascript
   // archivo: app.js (CommonJS)
   const { sumar } = await import('./math.js');

   console.log(sumar(5, 3)); // 8
   ```

---

## **7. Conclusión**

- **CommonJS** es más antiguo y ampliamente utilizado, especialmente en proyectos Node.js tradicionales.
- **ESM** es el estándar moderno y recomendado para nuevos proyectos, alineándose con la especificación de JavaScript.

Conocer ambos sistemas permite trabajar de manera efectiva en diferentes entornos y proyectos.


---



## Key lessons
# [ES Node.js](https://developer.mozilla.org/es/docs/Learn/Server-side/Express_Nodejs/Introduction)
# [EN Node.js](https://developer.mozilla.org/es/docs/Learn/Server-side/Express_Nodejs/Introduction)

## Fix outdated npm packages
```sh
# Check outdated npm packages
npm outdated 

# Check updates outdated on npm packages
npx npm-check-updates -u

# Update npm packages
npm install

# Fix vulnerability
# npm audit fix --force
```

## NPM Basics
- NPM is the **package manager for Node.js packages**. It contains thousands of free packages available to download
- With the **CLI** or **command line interface** it's easy to download and update those packages
- NPM is commonly used with Node.js, so it is installed with the server environment.
- The way to install a package is with the command *npm install package_name*
- With each new app, NPM creates a **package.json** in which you can specify versions, dependencies and custom scripts


## Popular Node.js packages
- **Express**, the standard web development package. It's a framework that allos us to create a Node server
- **MongoDB**, brings the API for object databases in Nodejs
- **Socket.io**, it allows real-time bidiretional event-drive communication
- **Passport**, Authentication package


## Server & Endpoint setup on Express.js
Un "endpoint" es un punto de acceso a un servicio o recurso en una red. En el contexto del desarrollo web, un endpoint generalmente se refiere a una URL específica en un servidor que se utiliza para realizar operaciones específicas, como leer, escribir, actualizar o eliminar datos.

Node.js es un entorno de ejecución de JavaScript del lado del servidor que permite a los desarrolladores construir aplicaciones web escalables y de alto rendimiento. Permite ejecutar JavaScript en el servidor, lo que lo hace ideal para desarrollar aplicaciones web completas. Node.js utiliza el motor V8 de Google Chrome para ejecutar JavaScript de manera eficiente fuera del navegador.

Express.js es un marco de aplicación web para Node.js que facilita la creación de aplicaciones web y APIs. Proporciona un conjunto de utilidades para manejar rutas, solicitudes y respuestas HTTP de manera eficiente, lo que hace que el desarrollo de aplicaciones web sea más rápido y sencillo.

1. Instalar Node.js: Descarga e instala Node.js desde el sitio web oficial si aún no lo has hecho.

2. Inicializar un proyecto Node.js: Abre una terminal, navega hasta la carpeta donde quieres crear tu proyecto y ejecuta el siguiente comando para inicializar un nuevo proyecto Node.js:

```bash
npm init -y
```

3. Instalar Express.js: Una vez que tengas un proyecto Node.js configurado, instala Express.js ejecutando el siguiente comando en tu terminal:

```bash
npm install express
```

4. Crea un archivo JavaScript para tu aplicación Express: Crea un archivo llamado `app.js` (o cualquier otro nombre que prefieras) en la raíz de tu proyecto.

5. Configura tu aplicación Express en `app.js`:

```javascript
const express = require('express');
const app = express();
const PORT = 3000; // Puerto en el que se ejecutará el servidor

// Define un endpoint básico
app.get('/', (req, res) => {
  res.send('¡Hola, mundo!');
});

// Inicia el servidor
app.listen(PORT, () => {
  console.log(`Servidor iniciado en http://localhost:${PORT}`);
});
```

6. Ejecuta tu aplicación: En la terminal, navega hasta la ubicación de tu archivo `app.js` y ejecuta el siguiente comando:

```bash
node app.js
```

Ahora puedes acceder al endpoint que has creado navegando a `http://localhost:3000` en tu navegador. Verás el mensaje "¡Hola, mundo!" devuelto por tu endpoint.


## Arquitectura de Node.js
- Node.js utiliza la arquitectura *Single Threaded Event Loop* para manejar múltiples clientes al mismo tiempo
- En un modelo de solicitud-respuesta multihilo, varios clientes envían una solicitud y el servidor procesa cada una de ellas antes de devolver la respuesta. Se utilizan múltiples hilos para procesar las llamadas concurrentes, estos hilos se definen en un pool de hilos y cada vez que llega una petición, se asigna un hilo individual para manejarla
- Dado que Node.js utiliza menos hilos, utiliza menos recursos/memoria, lo que resulta en una ejecución más rápida de las tareas
- Para procesar tareas con muchos datos, tiene más sentido usar lenguajes multihilo como Java. Pero para apps en tiempo real, Node.js es la opción obvia

<p>
  <img src="../../img/nodejsArch.png" alt="Node Architecture">
</p>

1. Node.js mantiene un pool de hilos limitado para atender las peticiones
2. Cada vez que llega una solicitud, Node.js la coloca en una cola
3. Ahora el event loop de un sólo hilo entra en escena. Este bucle de eventos espera las peticiones indefinidamente
4. Cuando llega una solicitud, el bucle la recoge de la cola y comprueba si require una operación de E/S de bloqueo, si no, procesa la solicitud y envía una respuesta
5. Si la solicitud tiene una operación de bloquo que realizar, el bucle de eventos asigna un hilo del pool de hilos internos para procesar la solicitud. Los hilos internos disponibles son limitados. Este grupo de hilos auxiliares se llama grupo de trabajadores
6. El bucle de eventos rastrea las solicitudes que se bloquean y las coloca en la cola una vez que se procesa la taerea que se bloquea. Así es como mantiene su naturaleza no bloqueante


## Ejemplos de apps de Node.js
1. **Chats en tiempo real / Real-time services (chats, games, etc)**: Debido a su naturaleza asíncrona de un sólo hilo, Node.js es muy adecuado para procesar la comunicación en tiempo real
2. **IoT**: IoT suelen estar formadas por multiples sensores, ya que suelen enviar pequeños trozos de datos que pueden acumularse en un gran número de peticiones. Node.js es capaz de gestionar estas peticiones concurrentes con rapidez
3. **Streaming de datos**: Node.js es ligero y rápido, además de que proporciona una API de streaming nativa.
4. **SPAs**: En las Single Page Applications toda la app se carga en una sola página. Lo que significa que hay un par de peticiones realizadas en segundo plano para componentnes específicos. El bucle de evnetos de Node.js procesa las solicitudes de forma no bloqueante.
5. **Apps backend y apps basadas en REST API**: Un servidor puede comunicarse fácilmente con el frontend a través de APIs REST utilizando Node.js, ya que también proporciona paquetes como Express.js y Koa que facilitan la creación de aplicaciones web
6. **Blogs, CMS, Social apps**
7. **Utilities & Tools**
8. **Anything that is not CPU-intensive**

## Resources
### [Node.js w3](https://www.w3schools.com/nodejs/default.asp)
### [Node.js Tutorial Mosh](https://www.youtube.com/watch?v=TlB_eWDSMt4)
### [Node.js Crash Course Traversy](https://www.youtube.com/watch?v=fBNz5xF-Kx4)
### [Node.js Crash Course Tutorial](https://www.youtube.com/watch?v=zb3Qk8SG5Ms&list=PL4cUxeGkcC9jsz4LDYc6kv3ymONOKxwBU)


## package.json
**package.json** is a really important file that is used in node packages and applications
- It goes in the root of your package/application
- Tells npm how your package is structured and what will do to install it
```json
{
	"name": "mytasklist",
	"version": "1.0.0",
	"description": "Simple task manager",
	// main describes the file that it's the entry point of our application like index.js
	"main": "server.js",
	"author": "Johnny Melavo",
	"license": "ISC",
	"dependencies": {
		"body-parser": "^1.15.2",
		"express": "^4.14.0",
		"mongojs": "^2.4.0"
	}
}
```
We can create a package.json manually or we can run
```sh
npm init
```
With Node.js we can run the JavaScript files from the command line!


## Creating a basic web server that uses filesystem
When we upload our PHP file to Apache, this takes care of all the requests
With Node.js is a little different, you have to create your own server

So we're gount yo build a simple server that's on the node.js website
```javascript
// We're including a Node module that it's already including in the system (no need to install it)
const http = require('http');

// We're bringing the filesystem module
const fs = require('fs');

// We're working on our localhost so we'll use the loopback address
const hostname = '127.0.0.1'
const port = 3000;

fs.readFile('index.html', (err, html) => {

	if(err) {
		throw err;
	}

	const server = http.createServer((req, res) => {

		res.statusCode = 200;
		res.setHeader('Content-type', 'text/html');
		res.write(html);
		res.end();
	});

	server.listen(port, hostname, () => {

		console.log('Server started on port ' + port);
	});
});
```

**Now our server is running and parsing the HTML!**


# Understanding Node.js step by step
## Step 1 Introduction
When we visit a URL on the internet, it points to your server
When the request is received we can use node to handle the requests and read a file from the server's filesystem
Then responds back to the client so they can view the HTML in the browser


## Step 2 Install Node
On a terminal
```sh
# Checking in node is installed
node -v

# If not, install it with NVM (Node Version Manager) github.com/nvm-sh/nvm
nvm install  12.16.3 #example
```


## Step 3 Hello World
One way to start our first steps in Node is with REPL
**REPL** stands for Read Eval Print Loop
When we type node into the command line, it allows us to run JavaScript code and will print out the results
```sh
node

> console.log("Hello World") # Hello World
```

But mostly we'll want to execute JavaScript code that lives in an actual file
The default entry point into a node.js app is the index.js file

On index.js
```javascript
console.log("Hello World");
```

Now we can run from the terminal
```sh
node index.js # Hello World

# And because it's an index file, we can actually point to the parent directory
node . # Hello World
```


## Step 4 Events
Node.js is defined as an *asynchronous event-driven JavaScript runtime*
The runtime implements a thing called **event loop** just like a web browser does

This allows node to push intensive operations off to a separate thread, so only very fast non-blocking operations happen on the main thread

This is why  people call Node,  non-blocking, it's a design choice that makes node.js very suitable for things that require high throughput like real time apps, web servers, etc

So without a depper knowledge of those low-level details, we need to know how **events** and **callbacks** work

In most cases, we'll listen to events, events can come in many forms, but one example is on the process global
Before a node process finishes, it emits an event named exit, we can listen to this event using on an then register a callback function as the second argument

Where the event is exit and the callback is the function associated with it
When the exit event occurs node.js will run this function
```sh
process.on('exit', function(){

	// do something!
});
```

The functions isn't called the first time node.js sees it
Its only called after the exit event occurs at some point in the future

This event is built-int in node, but we can also create our own from scratch
```javascript
// Importing an event emitter from the events module that is built into node
const { EventEmitter } = require('events');

// We can create a custom event emitter by instantiating the class
const eventEmitter = new EventEmitter();

// Then we'll register a callback that fires on the lunch event
eventEmitter.on('lunch', () => {

	console.log("I'm having a lunch!");
});

// Now the callback is registered, we can call it. This triggers our callback function
eventEmitter.emit('lunch'); # I'm having a lunch!
```

This event-driven style of programming is extremely useful when we have something that is CPU intensive


## Step 5 File System
Node has a built-int file system module called fs
It can read, write and delete files on the file system among other things
It also can do things in a blocking or non-blocking way

We'll create a *hello.txt* file
```txt
This is a text example!
```

In our JavaScript code, we'll import two functions from the file system module, **readFile** and **readFileSync**

**sync === blocking**
Anytime we see a function that ends in sync, think blocking, because it will need to finish all of its work before any of our other code can run

#### Blocking example
```javascript
const { readFile, readFileSync } = require('fs');

// We can read a text file on node by passing the path to that file, then we'll specify the enconding as UTF-8
const txt = readFileSync('./hello.txt', 'utf8');

console.log(txt);

// This console.log won't run until after that file has been read
console.log("do this ASAP");

// RESULTS
// This is a text example!
// do this ASAP
```

#### Non-blocking example
Luckily we can make our code non-blocking by refactoring this to a callback

Inside the callback function we can access an error object if the operation fails, or when successful, the actual text from the file
```javascript
const { readFile, readFileSync } = require('fs');


# We just add a callback function as the 3rd argument
const txt = readFileSync('./hello.txt', 'utf8', (err, txt) => {

	console.log(txt);
});

console.log("do this ASAP");

# RESULTS
# do this ASAP
# This is a text example!
```

The good thing about this is that even though the console log to the text file comes first in our script, it's not the thing that gets executed first

Node registers the callback, executes the rest of the script and then finally runs the callback when the file has been read

#### Promise example
Promises are also asynchronous and non-blocking and they tend to produce much cleaner code when compared to callbacks

We're importing read file from the promises namespace, this gives us a function that returns a promise when called

This code is much easier to read specially with many async calls in the same function
```
const { readFile } = require('fs').promises;

async function hello() {
	const file = await readFile('./hello.txt', 'utf8');
}
```

#### Modules & NPM
A module is nothing more than a JavaScript file that exports its code
Node has a bunch of built-in modules like **fs** and **events**
And there's a long list of other modules beyond that

The traditional way to import a module is tu use a **require()** function
Node also has a support for ES6 modules which use the import-export syntax (but most Node modules written in Vanilla JavaScript still use require)

We'll create a new file called *my-module.js*
We'll reference this module with module.exports and whatever we add inside, it will be available to use in the other file
```javascript
module.exports = {
	science: 'sociology'
}
```

On *index.js*
```javascript
// We'll import our mode
const myModule = require('./my-module')
```

The primary place to use somebody else's code will be using NPM (Node Package Manager)
NPM is installed with Node and it's a tool we can use to install remote packages to use in our own code

On the terminal, we'll write **npm init** to create a **package.json file in the root of the application**
```sh
npm init -y
```

This **package.json** file contains metadata about our project, but most importantly, it keeps track of the dependencies that we use here

Now we'll use npm to install **express**
```sh
npm install express
```

Express is a minimal web application framework and one of the most popular third-party modules

Now, in our *package.json* file, it added Express to the dependencies and pegged to a specific version
This dependencies object allows us to manage multiple dependencies in a project and then reinstall them all at once on a different system

With this package installed, we can import it by name in our js code
With express, now we're ready to build a real full-stack application and deploy it to the cloud

Our server will live in a url, and when an user makes a request to this url in the browser the server will respond with some HTML

In our code, we'll first create an instance of an express app
**An express app allows us to create different URLs and endpoints that a user can navigate to in the browser**, and then we define code for the server to handle those requests

When an user navigates to a URL in the browser, it's what's known as a get request
This means they're requesting some data on the server and not trying to modify or update anything on the server

With express we can set up an endpoint by calling **app.get()**
```javascript
const express = require('express');

const app = express();

// The first argument is the URL that the user will navigate to
// The second argument is the callback function
app.get('/foo/bar', (request, response) => {

	// We need to read some HTML from our file system and then send it back to the browser
	readFile('./home.html', 'utf8', (err, html) => {

		// If theres an error, we can handle that by sending a response
		if (err) {
			response.status(500).send('sorry out of order!')
		}

		// Now we send the response back down to the client
		response.send(html)
	});
});
```

We can think of every request to a URL as an event and then we handle that event with the function
- **request** - user's incoming data
- **response** - our outgoing data

Now we just need to tell our Express app to start listening to incoming requests
We do that by defining a port which will normally come from a node environment variable
```javascript
app.listen(process.env.PORT || 3000, () => console.log('App available on http://localhost:3000'));
```

Now we can start it up on the terminal
```sh
node . # App available on http://localhost:3000
```

To avoid nested callbacks, it's recommended to use promises instead of callbacks
Instead of importing readFile from fs, we'll import it from fs.promises
```javascript
const { readFile } = require('fs').promises;
```

We can make our callback function async and then we can write the response in a single line of code by saying response.send and then await the operation to read file

```javascript
const { readFile } = require('fs').promises;

app.get('/', async (request, response) => {

	response.send( await readFile('./home.html', 'utf8') );

});
```
