# JavaScript Key Concepts
### [JavaScript, using let or const?](https://stackoverflow.com/questions/22308071/what-is-the-difference-between-let-and-const-ecmascript-2015-es6)

#### let
- Use block scope in programming.
- for every block let create its own new scope which you cannot access in outside of that block.
- value can be changed as many times as you want.
- let is extremely useful to have for the vast majority of code. It can greatly enhance your code readability and decrease the chance of a programming error.

#### const
- It allows you to be immutable with variables.
- const is a good practice for both readability and maintainability and avoids using magic literals e.g.
- const declarations must be initialized

---

## Objects in JavaScript
En JavaScript, los objetos son una de las estructuras de datos fundamentales. Son utilizados para almacenar colecciones de datos y más complejas entidades. Un objeto es una colección de propiedades, y una propiedad es una asociación entre un nombre (o clave) y un valor. El valor de una propiedad puede ser una función, en cuyo caso la propiedad se llama método.

## Vocabulario sintaxis
## Qué es: operador, expresión y keyword?

## El objeto Promise
## [Async/Await y js asincronico](https://www.freecodecamp.org/espanol/news/como-usar-async-await-para-escribir-un-codigo-mejor-en-javascript/)

## JavaScript complex data structures
- **Objects** are used for storing key collections
- **Arrays** are used for storing ordered collections
- **Maps** are similar to objects but you can use anything as a key
- **Sets** are a great choice to store data without duplicates

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



## Restful APIs en JavaScript
Una RESTful API (Application Programming Interface) es una interfaz de programación de aplicaciones que sigue los principios de REST (Representational State Transfer). REST es un estilo de arquitectura que utiliza las capacidades del protocolo HTTP para crear, leer, actualizar y eliminar recursos. En el contexto de JavaScript, una RESTful API permite la comunicación entre un cliente (como una aplicación web o móvil) y un servidor a través de HTTP usando operaciones estándar como GET, POST, PUT, DELETE, etc.

### Características de una RESTful API

1. **Recursos identificados por URIs**:
   - Cada recurso (datos como usuarios, productos, etc.) se identifica mediante una URI (Uniform Resource Identifier).
   - Ejemplo: `https://api.example.com/users/123` podría identificar al usuario con ID 123.

2. **Operaciones CRUD mediante métodos HTTP**:
   - **GET**: Recuperar recursos.
   - **POST**: Crear nuevos recursos.
   - **PUT/PATCH**: Actualizar recursos existentes.
   - **DELETE**: Eliminar recursos.

3. **Stateless**:
   - Cada petición del cliente al servidor debe contener toda la información necesaria para entender y procesar la solicitud. El servidor no guarda el estado de la sesión entre las peticiones.

4. **Representaciones de recursos**:
   - Los recursos se pueden representar en diferentes formatos (JSON, XML, HTML, etc.), siendo JSON el más común en aplicaciones web modernas.

5. **Uniform Interface**:
   - Una interfaz uniforme simplifica y desacopla la arquitectura, lo que permite que cada parte de la aplicación (cliente y servidor) evolucione de manera independiente.

### Crear una RESTful API en JavaScript (con Node.js y Express)

A continuación, se muestra un ejemplo de cómo crear una RESTful API básica utilizando Node.js y Express:

1. **Instalar Node.js y Express**:

   ```bash
   npm init -y
   npm install express
   ```

