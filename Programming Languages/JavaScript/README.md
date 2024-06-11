# JavaScript Roadmap
0. Basic Syntax & Concepts
1. Function types, arrow functions, "this" keyword
2. Scope, Hoisting & Closures
3. DOM & Global Objects
4. Event listeners, event bubbling y event handling
5. Callback functions
6. Async Await, Promises
7. Fetch API, RESTFUL APIS, JSON parse & JSON.stringify
8. Array Methods & String Methods
9. ES6 + JS Models (template literals, destructuring, spread operator, classes, modules import export)
10. Object Oriented Programming, prototype
11. Error Handling, try/catch, Custom errors




# 0. Basic Syntax & Concepts
## 0.1 Por qué se dice que en JavaScript todo son objetos?
En JavaScript, se dice que "todo es un objeto" porque la mayoría de las entidades y valores se comportan como objetos o pueden ser tratados como objetos, lo que proporciona una gran flexibilidad y poder al lenguaje. Aquí hay algunas razones y explicaciones más detalladas:

1. **Primitivos y objetos envolventes**:
   - JavaScript tiene tipos de datos primitivos (números, cadenas, booleanos, null, undefined, y símbolos). Sin embargo, estos primitivos pueden ser tratados temporalmente como objetos porque JavaScript proporciona objetos envolventes (wrappers) que permiten acceder a métodos y propiedades.
   - Por ejemplo, una cadena puede usar métodos de la clase `String`:
     ```javascript
     let str = "Hola";
     console.log(str.length); // 4
     console.log(str.toUpperCase()); // "HOLA"
     ```
   - Internamente, `str` es un valor primitivo, pero JavaScript lo convierte temporalmente en un objeto `String` para que se puedan usar sus métodos.

2. **Objetos y arrays**:
   - Los objetos son fundamentales en JavaScript y se utilizan para almacenar colecciones de datos y entidades más complejas.
   - Los arrays son un tipo especial de objeto con propiedades y métodos diseñados para gestionar listas de elementos:
     ```javascript
     let arr = [1, 2, 3];
     console.log(arr.length); // 3
     arr.push(4);
     console.log(arr); // [1, 2, 3, 4]
     ```

3. **Funciones como objetos**:
   - En JavaScript, las funciones son objetos de primera clase, lo que significa que pueden ser tratadas como cualquier otro objeto. Pueden tener propiedades y métodos, ser asignadas a variables, pasadas como argumentos, y devueltas por otras funciones:
     ```javascript
     function saludo() {
         console.log("Hola");
     }
     saludo.propiedad = "Soy una propiedad de la función";
     console.log(saludo.propiedad); // "Soy una propiedad de la función"
     ```

4. **Prototipos y herencia**:
   - JavaScript utiliza un sistema de herencia basado en prototipos, lo que significa que los objetos pueden heredar propiedades y métodos de otros objetos. Cada objeto tiene una propiedad interna `[[Prototype]]` (accesible a través de `__proto__` en algunos entornos) que apunta a otro objeto, formando una cadena de prototipos.
     ```javascript
     let obj = {};
     console.log(obj.toString()); // [object Object]
     ```

5. **El DOM y otros APIs**:
   - En el contexto del navegador, los elementos del DOM (Document Object Model) también son objetos, lo que permite manipular y gestionar el contenido de la página web de manera dinámica.
     ```javascript
     let elemento = document.getElementById('miElemento');
     console.log(elemento.innerHTML);
     ```

6. **Flexibilidad del lenguaje**:
   - La capacidad de tratar casi cualquier cosa como un objeto hace que JavaScript sea muy flexible y potente. Esta característica permite a los desarrolladores escribir código más dinámico y reutilizable.

La naturaleza orientada a objetos de JavaScript proporciona una base sólida para construir estructuras de datos complejas y funcionalidades avanzadas, lo que hace que el lenguaje sea extremadamente versátil y adecuado para una amplia variedad de tareas de programación.




# 1. Function types, arrow functions, "this" keyword
## 1.1 / 10 tipos de funciones JavaScript
### 1. Función declarada / Named function o Basic function
Es la declaración básica de JavaScript, usa la keyword `function`.

Se recomienda para funciones con nombre o cuando se necesite `hoisting`.
Las funciones declaradas con la keyword `function`, se pueden elevar a la parte superior de su ámbito, es decir, del scope que las contiene. Esto permite llamar a la función antes de ser declarada.
```js
saludar(); // Hola mundo!

function saludar() {
  console.log('Hola mundo!')
}
```

### 2. Función expresada / Function expression
Es la función que está dentro de una variable.

Son útiles para funciones anónimas, para cuando se quiere controlar dónde va a estar disponible la función o para cuando va a ser usada como argumento para otra función.
```js
const saludar = function() {
  console.log('Hola mundo!')
} 
saludar(); // Hola mundo!
```

### 3. Función anónima / Anonymous function
No tiene nombre y se usan como callbacks generalmente.
```js
setTimeout(function() {
  console.log('Hola mundo!');
}, 1000);
```

### 4. Función de flecha / Arrow function
Especialmente útil para escribir funciones de una línea. No tienen su propio `this` y siempre son anónimas.
```js
const sumar = (a, b) => a + b;

console.log(sumar(2, 3)); // 5
```

### 5. Función de métodos / Method function
Son las funciones definidas dentro de un objeto o clase.
```js
const persona = {
  nombre: "Valeria",
  saludar() {
    console.log(`Hola! me llamo ${this.nombre}`);
  }
}
persona.saludar(); // Hola! me llamo Valeria
```

### 6. Función de constructor / Constructor function
Se usan para crear objetos, se invocan usando el keyword `new`.
```js
function Usuario(nombre, id) {
  this.nombre = nombre;
  this.id = id;
}

const marcos = new Usuario('Marcos', 12345);
console.log(marcos.id); //12345
```

### 7. Expresión de función ejecutada inmediatamente / IIFE - Immediately Invoked Function Expressions
Las IIFE son funciones que se ejecuten inmediatamente después de haberse definido.
```js
(function() {
  console.log('Esta es una IIFE!');
})();

// Esta es una IIFE!
```

