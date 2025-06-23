# Express II

## Refactorizar y aplicar el patron MVC
Refactorizar un proyecto y aplicar el patrón **MVC** (Modelo-Vista-Controlador) en una aplicación de **Express.js** implica reorganizar y mejorar el código para que sea más **modular, mantenible y escalable**.

---

### 🔄 ¿Qué significa **refactorizar**?

**Refactorizar** es **reestructurar** el código sin cambiar su funcionalidad externa. El objetivo es mejorar su legibilidad, reducir duplicación, facilitar pruebas y hacer que el mantenimiento sea más fácil.

En un proyecto Express, esto podría significar:

* Separar rutas, controladores, modelos, y utilidades en archivos distintos.
* Eliminar código duplicado.
* Usar middleware de forma eficiente.
* Organizar mejor los archivos y carpetas.

---

### 🧠 ¿Qué es el patrón **MVC**?

**MVC** divide la aplicación en tres capas:

1. **Modelo (Model):**  

   * Gestiona los datos y la lógica de negocio. *La lógica de negocio se refiere a las reglas y procesos que definen cómo funciona la aplicación, incluyendo las decisiones y operaciones que se realizan para cumplir los objetivos del negocio*.
   * Se comunica con la base de datos.
   * En Express.js, son los archivos donde defines los esquemas y métodos para acceder/modificar datos (por ejemplo, usando Mongoose si es MongoDB).

2. **Vista (View):**

   * Presenta los datos al usuario.
   * En Express.js, puede ser una plantilla (como EJS, Handlebars, Pug), o simplemente se maneja con JSON si es una API REST.

3. **Controlador (Controller):**

   * Contiene la lógica que conecta modelos y vistas.
   * Recibe las peticiones del cliente, llama a los modelos si es necesario, y devuelve una respuesta.

---

### 📦 Aplicando MVC en una app Express.js

Supón que tienes un proyecto Express desorganizado. Así podrías reorganizarlo siguiendo MVC:

```
/project
│
├── app.js                  -> Configuración principal de Express
├── routes/
│   └── userRoutes.js       -> Define rutas para /users
├── controllers/
│   └── userController.js   -> Lógica para manejar peticiones de usuarios
├── models/
│   └── userModel.js        -> Esquema del usuario y funciones de DB
├── views/
│   └── userView.ejs        -> Plantillas si usas vistas (opcional en APIs)
└── config/
    └── db.js               -> Conexión a la base de datos
```

---

### ✅ Ventajas de usar MVC

* **Organización clara del código.**
* **Reutilización de componentes.**
* **Fácil mantenimiento.**
* **Escalabilidad para proyectos grandes.**

