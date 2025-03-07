# Codigos de estado HTTP en nuestra API Rest
En una **API REST**, los códigos de estado son una parte esencial de la comunicación entre el cliente y el servidor. Estos códigos forman parte del protocolo **HTTP** y proporcionan información sobre el resultado de una solicitud. Se dividen en cinco categorías principales, según su propósito y significado.

---

## **1. Categorías Principales de Códigos HTTP**

### **1xx: Informativos**
Estos códigos indican que el servidor recibió la solicitud y que el cliente debe esperar más información para completar el proceso. Rara vez se usan en APIs REST.

| Código | Nombre             | Descripción                                                   |
|--------|--------------------|---------------------------------------------------------------|
| 100    | Continue           | El cliente debe continuar con la solicitud.                  |
| 101    | Switching Protocols| El servidor acepta cambiar a un protocolo diferente.         |

---

### **2xx: Éxito**
Indican que la solicitud fue recibida, entendida y procesada con éxito.

| Código | Nombre             | Descripción                                                   |
|--------|--------------------|---------------------------------------------------------------|
| 200    | OK                 | La solicitud se procesó con éxito y el servidor envió una respuesta. |
| 201    | Created            | Un nuevo recurso fue creado con éxito. Se utiliza en operaciones `POST`. |
| 202    | Accepted           | La solicitud fue aceptada pero aún no se ha procesado completamente. |
| 204    | No Content         | La solicitud fue exitosa, pero no se envía contenido en la respuesta. |

**Ejemplo de uso (201 Created):**
- Método `POST /usuarios`
  - Solicitud:
    ```json
    { "nombre": "Juan", "email": "juan@example.com" }
    ```
  - Respuesta:
    ```json
    {
      "id": 1,
      "nombre": "Juan",
      "email": "juan@example.com"
    }
    ```

---

### **3xx: Redirecciones**
Indican que el cliente necesita realizar acciones adicionales para completar la solicitud. Estos códigos no son comunes en APIs REST.

| Código | Nombre             | Descripción                                                   |
|--------|--------------------|---------------------------------------------------------------|
| 301    | Moved Permanently  | El recurso solicitado se ha movido de manera permanente a otra URL. |
| 302    | Found              | El recurso se encuentra temporalmente en otra URL.           |
| 304    | Not Modified       | No hay cambios en el recurso desde la última solicitud del cliente. |

---

### **4xx: Errores del Cliente**
Estos códigos indican que la solicitud enviada por el cliente tiene algún problema.

| Código | Nombre             | Descripción                                                   |
|--------|--------------------|---------------------------------------------------------------|
| 400    | Bad Request        | La solicitud es inválida debido a errores en los datos enviados. |
| 401    | Unauthorized       | El cliente no tiene credenciales válidas para acceder al recurso. |
| 403    | Forbidden          | El cliente no tiene permisos para acceder al recurso.        |
| 404    | Not Found          | El recurso solicitado no existe.                             |
| 405    | Method Not Allowed | El método HTTP usado no está permitido para este recurso.    |
| 422    | Unprocessable Entity | El servidor entiende la solicitud, pero los datos son inválidos. |

**Ejemplo de uso (404 Not Found):**
- Método `GET /usuarios/999`:
  - Respuesta:
    ```json
    {
      "error": "Usuario no encontrado"
    }
    ```

---

### **5xx: Errores del Servidor**
Indican que hubo un problema interno en el servidor al procesar la solicitud.

| Código | Nombre             | Descripción                                                   |
|--------|--------------------|---------------------------------------------------------------|
| 500    | Internal Server Error | Ocurrió un error genérico en el servidor.                 |
| 502    | Bad Gateway        | El servidor recibió una respuesta inválida de otro servidor. |
| 503    | Service Unavailable | El servidor no está disponible temporalmente.              |
| 504    | Gateway Timeout    | El servidor no recibió respuesta a tiempo desde otro servidor. |