### 8. Función generadora o Generadores / Generator function
Son un tipo especial de funciones que sirven como una fábrica de iteradores. Es decir, pausan su ejecución y continúan más tarde.

Se definen usando la expresión `function*`.
```js
function* crearId() {
  let index = 0;
  while(true) {
    yield index++;
  }
}

const generador = crearId();

console.log(generador.next().value); // 0
console.log(generador.next().value); // 1
console.log(generador.next().value); // 2
console.log(generador.next().value); // 3
```

### 9. Función de orden superior / High order function
Las high order functions nos permiten usar otras funciones como parámetros o devolver funciones como resultado.

Ejemplos de estas funciones son `map()`, `filter()`, `reduce()`, `forEach()`, `every()` y `some()`.
```js
// Ej 1: Array.prototype.map() Devuelve un nuevo array con los resultados de aplicar esa función a cada uno de los elementos del array original
let lista = [1,2,3,4,5];
const duplicar = lista.map(num => num * 2); 
console.log(duplicar); // [2,4,6,8,10]

// Ej 2:
function ordenSuperior(func) {
  return function()  {
    console.log('Antes de llamar la función');
    func();
    console.log('Despues de llamar la función');
  }
}

function saludar() {
  console.log('Hola!');
}

const funcionAgrupada = ordenSuperior(saludar);
funcionAgrupada();
/*"Antes de llamar la función"
  "Hola!"
  "Despues de llamar la función"*/
```

### 10. Función asincrónica / Async function
Las funciones asincrónicas se declaran con la keyword `async` y devuelven un objeto `Promise` que representa la terminación o el fracaso de una operación asíncrona.

Se usa el operador `await` para esperar a la operación asincrónica.
```js
async function fetchData() {
  let response = await fetch('https://jsonplaceholder.typicode.com/todos/1');
  let data = await response.json();
  return data;
}

fetchData().then(data => console.log(data));
/*{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}/*
```

## 1.2 / 6 types of arrow functions
## 1. Sin parámetros
Si la función no lleva parámetros, se pueden usar paréntesis vacías
```js
const saludar = () => console.log("Hola!");
saludar(); // Hola!
```

## 2. Un solo parámetro
Si sólo hay un parámetro, los paréntesis son opcionales
```js
const cuadrado = x => x * x;
console.log(cuadrado(4)); // 16
```

## 3. Más de un parámetro
```js
const sumar = (a, b) => a + b;
console.log(sumar(2, 3)); // 5
```

## 4. Más de una instrucción en la función
Si el cuerpo de la función tiene más de una instrución, necesitas usar `{}` y usar la palabra clave `return` para devolver un valor.
```js
const saludarPersona = nombre => {
  const saludo = `Hola, ${nombre}!`;
  return saludo;
}
console.log(saludarPersona("Nahuel")); // Hola, Nahuel!
```

## 5. Devolviendo un objeto
Para devolver un objeto literal, debe estar envuelto en paréntesis para que no se confunda con el cuerpo de la función
```js
const creaPersona = (nombre, edad) => ({nombre: nombre, edad: edad});
console.log(creaPersona("Antxon", 30)); 
// Objecto { "nombre": "Antxon", "edad": 30 }
```

## 6. Funciones de orden superior y callbacks
Las funciones de flecha son especialmente populares cuando se usan como callbacks
```js
const numeros = [1, 2, 3, 4];
const duplicar = numeros.map(num => num * 2);
console.log(duplicar); // Array(4) [ 2, 4, 6, 8 ]
```

## 1.3 This keyword
El keyword `this` en JavaScript es un contexto especial dentro de una función que se refiere al objeto al que pertenece esa función. El valor de `this` depende de cómo se llama a la función y del contexto en el que se encuentra.

### Contextos y Uso de `this`
1. **En el Contexto Global**
   En el contexto global (fuera de cualquier función), `this` se refiere al objeto global. En un navegador web, este objeto global es `window`.
   ```javascript
   console.log(this); // En un navegador, esto será el objeto window
   ```

2. **Dentro de un Objeto (Métodos de Objeto)**
   Cuando `this` se usa dentro de un método de un objeto, se refiere al propio objeto.
   ```javascript
   let person = {
       name: "Alice",
       greet: function() {
           console.log(this.name); // "Alice"
       }
   };

   person.greet();
   ```

3. **En una Función Sola**
   En una función, si se llama en el contexto global, `this` se refiere al objeto global (`window` en navegadores).
   ```javascript
   function show() {
       console.log(this);
   }

   show(); // En un navegador, esto será el objeto window
   ```

4. **En una Función en Modo Estricto**
   En modo estricto, `this` es `undefined` dentro de una función que se llama en el contexto global.
   ```javascript
   "use strict";

   function show() {
       console.log(this); // undefined
   }

   show();
   ```

5. **En una Función Constructor**
   Cuando se usa una función como constructor (con la palabra clave `new`), `this` se refiere al nuevo objeto que se está creando.
   ```javascript
   function Person(name) {
       this.name = name;
   }

   let person1 = new Person("Bob");
   console.log(person1.name); // "Bob"
   ```

6. **En una Función Flecha**
   Las funciones flecha no tienen su propio `this`. 
   En su lugar, `this` se hereda del contexto léxico en el que se definieron (contexto circundante).
   ```javascript
   let person = {
       name: "Charlie",
       greet: function() {
           let innerGreet = () => {
               console.log(this.name); // "Charlie"
           };
           innerGreet();
       }
   };

   person.greet();
   ```

### Ejemplos Adicionales
1. **Uso de `call`, `apply` y `bind`**
   Puedes cambiar explícitamente el valor de `this` usando los métodos `call`, `apply` y `bind`.
   ```javascript
   function greet() {
       console.log(this.name);
   }

   let person1 = { name: "David" };
   let person2 = { name: "Emma" };

   greet.call(person1);  // "David"
   greet.apply(person2); // "Emma"

   let boundGreet = greet.bind(person1);
   boundGreet(); // "David"
   ```

2. **Dentro de un Evento**
   En un controlador de eventos en HTML, `this` se refiere al elemento que recibió el evento.
   ```html
   <button id="myButton">Click me</button>
   <script>
       document.getElementById('myButton').addEventListener('click', function() {
           console.log(this); // <button id="myButton">Click me</button>
       });
   </script>
   ```

