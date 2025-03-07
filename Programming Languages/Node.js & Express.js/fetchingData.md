# Fetching data in Express.js

## **Explicación Técnica del Código**

El siguiente ejemplo utiliza `fetch()` para realizar una petición HTTP a un servidor. Analicemos cada parte en detalle:

```js
const response = await fetch(`/api/users/${idUser}`);
```
🔹 **Explicación**:  
- `fetch()` es una función nativa de JavaScript que permite hacer peticiones HTTP.
- `/api/users/${idUser}` es la URL del endpoint al que se está realizando la solicitud.
- `await` se usa para esperar a que `fetch()` complete la solicitud antes de continuar.
- `response` almacenará el objeto `Response` devuelto por `fetch()`.

### **¿Qué es `response`?**
El objeto `response` es una instancia de la clase [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response), que representa la respuesta de la solicitud HTTP. Contiene metadatos y métodos para procesar el cuerpo de la respuesta.

Ejemplo de lo que podría contener `response`:
```json
{
  "ok": true,
  "status": 200,
  "statusText": "OK",
  "headers": { "content-type": "application/json" },
  "body": ReadableStream
}
```

📌 **Propiedades clave de `response`**:
1. **`response.ok`**: Devuelve `true` si el código de estado está entre 200 y 299 (respuesta exitosa).
2. **`response.status`**: Devuelve el código de estado HTTP (por ejemplo, 200 para éxito, 404 para no encontrado).
3. **`response.statusText`**: Mensaje textual del estado (por ejemplo, `"OK"` o `"Not Found"`).
4. **`response.headers`**: Contiene los encabezados de la respuesta.
5. **`response.body`**: Es un `ReadableStream` que representa el cuerpo de la respuesta.

---

```js
if (response.ok) {
    console.log(response);
```
🔹 **Explicación**:  
- Se verifica si `response.ok` es `true` (lo que indica que la solicitud fue exitosa).
- Si la respuesta es exitosa, se imprime `response` en la consola.

🔍 **Ejemplo de lo que imprimiría `console.log(response)` en una respuesta exitosa**:
```json
Response {
  type: "cors",
  url: "http://localhost:3000/api/users/123",
  redirected: false,
  status: 200,
  ok: true,
  statusText: "OK",
  headers: Headers,
  body: ReadableStream
}
```

---

```js
const result = await response.json();
console.log(result);
```
🔹 **Explicación**:  
- `response.json()` es un método que convierte el cuerpo de la respuesta en un objeto JSON.
- `await` espera a que la conversión JSON se complete.
- `result` almacenará los datos en formato JSON.

### **¿Qué es `result`?**
- `result` contendrá el contenido real de la respuesta en formato JSON.
- Mientras que `response` es un objeto con metadatos, `result` es el contenido procesado.

🔍 **Ejemplo de lo que imprimiría `console.log(result)` en caso de éxito**:
```json
{
  "id": 123,
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "age": 25
}
```

📌 **Diferencia clave entre `response` y `result`**:
| Propiedad   | `response` (Objeto `Response`) | `result` (Contenido JSON) |
|-------------|--------------------------------|---------------------------|
| **Tipo**    | Objeto `Response` | JSON convertido en objeto |
| **Qué contiene** | Metadatos de la respuesta HTTP | Datos de la respuesta |
| **Ejemplo** | `{ status: 200, ok: true, body: ReadableStream }` | `{ id: 123, name: "Juan Pérez" }` |
| **Método para obtenerlo** | Devuelto directamente por `fetch()` | `await response.json()` |

---

## **Ejemplo Completo con un Servidor Simulado**
Para ilustrarlo mejor, aquí tienes un servidor en Express que respondería a la petición:

```js
const express = require('express');
const app = express();

app.get('/api/users/:id', (req, res) => {
    const { id } = req.params;
    res.json({ id, name: "Juan Pérez", email: "juan@example.com", age: 25 });
});

app.listen(3000, () => console.log("Servidor en http://localhost:3000"));
```

Si ejecutamos el código en el cliente:
```js
const idUser = 123;

const fetchUser = async () => {
    const response = await fetch(`/api/users/${idUser}`);

    if(response.ok) {
        console.log(response); // Muestra el objeto Response
        const result = await response.json();
        console.log(result); // Muestra el objeto JSON con datos del usuario
    }
};

fetchUser();
```
📌 **Salida esperada en consola**:
```json
Response {
  status: 200,
  ok: true,
  body: ReadableStream,
  headers: Headers,
  url: "http://localhost:3000/api/users/123"
}

{
  "id": 123,
  "name": "Juan Pérez",
  "email": "juan@example.com",
  "age": 25
}
```

---

## **Conclusión**
1. `fetch()` devuelve un objeto `Response`, que contiene información sobre la respuesta HTTP.
2. `response.ok` indica si la respuesta fue exitosa (`true` para códigos 200-299).
3. `response.json()` convierte el cuerpo de la respuesta en JSON.
4. `response` contiene los **metadatos** de la respuesta.
5. `result` contiene los **datos** procesados en JSON.

Este flujo es fundamental en aplicaciones web para interactuar con APIs y manejar datos dinámicos de manera eficiente. 🚀