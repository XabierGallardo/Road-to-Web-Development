## Conceptos fundamentales

- **Un endpoint es una URL específica a la que una aplicación cliente envía una solicitud para acceder a una funcionalidad o recurso particular ofrecido por una API del servidor, actuando como el punto final de una conexión API**  

- Por otro lado, **una ruta se refiere a la estructura de la URL que determina cómo se procesa una solicitud, incluyendo la base de ruta y el recurso específico, y puede estar asociada a un endpoint**  

- **En el contexto de APIs, la ruta define la dirección a la que se envía la solicitud, mientras que el endpoint es la ubicación exacta donde se procesa esa solicitud**

Aunque el término "ruta" puede referirse a la estructura general de la URL, el "endpoint" se enfoca en la dirección específica que responde a una solicitud, especialmente en el contexto de APIs REST, donde se utilizan métodos HTTP como GET, POST, PUT o PATCH para realizar acciones sobre los recursos  Así, mientras la ruta define la estructura de acceso, el endpoint es la dirección concreta donde se realiza la operación 


---


## Diferencia entre REST y RESTful

REST (Representational State Transfer) es un estilo de arquitectura de software que se basa en los principios del protocolo HTTP para facilitar la comunicación entre sistemas, especialmente en entornos de red como Internet Este enfoque define cómo deben diseñarse los servicios web para que sean escalables, independientes y eficientes, con características clave como la separación entre cliente y servidor, la ausencia de estado en las solicitudes y el uso de recursos identificados por URI

Por otro lado, RESTful se refiere a un servicio web o API que implementa efectivamente los principios y restricciones de la arquitectura REST En otras palabras, una API RESTful es una implementación concreta que sigue las reglas de REST, como el uso adecuado de los métodos HTTP (GET, POST, PUT, DELETE) para manipular recursos, la representación de estos recursos mediante formatos como JSON o XML, y la comunicación sin estado Aunque a menudo se usan como sinónimos, REST es el concepto teórico o arquitectónico, mientras que RESTful describe la realización práctica de ese concepto

En resumen, REST es la arquitectura, y RESTful es la aplicación de esa arquitectura en servicios reales Una API REST se refiere al estándar o interfaz definida por estos principios, mientras que un servicio web RESTful es la implementación que cumple con esos estándares, por ejemplo, utilizando métodos HTTP apropiados y recursos bien definidos


---

## Que es el middleware `Router`?

En Express.js, un Router es una instancia aislada de middleware y rutas que se comporta como una miniaplicación independiente, también conocida como una "miniapp"  **Permite crear manejadores de rutas montables y modulares, facilitando la organización y estructuración del código, especialmente en aplicaciones grandes y complejas**  

**Al igual que la instancia principal de Express (app), un Router puede utilizar métodos como `get`, `post`, `put`, `delete`, y otros para definir rutas HTTP específicas**  Además, puede incluir middleware personalizado, manejar parámetros de ruta mediante `router.param()`, y utilizar `router.route()` para definir múltiples métodos HTTP en una sola ruta, evitando errores de escritura 

**El Router se crea con `express.Router()` y puede ser montado en una aplicación principal mediante `app.use()` con un prefijo de ruta**, lo que permite agrupar rutas relacionadas bajo un mismo camino, como `/usuarios` o `/wiki`  Esto mejora la modularidad, la reutilización del código y la separación de responsabilidades  Las funciones de middleware definidas en un Router solo se ejecutan para las rutas que pertenecen a ese Router, y no se heredan a aplicaciones o routers secundarios  El orden de los middleware y rutas dentro del Router es crucial, ya que se ejecutan secuencialmente de arriba hacia abajo 


#### Y por que se considera una mini aplicacion?

Express Router se considera una «mini aplicación» porque es una instancia aislada de middleware y funcionalidad de enrutamiento, capaz de manejar tanto el middleware como las definiciones de rutas de forma independiente.  Funciona como un sistema autónomo que se puede montar dentro de una aplicación Express más grande, lo que permite a los desarrolladores modularizar las rutas y el middleware en archivos o componentes separados.  Este diseño modular permite la creación de controladores de rutas reutilizables, como los destinados a funciones específicas, como la gestión de usuarios o los servicios de calendario, que pueden integrarse fácilmente en la aplicación principal mediante app.use().  Dado que un enrutador se comporta como un middleware en sí mismo, puede utilizarse como argumento en app.use() o dentro de otros enrutadores, lo que refuerza aún más su función como miniaplicación independiente. 


---


## Como se envian los datos de los formularios en html?
Tipos de Datos en Formularios HTML