**Ejemplo de uso (500 Internal Server Error):**
- Método `GET /usuarios`:
  - Respuesta:
    ```json
    {
      "error": "Ocurrió un problema interno"
    }
    ```

---

## **2. Códigos Comunes en APIs REST**

En las APIs REST, los códigos más usados están en las categorías `2xx` (éxito) y `4xx` (errores del cliente). A continuación, se presentan los códigos más comunes:

| Categoría | Código | Descripción                                                   |
|-----------|--------|---------------------------------------------------------------|
| Éxito     | 200    | Operación exitosa.                                            |
|           | 201    | Recurso creado con éxito.                                     |
|           | 204    | Operación exitosa sin contenido en la respuesta.              |
| Errores   | 400    | Error en los datos enviados por el cliente.                   |
|           | 401    | Credenciales inválidas o no proporcionadas.                   |
|           | 403    | Acceso no autorizado a un recurso.                            |
|           | 404    | Recurso no encontrado.                                        |
|           | 422    | Datos inválidos en la solicitud.                              |
| Errores del servidor | 500 | Error interno en el servidor.                          |

---

## **3. Ejemplo Práctico de Códigos HTTP en una API REST con Express.js**

### **Código de la API**
```javascript
const express = require('express');
const app = express();
app.use(express.json());

let usuarios = [
    { id: 1, nombre: "Juan", email: "juan@example.com" },
    { id: 2, nombre: "Ana", email: "ana@example.com" }
];

// GET: Obtener todos los usuarios
app.get('/usuarios', (req, res) => {
    res.status(200).json(usuarios); // Código 200
});

// POST: Crear un nuevo usuario
app.post('/usuarios', (req, res) => {
    const { nombre, email } = req.body;
    if (!nombre || !email) {
        return res.status(400).json({ error: "Faltan campos requeridos" }); // Código 400
    }
    const nuevoUsuario = { id: usuarios.length + 1, nombre, email };
    usuarios.push(nuevoUsuario);
    res.status(201).json(nuevoUsuario); // Código 201
});

// GET: Obtener un usuario por ID
app.get('/usuarios/:id', (req, res) => {
    const usuario = usuarios.find(u => u.id === parseInt(req.params.id));
    if (!usuario) {
        return res.status(404).json({ error: "Usuario no encontrado" }); // Código 404
    }
    res.status(200).json(usuario); // Código 200
});

// PUT: Actualizar un usuario
app.put('/usuarios/:id', (req, res) => {
    const usuario = usuarios.find(u => u.id === parseInt(req.params.id));
    if (!usuario) {
        return res.status(404).json({ error: "Usuario no encontrado" }); // Código 404
    }
    const { nombre, email } = req.body;
    if (!nombre || !email) {
        return res.status(400).json({ error: "Faltan campos requeridos" }); // Código 400
    }
    usuario.nombre = nombre;
    usuario.email = email;
    res.status(200).json(usuario); // Código 200
});

// DELETE: Eliminar un usuario
app.delete('/usuarios/:id', (req, res) => {
    const usuarioIndex = usuarios.findIndex(u => u.id === parseInt(req.params.id));
    if (usuarioIndex === -1) {
        return res.status(404).json({ error: "Usuario no encontrado" }); // Código 404
    }
    usuarios.splice(usuarioIndex, 1);
    res.status(204).send(); // Código 204
});

// Iniciar servidor
app.listen(3000, () => {
    console.log("Servidor en http://localhost:3000");
});
```

### **Pruebas**
- **GET `/usuarios`** → 200 OK
- **POST `/usuarios` con datos incompletos** → 400 Bad Request
- **GET `/usuarios/999`** → 404 Not Found
- **DELETE `/usuarios/1` exitoso** → 204 No Content

---

## **Conclusión**
Los códigos de estado en una API REST son cruciales para comunicar al cliente el resultado de una solicitud. Usar los códigos adecuados mejora la claridad, facilita el manejo de errores y garantiza una mejor experiencia para los desarrolladores que consumen la API.