### Resumen
El valor de `this` en JavaScript puede ser confuso al principio debido a su naturaleza dinámica, pero entender cómo cambia según el contexto y las diferentes formas de manipularlo te ayudará a escribir código más predecible y manejable.

| Contexto                       | Valor de `this`                           |
|--------------------------------|-------------------------------------------|
| Contexto global                | Objeto global (`window` en navegadores)   |
| Método de objeto               | El propio objeto                          |
| Función simple                 | Objeto global (`window` en navegadores)   |
| Función en modo estricto       | `undefined`                               |
| Función constructor            | Nuevo objeto instanciado                  |
| Función flecha                 | `this` del contexto léxico circundante    |
| Método `call`, `apply`, `bind` | Valor especificado en la llamada          |
| Manejador de eventos           | Elemento que recibió el evento            |

Comprender `this` es crucial para trabajar eficazmente con JavaScript, especialmente en programación orientada a objetos y en el manejo de eventos.




# 2. Scope, Hoisting & Closures
## 2.1 Que es el scope en JavaScript?
El scope (o ámbito) en JavaScript se refiere al contexto en el cual las variables y las funciones son accesibles y pueden ser referenciadas. Entender el scope es crucial para escribir código claro y sin errores. En JavaScript, existen diferentes tipos de scope:

### Tipos de Scope en JavaScript
1. **Global Scope (Ámbito Global)**:
   - Las variables declaradas fuera de cualquier función o bloque tienen alcance global y son accesibles desde cualquier parte del código.
   - En un navegador, las variables globales se adjuntan al objeto `window`.
   ```javascript
   var globalVar = "Soy global";

   function mostrarGlobal() {
       console.log(globalVar);  // "Soy global"
   }

   mostrarGlobal();
   console.log(globalVar);  // "Soy global"
   ```

2. **Local Scope (Ámbito Local)**:
   - Las variables declaradas dentro de una función solo son accesibles dentro de esa función. Estas variables tienen un ámbito local.
   ```javascript
   function mostrarLocal() {
       var localVar = "Soy local";
       console.log(localVar);  // "Soy local"
   }

   mostrarLocal();
   console.log(localVar);  // Error: localVar no está definida
   ```

3. **Block Scope (Ámbito de Bloque)**:
   - Las variables declaradas con `let` y `const` tienen alcance de bloque, lo que significa que solo son accesibles dentro del bloque en el que se declararon (por ejemplo, dentro de llaves `{}` de un `if`, `for`, etc.).
   ```javascript
   if (true) {
       let bloqueVar = "Soy de bloque";
       console.log(bloqueVar);  // "Soy de bloque"
   }

   console.log(bloqueVar);  // Error: bloqueVar no está definida
   ```

### Scope Chain (Cadena de Ámbito)
Cuando se intenta acceder a una variable, JavaScript busca en la cadena de ámbito, comenzando por el ámbito más interno y moviéndose hacia los ámbitos externos hasta encontrar la variable o llegar al ámbito global.
```javascript
var globalVar = "Soy global";

function externa() {
    var externaVar = "Soy de externa";

    function interna() {
        var internaVar = "Soy de interna";
        console.log(globalVar);    // "Soy global"
        console.log(externaVar);   // "Soy de externa"
        console.log(internaVar);   // "Soy de interna"
    }

    interna();
    console.log(internaVar);  // Error: internaVar no está definida
}

externa();
```

### Function Scope (Ámbito de Función) vs Block Scope (Ámbito de Bloque)
- **Function Scope**: Las variables declaradas con `var` tienen ámbito de función. Esto significa que si se declaran dentro de una función, no son accesibles fuera de esa función, pero no están limitadas por bloques.
  ```javascript
  function scopeFuncion() {
      if (true) {
          var funcionVar = "Soy de función";
      }
      console.log(funcionVar);  // "Soy de función"
  }

  scopeFuncion();
  ```

- **Block Scope**: Las variables declaradas con `let` y `const` están limitadas por el bloque en el que se declaran.
  ```javascript
  function scopeBloque() {
      if (true) {
          let bloqueLet = "Soy de bloque";
          const bloqueConst = "Soy de bloque también";
      }
      console.log(bloqueLet);  // Error: bloqueLet no está definida
      console.log(bloqueConst);  // Error: bloqueConst no está definida
  }

  scopeBloque();
  ```

### Hoisting (Elevación)
Las declaraciones de variables y funciones en JavaScript se mueven "hacia arriba" de su contexto de ejecución (scope). Solo las declaraciones son elevadas, no las inicializaciones.

- **Variables con `var`**: Se elevan y se inicializan con `undefined`.
  ```javascript
  console.log(elevadaVar);  // undefined
  var elevadaVar = "Soy elevada";
  console.log(elevadaVar);  // "Soy elevada"
  ```

- **Variables con `let` y `const`**: Se elevan pero no se inicializan, lo que lleva a un error si se accede antes de la declaración.
  ```javascript
  console.log(elevadaLet);  // Error: no se puede acceder antes de la inicialización
  let elevadaLet = "Soy elevada";
  console.log(elevadaLet);  // "Soy elevada"
  ```

En resumen, el scope en JavaScript determina dónde y cómo se pueden acceder a las variables y funciones. Comprender el scope es fundamental para escribir código organizado, evitar errores y gestionar adecuadamente el alcance de las variables.


## 2.2 Que es el `hoisting` en JavaScript?
**Hoisting** es un comportamiento en JavaScript que se refiere al proceso en el que las declaraciones de variables y funciones son "elevadas" al comienzo del contexto de ejecución. Esto significa que puedes usar variables y funciones antes de declararlas en el código. Sin embargo, este comportamiento tiene matices importantes que debes comprender para evitar errores.

### Hoisting de Variables
Cuando se declaran variables con `var`, `let` o `const`, el JavaScript Engine eleva sus declaraciones al inicio de su contexto (función o bloque). Sin embargo, solo `var` inicializa la variable con `undefined` en el hoisting, mientras que `let` y `const` no lo hacen, lo que puede llevar a errores de referencia si se accede a ellas antes de su declaración.

