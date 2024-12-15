# Objetos en JavaScript

## Iterando objetos en JavaScript
En JavaScript, existen varias formas de iterar sobre un objeto.

---

### **1. Usando `for...in`**
El bucle `for...in` recorre todas las propiedades enumerables de un objeto.

#### Ejemplo:
```javascript
const user = {
    id: 1,
    name: "Juan",
    email: "juan@example.com",
};

for (const key in user) {
    console.log(`${key}: ${user[key]}`);
}
```

**Salida:**
```
id: 1
name: Juan
email: juan@example.com
```

**Consideraciones:**
- Incluye propiedades heredadas de la cadena de prototipos. Si no las deseas, usa `hasOwnProperty`:
  ```javascript
  if (user.hasOwnProperty(key)) {
      console.log(`${key}: ${user[key]}`);
  }
  ```

---

### **2. Usando `Object.keys()`**
Este método devuelve un arreglo con las claves propias del objeto (sin incluir propiedades heredadas). Se puede usar con un bucle `for` o métodos de arrays como `forEach`.

#### Ejemplo:
```javascript
Object.keys(user).forEach(key => {
    console.log(`${key}: ${user[key]}`);
});
```

**Salida:**
```
id: 1
name: Juan
email: juan@example.com
```

---

### **3. Usando `Object.values()`**
Devuelve un arreglo con los valores de las propiedades del objeto, lo que resulta útil cuando no necesitas las claves.

#### Ejemplo:
```javascript
Object.values(user).forEach(value => {
    console.log(value);
});
```

**Salida:**
```
1
Juan
juan@example.com
```

---

### **4. Usando `Object.entries()`**
Este método devuelve un arreglo de pares `[clave, valor]`, lo que facilita iterar tanto las claves como los valores simultáneamente.

#### Ejemplo:
```javascript
Object.entries(user).forEach(([key, value]) => {
    console.log(`${key}: ${value}`);
});
```

**Salida:**
```
id: 1
name: Juan
email: juan@example.com
```

---

### **5. Usando `for...of` con `Object.entries()`**
El bucle `for...of` combinado con `Object.entries()` permite una sintaxis más limpia para recorrer pares clave-valor.

#### Ejemplo:
```javascript
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}
```

**Salida:**
```
id: 1
name: Juan
email: juan@example.com
```

---

### **6. Usando `Map` para objetos tipo mapa**
Si el objeto es un `Map` (una estructura de datos para pares clave-valor), puedes usar directamente `for...of`.

#### Ejemplo:
```javascript
const userMap = new Map([
    ["id", 1],
    ["name", "Juan"],
    ["email", "juan@example.com"],
]);

for (const [key, value] of userMap) {
    console.log(`${key}: ${value}`);
}
```

**Salida:**
```
id: 1
name: Juan
email: juan@example.com
```

---

### **7. Usando `Object.getOwnPropertyNames()`**
Devuelve todas las propiedades propias del objeto, incluidas las no enumerables.

#### Ejemplo:
```javascript
Object.getOwnPropertyNames(user).forEach(key => {
    console.log(`${key}: ${user[key]}`);
});
```

---

### **8. Usando `Reflect.ownKeys()`**
Este método devuelve todas las claves propias del objeto, incluidas las simbólicas y no enumerables.

#### Ejemplo:
```javascript
Reflect.ownKeys(user).forEach(key => {
    console.log(`${key}: ${user[key]}`);
});
```

---

### **¿Cuál usar?**

- **`for...in`:** Útil para iterar propiedades enumerables, pero cuidado con las heredadas.
- **`Object.keys()`:** Ideal si solo necesitas las claves del objeto.
- **`Object.entries()`:** Muy conveniente para trabajar con claves y valores.
- **`for...of` con `Object.entries()`:** Limpio y fácil de leer.
- **`Reflect.ownKeys()` o `Object.getOwnPropertyNames()`:** Útiles para casos avanzados con propiedades no enumerables.


---


## 1. ¿Qué es un objeto en JavaScript?
Un **objeto** en JavaScript es una estructura de datos que permite almacenar un conjunto de pares clave-valor. Cada clave es una propiedad (o atributo) del objeto, y cada valor puede ser cualquier tipo de dato (números, cadenas, funciones, otros objetos, etc.). Los objetos son fundamentales en JavaScript porque permiten agrupar información relacionada y proporcionar un acceso organizado a los datos.

