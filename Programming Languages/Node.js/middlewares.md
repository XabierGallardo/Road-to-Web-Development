## **Middlewares en Express.js**

---

### **¿Qué es un Middleware?**
Un **middleware** en **Express.js** es una función que tiene acceso al **objeto de solicitud (`req`)**, al **objeto de respuesta (`res`)** y a la **siguiente función de middleware (`next`)** en el ciclo de procesamiento de una solicitud. Su propósito es realizar alguna operación antes de que la solicitud sea manejada por el controlador o antes de enviar una respuesta al cliente.

### **Sintaxis Básica**
```javascript
function middlewareEjemplo(req, res, next) {
    // Lógica del middleware
    next(); // Llama al siguiente middleware
}
```

---

### **¿Para qué se usan los Middlewares?**
Los middlewares son fundamentales para gestionar el flujo de las solicitudes en una aplicación Express.js. Algunas de sus aplicaciones más comunes incluyen:

1. **Autenticación y Autorización**: Verificar si el usuario tiene permisos para acceder a un recurso.
2. **Validación de Datos**: Validar el cuerpo, los parámetros o las cabeceras de una solicitud.
3. **Registro de Actividades**: Registrar información sobre cada solicitud (logging).
4. **Gestión de Errores**: Manejar errores globales o específicos.
5. **Procesamiento de Datos**: Parsear datos en el cuerpo de la solicitud (por ejemplo, JSON o formularios).
6. **Servir Archivos Estáticos**: Usar middleware como `express.static`.

---

### **Ciclo de Vida del Middleware**
Cuando un cliente realiza una solicitud, Express sigue un flujo secuencial a través de los middlewares definidos. Esto ocurre en tres pasos principales:

1. **Middleware Previo**: Ejecuta lógica previa al controlador.
2. **Controlador**: Maneja la lógica principal de la solicitud y prepara la respuesta.
3. **Middleware Posterior**: Realiza tareas posteriores, como el manejo de errores.

Cada middleware decide si pasa el control al siguiente middleware utilizando la función `next()`.

---

### **Tipos de Middlewares**

#### **1. Middlewares Incorporados**
Son funciones ya incluidas en Express.js para tareas comunes, como:
- `express.json()`: Parsear JSON en el cuerpo de la solicitud.
- `express.urlencoded()`: Parsear datos codificados en URL.
- `express.static()`: Servir archivos estáticos.

#### **2. Middlewares Definidos por el Usuario**
Son funciones personalizadas creadas por el desarrollador para realizar tareas específicas.

#### **3. Middlewares de Terceros**
Son paquetes instalados desde npm que extienden la funcionalidad de Express.js, como:
- `cors`: Para manejar el intercambio de recursos entre dominios.
- `morgan`: Para registrar las solicitudes.

#### **4. Middleware de Manejo de Errores**
Se usa específicamente para capturar y manejar errores en la aplicación. Su estructura incluye cuatro argumentos: `(err, req, res, next)`.

---

### **Ejemplos de Uso**

#### **1. Middleware Global**
Este middleware se ejecuta para todas las rutas de la aplicación.

```javascript
const express = require('express');
const app = express();

// Middleware global: registra cada solicitud
app.use((req, res, next) => {
    console.log(`[${new Date().toISOString()}] ${req.method} - ${req.url}`);
    next(); // Pasa al siguiente middleware
});

app.get('/', (req, res) => {
    res.send('Inicio');
});

app.listen(3000, () => console.log('Servidor corriendo en http://localhost:3000'));
```

**Salida en consola para `/`**:
```
[2024-11-19T12:00:00.000Z] GET - /
```

---

#### **2. Middleware Específico de Ruta**
Este middleware solo se aplica a una ruta específica.

```javascript
app.get('/usuarios', (req, res, next) => {
    console.log('Middleware específico para /usuarios');
    next();
}, (req, res) => {
    res.send('Lista de usuarios');
});
```

---

#### **3. Middleware Incorporado**
Se utiliza para parsear JSON del cuerpo de la solicitud.

```javascript
app.use(express.json());

app.post('/usuarios', (req, res) => {
    console.log(req.body); // Muestra los datos enviados en JSON
    res.send('Usuario creado');
});

// Solicitud: POST /usuarios
// Cuerpo: { "nombre": "Juan", "edad": 30 }
```

**Salida en consola**:
```json
{ "nombre": "Juan", "edad": 30 }
```

---

#### **4. Middleware de Terceros**
Usando el middleware `morgan` para registrar las solicitudes HTTP.

```javascript
const morgan = require('morgan');
app.use(morgan('tiny'));

app.get('/', (req, res) => {
    res.send('Inicio');
});
```

**Salida en consola para `/`**:
```
GET / 200 - - 6.100 ms
```

---

#### **5. Middleware de Manejo de Errores**
Captura errores y envía una respuesta al cliente.

```javascript
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Algo salió mal');
});

// Generar un error intencional
app.get('/error', (req, res) => {
    throw new Error('Error intencional');
});
```

**Salida en consola para `/error`**:
```
Error: Error intencional
    at ...
```

---

### **Orden de los Middlewares**

El orden en el que se declaran los middlewares es crucial porque Express.js los procesa secuencialmente. Por ejemplo:

```javascript
// Este middleware se ejecutará primero
app.use((req, res, next) => {
    console.log('Primero');
    next();
});

// Este middleware se ejecutará segundo
app.use((req, res, next) => {
    console.log('Segundo');
    next();
});

app.get('/', (req, res) => {
    res.send('Hola Mundo');
});
```

**Salida en consola para `/`**:
```
Primero
Segundo
```

---

### **Middleware Condicional**

Se puede agregar lógica para ejecutar un middleware solo si se cumplen ciertas condiciones.

```javascript
app.use((req, res, next) => {
    if (req.method === 'POST') {
        console.log('Solicitud POST detectada');
    }
    next();
});
```

---

### **Conclusión**
Los **middlewares** son componentes clave en **Express.js** para gestionar las solicitudes y respuestas. Su diseño modular y flexible permite:
- Realizar tareas comunes de forma reutilizable.
- Encadenar múltiples operaciones en un flujo de trabajo.
- Manejar errores de manera eficiente.
  
Entender y usar correctamente los middlewares es esencial para construir aplicaciones escalables y bien organizadas.