**Ejemplo con `var`**:
```javascript
console.log(x); // undefined
var x = 5;
console.log(x); // 5
```
El código anterior se comporta como si fuera reescrito de la siguiente manera debido al hoisting:
```javascript
var x;
console.log(x); // undefined
x = 5;
console.log(x); // 5
```

**Ejemplo con `let` y `const`**:
```javascript
console.log(y); // ReferenceError: Cannot access 'y' before initialization
let y = 5;

console.log(z); // ReferenceError: Cannot access 'z' before initialization
const z = 10;
```
En estos casos, la declaración es elevada, pero no la inicialización. Por lo tanto, intentar acceder a `y` o `z` antes de la declaración resulta en un error de referencia.

### Hoisting de Funciones
Las funciones declaradas con el keyword `function` también son elevadas completamente, incluidas sus definiciones, permitiéndoles ser llamadas antes de su declaración en el código.

```javascript
greet(); // "Hello, world!"

function greet() {
    console.log("Hello, world!");
}
```

El código anterior se comporta como si fuera reescrito de la siguiente manera:
```javascript
function greet() {
    console.log("Hello, world!");
}

greet(); // "Hello, world!"
```

### Hoisting de Function Expressions y Arrow Functions
Las funciones expresadas y las funciones flecha no son completamente elevadas. Solo la declaración de la variable se eleva, no la asignación.
```javascript
console.log(foo); // undefined
var foo = function() {
    console.log("Hello, world!");
};

console.log(bar); // ReferenceError: Cannot access 'bar' before initialization
let bar = () => {
    console.log("Hello, world!");
};
```

En este caso, `foo` se eleva, pero su valor es `undefined` hasta que la asignación se realiza, mientras que `bar` no puede ser accedida antes de su declaración debido a la naturaleza de `let`.

### Resumen
- **Declaraciones de variables con `var`**: Se elevan y se inicializan con `undefined`.
- **Declaraciones de variables con `let` y `const`**: Se elevan, pero no se inicializan, resultando en un error de referencia si se accede a ellas antes de su declaración.
- **Declaraciones de funciones**: Se elevan completamente, incluyendo su cuerpo, permitiendo su uso antes de la declaración.
- **Expresiones de funciones y funciones flecha**: Solo la variable se eleva, pero no la asignación, lo que resulta en `undefined` o un error de referencia si se accede a ellas antes de su declaración.

Entender el hoisting es fundamental para escribir código JavaScript más claro y evitar errores inesperados.

Entre los *beneficios del hoisting* se encuentran
- Mayor flexibilidad en la legibilidad y el orden del código
- Evitar errores de referencia, el hoisting de var inicializa las variables como undefined
- El hoisting no es una característica que se usa explícitamente sino un comportamiento interno del motor de JavaScript y de cómo se procesa su código.


## 2.3 Closures
# Closures
A closure in JavaScript is a feature where an inner function has access to variables from its outer (enclosing) function's scope, even after the outer function has finished executing. This allows the inner function to remember and access its lexical scope, which includes any variables declared in the outer function.

#### Example outer variable
```javascript
function outerFunction() {
  let outerVariable = 'I am outside!';
  
  function innerFunction() {
    console.log(outerVariable);
  }
  
  return innerFunction;
}

const myInnerFunction = outerFunction();
myInnerFunction(); // Logs 'I am outside!'
```

Closures allow functions to have private variables. This is particularly useful in scenarios such as:

- **Data Encapsulation**: Closures can create private variables that can only be accessed by specific functions.
- **Maintaining State**: Functions can maintain state between calls.
- **Functional Programming Patterns**: Closures enable more complex functional programming patterns and callback structures.

#### Example using a counter
```javascript
function createCounter() {
  let count = 0;
  
  return function() {
    count++;
    return count;
  };
}

const counter1 = createCounter();
console.log(counter1()); // 1
console.log(counter1()); // 2

const counter2 = createCounter();
console.log(counter2()); // 1
console.log(counter2()); // 2
```

#### Example with iterators
Closures can be used to create iterators that maintain their state between calls, facilitating efficient and memory-friendly iteration over data structures.
```js
function createIterator(items) {
  let index = 0;
  return function() {
    return items[index++];
  }
}

let fruitList = ['apple', 'banana', 'orange'];
const fruitsIterator = createIterator(fruitList);

console.log(fruitsIterator()); // apple
console.log(fruitsIterator()); // banana
console.log(fruitsIterator()); // orange
```

## Summary
Imagine you have a function within another function, and **the inner function can access variables from the outer function even after the outer function has finished executing**, that's closure

**Closures enable the creation of private variables in JS encapsulating data within functions and preventing direct access from outside**.




# 3. DOM & Global Objects
## 3.1 Shadow DOM
### Shadow DOM
El Shadow DOM es una tecnología de encapsulación de JavaScript que permite crear un árbol de DOM separado e independiente del árbol de DOM principal del documento. Este árbol separado es conocido como "Shadow Tree" y permite la encapsulación de estilos y lógica de componentes, evitando conflictos con otros elementos de la página.

#### Beneficios del Shadow DOM
1. **Encapsulación**:
   - Los estilos y scripts definidos dentro del Shadow DOM no afectan al resto del documento, y viceversa. Esto evita problemas de estilo y comportamiento no deseados.

2. **Composición de Componentes**:
   - Permite la creación de componentes web reutilizables que pueden ser utilizados en diferentes partes de una aplicación sin que sus estilos o scripts interfieran con otros componentes.

#### Uso del Shadow DOM
1. **Crear un Shadow Root**:
   - Asociar un Shadow Root a un elemento del DOM.
   ```javascript
   let host = document.getElementById('miComponente');
   let shadowRoot = host.attachShadow({ mode: 'open' });
   ```

2. **Añadir Contenido al Shadow DOM**:
   - Agregar elementos y estilos dentro del Shadow Root.
   ```javascript
   shadowRoot.innerHTML = `
       <style>
           p {
               color: red;
           }
       </style>
       <p>Texto encapsulado</p>
   `;
   ```

3. **Modos de Encapsulación**:
   - `mode: 'open'`: El Shadow DOM es accesible desde JavaScript.
   - `mode: 'closed'`: El Shadow DOM no es accesible desde JavaScript.
   ```javascript
   let shadowRootCerrado = host.attachShadow({ mode: 'closed' });
   ```

