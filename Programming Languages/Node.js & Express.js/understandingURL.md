# Diferencia entre Endpoint y Ruta

Un endpoint es una URL específica a la que una aplicación cliente envía una solicitud para acceder a una funcionalidad o recurso particular ofrecido por una API del servidor, actuando como el punto final de una conexión API  Por otro lado, una ruta se refiere a la estructura de la URL que determina cómo se procesa una solicitud, incluyendo la base de ruta y el recurso específico, y puede estar asociada a un endpoint  En el contexto de APIs, la ruta define la dirección a la que se envía la solicitud, mientras que el endpoint es la ubicación exacta donde se procesa esa solicitud 

Aunque el término "ruta" puede referirse a la estructura general de la URL, el "endpoint" se enfoca en la dirección específica que responde a una solicitud, especialmente en el contexto de APIs REST, donde se utilizan métodos HTTP como GET, POST, PUT o PATCH para realizar acciones sobre los recursos  Así, mientras la ruta define la estructura de acceso, el endpoint es la dirección concreta donde se realiza la operación 

---




# Understanding URLs

## **Trabajando con URLs en Express.js: Guía Completa**

En Express.js, trabajar con URLs es esencial para manejar rutas dinámicas, extraer parámetros y procesar consultas. En esta guía, exploraremos en profundidad cómo manipular URLs en Express, cubriendo:

1. **Manejo de rutas y `req.params`**
2. **Extracción de `req.query`**
3. **Uso de `req.path`, `req.baseUrl` y `req.originalUrl`**
4. **Redirección y reescritura de URLs**
5. **Generación dinámica de URLs**
6. **Middleware para manipular URLs**

---

## **1. Manejo de rutas y `req.params`**
### **¿Qué es `req.params`?**
`req.params` es un objeto que almacena los parámetros de la URL definidos en la ruta.

### **Ejemplo básico**
```js
const express = require('express');
const app = express();

app.get('/usuario/:id', (req, res) => {
    const { id } = req.params; // Extrae el parámetro "id"
    res.send(`Usuario con ID: ${id}`);
});

app.listen(3000, () => console.log('Servidor en http://localhost:3000'));
```
🔹 **Explicación:**
- `:id` en la ruta es un parámetro dinámico.
- Si accedemos a `http://localhost:3000/usuario/123`, `req.params` contendrá `{ id: "123" }`.

### **Parámetros múltiples**
```js
app.get('/producto/:categoria/:id', (req, res) => {
    const { categoria, id } = req.params;
    res.send(`Categoría: ${categoria}, Producto ID: ${id}`);
});
```
📌 URL de ejemplo: `/producto/electronica/456`  
📌 `req.params` devuelve: `{ categoria: "electronica", id: "456" }`

### **Rutas con parámetros opcionales**
Puedes definir parámetros opcionales agregando `?`:
```js
app.get('/cliente/:id?', (req, res) => {
    if (req.params.id) {
        res.send(`Cliente ID: ${req.params.id}`);
    } else {
        res.send('Lista de clientes');
    }
});
```
📌 `/cliente/789` → "Cliente ID: 789"  
📌 `/cliente` → "Lista de clientes"

---

## **2. Extracción de `req.query` (Parámetros de consulta)**
Los parámetros de consulta son datos enviados en la URL después de `?`. Se acceden mediante `req.query`.

### **Ejemplo con `req.query`**
```js
app.get('/buscar', (req, res) => {
    const { q, pagina } = req.query;
    res.send(`Buscando: ${q}, Página: ${pagina}`);
});
```
📌 URL de ejemplo: `/buscar?q=laptop&pagina=2`  
📌 `req.query` devuelve: `{ q: "laptop", pagina: "2" }`

### **Uso combinado con `req.params`**
```js
app.get('/productos/:id', (req, res) => {
    const { id } = req.params;
    const { color, talla } = req.query;
    res.send(`Producto ID: ${id}, Color: ${color}, Talla: ${talla}`);
});
```
📌 URL: `/productos/101?color=rojo&talla=M`  
📌 Respuesta: `"Producto ID: 101, Color: rojo, Talla: M"`

---

## **3. Uso de `req.path`, `req.baseUrl` y `req.originalUrl`**
Estos métodos permiten analizar la estructura de la URL dentro de Express.

### **`req.path`**
Obtiene la ruta sin el dominio ni los parámetros de consulta.
```js
app.get('/test', (req, res) => {
    res.send(`Ruta: ${req.path}`);
});
```
📌 `/test?x=1` devuelve `"Ruta: /test"`

### **`req.originalUrl`**
Obtiene la URL completa, incluyendo la ruta y los parámetros.
```js
app.get('/test', (req, res) => {
    res.send(`URL completa: ${req.originalUrl}`);
});
```
📌 `/test?x=1` devuelve `"URL completa: /test?x=1"`