Los formularios HTML envían datos en pares nombre/valor cuando se envían al servidor Estos datos pueden incluir texto, contraseñas, fechas, números, selecciones de opciones, archivos adjuntos, entre otros, dependiendo del tipo de control de formulario utilizado El tipo de datos enviado depende del atributo `type` de los elementos dentro del formulario, como `text`, `password`, `email`, `number`, `date`, `checkbox`, `radio`, `file`, entre otros

El formato de codificación de los datos se define mediante el atributo `enctype` del elemento `form` **Por defecto, los formularios se envían con el formato `application/x-www-form-urlencoded`**, que sustituye espacios por `+` y convierte caracteres especiales en secuencias de escape, separando los pares nombre/valor con `=` y las combinaciones con `&` Este formato es adecuado para datos pequeños y no confidenciales, especialmente cuando se usa el método `GET`

Para formularios que incluyen imágenes o grandes volúmenes de información, se debe utilizar el tipo `multipart/form-data`, que envía los datos en partes separadas conocidas como `form-data` Este formato es necesario cuando se usa el atributo `type="file"` en un campo de entrada

El método de envío, especificado con el atributo `method` en el elemento `form`, puede ser `GET` o `POST` Con `GET`, los datos se incluyen en la URL, lo que los hace visibles y limita la cantidad de datos que se pueden enviar Con `POST`, los datos se envían en el cuerpo de la solicitud HTTP, lo que los hace más seguros, especialmente para datos sensibles


## Y como recibimos en Express los datos de un `<form>`?
**Este middleware analiza los cuerpos de las solicitudes entrantes con el tipo de contenido `application/x-www-form-urlencoded` y hace que los datos analizados estén disponibles en `req.body`**. 

Para un uso básico, añada el middleware a su aplicación Express:

```javascript
const express = require(“express”);
const app = express();

// Analizar datos de formularios codificados en URL
app.use(express.urlencoded({ extended: true }));
```


---


Parse URL Encoded Data in Express

To parse URL-encoded form data in Express.js, use the built-in `express.urlencoded()` middleware. This middleware parses incoming request bodies with the `application/x-www-form-urlencoded` content type and makes the parsed data available in `req.body` 

For basic usage, add the middleware to your Express application:

```javascript
const express = require('express');
const app = express();

// Parse URL-encoded form data
app.use(express.urlencoded({ extended: true }));
```

The `extended: true` option enables parsing of nested objects and arrays using the `qs` library, while `extended: false` limits parsing to simple key-value pairs The middleware should be placed before defining routes that need to access the form data

For Express versions 4.16 and later, `express.urlencoded()` is included by default and does not require the separate `body-parser` package This middleware processes form data sent via POST requests with the `application/x-www-form-urlencoded` MIME type, converting it into a JavaScript object accessible through `req.body`

Example route handling parsed form data:

```javascript
app.post('/', (req, res) => {
  const formData = req.body; // Parsed form data is available here
  console.log(formData);
  res.send('Form submitted successfully');
});
```

This approach is the standard and recommended method for handling form submissions in Express.js applications


---


## Que es CORS?

CORS, o Intercambio de Recursos de Origen Cruzado, es un mecanismo de seguridad implementado por los navegadores web que permite a una página web 
solicitar recursos desde un dominio diferente al del origen actual

Este mecanismo se activa cuando una solicitud HTTP se realiza a un recurso 
en un dominio distinto al de la página que la originó, y su propósito principal es proteger a los usuarios de ataques  como el secuestro de sesión o el acceso no autorizado a datos sensibles  CORS funciona mediante la verificación de encabezados HTTP específicos,  como `Access-Control-Allow-Origin`, que el servidor debe incluir en su respuesta para indicar si está autorizado el acceso desde un origen determinado   

Sin este permiso explícito, el navegador bloquea la solicitud para mantener la seguridad de la política del mismo origen


---


## Que es payload?
El término "payload" en el contexto de bases de datos se refiere  a la parte de los datos transmitidos que constituye el mensaje real o la información útil, excluyendo los encabezados, metadatos o información de control necesaria para la entrega del mensaje


---


## Que es `FormData`?
Que es FormData?

En JavaScript, FormData es un objeto que permite crear un conjunto de pares clave-valor que representan los campos de un formulario HTML y sus valores, facilitando su envío a un servidor mediante métodos como fetch o XMLHttpRequest.
Este objeto replica la funcionalidad de un formulario HTML y se utiliza comúnmente para enviar datos de formularios, incluyendo archivos, de manera dinámica sin recargar la página

Este objeto es especialmente útil en aplicaciones modernas que requieren enviar datos de forma asincrónica, ya que simplifica el manejo de formularios, incluyendo campos de texto, casillas de verificación, botones de radio y campos de carga de archivos



---