#### Ejemplo Completo
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shadow DOM Ejemplo</title>
</head>
<body>
    <div id="miComponente"></div>

    <script>
        // Seleccionar el host
        let host = document.getElementById('miComponente');

        // Crear un Shadow Root
        let shadowRoot = host.attachShadow({ mode: 'open' });

        // Añadir contenido al Shadow DOM
        shadowRoot.innerHTML = `
            <style>
                p {
                    color: red;
                }
            </style>
            <p>Texto encapsulado</p>
        `;

        // Verificar el Shadow Root
        console.log(host.shadowRoot);  // Mostrará el contenido del Shadow Root
    </script>
</body>
</html>
```

## 3.2 Global Objects
Los objetos globales en JavaScript son objetos que están disponibles en todo el entorno de ejecución, independientemente de dónde se encuentre el código. Estos objetos se pueden usar en cualquier parte de tu programa sin necesidad de ser importados o definidos explícitamente.

### Objetos Globales Comunes en JavaScript
1. **`window` (en navegadores web)**:
   - El objeto `window` es el objeto global en los navegadores web. Todas las variables globales y funciones globales son propiedades de `window`.
   ```javascript
   window.alert('Hola, mundo!');  // Muestra una alerta
   console.log(window.innerWidth);  // Ancho de la ventana del navegador
   ```

2. **`global` (en Node.js)**:
   - En Node.js, el objeto global es `global`, que tiene una función similar a `window` en los navegadores.
   ```javascript
   global.console.log('Hola desde Node.js');
   ```

3. **`globalThis`**:
   - `globalThis` es un objeto global estándar que proporciona una manera uniforme de acceder al objeto global en cualquier entorno (navegador, Node.js, etc.).
   ```javascript
   globalThis.console.log('Esto funciona en cualquier entorno');
   ```

### Otros Objetos Globales Importantes
1. **`Math`**:
   - Proporciona propiedades y métodos matemáticos.
   ```javascript
   Math.PI;  // 3.141592653589793
   Math.sqrt(16);  // 4
   ```

2. **`Date`**:
   - Proporciona métodos para manejar fechas y horas.
   ```javascript
   let ahora = new Date();
   console.log(ahora.toString());
   ```

3. **`JSON`**:
   - Proporciona métodos para analizar y convertir datos JSON.
   ```javascript
   let obj = { nombre: 'Juan', edad: 30 };
   let jsonString = JSON.stringify(obj);
   let jsonObj = JSON.parse(jsonString);
   ```

4. **`console`**:
   - Proporciona métodos para la salida de depuración.
   ```javascript
   console.log('Mensaje de depuración');
   ```

5. **`Array`**, **`String`**, **`Object`**, **`Number`**, **`Boolean`**:
   - Constructores para los tipos de datos fundamentales de JavaScript.
   ```javascript
   let arr = new Array(1, 2, 3);
   let str = new String('Hola');
   let obj = new Object();
   let num = new Number(100);
   let bool = new Boolean(true);
   ```

### Funciones Globales
1. **`parseInt`**, **`parseFloat`**:
   - Convertir cadenas a números enteros o de punto flotante.
   ```javascript
   parseInt('10');  // 10
   parseFloat('3.14');  // 3.14
   ```

2. **`isNaN`**:
   - Verificar si un valor es `NaN` (Not-a-Number).
   ```javascript
   isNaN('hola');  // true
   ```

3. **`setTimeout`**, **`setInterval`**:
   - Temporizadores para ejecutar código después de un cierto tiempo o a intervalos regulares.
   ```javascript
   setTimeout(() => console.log('Esto se ejecuta después de 1 segundo'), 1000);
   setInterval(() => console.log('Esto se ejecuta cada 2 segundos'), 2000);
   ```

4. **`alert`**, **`prompt`**, **`confirm`** (en navegadores):
   - Mostrar diálogos modales.
   ```javascript
   alert('Hola!');
   let nombre = prompt('¿Cuál es tu nombre?');
   let confirmacion = confirm('¿Estás seguro?');
   ```

### Variables Globales
- Las variables declaradas sin `var`, `let` o `const` se convierten automáticamente en propiedades del objeto global (aunque esto es considerado una mala práctica).
```javascript
miVariableGlobal = 'Esto es global';
console.log(window.miVariableGlobal);  // "Esto es global" (en el navegador)
console.log(global.miVariableGlobal);  // "Esto es global" (en Node.js)
```

### Evitar el Uso Excesivo de Variables Globales
El uso excesivo de variables y funciones globales puede llevar a problemas de mantenimiento y errores difíciles de depurar debido a conflictos de nombres y efectos secundarios no deseados. Es una buena práctica minimizar el uso de variables globales y encapsular el código en funciones o módulos.

### Resumen
Los objetos globales en JavaScript son accesibles desde cualquier parte del código y proporcionan funcionalidades esenciales como manejo de fechas, operaciones matemáticas, manipulación de cadenas, y más. Si bien estos objetos son extremadamente útiles, es importante usarlos con cuidado para evitar problemas de conflicto y mantener el código limpio y manejable.




# 4. Event listeners y event bubbling
### Event Handlers (Manejadores de Eventos)
Son las funciones específicas que se ejecutan cuando un evento se dispara.

### Event Bubbling en JavaScript
**Event Bubbling** es un mecanismo en JavaScript donde un evento desencadenado en un elemento se propaga hacia arriba a través de sus ancestros en el DOM.

#### Fases del Evento:
1. **Captura**: El evento se mueve desde el `document` hasta el elemento objetivo.
2. **Objetivo**: El evento llega al elemento objetivo.
3. **Burbuja**: El evento se propaga hacia arriba desde el elemento objetivo hasta el `document`.

#### Prevenir el Bubbling:
```javascript
innerButton.addEventListener('click', function(event) {
    console.log('Button clicked');
    event.stopPropagation();
});
```

#### Event Capturing:
Para manejar eventos durante la fase de captura:
```javascript
outerDiv.addEventListener('click', function() {
    console.log('Outer DIV clicked');
}, true);
```

#### Delegación de Eventos:
Usa event bubbling para manejar eventos en elementos hijos a través de un ancestro común.
```javascript
outerDiv.addEventListener('click', function(event) {
    if (event.target.tagName === 'BUTTON') {
        console.log('Button clicked via delegation');
    }
});
```

### Resumen:
- **Event Bubbling**: Propagación de eventos hacia arriba en el DOM.
- **Fases del Evento**: Captura, Objetivo, Burbuja.
- **Prevenir Bubbling**: `event.stopPropagation()`.
- **Event Capturing**: Manejo de eventos durante la fase de captura.
- **Delegación de Eventos**: Manejo de eventos en elementos hijos a través de un ancestro común.

Además, el método `addEventListener` se utiliza para añadir event listeners a elementos del DOM. Este método puede aceptar tres argumentos:
1. **El tipo de evento** (como `'click'`, `'mouseover'`, etc.).
2. **La función manejadora** (la función que se ejecutará cuando ocurra el evento).
3. **Un objeto opcional de opciones** o un booleano (opcional).

El tercer argumento puede ser un objeto con varias propiedades o un valor booleano (`true` o `false`). Este booleano especifica si el evento debe ser capturado durante la fase de captura o la fase de burbuja del flujo del evento.

### Capturing vs. Bubbling
- **Fase de Burbuja (`false`)**: El evento se propaga desde el elemento objetivo hacia arriba.
- **Fase de Captura (`true`)**: El evento se propaga desde el `document` raíz hacia el elemento objetivo.

### Tercer Argumento en `addEventListener`
- **`true`**: Indica que el evento debe ser capturado durante la fase de captura.
- **`false`** (o omitir el argumento): Indica que el evento debe ser capturado durante la fase de burbuja.




# 5. Callback functions
### Callbacks en JavaScript
Una **callback** en JavaScript es una función que se pasa como argumento a otra función y se ejecuta después de que se haya completado una operación. Este concepto es fundamental en JavaScript, especialmente en la programación asíncrona, como las operaciones de red (fetch), temporizadores (setTimeout), y eventos.

### Uso Común de Callbacks
Las callbacks se usan frecuentemente para manejar operaciones asíncronas, como:
1. **Temporizadores**:
```javascript
setTimeout(function() {
    console.log('Esto se muestra después de 2 segundos');
}, 2000);
```

2. **Eventos del Usuario**:
```javascript
document.getElementById('myButton').addEventListener('click', function() {
    alert('Botón clickeado!');
});
```

3. **Llamadas AJAX (usando `fetch`)**:
```javascript
fetch('https://api.example.com/data')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        console.log(data);
    });
