# Express.js I

## 1. Entendiendo un ejemplo minimo de servidor en Express.js

```js
import express from "express";
const app = express();

app.get("/", (req, res) => {
	res.send("Hola mundo");
});

app.listen(3000, () => {
	console.log(`Servidor corriendo en el puerto 3000`);
});

```

---

### 🧩 **Métodos de `app` (instancia de Express)**

#### 1. **`app.get(path, callback)`**

* Este método define una **ruta HTTP GET**.
* En el ejemplo:

  ```js
  app.get("/", (req, res) => {
      res.send("Hola mundo");
  });
  ```

  * `" / "`: Es la ruta raíz del servidor (por ejemplo, `http://localhost:3000/`).
  * `(req, res) => { ... }`: Es la **función callback** que se ejecuta cuando se recibe una petición GET a esa ruta.

---

### 🔄 **Parámetros `req` y `res`**

#### - `req` (abreviación de **request**):

Representa la **solicitud del cliente** al servidor.

* Contiene información como:

  * Parámetros de la URL
  * Cuerpo del mensaje (para POST/PUT)
  * Cabeceras HTTP
  * Datos de sesión, cookies, etc.

#### - `res` (abreviación de **response**):

Representa la **respuesta del servidor** hacia el cliente.

* Se utiliza para:

  * Enviar texto, HTML, JSON, archivos, etc.
  * Establecer códigos de estado
  * Redireccionar
  * Finalizar la respuesta

**Ejemplo**:

```js
res.send("Hola mundo");
```

Esto **envía una respuesta simple** de texto al navegador del cliente.



### 🔚 En resumen:

* `app.get()` define rutas que responden a solicitudes GET.
* `req` y `res` son objetos que te permiten **leer la solicitud del cliente** y **enviar una respuesta**.
* `app.listen()` pone el servidor en marcha y comienza a escuchar peticiones.


---


## 2. **Los objetos `req` y `res` en Express.js**  

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


## Entendiendo `app` y sus métodos
`app` es la instancia del servidor creada con `express()`. Se usa para configurar rutas, middleware, y lanzar el servidor.

---

## ✅ **Métodos HTTP más comunes**

Estos métodos se usan para **definir rutas** que respondan a distintos tipos de peticiones HTTP:

### 1. **`app.get(path, callback)`**

* Maneja solicitudes **GET**, como cuando visitas una página web.
* Ejemplo:

  ```js
  app.get("/usuarios", (req, res) => { ... });
  ```

### 2. **`app.post(path, callback)`**

* Maneja solicitudes **POST**, típicas para **enviar datos** (como formularios).
* Ejemplo:

  ```js
  app.post("/crear", (req, res) => { ... });
  ```

### 3. **`app.put(path, callback)`**

* Maneja solicitudes **PUT**, usadas para **actualizar recursos**.
* Ejemplo:

  ```js
  app.put("/usuario/:id", (req, res) => { ... });
  ```

### 4. **`app.delete(path, callback)`**

* Maneja solicitudes **DELETE**, usadas para **eliminar recursos**.
* Ejemplo:

  ```js
  app.delete("/usuario/:id", (req, res) => { ... });
  ```

---

## 🧰 **Otros métodos útiles de `app`**

### 5. **`app.use(middleware)`**

* Aplica **middleware** globalmente, como para manejar JSON, rutas estáticas, o autenticación.
* Ejemplo:

  ```js
  app.use(express.json()); // Para leer cuerpos JSON
  ```

### 6. **`app.listen(port, callback)`**

* Inicia el servidor en el puerto especificado.
* Ejemplo:

  ```js
  app.listen(3000, () => console.log("Servidor iniciado"));
  ```

### 7. **`app.set(key, value)`**

* Establece configuraciones internas (por ejemplo, el motor de plantillas).
* Ejemplo:

  ```js
  app.set("view engine", "ejs");
  ```

### 8. **`app.engine()`**

* Permite registrar motores de plantillas personalizados.

### 9. **`app.route(path)`**

* Permite encadenar varios métodos HTTP para una misma ruta.
* Ejemplo:

  ```js
  app.route("/producto")
     .get((req, res) => { ... })
     .post((req, res) => { ... });
  ```

---

## 🎯 En resumen: métodos más usados

| Método         | Propósito principal                         |
| -------------- | ------------------------------------------- |
| `app.get()`    | Leer recursos                               |
| `app.post()`   | Crear recursos (enviar datos)               |
| `app.put()`    | Actualizar recursos                         |
| `app.delete()` | Eliminar recursos                           |
| `app.use()`    | Aplicar middleware global                   |
| `app.listen()` | Iniciar el servidor                         |
| `app.set()`    | Configurar opciones (como motores de vista) |



