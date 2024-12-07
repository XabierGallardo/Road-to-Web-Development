# **Modelo-Vista-Controlador (MVC) en Express**

El patrón **Modelo-Vista-Controlador (MVC)** es una arquitectura de diseño de software que organiza y separa una aplicación en tres componentes principales: **Modelo**, **Vista** y **Controlador**. Este patrón es especialmente útil en aplicaciones web porque mejora la **modularidad**, **mantenibilidad** y **escalabilidad** del código.

---

### **Componentes del patrón MVC**

1. **Modelo (Model):**
   - Es el encargado de la **lógica de datos** y la interacción con la base de datos.
   - Define cómo se estructuran y gestionan los datos en la aplicación.
   - Realiza operaciones como consultas, inserciones, actualizaciones o eliminaciones.

2. **Vista (View):**
   - Es responsable de la **presentación de la información** al usuario.
   - En una aplicación web, las vistas suelen ser plantillas HTML renderizadas en el navegador.
   - Recibe datos del controlador y los muestra al usuario de manera adecuada.

3. **Controlador (Controller):**
   - Es el **intermediario** entre el Modelo y la Vista.
   - Maneja las solicitudes del usuario, interactúa con el Modelo para obtener o modificar datos, y selecciona la Vista adecuada para la respuesta.
   - Contiene la lógica de control, pero no interactúa directamente con la base de datos ni genera las vistas.

---

### **¿Por qué usar MVC en Express?**

Express es un framework minimalista y flexible que permite implementar MVC para:
1. **Separar responsabilidades:** Cada componente tiene su propia tarea, lo que facilita la lectura y mantenimiento del código.
2. **Reutilización de código:** Los modelos y las vistas pueden ser reutilizados en diferentes partes de la aplicación.
3. **Escalabilidad:** Ayuda a estructurar aplicaciones más grandes de manera ordenada.

---

### **Ejemplo completo de una aplicación Express con MVC**

#### **Estructura del proyecto**
```
/mi-aplicacion
│
├── /controllers       # Controladores (lógica de negocio)
│   └── userController.js
│
├── /models            # Modelos (gestión de datos)
│   └── userModel.js
│
├── /routes            # Rutas (asignan URLs a controladores)
│   └── userRoutes.js
│
├── /views             # Vistas (plantillas HTML/EJS)
│   └── index.ejs
│   └── user.ejs
│
├── app.js             # Archivo principal
├── package.json       # Configuración del proyecto
├── .env               # Variables de entorno
└── /node_modules      # Dependencias
```

---

### **1. Modelo (Model)**

**Archivo: `models/userModel.js`**

Aquí definimos cómo se gestionan los datos relacionados con los usuarios. En este ejemplo, usamos una base de datos MySQL con el módulo `mysql2`.

```javascript
const db = require('../config/db'); // Conexión a la base de datos

// Función para obtener todos los usuarios
const getAllUsers = () => {
    return new Promise((resolve, reject) => {
        db.query('SELECT * FROM users', (err, results) => {
            if (err) reject(err);
            resolve(results);
        });
    });
};

// Función para agregar un usuario
const addUser = (user) => {
    return new Promise((resolve, reject) => {
        db.query('INSERT INTO users SET ?', user, (err, results) => {
            if (err) reject(err);
            resolve(results);
        });
    });
};

module.exports = {
    getAllUsers,
    addUser,
};
```

---

### **2. Controlador (Controller)**

**Archivo: `controllers/userController.js`**

El controlador actúa como intermediario entre las rutas y los modelos. Aquí gestionamos las solicitudes HTTP y las respuestas.

```javascript
const userModel = require('../models/userModel');

// Controlador para obtener todos los usuarios
const getUsers = async (req, res) => {
    try {
        const users = await userModel.getAllUsers();
        res.render('user', { users }); // Renderiza la vista 'user.ejs' con los datos
    } catch (error) {
        res.status(500).send('Error al obtener usuarios');
    }
};

// Controlador para agregar un usuario
const createUser = async (req, res) => {
    try {
        const newUser = req.body;
        await userModel.addUser(newUser);
        res.redirect('/users'); // Redirige a la lista de usuarios
    } catch (error) {
        res.status(500).send('Error al agregar usuario');
    }
};

module.exports = {
    getUsers,
    createUser,
};
```

---

### **3. Rutas (Routes)**

**Archivo: `routes/userRoutes.js`**

Define las rutas que conectan las solicitudes HTTP con los controladores.

```javascript
const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');

// Ruta para obtener todos los usuarios
router.get('/', userController.getUsers);

// Ruta para agregar un usuario
router.post('/add', userController.createUser);

module.exports = router;
```

---

### **4. Vistas (Views)**

**Archivo: `views/user.ejs`**

Esta es la plantilla que muestra los usuarios al cliente. Utiliza el motor de plantillas EJS para renderizar datos dinámicos.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Usuarios</title>
</head>
<body>
    <h1>Lista de Usuarios</h1>
    <ul>
        <% users.forEach(user => { %>
            <li><%= user.name %> - <%= user.email %></li>
        <% }) %>
    </ul>

    <h2>Agregar Usuario</h2>
    <form action="/users/add" method="POST">
        <input type="text" name="name" placeholder="Nombre" required>
        <input type="email" name="email" placeholder="Correo" required>
        <button type="submit">Agregar</button>
    </form>
</body>
</html>
```

---

### **5. Archivo principal**

**Archivo: `app.js`**

Este archivo inicializa la aplicación Express y monta las rutas.

```javascript
require('dotenv').config(); // Cargar variables de entorno
const express = require('express');
const app = express();
const userRoutes = require('./routes/userRoutes');

// Configuración del middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Motor de plantillas
app.set('view engine', 'ejs');

// Rutas principales
app.use('/users', userRoutes);

// Iniciar servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
```

---

### **Ventajas de usar MVC en Express**

1. **Separación de responsabilidades:**
   - El modelo maneja los datos.
   - El controlador actúa como intermediario.
   - La vista maneja la presentación.

2. **Facilidad de mantenimiento:**
   - Los cambios en la presentación o lógica no afectan al resto de la aplicación.

3. **Escalabilidad:**
   - La estructura MVC facilita la ampliación de la funcionalidad del proyecto.

4. **Reutilización:**
   - Los modelos y vistas pueden ser reutilizados en diferentes partes del proyecto.

---

### **Conclusión**

El patrón **Modelo-Vista-Controlador (MVC)** organiza una aplicación en componentes separados que trabajan en conjunto para manejar las solicitudes del usuario. En un proyecto Express, implementar MVC facilita el desarrollo colaborativo, el mantenimiento y la escalabilidad. Con esta estructura, puedes manejar desde pequeñas aplicaciones hasta grandes proyectos de forma eficiente y ordenada.