```

### Beneficios de las Callbacks
- **Asincronía**: Permiten que el código continúe ejecutándose mientras se espera una operación asincrónica, como una llamada a una API, evitando que la aplicación se bloquee.
- **Modularidad**: Separan la lógica principal de la lógica que debe ejecutarse después, haciendo el código más limpio y modular.
- **Reutilización**: Las funciones callback pueden ser reutilizadas en diferentes contextos y con diferentes funciones.

### Ejemplo Básico de Callback
```javascript
function greeting(name) {
    console.log('Hello ' + name);
}

function processUserInput(callback) {
    const name = prompt('Please enter your name.');
    callback(name);
}
processUserInput(greeting);
```
En este ejemplo:

- `greeting` es una función que toma un argumento `name` y muestra un saludo en la consola.
- `processUserInput` es una función que pide al usuario que ingrese su nombre y luego llama a `callback` con el nombre ingresado.
- `processUserInput(greeting)` pasa la función `greeting` como una callback a `processUserInput`, que luego la ejecuta con el nombre proporcionado por el usuario.


<hr>

# 6. Async Await, Promises
# Promesas en JavaScript
Las **promesas** en JavaScript son una forma de manejar operaciones asincrónicas, como llamadas a APIs, temporizadores, o tareas que llevan tiempo, de manera más legible y manejable que las callbacks tradicionales. Una promesa representa un valor que puede estar disponible ahora, en el futuro o nunca.

1. **Pendiente (Pending)**: La operación asincrónica aún no ha terminado.
2. **Cumplida (Fulfilled)**: La operación asincrónica se ha completado con éxito y tiene un resultado.
3. **Rechazada (Rejected)**: La operación asincrónica ha fallado y tiene un motivo de fallo.

Para crear una promesa, se usa el constructor `Promise` y se le pasa una función con dos parámetros: `resolve` y `reject`. `resolve` se llama cuando la operación se completa con éxito, y `reject` se llama cuando hay un error.

```javascript
let myPromise = new Promise((resolve, reject) => {
    // Simula una operación asincrónica, como una llamada a una API
    setTimeout(() => {
        let success = true; // Cambia esto a false para simular un error
        if (success) {
            resolve("¡Operación exitosa!"); // Llama a resolve si la operación tiene éxito
        } else {
            reject("Algo salió mal"); // Llama a reject si hay un error
        }
    }, 2000); // Simula un retraso de 2 segundos
});
```

### Usar una Promesa
Para manejar el resultado de una promesa, se usan los métodos `then` y `catch`. `then` se usa para manejar un resultado exitoso, y `catch` se usa para manejar errores.

```javascript
myPromise
    .then((message) => {
        console.log(message); // Esto se ejecuta si la promesa se cumple
    })
    .catch((error) => {
        console.error(error); // Esto se ejecuta si la promesa es rechazada
    });
```

### Beneficios de las Promesas
- **Legibilidad**: Hacen que el código asincrónico sea más legible y fácil de seguir que las callbacks anidadas.
- **Manejo de errores**: Proporcionan una forma clara de manejar errores usando `catch`.
- **Encadenamiento**: Permiten encadenar múltiples operaciones asincrónicas de una manera ordenada.


Supongamos que queremos obtener datos de una API y luego procesar esos datos.
```javascript
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            let data = "Datos de la API";
            resolve(data); // Simula una operación exitosa
        }, 2000);
    });
}

function processData(data) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            let processedData = data + " procesados";
            resolve(processedData);
        }, 1000);
    });
}