2. **Crear un servidor básico**:

   ```javascript
   // app.js
   const express = require('express');
   const app = express();
   const port = 3000;

   app.use(express.json()); // Middleware para parsear JSON

   let users = [
       { id: 1, name: 'Alice' },
       { id: 2, name: 'Bob' },
   ];

   // Obtener todos los usuarios
   app.get('/users', (req, res) => {
       res.json(users);
   });

   // Obtener un usuario por ID
   app.get('/users/:id', (req, res) => {
       const user = users.find(u => u.id === parseInt(req.params.id));
       if (!user) return res.status(404).send('User not found');
       res.json(user);
   });

   // Crear un nuevo usuario
   app.post('/users', (req, res) => {
       const user = {
           id: users.length + 1,
           name: req.body.name
       };
       users.push(user);
       res.status(201).json(user);
   });

   // Actualizar un usuario existente
   app.put('/users/:id', (req, res) => {
       const user = users.find(u => u.id === parseInt(req.params.id));
       if (!user) return res.status(404).send('User not found');
       user.name = req.body.name;
       res.json(user);
   });

   // Eliminar un usuario
   app.delete('/users/:id', (req, res) => {
       const userIndex = users.findIndex(u => u.id === parseInt(req.params.id));
       if (userIndex === -1) return res.status(404).send('User not found');
       users.splice(userIndex, 1);
       res.status(204).send();
   });

   app.listen(port, () => {
       console.log(`Server running at http://localhost:${port}/`);
   });
   ```

3. **Estructura del proyecto**:

   ```
   my-restful-api/
   ├── app.js
   ├── package.json
   └── package-lock.json
   ```

### Explicación del código

- **app.js**: Este archivo contiene el código del servidor Express.
  - `express.json()`: Middleware que permite al servidor entender datos JSON en el cuerpo de las solicitudes.
  - **Rutas de la API**:
    - `GET /users`: Devuelve una lista de todos los usuarios.
    - `GET /users/:id`: Devuelve un usuario específico basado en el ID.
    - `POST /users`: Crea un nuevo usuario.
    - `PUT /users/:id`: Actualiza un usuario existente basado en el ID.
    - `DELETE /users/:id`: Elimina un usuario basado en el ID.

### Probar la API

Puedes probar la API utilizando herramientas como Postman o curl. Aquí hay algunos ejemplos de cómo hacer peticiones:

- **Obtener todos los usuarios**:
  ```bash
  curl http://localhost:3000/users
  ```

- **Obtener un usuario por ID**:
  ```bash
  curl http://localhost:3000/users/1
  ```

- **Crear un nuevo usuario**:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name": "Charlie"}' http://localhost:3000/users
  ```

- **Actualizar un usuario**:
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"name": "Charlie Updated"}' http://localhost:3000/users/1
  ```

- **Eliminar un usuario**:
  ```bash
  curl -X DELETE http://localhost:3000/users/1
  ```

Este ejemplo te proporciona una base para crear una RESTful API en JavaScript utilizando Node.js y Express. Puedes extenderla según las necesidades de tu aplicación.

## La keyword `return`
La palabra clave `return` en JavaScript es fundamental en la definición y control del flujo de las funciones:

1. **Devolver un valor**:
- La declaración `return` se usa dentro de una función para devolver un valor al punto donde se llamó la función. Este valor puede ser de cualquier tipo: un número, una cadena, un objeto, un array, una función, etc.
```javascript
function suma(a, b) {
    return a + b;  // Devuelve la suma de a y b
}

let resultado = suma(5, 3);  // resultado es 8
```

2. **Finalizar la ejecución de una función**:
- Cuando se encuentra una declaración `return` dentro de una función, la ejecución de la función se detiene inmediatamente y se sale de ella. Cualquier código después del `return` no se ejecutará.
```javascript
function verificarNumero(num) {
    if (num > 10) {
        return "El número es mayor que 10";  // Finaliza la función aquí si la condición se cumple
    }
    return "El número es 10 o menor";  // De lo contrario, devuelve este mensaje
}

console.log(verificarNumero(15));  // "El número es mayor que 10"
console.log(verificarNumero(5));   // "El número es 10 o menor"
```

3. **Retorno implícito en funciones de flecha**:
- Las funciones de flecha (arrow functions) de una sola expresión pueden tener un retorno implícito, es decir, no necesitan la palabra clave `return`.
```javascript
const multiplicar = (a, b) => a * b;

let resultado = multiplicar(4, 2);  // resultado es 8
```

4. **Retorno sin valor**:
- Si `return` se usa sin especificar un valor, la función devolverá `undefined`.
```javascript
function sinValor() {
    return;  // No se especifica valor, devuelve undefined
}

let resultado = sinValor();  // resultado es undefined
```

5. **No usar `return` en una función**:
- Si una función no tiene una declaración `return`, también devolverá `undefined` de manera implícita.
```javascript
function funcionVacia() {
    // No hay declaración return
}

let resultado = funcionVacia();  // resultado es undefined
```

6. **Uso en combinación con otras estructuras**:
- `return` se puede usar en combinación con otras estructuras de control para gestionar el flujo de la función de manera más compleja.
```javascript
function clasificarEdad(edad) {
    if (edad < 13) {
        return "Niño";
    } else if (edad < 20) {
        return "Adolescente";
    } else {
        return "Adulto";
    }
}