### **`req.baseUrl`**
Se usa en routers anidados.
```js
const router = express.Router();
router.get('/info', (req, res) => {
    res.send(`Base URL: ${req.baseUrl}`);
});

app.use('/api', router);
```
📌 `/api/info` devuelve `"Base URL: /api"`

---

## **4. Redirección y reescritura de URLs**
Express permite redirigir al usuario a otra URL con `res.redirect()`.

### **Redirección simple**
```js
app.get('/antigua', (req, res) => {
    res.redirect('/nueva');
});

app.get('/nueva', (req, res) => {
    res.send('Nueva URL');
});
```
📌 `/antigua` redirige a `/nueva`.

### **Redirección con código de estado**
```js
app.get('/moved', (req, res) => {
    res.redirect(301, '/nuevo-lugar'); // Redirección permanente
});
```

---

## **5. Generación dinámica de URLs**
Puedes generar URLs dinámicamente usando `req.protocol`, `req.hostname` y `req.baseUrl`.

```js
app.get('/link', (req, res) => {
    const url = `${req.protocol}://${req.get('host')}/destino`;
    res.send(`Visita: <a href="${url}">${url}</a>`);
});
```
📌 Devuelve un enlace con la URL del servidor.

---

## **6. Middleware para manipular URLs**
Los middlewares pueden interceptar y modificar las URLs antes de que lleguen a las rutas.

### **Ejemplo: Middleware que normaliza URLs**
```js
app.use((req, res, next) => {
    req.url = req.url.toLowerCase(); // Convierte URLs a minúsculas
    next();
});

app.get('/productos', (req, res) => {
    res.send('Lista de productos');
});
```
📌 `/PRODUCTOS` → Se convierte a `/productos`

---

## **Resumen y mejores prácticas**
✅ **Usa `req.params`** para capturar valores en rutas dinámicas.  
✅ **Usa `req.query`** para obtener datos adicionales desde la URL.  
✅ **Usa `req.path`, `req.baseUrl` y `req.originalUrl`** para obtener diferentes partes de la URL.  
✅ **Usa `res.redirect()`** para manejar cambios en las rutas.  
✅ **Usa middlewares** para manipular URLs antes de procesarlas.  


---


## **¿Qué es `req.params` en Express.js?**
En Express.js, `req.params` es un objeto que contiene los parámetros de la URL cuando se usa una ruta con parámetros dinámicos. Se usa en las rutas que incluyen segmentos con `:` (dos puntos), lo que permite capturar valores específicos de la URL.

#### **Ejemplo de `req.params` en uso**
```js
app.get('/usuarios/:id', (req, res) => {
    console.log(req.params); // { id: '123' } si la URL es /usuarios/123
    res.send(`Usuario con ID: ${req.params.id}`);
});
```
Si un usuario accede a `http://localhost:3000/usuarios/123`, el objeto `req.params` tendrá `{ id: '123' }`.

---

### **¿Por qué se usa destructuring en `const { id } = req.params;`?**
En el siguiente código:
```js
const { id } = req.params;
```
Se está usando **destructuring** de objetos en JavaScript para extraer directamente el valor de `id` desde `req.params`. 

#### **Sin destructuring:**
```js
const id = req.params.id;
```
Esto funciona igual, pero el destructuring simplifica el código y lo hace más limpio.

#### **Con destructuring:**
```js
const { id } = req.params;
```
Aquí, estamos extrayendo `id` directamente de `req.params`, lo que evita escribir `req.params.id` en cada lugar donde se necesite.

---

### **Ventajas de usar destructuring**
1. **Código más limpio y corto**  
   - En lugar de escribir `req.params.id` repetidamente, solo usamos `id`.
   
2. **Fácil de leer y mantener**  
   - Permite ver de inmediato qué valores se están extrayendo de `req.params`.

3. **Útil si hay varios parámetros**  
   - Si hay más de un parámetro, se pueden extraer varios valores de forma eficiente:
   ```js
   const { id, nombre } = req.params;
   ```

---

### **Ejemplo completo en Express.js**
```js
const express = require('express');
const app = express();

app.get('/productos/:id', (req, res) => {
    const { id } = req.params; // Extrae "id" de req.params
    res.send(`Producto con ID: ${id}`);
});

app.listen(3000, () => console.log('Servidor en http://localhost:3000'));
```
Si accedes a `http://localhost:3000/productos/42`, la respuesta será `"Producto con ID: 42"`.

---

### **Conclusión**
- `req.params` contiene los parámetros dinámicos de la URL.
- `const { id } = req.params;` usa destructuring para extraer `id` de forma más limpia.
- Es una forma eficiente de manejar rutas dinámicas en Express.js. 🚀