// Usar las promesas
fetchData()
    .then((data) => {
        console.log("Datos recibidos:", data);
        return processData(data); // Encadena otra promesa
    })
    .then((processedData) => {
        console.log("Datos procesados:", processedData);
    })
    .catch((error) => {
        console.error("Error:", error);
    });
```

En este ejemplo:

1. `fetchData` simula obtener datos de una API.
2. `processData` simula el procesamiento de esos datos.
3. Usamos `then` para manejar cada etapa del proceso y `catch` para manejar cualquier error que ocurra.

### Resumen promesas
*Las promesas son clave para manejar operaciones asincrónicas de manera más legible y manejable que las callbacks tradicionales. Nos permiten escribir código asincrónico que se parece más al código síncrono, mejorando la claridad y la facilidad de manejo de errores.*

- Introducidas en ES6 para resolver los problemas asociados a los callbacks
- Una promesa representa una operacion que aun no se ha completado pero se espera que lo haga en el futuro
- Una promesa puede tener tres estados: pendiente, resuelta o rechazada
- Las promesas tienen los metodos `then()`, `catch()` y `finally()`. Que podemos utilizar para adjuntar **callbacks** que se ejecutaran cuando la promesa se resuelva o se rechace
- Algunos metodos como `fetch()` directamente devuelven una promesa y se puede usar `then()` o `catch()` 
```js
// Promise creation
let promise = new Promise(function(resolve, reject) {
  let condition = true;
  if(condition){
    resolve("Your result here");
  } else {
    reject(new Error("Something happened"));
  }
})

// Using .then, .catch & .finally
promise.then(function(result) {
  console.log(result);
}).catch(function(error) {
  console.log(error);
}).finally(function() {
  console.log("After all...");
})
```


# `Callbacks` vs `Promesas`

### Comparación
- **Manejo de Errores**:
  - Callbacks: Los errores se manejan dentro de cada función de callback.
  - Promesas: Los errores se manejan de manera centralizada usando `catch`.

- **Legibilidad**:
  - Callbacks: Pueden llevar al "callback hell" con múltiples niveles de anidación.
  - Promesas: Son más lineales y fáciles de leer gracias al encadenamiento de `then`.

- **Encadenamiento**:
  - Callbacks: Difícil de seguir cuando se tienen muchas operaciones asincrónicas.
  - Promesas: Encadenamiento sencillo y legible.

- La principal diferencia es que al usar callbacks, normalmente pasamos el callback en una funcion
- En las promesas, el callbacks que se ejecuta cuando la promesa se resuelve o se rechaza

### Promesas
Las sintaxis de las `promesas` es mas amigable y el manejo de errores es más fácil de manejar
```js
api()
  .then(function (result) {
    return api2();
  })
  .then(function (result2) {
    return api3();
  })
  .then(function (result3) {
    // ...
  })
  .catch(function (error) {
    // maneja el error
  });
```

### Callbacks
Las `callbacks` tienen una sintaxis más difícil de comprender y el manejo de errores puede ser complicado de manejar

```js
api(function(result) {
  api2(function(result2) {
    api3(function(result3) {
      // ...

      if(error) {
        // haz algo
      } else {
        // haz otra cosa
      }
    })
  })
})
```

### Callback hell
Cuando se necesitan múltiples operaciones asincrónicas anidadas, el código puede volverse difícil de leer y mantener.
```js
doSomething(function(result1) {
    doSomethingElse(result1, function(result2) {
        doAnotherThing(result2, function(result3) {
            doFinalThing(result3, function(result4) {
                console.log('Hecho!');
            });
        });
    });
});
```

### Async/Await
- ES7 introdujo **async/await** para simplificar aun mas el manejo de operaciones asincronas construyendo sobre las promesas
- **async/await** son especialmente utiles cuando necesitamos sincronia en las llamadas http, en el caso de que tengamos que encadenar varias llamadas y necesitemos el resultado de una para llamar a la otra
- `await`*operator makes your program behave as if it were waiting for the asynchronous computation to complete (but it does this without actually blocking, and it does not prevent other asynchronous operations from proceeding at the same time). The value of the await operator is the fulfillment value of the Promise object. Importantly, await is only legal within functions that have been declared asynchronous with the async keyword*
```js
// asnyc/await example
async function fetchUserData() {
  try {
    let response = await
    fetch('https://api.example.com/user');
    let data = await response.json();
    console.log(data);
  } catch(error) {
    console.error("Error:", error)
  }
}
```












# Fetch API
- La API fetch es una interfaz moderna que permite realizar peticiones HTTP a servidores desde los navegadores web.
- La API fetch realiza todas las tareas del objeto `XMLHttpRequest` pero de una manera mucho más limpia y sencilla.
- Se basa en `Promesas`, lo que permite que el código sea más claro y conciso 
- Permite configurar las solicitudes HTTP con opciones como métodos (`GET`, `POST`, `PUT`, `DELETE`), `headers`, `body`, etc
- Proporciona métodos para manejar diferentes tipos de respuesta, como JSON, texto, etc


### Enviando una request
El método `fetch()` sólo necesita un parámetro, la `URL` del recurso que quiere solicitar. Cuando se completa la request, la promesa retorna como un objeto `Response`
```js
let response = fetch(url)
```

El método `text()` retorna una promesa que devuelve el contenido completo del recurso solitado
```js
fetch('/readme.txt')
  .then(res => res.text())
  .then(data => console.log(data));
```
Además de este método, el objeto Response incluye otros métodos como `json()`, `blob()`, `formatData()` y `arrayBuffer()` para manejar los distintos tipos de datos


### Leyendo la response
El método `fetch()` devuelve una promesa, de manera que podemos usar `then()` y `catch()` para manejarla.
```js
fetch(url)
  .then((res) => {
    // manejo de la response
  })
  .catch((err) =? {
    // manejo del error
  })
