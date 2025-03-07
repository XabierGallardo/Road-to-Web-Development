## Variables de entorno `.env` y [modulo dotenv](https://www.npmjs.com/package/dotenv)

### **Variables de Entorno (`.env`)**

Las variables de entorno son configuraciones externas a una aplicación que permiten personalizar su comportamiento sin necesidad de modificar el código fuente. Estas variables suelen utilizarse para almacenar información sensible o dependiente del entorno, como claves API, credenciales de bases de datos, puertos de servidor, o configuraciones específicas de un entorno de desarrollo, prueba o producción.

---

### **¿Qué es un archivo `.env`?**

Un archivo `.env` es un archivo de texto plano que contiene pares clave-valor en formato:

```
NOMBRE_VARIABLE=valor
```

Ejemplo de un archivo `.env`:
```env
PORT=3000
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=12345
JWT_SECRET=mysecretkey
```

---

### **¿Por qué usar variables de entorno?**
1. **Separación de configuraciones sensibles**: Evita incluir información sensible directamente en el código fuente.
2. **Flexibilidad entre entornos**: Permite configurar una aplicación para diferentes entornos (desarrollo, prueba, producción).
3. **Facilidad de mantenimiento**: Centraliza las configuraciones en un solo lugar.
4. **Seguridad**: Al combinarse con prácticas como `.gitignore`, evita que las variables de entorno sensibles se incluyan en el control de versiones.

---

### **Cómo usar variables de entorno en una aplicación con Express**

#### **1. Configurar el archivo `.env`**
1. Crea un archivo `.env` en la raíz de tu proyecto.
2. Define las variables necesarias:
   ```env
   PORT=3000
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=12345
   ```

#### **2. Instalar y configurar `dotenv`**
El paquete `dotenv` permite cargar las variables definidas en el archivo `.env` en el objeto global `process.env`.

**Instalación:**
```bash
npm install dotenv
```

#### **3. Cargar el archivo `.env` en tu aplicación**
En el archivo principal de tu aplicación (por ejemplo, `app.js` o `server.js`), carga las variables al inicio del código:

```javascript
require('dotenv').config(); // Cargar el archivo .env
const express = require('express');

const app = express();

// Usar las variables de entorno
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
    res.send('¡Hola Mundo!');
});

app.listen(PORT, () => {
    console.log(`Servidor corriendo en el puerto ${PORT}`);
});
```

---

### **Ejemplo Completo: Variables de Entorno para una Aplicación con Base de Datos**

#### **1. Archivo `.env`**
```env
PORT=4000
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=12345
DB_NAME=mi_base_de_datos
```

#### **2. Archivo principal `app.js`**
```javascript
require('dotenv').config(); // Cargar las variables del archivo .env
const express = require('express');
const mysql = require('mysql2');

const app = express();

// Configuración del servidor
const PORT = process.env.PORT || 3000;

// Crear conexión a la base de datos
const db = mysql.createConnection({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
});

// Conectar a la base de datos
db.connect((err) => {
    if (err) {
        console.error('Error al conectar a la base de datos:', err);
        process.exit(1); // Salir si hay error crítico
    }
    console.log('Conexión exitosa a la base de datos');
});

// Rutas
app.get('/', (req, res) => {
    res.send('¡Servidor Express con variables de entorno y MySQL!');
});

// Iniciar el servidor
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
```

---

### **Buenas Prácticas**
1. **No subir archivos `.env` al control de versiones:**
   - Incluye el archivo `.env` en `.gitignore` para evitar exponer información sensible:
     ```
     # Archivo .gitignore
     .env
     ```

2. **Usar variables de entorno predeterminadas:**
   - Proporciona valores por defecto si las variables no están definidas en el entorno:
     ```javascript
     const PORT = process.env.PORT || 3000;
     ```

3. **Validar las variables de entorno:**
   - Asegúrate de que todas las variables necesarias estén definidas antes de ejecutar el servidor:
     ```javascript
     if (!process.env.DB_HOST || !process.env.DB_USER || !process.env.DB_PASSWORD) {
         console.error('Error: Faltan variables de entorno requeridas.');
         process.exit(1);
     }
     ```

4. **Usar herramientas como `dotenv-safe`:**
   - `dotenv-safe` asegura que todas las variables requeridas estén definidas y permite mantener un archivo `.env.example` como referencia para otros desarrolladores.
   ```bash
   npm install dotenv-safe
   ```

   **Ejemplo de uso:**
   ```javascript
   require('dotenv-safe').config({
       example: './.env.example', // Archivo de ejemplo con variables esperadas
   });
   ```

   Archivo `.env.example`:
   ```
   PORT=
   DB_HOST=
   DB_USER=
   DB_PASSWORD=
   ```

---

### **Ventajas del uso de `.env` con `dotenv`**
1. **Simplicidad:** Fácil de configurar y usar.
2. **Portabilidad:** Facilita compartir configuraciones entre desarrolladores sin exponer datos sensibles.
3. **Flexibilidad:** Soporte para múltiples entornos (puedes tener `.env.development`, `.env.production`, etc.).

---

### **Conclusión**
Las variables de entorno y el archivo `.env` son herramientas esenciales para manejar configuraciones sensibles y específicas de un entorno en aplicaciones con Express.js. Con el uso de paquetes como `dotenv`, puedes mantener tu código limpio, seguro y adaptable para diferentes escenarios, desde desarrollo hasta producción.