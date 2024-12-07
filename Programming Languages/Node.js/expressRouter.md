# `express.Router`

### **`express.Router` y su uso en aplicaciones Express**

`express.Router` es una funcionalidad de Express que permite crear **módulos de rutas** para organizar y estructurar una aplicación web o API de manera más eficiente. En lugar de definir todas las rutas en un solo archivo, puedes agruparlas lógicamente en módulos separados, mejorando la claridad y el mantenimiento del código.

---

### **¿Qué es `express.Router`?**
- Es un mini-manejador de rutas en Express que actúa como una "mini aplicación".
- Puedes definir rutas (por ejemplo, `GET`, `POST`, `PUT`, etc.) en el objeto `Router` y luego montarlo en la aplicación principal.
- Ayuda a separar y modularizar las rutas, especialmente en aplicaciones grandes.

---

### **¿Cómo usar `express.Router`?**
1. **Crear un módulo de rutas**:
   Define un conjunto de rutas en un archivo separado usando `express.Router`.

2. **Montar las rutas en la aplicación principal**:
   Usa `app.use()` para registrar las rutas definidas en el módulo.

#### **Ejemplo de uso de `express.Router`:**
**Archivo `routes/users.js`:**
```javascript
const express = require('express');
const router = express.Router();

// Ruta para obtener todos los usuarios
router.get('/', (req, res) => {
  res.send('Lista de usuarios');
});

// Ruta para obtener un usuario específico por ID
router.get('/:id', (req, res) => {
  res.send(`Usuario con ID: ${req.params.id}`);
});

// Ruta para crear un nuevo usuario
router.post('/', (req, res) => {
  res.send('Usuario creado');
});

module.exports = router;
```

**Archivo `app.js`:**
```javascript
const express = require('express');
const app = express();
const userRoutes = require('./routes/users');

// Middleware para usar las rutas de usuarios
app.use('/users', userRoutes);

app.listen(3000, () => {
  console.log('Servidor ejecutándose en http://localhost:3000');
});
```

#### **Funcionamiento:**
1. Al acceder a `http://localhost:3000/users`, se ejecuta la ruta raíz de `users.js`.
2. Al acceder a `http://localhost:3000/users/123`, se ejecuta la ruta que devuelve un usuario específico.

---

### **`app.get()` vs `app.use()`**

Ambos son métodos de Express que se usan para manejar solicitudes, pero tienen propósitos diferentes:

#### **`app.get()`**
- Maneja específicamente solicitudes HTTP **GET**.
- Se usa para definir una ruta y su lógica correspondiente.
- Por ejemplo, para manejar `GET /ruta`:

```javascript
app.get('/ruta', (req, res) => {
  res.send('Respuesta para GET /ruta');
});
```

#### **`app.use()`**
- Registra un middleware o grupo de rutas en una aplicación.
- Puede usarse con rutas específicas o sin especificar una ruta:
  - Si no se especifica una ruta, el middleware se aplica a todas las solicitudes.
  - Si se especifica una ruta, se aplica a esa ruta y sus subrutas.
- Se utiliza para registrar módulos de rutas (`Router`), middlewares, o lógica general.

```javascript
app.use('/ruta', (req, res, next) => {
  console.log('Middleware para /ruta');
  next(); // Pasa al siguiente middleware o manejador
});
```

#### **Cuándo usar cada uno:**

| Método         | Usos principales                                                                                      |
|----------------|------------------------------------------------------------------------------------------------------|
| **`app.get()`** | Para manejar solicitudes HTTP GET en rutas específicas (por ejemplo, mostrar datos).                |
| **`app.use()`** | - Para registrar middlewares.                                                                       |
|                | - Para montar rutas modulares creadas con `express.Router`.                                          |
|                | - Para aplicar lógica o configuración a varias rutas (por ejemplo, autenticación o análisis de JSON). |

---

### **Rutas modulares con `app.use()`**
Cuando trabajas con rutas modulares, usas `app.use()` para montar los módulos en una ruta base.

#### Ejemplo:
1. Archivo `routes/products.js`:
```javascript
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.send('Lista de productos');
});

router.post('/', (req, res) => {
  res.send('Producto creado');
});

module.exports = router;
```

2. Archivo principal `app.js`:
```javascript
const express = require('express');
const app = express();
const productRoutes = require('./routes/products');

// Montar el módulo de rutas en la base "/products"
app.use('/products', productRoutes);

app.listen(3000, () => {
  console.log('Servidor corriendo en http://localhost:3000');
});
```

#### Resultado:
- **GET `/products`** → "Lista de productos".
- **POST `/products`** → "Producto creado".

---

### **Resumen clave:**
- **`express.Router`**: Ayuda a modularizar las rutas, organizándolas en archivos separados.
- **`app.get()`**: Maneja solicitudes específicas de tipo HTTP GET.
- **`app.use()`**: Monta middlewares o módulos de rutas en una aplicación, aplicándolos globalmente o a rutas específicas.
- Usar rutas modulares es fundamental en aplicaciones grandes para mejorar la organización y la mantenibilidad.