console.log(clasificarEdad(10));  // "Niño"
console.log(clasificarEdad(16));  // "Adolescente"
console.log(clasificarEdad(25));  // "Adulto"
```

La palabra clave `return` en JavaScript es esencial para controlar cómo y qué valores devuelven las funciones, así como para detener la ejecución de una función en un punto específico. Esto permite a los desarrolladores escribir funciones más eficientes y controladas.

Ahora, no siempre es necesario escribir `return` en una función en JavaScript. Depende del propósito de la función y si necesitas devolver un valor específico.

### Casos donde `return` no es necesario:

1. **Funciones que no necesitan devolver un valor**:
- Algunas funciones están diseñadas para realizar acciones sin necesidad de devolver un valor. Estas funciones realizan tareas como modificar variables globales, actualizar el DOM, o registrar información en la consola.
```javascript
function saludar() {
    console.log("Hola, mundo!");
}

saludar();  // "Hola, mundo!" se muestra en la consola, pero no se devuelve ningún valor
```

2. **Funciones que se usan por sus efectos secundarios**:
- Si el objetivo de la función es tener efectos secundarios (por ejemplo, modificar un objeto o actualizar la interfaz de usuario), no necesitas `return`.
```javascript
let contador = 0;

function incrementarContador() {
    contador++;
}

incrementarContador();
console.log(contador);  // 1
```

3. **Funciones que actúan como manejadores de eventos**:
- Los manejadores de eventos a menudo no necesitan devolver un valor ya que su propósito es manejar una interacción del usuario.
```javascript
document.getElementById('miBoton').addEventListener('click', function() {
    alert('Botón clickeado');
});
```

### Casos donde `return` es necesario:

1. **Funciones que necesitan devolver un valor**:
- Si quieres que la función proporcione un valor que pueda ser utilizado en otra parte del código, necesitas usar `return`.
```javascript
function obtenerAreaRectangulo(ancho, alto) {
    return ancho * alto;
}

let area = obtenerAreaRectangulo(5, 3);  // area es 15
```

2. **Funciones de flecha con retorno implícito**:
- Las funciones de flecha con una sola expresión tienen un retorno implícito, por lo que no necesitas escribir `return`.
```javascript
const multiplicar = (a, b) => a * b;

let resultado = multiplicar(4, 2);  // resultado es 8
```

3. **Detener la ejecución de la función**:
- Puedes usar `return` para detener la ejecución de la función en un punto específico.
```javascript
function verificarNumero(num) {
    if (num > 10) {
        return "El número es mayor que 10";
    }
    console.log("Esta línea no se ejecutará si el número es mayor que 10");
    return "El número es 10 o menor";
}
```

En resumen, no siempre es necesario escribir `return` en una función en JavaScript. La necesidad de usar `return` depende del comportamiento que se espera de la función y si se requiere que la función devuelva un valor específico o simplemente realice una acción.

## El ámbito léxico en JavaScript
El **ámbito léxico** (también conocido como **contexto léxico** o **alcance léxico**) en JavaScript se refiere a la manera en que el intérprete de JavaScript determina el acceso a las variables basándose en la estructura física del código, es decir, cómo y dónde están declaradas las funciones y variables en el código fuente.

### Explicación del Ámbito Léxico

1. **Declaración de Variables y Funciones**:
   - Cuando una variable o función se declara dentro de otra función, se encuentra en el ámbito léxico de esa función.
   - Esto significa que la variable o función está disponible en la función donde se declara y en cualquier función anidada dentro de ella.

2. **Ámbito en Tiempo de Escritura**:
   - El ámbito léxico se define en tiempo de escritura, no en tiempo de ejecución. Esto significa que la estructura del código tal como está escrito determina qué variables y funciones están disponibles en un punto específico del código.

### Ejemplo Básico

```javascript
function outerFunction() {
    const outerVariable = 'Estoy en la función externa';

    function innerFunction() {
        console.log(outerVariable);
    }

    innerFunction();
}

outerFunction(); // 'Estoy en la función externa'
```

En este ejemplo:
- `outerFunction` contiene una variable `outerVariable` y una función `innerFunction`.
- `innerFunction` tiene acceso a `outerVariable` debido al ámbito léxico, ya que está definida dentro de `outerFunction`.

### Anidamiento de Ámbitos Léxicos

El ámbito léxico puede anidarse. Cada función crea un nuevo ámbito léxico que puede acceder a variables en su propio ámbito y en cualquier ámbito que lo contenga.

```javascript
function outerFunction() {
    const outerVariable = 'Estoy en la función externa';

    function middleFunction() {
        const middleVariable = 'Estoy en la función intermedia';

        function innerFunction() {
            console.log(outerVariable); // Accede a la variable del ámbito exterior
            console.log(middleVariable); // Accede a la variable del ámbito inmediato
        }

        innerFunction();
    }

    middleFunction();
}