Un objeto en JavaScript se puede considerar una colección de propiedades, donde cada propiedad tiene un nombre (clave) y un valor asociado.

#### Creación de un objeto:
Existen diversas maneras de crear objetos en JavaScript, pero la más común es mediante la sintaxis de **objeto literal** (explicada a continuación). También se puede usar la palabra clave `new Object()` o clases (en versiones más modernas de JavaScript).

#### Ejemplo básico de un objeto:

```javascript
let persona = {
  nombre: "Juan",
  edad: 30,
  profesion: "Ingeniero",
  saludar: function() {
    console.log("Hola, mi nombre es " + this.nombre);
  }
};

console.log(persona.nombre);  // "Juan"
persona.saludar();            // "Hola, mi nombre es Juan"
```

En este ejemplo, el objeto `persona` tiene tres propiedades: `nombre`, `edad`, y `profesion`, así como un método `saludar` que es una función. Puedes acceder a las propiedades usando la notación de punto (.) o la notación de corchetes (`[]`).

#### Acceso a propiedades de un objeto:
- **Notación de punto**: Se usa para acceder a propiedades que no tienen caracteres especiales en su nombre.
  
  ```javascript
  console.log(persona.nombre);  // "Juan"
  ```

- **Notación de corchetes**: Se utiliza para propiedades cuyos nombres pueden contener caracteres especiales o si se accede de manera dinámica.
  
  ```javascript
  console.log(persona["profesion"]);  // "Ingeniero"
  ```

#### Actualización de propiedades:
Puedes modificar el valor de las propiedades de un objeto después de su creación:

```javascript
persona.edad = 31;
console.log(persona.edad);  // 31
```

### ¿Qué es un **objeto literal** en JavaScript?

Un **objeto literal** es una de las formas más sencillas y comunes de crear objetos en JavaScript. La sintaxis de objeto literal consiste en definir un objeto directamente usando pares clave-valor entre llaves `{}`. Es "literal" porque el objeto se crea directamente con valores fijos.

#### Ejemplo de objeto literal:
```javascript
let coche = {
  marca: "Toyota",
  modelo: "Corolla",
  anio: 2020,
  arrancar: function() {
    console.log("El coche está arrancando");
  }
};

console.log(coche.marca);  // "Toyota"
coche.arrancar();          // "El coche está arrancando"
```

#### Características del objeto literal:
1. **Clave-Valor**: Cada propiedad se define como una clave (que puede ser una cadena) y un valor (que puede ser de cualquier tipo de dato, incluso una función).
   
2. **Fácil de usar**: La sintaxis literal es la forma más rápida de definir objetos. Se utiliza mucho cuando necesitas crear un objeto simple y no necesitas usar clases o constructores.

3. **Funciones como métodos**: Puedes definir funciones dentro de los objetos, que se denominan "métodos" cuando forman parte de un objeto. En el ejemplo anterior, `arrancar` es un método del objeto `coche`.

4. **Acceso y modificación**: Los objetos literales permiten un fácil acceso y modificación de sus propiedades, como se vio anteriormente.

#### Ejemplo con acceso dinámico:
```javascript
let propiedad = "modelo";
console.log(coche[propiedad]);  // "Corolla"
```

En este caso, se usa una variable (`propiedad`) para acceder dinámicamente a una clave del objeto.

### Diferencia entre objetos y objetos literales
- **Objetos**: Son la estructura básica de datos de JavaScript, capaces de almacenar propiedades y métodos. Los objetos en JavaScript se pueden crear usando varias técnicas, incluyendo la creación de clases y constructores.
  
- **Objetos literales**: Es una de las formas más comunes y directas de crear un objeto en JavaScript. La sintaxis de objeto literal usa `{}` y asigna pares clave-valor directamente.

#### Otras maneras de crear objetos (alternativas al objeto literal):

1. **Constructor `new Object()`**:
   
   ```javascript
   let persona = new Object();
   persona.nombre = "Ana";
   persona.edad = 25;
   ```

