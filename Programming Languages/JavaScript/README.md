# JavaScript Index
## Placing our js `<script>` before the `</body>` tag
Placing the `<script>` tag before the `</body>` tag in an HTML document is considered a best practice for several reasons:

1. **Page Loading Performance**: Placing `<script>` tags at the end of the `<body>` allows the HTML content to load first. JavaScript execution can block rendering, which means if scripts are placed in the `<head>` section, the browser will pause rendering until the script is fetched and executed. Moving scripts to the end of the body ensures that the page content is displayed to users more quickly.

2. **Progressive Rendering**: By loading and displaying the HTML content first, users can see and interact with the page while JavaScript is still being downloaded and executed. This provides a better user experience, especially on slower connections or devices.

3. **Avoiding Render Blocking**: Placing `<script>` tags at the end of the body minimizes render-blocking behavior. Browsers typically download and execute JavaScript files sequentially, which can delay the rendering of subsequent HTML content if scripts are placed in the `<head>`. By placing scripts at the end of the body, HTML content can be parsed and displayed without waiting for scripts to download and execute.

4. **Content Accessibility**: Ensuring that HTML content is rendered and accessible before JavaScript execution enhances accessibility. Screen readers and other assistive technologies can start reading and interpreting the content while scripts are still loading and executing.

5. **Reducing Flash of Unstyled Content (FOUC)**: Placing scripts at the end of the body helps reduce the likelihood of FOUC, where content is briefly displayed without styles due to delayed script execution. By the time scripts are executed, the HTML content is already rendered, and stylesheets have been applied, minimizing the chance of FOUC.

Overall, placing `<script>` tags before the `</body>` tag improves page loading performance, enhances user experience, and ensures content accessibility by prioritizing the rendering of HTML content before JavaScript execution.

## This en JavaScript
En JavaScript, `this` es una palabra clave especial que se refiere al contexto de ejecución actual. El valor de `this` depende de cómo se llama la función en la que se encuentra y puede variar según el contexto de ejecución en el que se utiliza.

La referencia `this` generalmente se utiliza dentro de métodos de objetos para hacer referencia al objeto en el que se está llamando el método. Por ejemplo:

```javascript
const persona = {
  nombre: 'Juan',
  saludar: function() {
    console.log('Hola, soy ' + this.nombre);
  }
};

persona.saludar(); // Imprime: Hola, soy Juan
```

En este ejemplo, `this` dentro del método `saludar` hace referencia al objeto `persona`, ya que `saludar` fue llamado en el contexto de `persona`.

Sin embargo, el valor de `this` puede cambiar según el contexto de ejecución. Por ejemplo:

```javascript
function mostrarNombre() {
  console.log('Mi nombre es ' + this.nombre);
}

const persona1 = {
  nombre: 'Juan',
  mostrarNombre: mostrarNombre
};

const persona2 = {
  nombre: 'María',
  mostrarNombre: mostrarNombre
};

persona1.mostrarNombre(); // Imprime: Mi nombre es Juan
persona2.mostrarNombre(); // Imprime: Mi nombre es María
```

En este caso, `this` dentro de la función `mostrarNombre` cambia su valor según el objeto que llama al método `mostrarNombre`.

Es importante tener en cuenta que el valor de `this` puede ser más complicado en ciertas situaciones, especialmente cuando se utiliza en funciones flecha (`=>`), dentro de callbacks, o cuando se utiliza en métodos de clases. En tales casos, el valor de `this` puede ser lexico y no referirse al contexto de ejecución actual, sino al contexto en el que se definió la función.

Comprender cómo `this` funciona en JavaScript es fundamental para escribir código correcto y evitar errores comunes relacionados con el alcance y el contexto de ejecución.

## [JavaScript W3 Schools](https://www.w3schools.com/js/default.asp)
## [HTTP Networking in JavaScript, Handbook](https://www.freecodecamp.org/news/http-full-course/)

## JS Array Methods
<p align="center">
        <img src="media/JavaScript Array Methods.jpeg" alt="JavaScript Array Methods">
</p>


## ES6 Cheatsheet
<p align="center">
        <img src="media/ES6 Cheatsheet.png" alt="ES6 Cheatsheet">
</p>

<p align="center">
        <img src="media/ES6 Cheatsheet 2.png" alt="ES6 Cheatsheet 2">
</p>

## Parse JSON to other languages [Tool](https://app.quicktype.io/)
> Herramienta para parsear codigo JSON a varios lenguajes.
> Me resultó muy práctica para crear interfaces y tipos en base a los datos traídos por una API en Typescript. Ya que muchas veces tenemos que crear las interfaces nosotros mismos esto podría ahorrar bastante tiempo.
> También posee una extensión para VSCode y Visual Studio. 
<p align="center">
        <img src="media/quicktype1.jpeg" alt="Quicktype 1">
        <img src="media/quicktype2.jpeg" alt="Quicktype 2">
</p>