outerFunction();
// 'Estoy en la función externa'
// 'Estoy en la función intermedia'
```

En este ejemplo:
- `innerFunction` puede acceder tanto a `middleVariable` (del ámbito de `middleFunction`) como a `outerVariable` (del ámbito de `outerFunction`).

### Beneficios del Ámbito Léxico

1. **Predecibilidad**:
   - Dado que el ámbito léxico se determina en tiempo de escritura, es predecible y comprensible al leer el código.

2. **Encapsulación**:
   - Permite la encapsulación de variables dentro de funciones, evitando conflictos de nombres y accesos no deseados.

3. **Closures**:
   - El ámbito léxico es fundamental para entender los closures, ya que los closures recuerdan su ámbito léxico incluso después de que la función externa haya terminado de ejecutarse.

### Diferencia entre Ámbito Léxico y Ámbito Dinámico

- **Ámbito Léxico**: Determinado por la estructura del código fuente. JavaScript usa ámbito léxico.
- **Ámbito Dinámico**: Determinado por el orden de ejecución del código (el ámbito se determina en tiempo de ejecución). Algunos lenguajes como Lisp pueden usar ámbito dinámico.

### Conclusión

El ámbito léxico en JavaScript define cómo las variables y funciones se resuelven en base a su ubicación en el código fuente. Este concepto es crucial para entender cómo las variables son accesibles y cómo funcionan los closures, lo que a su vez permite la escritura de código más robusto y predecible.

## Concepto de estado en JavaScript
En JavaScript, el **estado** se refiere a los datos que una aplicación o componente maneja en un momento dado. Es una forma de almacenar y gestionar información que puede cambiar con el tiempo a medida que los usuarios interactúan con la aplicación.

### Estado en JavaScript

El estado se puede gestionar a diferentes niveles, incluyendo:

1. **Variables**:
   - Las variables almacenan datos que pueden cambiar a lo largo del tiempo. Por ejemplo, un contador que incrementa su valor cada vez que se presiona un botón.

   ```javascript
   let count = 0;
   
   function increment() {
       count++;
       console.log(count);
   }
   
   increment(); // 1
   increment(); // 2
   ```

2. **Objetos y Arrays**:
   - Los objetos y arrays pueden almacenar estados más complejos y estructurados. Por ejemplo, un objeto que almacena información de un usuario.

   ```javascript
   let user = {
       name: "Alice",
       age: 25
   };
   
   function updateAge(newAge) {
       user.age = newAge;
   }
   
   updateAge(26);
   console.log(user.age); // 26
   ```

3. **Closures**:
   - Los closures permiten mantener el estado dentro de funciones anidadas, lo cual es útil para la encapsulación.

   ```javascript
   function createCounter() {
       let count = 0;
       return function() {
           count++;
           return count;
       };
   }
   
   const counter = createCounter();
   console.log(counter()); // 1
   console.log(counter()); // 2
   ```

### Estado de las Variables

El **estado de las variables** se refiere al valor actual de una variable en un momento específico. Las variables pueden tener diferentes estados a lo largo del tiempo debido a las operaciones que se realizan sobre ellas.

### Ejemplo de Estado de Variables

Consideremos un ejemplo donde el estado de una variable cambia con el tiempo:

```javascript
let mood = "happy";

function changeMood(newMood) {
    mood = newMood;
}

console.log(mood); // "happy"
changeMood("sad");
console.log(mood); // "sad"
```

En este ejemplo:
- La variable `mood` inicialmente tiene el estado "happy".
- Después de llamar a `changeMood("sad")`, el estado de `mood` cambia a "sad".

### Estado en Componentes React (ejemplo avanzado)

En bibliotecas como React, el estado es un concepto central para gestionar datos dentro de componentes. Cada componente puede tener su propio estado que puede cambiar en respuesta a eventos.

```javascript
import React, { useState } from 'react';

function Counter() {
    const [count, setCount] = useState(0);

    function increment() {
        setCount(count + 1);
    }

    return (
        <div>
            <p>{count}</p>
            <button onClick={increment}>Increment</button>
        </div>
    );
}
```

En este ejemplo de React:
- `useState` se usa para declarar una variable de estado `count` y una función `setCount` para actualizar su estado.
- Cada vez que se llama a `setCount`, el estado del componente se actualiza y React vuelve a renderizar el componente con el nuevo estado.

### Conclusión
El estado en JavaScript se refiere a los datos que una aplicación o componente gestiona y que pueden cambiar con el tiempo. Las variables, objetos, arrays, y closures son formas comunes de mantener el estado. En frameworks como React, el estado se maneja explícitamente para permitir que los componentes respondan a las interacciones del usuario de manera dinámica y eficiente.