## Que son los objetos `req` y `res` en Express

En Express.js, los objetos `req` (request) y `res` (response) son fundamentales para manejar las solicitudes y respuestas HTTP en una aplicación web. El objeto `req` representa la solicitud entrante del cliente y contiene información como la URL, los encabezados, los parámetros de la ruta, los datos del cuerpo y las cadenas de consulta  Por ejemplo, `req.params` se utiliza para acceder a los parámetros definidos en la ruta, como en `/user/:id`, donde `req.params.id` contiene el valor del ID  `req.query` permite obtener los parámetros de la cadena de consulta (query string), como en `?name=John&age=30`, donde `req.query.name` devuelve "John"  Además, `req.body` contiene los datos enviados en el cuerpo de la solicitud, pero requiere middleware como `express.json()` o `express.urlencoded()` para ser accesible 

Por otro lado, el objeto `res` representa la respuesta que se enviará al cliente y se utiliza para enviar datos, establecer códigos de estado, encabezados y gestionar errores  Métodos comunes incluyen `res.send()` para enviar una respuesta en texto plano, `res.json()` para enviar datos en formato JSON, y `res.status()` para definir el código de estado HTTP  También se puede usar `res.sendFile()` para enviar un archivo como respuesta  El objeto `res` incluye propiedades como `res.headersSent`, que indica si los encabezados ya fueron enviados, y `res.locals`, útil para pasar datos a las vistas 

Ambos objetos son pasados como argumentos a las funciones de middleware y rutas, permitiendo una interacción dinámica con las solicitudes y respuestas  El ciclo de vida de `req` comienza cuando el cliente realiza una solicitud HTTP, mientras que el de `res` finaliza cuando se envía la respuesta al cliente  Es importante tratar con precaución los datos de `req.query` y `req.body`, ya que provienen directamente del usuario y deben validarse antes de confiar en ellos 


---

## Que es el objeto `ResultSetHeader`?
El objeto `ResultSetHeader` devuelto por mysql2 contiene metadatos sobre el resultado de una operación SQL, como INSERT, UPDATE o DELETE. Los valores específicos que ha proporcionado indican lo siguiente:

- `fieldCount: 0` significa que no se han devuelto campos del conjunto de resultados, lo cual es habitual en las sentencias que no son SELECT.
- `affectedRows: 1` indica que una fila se vio afectada por la operación (por ejemplo, se actualizó o se eliminó).
- `insertId: 9` es el ID generado automáticamente a partir de una operación INSERT, si procede.
- `info: “”` contiene información adicional sobre la ejecución de la consulta, como advertencias o mensajes de estado; en este caso, está vacío.
- `serverStatus: 2` significa que el modo de autocompromiso del servidor está habilitado.
- `warningStatus: 0` significa que no se generaron advertencias durante la ejecución de la consulta.
- `changedRows: 0` indica que no se produjeron cambios reales en los datos, lo que puede ocurrir en una operación UPDATE si los nuevos valores son iguales a los antiguos.

Esta estructura es estándar para operaciones como INSERT, UPDATE, DELETE o TRUNCATE en mysql2, y el tipo `ResultSetHeader` se utiliza para representar el resultado cuando la consulta no devuelve un conjunto de datos. 


---

## Como exportar todo el contenido de un modulo en Express con `ESM`?

Para **exportar todo el contenido de un módulo** en **Express con ECMAScript Modules (ESM)**, usa la sintaxis `export * from` en un archivo índice (por ejemplo, `routes/index.js`) para re-exportar todos los **named exports** de otros módulos.

### ✅ Exportar Todo (Named Exports)
```js
// routes/user.js
export const getUser = (req, res) => res.json({ user: 'John' });
export const updateUser = (req, res) => res.json({ status: 'Updated' });
```

```js
// routes/product.js
export const getProducts = (req, res) => res.json({ products: [] });
```

```js
// routes/index.js
export * from './user.js';
export * from './product.js';
```

```js
// app.js
import { getUser, getProducts } from './routes/index.js';
import express from 'express';

const app = express();

app.get('/user', getUser);
app.get('/products', getProducts);

app.listen(3000);
```

### ⚠️ Exportaciones por Defecto (`default`)
Si usas `export default`, debes re-exportar manualmente con alias:

```js
// routes/auth.js
const authRouter = require('express').Router();
authRouter.post('/login', (req, res) => res.json({ ok: true }));
export default authRouter;
```

```js
// routes/index.js
export { default as auth } from './auth.js';
```

```js
// app.js
import { auth } from './routes/index.js';
app.use('/auth', auth);
```

### Requisitos
- Asegúrate de tener `"type": "module"` en tu `package.json`.
- Usa extensiones `.js` en las rutas de importación/exportación.


