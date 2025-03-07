# Estructura de directorios de una aplicacion Express.js

La estructura de directorios de una aplicación **Express.js** completa y bien organizada facilita el desarrollo, la colaboración y el mantenimiento del proyecto. La siguiente es una estructura comúnmente utilizada en aplicaciones Express de gran tamaño.

---

### **Estructura de Directorios**

```
project-root/
├── config/
├── controllers/
├── middlewares/
├── models/
├── public/
│   ├── css/
│   ├── js/
│   └── images/
├── routes/
├── services/
├── utils/
├── views/
│   ├── partials/
│   ├── layouts/
│   └── pages/
├── tests/
├── logs/
├── database/
│   └── migrations/
│   └── seeds/
├── .env
├── app.js
├── package.json
├── README.md
```

---

### **Descripción de Cada Carpeta y Archivo**

#### **1. `config/`**
Contiene archivos relacionados con la configuración de la aplicación.

- **`config/database.js`**: Configuración de la base de datos, como credenciales y opciones de conexión.
- **`config/app.js`**: Configuración general de la aplicación (puerto, modos de depuración, etc.).
- **`config/env.js`**: Manejo de variables de entorno.

---

#### **2. `controllers/`**
Define la lógica de negocio para manejar las solicitudes entrantes.

- **`user.controller.js`**: Funciones para manejar rutas relacionadas con usuarios.
  ```javascript
  export const getAllUsers = async (req, res) => {
      // Lógica para obtener usuarios
  };
  ```
- **`course.controller.js`**: Funciones para manejar rutas relacionadas con cursos.
- **`auth.controller.js`**: Lógica para el manejo de autenticación.

---

#### **3. `middlewares/`**
Almacena middlewares personalizados que se ejecutan antes o después de las solicitudes.

- **`auth.middleware.js`**: Verificación de usuarios autenticados.
- **`error.middleware.js`**: Manejo de errores global.
- **`logger.middleware.js`**: Registro de solicitudes HTTP.

---

#### **4. `models/`**
Define las estructuras de datos y la interacción con la base de datos.

- **`user.model.js`**: Modelo para la tabla de usuarios.
  ```javascript
  import { DataTypes } from "sequelize";
  import sequelize from "../config/database.js";

  const User = sequelize.define("User", {
      id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true },
      name: { type: DataTypes.STRING, allowNull: false },
  });

  export default User;
  ```
- **`course.model.js`**: Modelo para la tabla de cursos.
- **`index.js`**: Archivo para consolidar y exportar todos los modelos.

---

#### **5. `public/`**
Carpeta estática para servir archivos públicos.

- **`css/`**: Hojas de estilos CSS.
  - `styles.css`
- **`js/`**: Archivos JavaScript del lado del cliente.
  - `app.js`
- **`images/`**: Archivos de imágenes estáticas.

---

#### **6. `routes/`**
Contiene las definiciones de rutas de la aplicación.

- **`user.routes.js`**: Define rutas para usuarios.
  ```javascript
  import { Router } from "express";
  import { getAllUsers } from "../controllers/user.controller.js";

  const router = Router();

  router.get("/", getAllUsers);

  export default router;
  ```
- **`auth.routes.js`**: Define rutas para autenticación.
- **`index.js`**: Archivo para combinar y registrar todas las rutas.

---

#### **7. `services/`**
Implementa lógica compleja de negocio, como integración con APIs externas.

- **`email.service.js`**: Funciones para enviar correos electrónicos.
- **`payment.service.js`**: Lógica para integrar con servicios de pago.

---

#### **8. `utils/`**
Contiene funciones auxiliares que se usan en múltiples partes de la aplicación.

- **`date.util.js`**: Funciones para formatear fechas.
- **`response.util.js`**: Plantillas para respuestas HTTP.
- **`validation.util.js`**: Validaciones personalizadas.

---

#### **9. `views/`**
Almacena las plantillas EJS o cualquier motor de vistas que estés usando.

- **`partials/`**: Fragmentos reutilizables de la interfaz.
  - `header.ejs`
  - `footer.ejs`
- **`layouts/`**: Diseños generales para las páginas.
  - `main.ejs`
- **`pages/`**: Vistas específicas.
  - `index.ejs`
  - `user.ejs`

---

#### **10. `tests/`**
Archivos para pruebas unitarias y de integración.

- **`user.test.js`**: Pruebas para el controlador de usuarios.
- **`course.test.js`**: Pruebas para el controlador de cursos.

---

#### **11. `logs/`**
Contiene archivos de registro generados por la aplicación.

- **`app.log`**: Registro general de la aplicación.
- **`error.log`**: Registro de errores.

---

#### **12. `database/`**
Almacena migraciones y semillas para la base de datos.

- **`migrations/`**: Archivos para estructurar la base de datos.
- **`seeds/`**: Datos iniciales para poblar la base de datos.

---

#### **13. Archivos raíz**

- **`.env`**: Archivo para variables de entorno (nunca debe compartirse públicamente).
  ```
  PORT=3000
  DATABASE_URL=mysql://user:password@localhost:3306/mydb
  ```
- **`app.js`**: Punto de entrada de la aplicación.
  ```javascript
  import express from "express";
  import userRoutes from "./routes/user.routes.js";

  const app = express();

  app.use(express.json());
  app.use("/users", userRoutes);

  app.listen(3000, () => console.log("Servidor corriendo en el puerto 3000"));
  ```
- **`package.json`**: Archivo de configuración de Node.js que contiene dependencias y scripts.

---

### **Ventajas de esta Estructura**

1. **Escalabilidad**: Permite agregar nuevas funcionalidades sin desorganizar el proyecto.
2. **Modularidad**: Cada parte del proyecto tiene su propio lugar definido.
3. **Mantenibilidad**: Facilita el diagnóstico y solución de problemas.
4. **Reutilización**: Fragmentos de código reutilizables, como funciones en `utils` o vistas parciales.

### **Conclusión**
Esta estructura no es estricta y puede adaptarse según las necesidades específicas del proyecto. El objetivo principal es mantener la organización y la claridad a medida que la aplicación crece.