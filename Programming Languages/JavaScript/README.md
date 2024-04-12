# JavaScript Index
## Function declaration in JavaScript
In JavaScript, you can define functions using either the `function` keyword or by assigning them to a variable using `let` or `const` declarations. The choice between these methods often depends on the specific use case and coding style preferences.

1. **Function Declaration with `function` keyword**:
   ```javascript
   function myFunction() {
       // Function logic here
   }
   ```
   Function declarations are hoisted, which means they are processed before the execution of the code. This allows you to call the function before it's declared in the code.

2. **Function Expression with `let` or `const`**:
   ```javascript
   const myFunction = function() {
       // Function logic here
   };
   ```
   or
   ```javascript
   let myFunction = function() {
       // Function logic here
   };
   ```
   Function expressions assign the function to a variable. They are not hoisted like function declarations, so you must define them before calling them in the code.

Both methods are valid and have their own use cases:

- Use the `function` keyword for function declarations when you want the function to be hoisted or when you're defining named functions that will be reused in multiple places.
  
- Use function expressions with `let` or `const` when you want to assign a function to a variable, especially if the function will be used as an argument to another function or if it's specific to a smaller scope.

In modern JavaScript, function expressions are more commonly used due to their flexibility and compatibility with other language features like arrow functions and closures. However, the choice ultimately depends on your coding style and the requirements of your project.



## Efficiency in JavaScript loops, which one is faster?
In JavaScript, when working with arrays and objects, the choice of loop can impact performance depending on the size of the data and the specific operations you're performing within the loop. Let's discuss the most performant options for both arrays and objects:

### Arrays:

1. **`for` loop**:
   ```javascript
   for (let i = 0; i < array.length; i++) {
       // Access array[i]
   }
   ```
   This traditional `for` loop tends to be the fastest for iterating over arrays. It directly accesses elements by index and is very efficient.

2. **`forEach` method**:
   ```javascript
   array.forEach(function(item) {
       // Access item
   });
   ```
   The `forEach` method is convenient and easy to read, but it can be slightly slower compared to a `for` loop, especially in older JavaScript engines. However, modern JavaScript engines have optimized it to be quite performant.

### Objects:

1. **`for...in` loop**:
   ```javascript
   for (let key in object) {
       if (object.hasOwnProperty(key)) {
           // Access object[key]
       }
   }
   ```
   The `for...in` loop iterates over the enumerable properties of an object, including those inherited from its prototype chain. It's generally slower than `for` loops for arrays and has some caveats, like the need to check `hasOwnProperty` to avoid iterating over inherited properties.

2. **`Object.keys()` method**:
   ```javascript
   Object.keys(object).forEach(function(key) {
       // Access object[key]
   });
   ```
   This method creates an array of an object's own enumerable property names and then iterates over them using `forEach`. It's generally faster and safer than `for...in` because it only iterates over own properties.

For modern JavaScript and performance-critical applications, using `for` loops for arrays and `Object.keys()` for objects is often recommended. However, it's essential to consider readability, maintainability, and specific use cases when choosing a loop construct. Additionally, always remember to profile your code to identify performance bottlenecks accurately.



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



## Summary of JavaScript String, Arrays, Objects & ES6 Methods
### String Methods:

1. `charAt()`
2. `charCodeAt()`
3. `concat()`
4. `includes()`
5. `indexOf()`
6. `lastIndexOf()`
7. `match()`
8. `replace()`
9. `search()`
10. `slice()`
11. `split()`
12. `substring()`
13. `toLowerCase()`
14. `toUpperCase()`
15. `trim()`

### Array Methods:

1. `concat()`
2. `every()`
3. `filter()`
4. `find()`
5. `findIndex()`
6. `forEach()`
7. `includes()`
8. `indexOf()`
9. `join()`
10. `map()`
11. `pop()`
12. `push()`
13. `reduce()`
14. `reduceRight()`
15. `reverse()`
16. `shift()`
17. `slice()`
18. `some()`
19. `sort()`
20. `splice()`
21. `toString()`
22. `unshift()`

### Object Methods:

1. `Object.keys()`
2. `Object.values()`
3. `Object.entries()`
4. `Object.assign()`
5. `Object.freeze()`
6. `Object.seal()`
7. `Object.create()`
8. `Object.defineProperty()`
9. `Object.getOwnPropertyDescriptor()`
10. `Object.getOwnPropertyNames()`
11. `Object.getPrototypeOf()`
12. `Object.setPrototypeOf()`
13. `Object.is()`

### ES6 Features for Arrays and Objects:

1. `Array.from()`
2. `Array.of()`
3. `Array.isArray()`
4. `Array.prototype.find()`
5. `Array.prototype.findIndex()`
6. `Array.prototype.fill()`
7. `Array.prototype.includes()`
8. `Array.prototype.entries()`
9. `Array.prototype.keys()`
10. `Array.prototype.values()`
11. `Array.prototype.forEach()`
12. `Array.prototype.map()`
13. `Array.prototype.filter()`
14. `Array.prototype.reduce()`
15. `Array.prototype.reduceRight()`
16. `Array.prototype.some()`
17. `Array.prototype.every()`
18. `Object.entries()`
19. `Object.values()`
20. `Object.getOwnPropertyDescriptors()`
21. `Object.fromEntries()`