---


## Que es MVC, Modelo Vista Controlador?

El Modelo-Vista-Controlador (MVC) es un patrón arquitectónico de software que divide el desarrollo de aplicaciones en tres componentes interconectados: el modelo, la vista y el controlador. Originalmente diseñado para interfaces gráficas de usuario de escritorio, hoy es ampliamente utilizado en el desarrollo de aplicaciones web 

**El modelo se encarga de gestionar los datos** y la lógica de negocio de la aplicación, **incluyendo el acceso a bases de datos**, validaciones y operaciones como crear, leer, actualizar y borrar (CRUD)  

**La vista es responsable de presentar la información al usuario, generalmente a través de una interfaz gráfica** o página web, y solo se ocupa de la representación visual sin incluir lógica de negocio  

El controlador actúa como intermediario entre el usuario, el modelo y la vista: recibe las acciones del usuario, gestiona la lógica de la solicitud, solicita datos al modelo y selecciona la vista adecuada para mostrar la respuesta. **El controlador se encarga de la logica de las peticiones y las respuestas**

Este patrón promueve una separación clara de responsabilidades, lo que facilita el mantenimiento, la escalabilidad y la reutilización del código  Además, permite que diferentes desarrolladores trabajen en distintas capas simultáneamente, mejorando la productividad en proyectos complejos  MVC es compatible con múltiples frameworks y lenguajes de programación, como Ruby on Rails, Django, Laravel, ASP.NET y Angular, entre otros  Aunque el patrón ha evolucionado con el tiempo, su enfoque fundamental sigue siendo la separación entre la lógica de negocio, la presentación y la gestión de eventos 

1. La url en nuestro archivo principal llama a la ruta
```js
// index.js
app.use("/api/products", productRoutes);
```

2. La ruta en nuestro archivo de ruta, llama al middleware y luego llama al controlador
```js
// product.routes.js
// Get product by id -> Consultar producto por su id
router.get("/:id", validateId, getProductById);
```

3. El controlador va a llamar al modelo
```js
// Get product by id -> Traer producto por id
export const getProductById = async (req, res) => {

    try {
        let { id } = req.params; // Aca extraemos el 
        let sql = "SELECT * FROM productos WHERE productos.id = ?"; 
        
        let [rows] = await 
```


---

## Modularizacion: El `await` va en el controlador y no el modelo?

Sí ✅ — **tu planteamiento es correcto** y, de hecho, es **una práctica común y recomendada** en aplicaciones Node.js con arquitectura MVC.
Te explico por qué funciona y cuándo usar `async/await` en el controlador, no en el modelo 👇

---

### 💡 Contexto

En tu código:

* El **modelo (`product.models.js`)** devuelve una *promesa* (`connection.query()` ya es una función asíncrona que retorna una promesa).
* El **controlador (`product.controller.js`)** usa `async/await` para resolver esa promesa y manejar errores con `try/catch`.

---

### 🧩 Explicación técnica

```js
// Modelo
const selectAllProducts = () => {
    const sql = "SELECT * FROM products";
    return connection.query(sql); // Retorna una Promesa
};
```

Aquí no necesitas `async/await`, porque **no estás manejando la resolución de la promesa** dentro del modelo; simplemente la devuelves al controlador.

Luego en el controlador:

```js
// Controlador
export const getAllProducts = async (req, res) => {
    try {
        const [rows] = await ProductModel.selectAllProducts(); // Aquí se espera la promesa
        res.status(200).json({ payload: rows });
    } catch (error) {
        res.status(500).json({ message: "Error interno" });
    }
};
```

Aquí sí tiene sentido usar `await`, porque:

* Necesitas esperar el resultado de la consulta para continuar.
* Si ocurre un error, puedes capturarlo con `try/catch`.

---

### ⚖️ Alternativa (menos recomendada)

Podrías usar `async` también en el modelo, así:

```js
const selectAllProducts = async () => {
    const sql = "SELECT * FROM products";
    const [rows] = await connection.query(sql);
    return rows;
};
```

Y en el controlador:

```js
const rows = await ProductModel.selectAllProducts();
```

Esto **también es correcto**, pero **traslada la responsabilidad de manejar la promesa al modelo**, lo cual no siempre es ideal si quieres mantener una separación clara entre:

* Lógica de datos (modelo)
* Lógica de negocio / respuesta HTTP (controlador)

---

### ✅ Conclusión

Tu enfoque actual es **perfectamente válido y limpio**:

* ✅ Modelo devuelve promesas sin `async/await`.
* ✅ Controlador maneja `await` y errores.

Esto mantiene la arquitectura **clara, desacoplada y escalable**.

