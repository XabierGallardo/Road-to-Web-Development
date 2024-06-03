# Callbacks en JavaScript
Una **callback** en JavaScript es una función que se pasa como argumento a otra función y se ejecuta después de que se haya completado una operación. Este concepto es fundamental en JavaScript, especialmente en la programación asíncrona, como las operaciones de red (fetch), temporizadores (setTimeout), y eventos.

```js
// Example 1
const greet = (name) => { console.log('Hi ' + name)};

// function
const callMe = (callback) => {
  // take input and save it in name
  let name = prompt('Enter your name');
  callback(name);
}

// passing function as a parameter
callMe(greet);
```


### Ejemplo de Callback

Supongamos que quieres hacer una llamada a una API y, una vez que recibas los datos, quieres mostrarlos en la consola. Puedes usar una callback para definir qué hacer con los datos después de que se reciban.

```javascript
// Función que simula una operación asincrónica como una llamada a una API
function fetchData(callback) {
    setTimeout(() => {
        const data = "Datos de la API";
        callback(data); // Llama a la función callback con los datos
    }, 2000); // Simula un retraso de 2 segundos
}

// Función callback que se pasa como argumento
function handleData(data) {
    console.log(data); // Muestra los datos en la consola
}

// Llamada a la función con la callback como argumento
fetchData(handleData);
```

En este ejemplo:

1. `fetchData` es una función que simula una operación asincrónica usando `setTimeout`.
2. `handleData` es la función callback que se pasa a `fetchData`.
3. Cuando la operación en `fetchData` termina (después de 2 segundos), se ejecuta `handleData`, mostrando los datos en la consola.

### Beneficios de las Callbacks

- **Asincronía**: Permiten que el código continúe ejecutándose mientras se espera una operación asincrónica, como una llamada a una API, evitando que la aplicación se bloquee.
- **Modularidad**: Separan la lógica principal de la lógica que debe ejecutarse después, haciendo el código más limpio y modular.
- **Reutilización**: Las funciones callback pueden ser reutilizadas en diferentes contextos y con diferentes funciones.

### Otro Ejemplo: Temporizadores

Usando `setTimeout`, que es una función nativa de JavaScript para ejecutar código después de un cierto período.

```javascript
function sayHello() {
    console.log("Hello!");
}

// Ejecuta la función `sayHello` después de 3 segundos
setTimeout(sayHello, 3000);
```

En este ejemplo, `sayHello` es la función callback que `setTimeout` ejecuta después de 3 segundos.

### Conclusión

*Las callbacks son funciones que se pasan como argumentos a otras funciones y se ejecutan después de que la operación principal haya terminado. Son esenciales para manejar la asincronía en JavaScript, permitiendo que el código se ejecute de manera no bloqueante y proporcionando una forma limpia y modular de estructurar el código.*



# Promesas en JavaScript
Las **promesas** en JavaScript son una forma de manejar operaciones asincrónicas, como llamadas a APIs, temporizadores, o tareas que llevan tiempo, de manera más legible y manejable que las callbacks tradicionales. Una promesa representa un valor que puede estar disponible ahora, en el futuro o nunca.

### Explicación Sencilla de Promesas

Imagina que una promesa es como un "futuro" o una "promesa" de obtener un resultado. Tiene tres estados posibles:

1. **Pendiente (Pending)**: La operación asincrónica aún no ha terminado.
2. **Cumplida (Fulfilled)**: La operación asincrónica se ha completado con éxito y tiene un resultado.
3. **Rechazada (Rejected)**: La operación asincrónica ha fallado y tiene un motivo de fallo.

### Crear una Promesa

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

### Ejemplo Completo

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


# 5 tipos de funciones JavaScript
### 1. Funcion declarada / Basic function
Es la declaración básica de JavaScript, usa la keyword `function`.

Se recomienda para funciones con nombre o cuando se necesite `hoisting`.
Las funciones declaradas con la keyword `function`, se pueden elevar a la parte superior de su ámbito, es decir, del scope que las contiene. Esto permite llamar a la función antes de ser declarada 
```js
saludar(); // Hola mundo!

function saludar() {
  console.log('Hola mundo!')
}
```

### 2. Funcion expresada / Function expressions
Es la función que está dentro de una variable.
Útil para funciones anónimas o cuando se quiere controlar dónde va a estar disponible la función.
Especialmente útiles si la función va a ser usada como argumento para otra función o si va a ser específica de un scope más pequeño.
```js
const saludar = function() {
  console.log('Hola mundo!')
}
```

### 3. Arrow function o funcion de flecha
Especialmente útil para escribir funciones de una línea
```js
const saludar = () => console.log('Hola mundo!');

const saludar2 = () => {
  console.log('Hola mundo!');
}
```


### 4. Funcion anonima
No tiene nombre y se usan como callbacks generalmente
```js
setTimeout(function() {
  console.log('Hola mundo!');
}, 1000);
```


### 5. Metodos
Son las funciones dentro de un objeto o clase
```js
const obj = {
  saludar: function() {
    console.log('Hola mundo!');
  }
}
```

### 6. Funcion de constructor / Function constructor
Se pude usar el constructor `Function`para crear una nueva función.
Poco común y no es recomendado por ser inseguro.
```js
var constructorFunction = new Function('console.log("Function Constructor")');
```

## Que es el `hoisting` en JavaScript?
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

**Ejemplo**:

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

Las expresiones de funciones y las funciones flecha no son completamente elevadas. Solo la declaración de la variable se eleva, no la asignación.

**Ejemplo**:

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

Entre los beneficios del hoisting se encuentran
- Mayor flexibilidad en la legibilidad y el orden del código
- Evitar errores de referencia, el hoisting de var inicializa las variables como undefined
- El hoisting no es una característica que se usa explícitamente sino un comportamiento interno del motor de JavaScript y de cómo se procesa su código.



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