---



## Tipos de importacion y exportacion en `environments.js`
La diferencia entre los dos bloques de código en **Express.js (o cualquier app Node.js)** es principalmente **estructural** y está relacionada con:

1. **La forma en que se organizan los datos de configuración**
2. **La manera en que se exportan**
3. **Cómo se importan después**

---

### ✅ Primer ejemplo: `export const environment = { ... }`

```js
export const environment = {
  dbHost: process.env.DB_HOST,
  dbUser: process.env.DB_USER,
  dbPassword: process.env.DB_PASSWORD,
  dbName: process.env.DB_NAME,
  port: process.env.PORT || 3000,
};
```

#### 📌 Características:

* Usa **`export const`** → Exportación **nombrada**.
* Todas las variables están **en el mismo nivel del objeto**.
* Al importar, debes hacer una **importación nombrada**:

```js
import { environment } from './config.js';

console.log(environment.dbHost);
```

---

### ✅ Segundo ejemplo: `export default { ... }`

```js
export default {
  port: process.env.PORT || 3000,
  database: {
    host: process.env.DB_HOST,
    name: process.env.DB_NAME,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD
  }
}
```

#### 📌 Características:

* Usa **`export default`** → Exportación por **defecto**.
* Las variables están **organizadas jerárquicamente**, por ejemplo, las del entorno de base de datos dentro de un objeto `database`.
* Al importar, usas la importación por defecto:

```js
import config from './config.js';

console.log(config.database.host);
```

---

### 🧠 Diferencias clave

| Concepto                       | `export const environment = {...}`              | `export default {...}`                    |
| ------------------------------ | ----------------------------------------------- | ----------------------------------------- |
| Tipo de exportación            | Exportación nombrada                            | Exportación por defecto                   |
| Organización                   | Plano (todas las variables al mismo nivel)      | Agrupado (estructura jerárquica)          |
| Forma de importar              | `import { environment }`                        | `import config`                           |
| Acceso a propiedades           | `environment.dbHost`                            | `config.database.host`                    |
| Ventaja principal              | Simplicidad                                     | Mejor organización y escalabilidad        |
| ¿Permite varias exportaciones? | Sí (puedes exportar varios elementos nombrados) | No (solo un `export default` por archivo) |

---

### 🧪 ¿Cuál conviene usar?

* Usa `export default` cuando quieres una **estructura única de configuración centralizada**, especialmente si usarás esa config en varios lugares del proyecto y quieres importar de forma directa sin destructuring.

* Usa `export const` cuando quieres **exportar múltiples cosas separadas** o tener más granularidad al importar solo lo que necesitas.


---


## Entendiendo `app.use(express.json())`

```js
app.use(express.json());
```

sirve para que tu aplicación Express **pueda interpretar automáticamente los datos enviados en formato JSON** dentro del cuerpo de una solicitud HTTP (como en peticiones `POST`, `PUT` o `PATCH`).

---

### 🧠 ¿Qué significa eso exactamente?

Cuando un cliente (por ejemplo, un formulario o una API frontend) envía una solicitud con **datos en el cuerpo** en formato JSON, Express por defecto **no sabe cómo interpretarlos**. Necesitas usar un **middleware** para que los convierta en un objeto JavaScript accesible desde `req.body`.

---

### 📦 ¿Qué hace `express.json()`?

Es un **middleware incorporado** en Express (desde la versión 4.16 en adelante) que:

* Lee el **cuerpo de la petición** (body)
* Si es un JSON válido, lo **convierte en un objeto JS**
* Lo agrega a `req.body` para que lo puedas usar fácilmente

---

### 🧪 Ejemplo práctico

#### Supongamos que tienes esta ruta:

```js
app.post("/usuarios", (req, res) => {
  console.log(req.body);
  res.send("Usuario recibido");
});
```

Y desde un cliente (como Postman o fetch) haces una solicitud `POST` con este JSON:

```json
{
  "nombre": "Ana",
  "edad": 25
}
```

Sin `app.use(express.json())`, **`req.body` estaría vacío o undefined**.

Con `app.use(express.json())`, `req.body` será:

```js
{ nombre: 'Ana', edad: 25 }
```

---

### 🧱 En resumen:

| Código                    | ¿Para qué sirve?                                                         |
| ------------------------- | ------------------------------------------------------------------------ |
| `app.use(express.json())` | Para que Express entienda datos JSON en el cuerpo de las peticiones HTTP |

---

¿Quieres que te muestre también cómo usar `urlencoded()` para datos enviados desde formularios HTML?