2. **Funciones constructoras**:
   
   ```javascript
   function Persona(nombre, edad) {
     this.nombre = nombre;
     this.edad = edad;
   }
   
   let juan = new Persona("Juan", 30);
   console.log(juan.nombre);  // "Juan"
   ```

3. **Clases (ES6)**:

   ```javascript
   class Persona {
     constructor(nombre, edad) {
       this.nombre = nombre;
       this.edad = edad;
     }

     saludar() {
       console.log("Hola, soy " + this.nombre);
     }
   }

   let maria = new Persona("María", 28);
   maria.saludar();  // "Hola, soy María"
   ```

### Resumen:

- **Objeto**: Es una colección de pares clave-valor que se usa para almacenar datos relacionados en una estructura organizada.
  
- **Objeto literal**: Es una forma directa y sencilla de crear objetos en JavaScript mediante la notación `{}`.
  
Los objetos son fundamentales en JavaScript ya que proporcionan una manera de representar datos estructurados, y la notación de objeto literal es una de las formas más comunes de definir objetos de manera rápida y eficiente.


___

## 2. Objetos globales en JavaScript
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

### Comparacion de objetos globales en el navegador y en node
### Objetos globales en JavaScript: Navegador vs Node.js

En JavaScript, un **objeto global** es un objeto que está disponible de manera automática y en todos los contextos dentro de un entorno específico. Este objeto global contiene todas las variables, funciones y otras propiedades que están disponibles de manera predeterminada en dicho entorno, sin necesidad de importarlas o declararlas. Sin embargo, el objeto global varía según el entorno en el que se ejecuta el código JavaScript. Los dos entornos más comunes son el navegador y Node.js.

### 1. **Objeto global en el Navegador: `window`**

En el entorno del navegador, el objeto global es `window`. Este objeto representa una ventana del navegador en la que se carga un documento, y contiene todas las funciones y variables globales de JavaScript. También incluye muchas propiedades y métodos que permiten interactuar con la página web y con el navegador.

#### Propiedades y métodos comunes de `window`:

- **`window.document`**: Proporciona acceso al DOM del documento HTML.
- **`window.location`**: Contiene la URL de la página actual y métodos para redirigir a otras páginas.
- **`window.alert()`**: Muestra un cuadro de alerta.
- **`window.setTimeout()`**: Ejecuta una función o código después de un retraso.
- **`window.setInterval()`**: Ejecuta una función repetidamente con un retraso específico.
- **`window.localStorage`**: Permite almacenar datos en el navegador de manera persistente.
- **`window.innerWidth`** y **`window.innerHeight`**: Proporcionan el ancho y la altura interna de la ventana del navegador.
  
#### Ejemplo:

```javascript
// Accediendo a propiedades y métodos del objeto global `window`
console.log(window.document.title);  // Imprime el título de la página actual
window.alert("Hola, Mundo!");        // Muestra una alerta en la página
console.log(window.location.href);   // Imprime la URL actual
```

El objeto `window` también actúa como un contenedor para todas las variables y funciones globales definidas en el script. Por ejemplo:

```javascript
var miVariable = "Soy global";
function miFuncion() {
  console.log("Soy una función global");
}

console.log(window.miVariable); // "Soy global"
window.miFuncion();             // "Soy una función global"
```

### 2. **Objeto global en Node.js: `global`**

En el entorno de Node.js, el objeto global es `global`. Similar al objeto `window` en el navegador, `global` contiene todas las variables y funciones globales en un entorno de ejecución de Node.js. Sin embargo, `global` no tiene muchas de las propiedades que `window` posee, ya que Node.js no tiene acceso a las funcionalidades del navegador (DOM, almacenamiento local, etc.).

#### Propiedades y métodos comunes de `global`:

- **`global.setTimeout()`** y **`global.setInterval()`**: Estos métodos funcionan igual que en el navegador, programando la ejecución de funciones después de un tiempo o en intervalos regulares.
- **`global.console`**: El objeto `console` permite imprimir mensajes en la consola, igual que en el navegador.
- **`global.process`**: Contiene información sobre el proceso de Node.js, como el entorno, los argumentos pasados al script, y los eventos del proceso.
- **`global.require()`**: Función utilizada para importar módulos en Node.js.

#### Ejemplo:

