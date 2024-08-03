# Full Stack Basics
- Modelo
- Middleware
- Controladores

## Que son los modelos?
Un modelo es una representacion de una entidad o concepto en el dominio de la aplicación. En una aplicación web un modelo suele ser una clase o función que define las propiedades y comportamientos de una entidad como un usuario, un producto, una orden, etc.

### Ejemplo de modelo Usuario con Mongoose
Mongoose es una biblioteca para interactuar con MongoDB.
El modelo User tiene tres propiedades, name, email y password que son definidas en el esquema userSchema.
```js
// models/User.js
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    name: String,
    email: String,
    password: String
});

const User = mongoose.model('User', userSchema);

module.exports = User;
```

Luego se puede utilizar este modelo en el controlador para interactuar con la base de datos
```js
// controllers/userController.js
const User = require('../models/User');

// Controlador para obtener todos los usuarios
app.get('users', async(req, res) => {
    try {
        // Obtener todos los usuarios de la BBDD
        const users = await User.find();

        // Devolver la lista de usuarios en JSON
        res.json(users);

    } catch(error) {
        console.error(error);
        res.status(500).json({message: 'Error al obtener usuarios' });
    }
});
```
En este ejemplo utilizamos el modelo User para obtener todos los usuarios de la BBDD utilizando el metodo `find()`. Luego se devuelve la lista de usuarios en formato JSON.




## Que son el middleware y los controladores y cómo se relacionan?
En una aplicación web, el middleware y los controladores son conceptos clave para manejar las solicitudes HTTP y realizar acciones específicas.

El middleware se ejecuta antes de que la solicitud llegue al controlador. El middleware entonces puede:
- Modificar la solicitud antes de que llegue al controlador
- Redirigir la solicitud a un controlador diferente
- Devolver una respuesta sin llegar al controlador

Una vez que la solicitud para por el middleware, llega al controlador que se encarga de realizar la lógica de negocio y devolver una respuesta

## Middleware
**El middleware es un software que se ejecuta entre la solicitud del cliente y la respuesta del servidor**. Su propósito es realizar tareas adicionales como:
- Autenticación y autorización
- Manejo de errores
- Login y registro
- Compresión y descompresión de datos
- Manejo de CORS, Cross Origin Resource Sharing
- Enrutamiento y redirección

El middleware se ejecuta en un orden específico y cada middleware puede modificar la solicitud o la respuesta antes de pasarla al siguiente middleware. De manera que se pueden encadenar varios middleware para realizar tareas complejas.

### Ejemplo de Middleware
```js
// middleware para autenticación
const authMiddleware = (req, res, next) => {
  // lógica para autenticar al usuario
  const token = req.header('Authorization');
  if (!token) {
    return res.status(401).json({ message: 'No autorizado' });
  }
  next();
};

// middleware para manejar errores
const errorMiddleware = (err, req, res, next) => {
  // lógica para manejar errores
  console.error(err);
  res.status(500).json({ message: 'Error interno del servidor' });
};

// middleware para loguear solicitudes
const logMiddleware = (req, res, next) => {
  // lógica para loguear solicitudes
  console.log(`Solicitud ${req.method} a ${req.url}`);
  next();
};
```




## Controladores
**Los controladores son funciones que se encargan de manejar las solicitudes HTTP y devolver una respuesta**, su propósito es:
- Recibir la solicitud HTTP y los parámetros asociados
- Realizar acciones específicas como leer o escribir datos en la BBDD
- Devolver una respuesta HTTP como un objeto JSON, un archivo o un mensaje de error

Los controladores suelen ser específicos para una ruta o un conjunto de rutas y se encargan de realizar la lógica de negocio asociada a esa ruta.


## Ejemplos de Middleware y Controladores para una app CRUD con Express
### Ejemplo de Controladores
```js
// controlador para obtener todos los usuarios
app.get('/users', (req, res) => {
  // lógica para obtener todos los usuarios
  const users = [{ id: 1, name: 'Johnny' }, { id: 2, name: 'Shauna' }];
  res.json(users);
});

// controlador para crear un nuevo usuario
app.post('/users', (req, res) => {
  // lógica para crear un nuevo usuario
  const user = { id: 3, name: req.body.name };
  res.json(user);
});

// controlador para obtener un usuario por ID
app.get('/users/:id', (req, res) => {
  // lógica para obtener un usuario por ID
  const id = (link unavailable);
  const user = { id: 1, name: 'Juan' };
  res.json(user);
});

// controlador para actualizar un usuario
app.put('/users/:id', (req, res) => {
  // lógica para actualizar un usuario
  const id = (link unavailable);
  const user = { id: 1, name: req.body.name };
  res.json(user);
});

// controlador para eliminar un usuario
app.delete('/users/:id', (req, res) => {
  // lógica para eliminar un usuario
  const id = (link unavailable);
  res.json({ message: 'Usuario eliminado' });
});
```

