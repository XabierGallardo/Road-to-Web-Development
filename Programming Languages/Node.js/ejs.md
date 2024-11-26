## **Motores de Plantillas y EJS**

Los **motores de plantillas** son herramientas que permiten generar contenido dinámico combinando una plantilla predefinida (HTML, XML, etc.) con datos dinámicos provenientes del servidor. En el contexto de desarrollo web, los motores de plantillas son útiles para:

- Generar páginas HTML dinámicas en el servidor.
- Insertar datos en estructuras HTML repetitivas (como listas o tablas).
- Mejorar la separación entre la lógica del servidor y la presentación (frontend).

---

### **¿Qué es EJS (Embedded JavaScript)?**

**EJS** (Embedded JavaScript Templates) es un motor de plantillas simple y eficiente para Node.js que permite insertar código JavaScript directamente en archivos de plantillas. EJS es muy popular en el desarrollo con **Express.js** debido a su sintaxis sencilla y su integración fluida.

**Características de EJS:**

1. **Sintaxis Similar a HTML**: Facilita trabajar con plantillas visuales.
2. **Lógica Integrada**: Permite usar JavaScript directamente en las plantillas.
3. **Renderización Condicional y Bucles**: Ideal para trabajar con datos dinámicos.
4. **Modularidad**: Soporte para incluir plantillas parciales y reutilizables.

---

### **Cómo Usar EJS en un Proyecto de Express.js**

#### **1. Configuración del Proyecto**

1. Inicializa un proyecto de Node.js:
   ```bash
   npm init -y
   ```

2. Instala Express y EJS:
   ```bash
   npm install express ejs
   ```

3. Crea la estructura básica del proyecto:
   ```
   /mi-proyecto
   ├── views/
   │   ├── index.ejs
   │   └── about.ejs
   ├── public/
   │   └── styles.css
   ├── app.js
   ├── package.json
   ```

---

#### **2. Configurar EJS en Express**

En **Express.js**, EJS se configura como el motor de plantillas utilizando el método `app.set()`.

```javascript
const express = require('express');
const path = require('path');

const app = express();

// Configurar EJS como motor de plantillas
app.set('view engine', 'ejs');

// Configurar el directorio de vistas
app.set('views', path.join(__dirname, 'views'));

// Middleware para archivos estáticos (CSS, imágenes, etc.)
app.use(express.static(path.join(__dirname, 'public')));

// Ruta para la página principal
app.get('/', (req, res) => {
    res.render('index', { title: 'Inicio', message: '¡Bienvenido a mi sitio web!' });
});

// Ruta para la página "Acerca de"
app.get('/about', (req, res) => {
    res.render('about', { title: 'Acerca de', description: 'Esto es una página dinámica con EJS.' });
});

app.listen(3000, () => console.log('Servidor corriendo en http://localhost:3000'));
```

---

#### **3. Crear Plantillas EJS**

- **`views/index.ejs`**:
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title><%= title %></title>
      <link rel="stylesheet" href="/styles.css">
  </head>
  <body>
      <h1><%= message %></h1>
      <a href="/about">Acerca de</a>
  </body>
  </html>
  ```

- **`views/about.ejs`**:
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title><%= title %></title>
      <link rel="stylesheet" href="/styles.css">
  </head>
  <body>
      <h1><%= title %></h1>
      <p><%= description %></p>
      <a href="/">Volver al Inicio</a>
  </body>
  </html>
  ```

- **`public/styles.css`**:
  ```css
  body {
      font-family: Arial, sans-serif;
      text-align: center;
      padding: 20px;
  }

  a {
      display: block;
      margin-top: 10px;
      text-decoration: none;
      color: blue;
  }
  ```

---

#### **4. Comportamiento del Proyecto**

1. **Inicio del Servidor**:
   Ejecuta el archivo `app.js`:
   ```bash
   node app.js
   ```

2. **Páginas Dinámicas**:
   - Navega a `http://localhost:3000/` para ver la página de inicio con el mensaje dinámico.
   - Haz clic en el enlace "Acerca de" para visitar `http://localhost:3000/about`.

3. **Datos Dinámicos**:
   - Los datos enviados desde el servidor (`title`, `message`, `description`) se renderizan dinámicamente en las plantillas EJS.

---

### **Sintaxis de EJS**

1. **Insertar Variables**:
   ```html
   <%= variable %> <!-- Escapa caracteres peligrosos como <, > -->
   <%- variable %> <!-- No escapa los caracteres -->
   ```

2. **Condicionales**:
   ```html
   <% if (condicion) { %>
       <p>Condición verdadera</p>
   <% } else { %>
       <p>Condición falsa</p>
   <% } %>
   ```

3. **Bucles**:
   ```html
   <% datos.forEach(dato => { %>
       <li><%= dato %></li>
   <% }) %>
   ```

4. **Incluir Plantillas Parciales**:
   Puedes dividir tu diseño en fragmentos reutilizables:
   - **`views/header.ejs`**:
     ```html
     <header>
         <h1>Mi Sitio Web</h1>
     </header>
     ```
   - **`views/footer.ejs`**:
     ```html
     <footer>
         <p>© 2024 Mi Sitio Web</p>
     </footer>
     ```

   - **Incluirlos en otras plantillas**:
     ```html
     <% include header %>
     <p>Contenido de la página</p>
     <% include footer %>
     ```

---

### **Ventajas y Limitaciones de EJS**

#### **Ventajas**
1. **Sintaxis Simples y Familiares**: Similar a HTML con JavaScript incrustado.
2. **Facilidad de Aprendizaje**: Ideal para principiantes.
3. **Flexibilidad**: Permite lógica como bucles y condicionales.
4. **Ligero y Rápido**: No requiere precompilación.

#### **Limitaciones**
1. **Lógica Mezclada con Presentación**: Puede complicar el mantenimiento si no se gestiona bien.
2. **Menos Poderoso que Frameworks Modernos**: No tiene capacidades reactivas como React o Vue.js.
3. **Desventaja en SPA**: No es ideal para aplicaciones de página única donde se necesita una experiencia interactiva en el cliente.

---

### **Conclusión**
EJS es un motor de plantillas potente, simple y bien integrado con Express.js, ideal para proyectos donde las vistas dinámicas son esenciales. Aunque no es tan avanzado como los frameworks de frontend modernos, sigue siendo una excelente opción para aplicaciones que necesitan renderización del lado del servidor.