```javascript
// Usando el objeto global `global` en Node.js
console.log(global.process.version);  // Imprime la versión de Node.js
global.setTimeout(() => {
  console.log("Hola después de 2 segundos");
}, 2000);

// Definir una variable global
global.miVariable = "Disponible globalmente";
console.log(global.miVariable);  // "Disponible globalmente"
```

### 3. **Comparación entre `window` y `global`**

Aunque ambos (`window` en el navegador y `global` en Node.js) sirven como el objeto global en sus respectivos entornos, hay diferencias significativas en las características que proporcionan:

| Característica               | `window` (Navegador)                | `global` (Node.js)                 |
|------------------------------|-------------------------------------|------------------------------------|
| **Interfaz del usuario**      | Proporciona métodos para interactuar con el DOM y con la interfaz del navegador (alert, prompt, etc.). | No tiene acceso al DOM ni a ninguna API del navegador. |
| **Eventos del navegador**     | Tiene acceso a eventos específicos del navegador, como `resize` y `scroll`. | No maneja eventos de interfaz gráfica. |
| **Almacenamiento**            | Tiene acceso a `localStorage`, `sessionStorage` y cookies. | No tiene acceso a almacenamiento del navegador. |
| **Manejo de archivos**        | No tiene acceso directo al sistema de archivos. | Tiene acceso a las APIs del sistema de archivos (`fs`). |
| **Variables globales**        | Definir variables globales con `var`, `let`, `const` las agrega a `window`. | Las variables globales no se agregan automáticamente a `global`. |
| **Módulos**                   | No tiene soporte de módulos nativo (utiliza `<script>`). | Usa el sistema de módulos de CommonJS con `require()` y `module.exports`. |

### Ejemplos de uso:

#### En el navegador (usando `window`):

```html
<!DOCTYPE html>
<html>
<head>
  <title>Ejemplo de Objeto Global</title>
</head>
<body>
  <h1>Usando el objeto global window</h1>
  <script>
    // Usar alert desde el objeto window (implícito)
    alert("Bienvenido al sitio web!");

    // Accediendo a propiedades del objeto global `window`
    console.log(window.location.href);  // URL actual
    console.log(window.innerWidth);     // Ancho de la ventana
  </script>
</body>
</html>
```

#### En Node.js (usando `global`):

```javascript
// archivo.js
// Usar el objeto global `global` en Node.js

// Mostrar información del proceso
console.log(global.process.version); // Versión de Node.js

// Usar setTimeout, que también es global
global.setTimeout(() => {
  console.log("Esto aparece después de 3 segundos.");
}, 3000);

// Definir una variable global explícitamente
global.miVariableGlobal = "¡Hola desde Node.js!";
console.log(global.miVariableGlobal); // "¡Hola desde Node.js!"
```

### 4. **¿Qué son los objetos globales en general?**
Un **objeto global** es aquel que está disponible en todo el programa sin necesidad de importarlo o referenciarlo específicamente. En JavaScript, estos objetos proporcionan funcionalidades básicas y esenciales que los desarrolladores usan con frecuencia.

Además de `window` y `global`, JavaScript incluye otros objetos y funciones globales que están disponibles en cualquier entorno de ejecución:

#### Otros objetos y funciones globales comunes:
- **`Math`**: Proporciona funciones y constantes matemáticas.
- **`Date`**: Proporciona funciones para manipular fechas y horas.
- **`JSON`**: Proporciona métodos para trabajar con datos JSON (`JSON.parse()`, `JSON.stringify()`).
- **`console`**: Proporciona métodos para imprimir mensajes en la consola (`console.log()`, `console.error()`).
- **`setTimeout` y `setInterval`**: Temporizadores que ejecutan código después de un tiempo específico o a intervalos regulares.
- **`parseInt` y `parseFloat`**: Convierte cadenas en números enteros o flotantes, respectivamente.

### Resumen:

- En el navegador, el objeto global es `window`, que proporciona acceso a la manipulación del DOM y a muchas características relacionadas con el navegador.
- En Node.js, el objeto global es `global`, que proporciona acceso a características del sistema y a las APIs de Node.js, pero no tiene acceso a funciones del navegador.
- Ambos objetos globales contienen funciones y propiedades esenciales que están disponibles en todo el entorno, como `console`, `setTimeout`, y `Math`.