```
Los contenidos de la response estan en texto plano, de manera que podemos usar el metodo text(). 
Generalmente se usa el `async`/`await` con fetch de la siguiente manera
```js
async function fetchText() {
  let response = await fetch('/readme.txt');
  let data = await response.text();
  console.log(data);
}
```

### Manejando los status codes
El objeto Response provee el status code y el status text a traves de las propiedades `status` y `statusText`.
```js
async function fetchText() {
  let response = await fetch('/readme.txt');

  console.log(response.status);     // 200
  console.log(response.statusText); // OK

  if(response.status == 200) {
    let data = await response.text();
    // Manejo de los datos
  }
}
```



<hr>




<hr>


# AJAX y SPA
## Que es AJAX?
Ajax (Asynchronous JavaScript and XML) es una técnica de desarrollo web que permite actualizar partes específicas de una página web sin necesidad de recargar toda la página. Se basa en el intercambio de datos asíncrono entre el navegador y el servidor, lo que permite a las aplicaciones web realizar solicitudes y recibir respuestas en segundo plano, sin interrumpir la experiencia del usuario.

Los principales componentes de Ajax son:

1. **JavaScript**:
   - Ajax utiliza JavaScript para enviar y recibir datos asíncronamente entre el cliente (navegador) y el servidor.
   - JavaScript maneja los eventos del usuario y las respuestas del servidor para actualizar dinámicamente el contenido de la página web.

2. **XMLHttpRequest (XHR)**:
   - XMLHttpRequest es un objeto de JavaScript que proporciona la capacidad de realizar solicitudes HTTP asíncronas desde el navegador web.
   - Permite enviar solicitudes al servidor y recibir respuestas sin necesidad de recargar la página completa.

3. **Manipulación del DOM**:
   - Una vez que se recibe la respuesta del servidor, JavaScript puede manipular el DOM (Document Object Model) para actualizar partes específicas de la página web con los datos recibidos.
   - Esto permite a las aplicaciones web ofrecer una experiencia más dinámica y receptiva al usuario, ya que pueden actualizar contenido sin tener que recargar la página completa.

4. **Formato de datos**:
   - Aunque el nombre de Ajax incluye "XML" (Extensible Markup Language), en la práctica se utilizan una variedad de formatos de datos, incluyendo JSON (JavaScript Object Notation), XML y texto plano, para intercambiar información entre el cliente y el servidor.
   - JSON se ha convertido en el formato de datos más comúnmente utilizado en aplicaciones web modernas debido a su ligereza y facilidad de uso con JavaScript.

Ajax se utiliza ampliamente en el desarrollo web para crear aplicaciones más interactivas y dinámicas, como interfaces de usuario de una sola página (Single Page Applications), chats en tiempo real, actualizaciones automáticas de contenido, formularios dinámicos y mucho más. Permite a los desarrolladores crear aplicaciones web más rápidas, eficientes y atractivas para los usuarios finales.

## Que son las SPA?
Una SPA (Single Page Application) es un tipo de aplicación web que carga una sola página HTML y dinámicamente actualiza el contenido de esa página a medida que el usuario interactúa con la aplicación, sin necesidad de recargar la página completa desde el servidor. En una SPA, la interactividad se logra principalmente a través de Ajax, JavaScript y manipulación dinámica del DOM (Document Object Model).

Algunas características y ventajas clave de las SPAs son:

1. **Interactividad sin recarga de página**: Las SPAs actualizan dinámicamente el contenido de la página en respuesta a las acciones del usuario, como hacer clic en un enlace, enviar un formulario o interactuar con elementos de la interfaz de usuario, sin necesidad de recargar la página completa desde el servidor.

2. **Rápida respuesta**: Debido a que solo se carga una página inicialmente y la mayoría de las interacciones se gestionan de forma asíncrona en el lado del cliente, las SPAs pueden proporcionar una experiencia de usuario más rápida y receptiva en comparación con las aplicaciones web tradicionales.

3. **Experiencia de usuario fluida**: Las SPAs pueden proporcionar una experiencia de usuario más fluida y similar a la de las aplicaciones nativas, con transiciones suaves entre vistas, carga instantánea de contenido y manipulación dinámica de elementos de la interfaz de usuario.

4. **Separación de preocupaciones**: Las SPAs suelen seguir el patrón de diseño Modelo-Vista-Controlador (MVC) o algún otro patrón similar, lo que facilita la separación clara de la lógica de presentación (Vista) y la lógica de la aplicación (Controlador), lo que mejora la mantenibilidad y la escalabilidad del código.

5. **Facilidad de desarrollo y mantenimiento**: Al utilizar frameworks y bibliotecas modernas de JavaScript, como React, Angular o Vue.js, el desarrollo de SPAs puede simplificarse y acelerarse. Además, una vez desplegada, la actualización y el mantenimiento de una SPA pueden ser más sencillos debido a su naturaleza basada en la web.

Las SPAs se utilizan ampliamente en aplicaciones web modernas, incluyendo aplicaciones de productividad, redes sociales, tiendas en línea, paneles de administración y muchas otras, debido a su capacidad para proporcionar una experiencia de usuario interactiva y fluida.



## JavaScript complex data structures
- **Objects** are used for storing key collections
- **Arrays** are used for storing ordered collections
- **Maps** are similar to objects but you can use anything as a key
- **Sets** are a great choice to store data without duplicates

## Object destructuring
```js
// Object destructuring is a way to extract properties from an object and assign them to variables. It makes working with objects simpler and easier to read

const userProfile = {
	name: 'Alex',
	email: 'alex@example.com',
	phone: '555-123-4567'
}

// Extracting name & email only and assigning them to new variables
const { name, email } = userProfile;

console.log(name + ", " + email); // Alex, alex@example.com
```


<hr>


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

## JavaScript Cheatsheet
```js
// Variables
let variableName = value; // Mutable
let constantName = value; // Immutable


// Data Types
let myString = "hello";
let myNumber = 50;
let myBoolean = true;
let myArray = [1,2,3];
let myObject = {key: 'value'};


// Arrays
myArray.push(4);  // Add to end
myArray.pop()     // Remove from end
myArray.unshift(0);//Add to beginning
myArray.shift();  // Remove from beginning


// Objects
let person = {
  name: 'John',
  age: 20,
  isStudent: true
};


// AJAX & Fetch
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error: ', error));


// ES6+ Features
// Destructuring
const { key } = object;

// Spread Opeartor
const newArray = [...oldArray];

// Template literals
`Hello, ${name}!`

// Promise
new Promise((resolve, reject) => {

});


// Async / Await
async function fetchData() {

}
```


