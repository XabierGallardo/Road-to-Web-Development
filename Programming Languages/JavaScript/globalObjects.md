
# 1. Objetos Globales en JavaScript: Navegador y Node.js

En JavaScript, los **objetos globales** son aquellos que están disponibles en todo el entorno de ejecución sin necesidad de importarlos o declararlos explícitamente. Los objetos globales varían ligeramente dependiendo del entorno de ejecución, ya sea un navegador web o Node.js, pero su propósito es facilitar el acceso a ciertas funciones y valores predeterminados.

#### 1. **Objetos Globales en el Navegador**
En el entorno del navegador, los objetos globales incluyen todos los objetos estándar de JavaScript (como `Array`, `String`, `Object`, etc.), así como un conjunto de objetos específicos para la interacción con la página web y su entorno.

##### 1.1. **`window`** 
El objeto global principal en el entorno del navegador es `window`. Este objeto representa la ventana del navegador y actúa como el contenedor global para todas las variables, funciones, y objetos globales en una página web. Todos los objetos, variables y funciones definidos en el ámbito global están automáticamente disponibles como propiedades del objeto `window`.

Ejemplo:
```javascript
var nombre = 'Juan';
console.log(window.nombre); // 'Juan'
```

##### Objetos y métodos importantes del objeto `window`:

- **`document`**: 
  - Representa el **DOM** de la página web actual, permitiendo el acceso y la manipulación de elementos HTML.
  - Ejemplo:
    ```javascript
    document.getElementById('miElemento');
    ```

- **`alert()`**, **`prompt()`**, **`confirm()`**: 
  - Métodos que permiten mostrar diálogos al usuario.
  - Ejemplo:
    ```javascript
    alert('Mensaje de alerta');
    ```

- **`setTimeout()`** y **`setInterval()`**:
  - Métodos para programar la ejecución de código después de un tiempo (`setTimeout`) o en intervalos regulares (`setInterval`).
  - Ejemplo:
    ```javascript
    setTimeout(() => console.log('Hola después de 2 segundos'), 2000);
    ```

- **`location`**: 
  - Proporciona información sobre la URL actual de la página y permite redireccionar a otras URL.
  - Ejemplo:
    ```javascript
    console.log(window.location.href); // URL actual
    ```

- **`navigator`**: 
  - Contiene información sobre el navegador, como la versión, el agente de usuario y la geolocalización.
  - Ejemplo:
    ```javascript
    console.log(navigator.userAgent); // Información del navegador
    ```

- **`console`**:
  - Proporciona acceso a la consola del navegador para mostrar mensajes de depuración.
  - Ejemplo:
    ```javascript
    console.log('Mensaje en la consola');
    ```

##### 1.2. **`document`**
El objeto `document` es un subobjeto de `window` y representa el **Document Object Model (DOM)** de la página web. Es la representación estructural de la página HTML que permite acceder, modificar, y manipular los elementos del documento.

Ejemplo:
```javascript
// Selecciona un elemento por su ID
const elemento = document.getElementById('miElemento');

// Cambia el contenido de texto
elemento.textContent = 'Nuevo texto';
```

##### 1.3. Otros Objetos Globales del Navegador:
- **`localStorage`** y **`sessionStorage`**:
  - Permiten almacenar datos en el navegador de manera persistente o temporal.
  - Ejemplo:
    ```javascript
    localStorage.setItem('nombre', 'Juan');
    console.log(localStorage.getItem('nombre')); // 'Juan'
    ```

- **`history`**: 
  - Proporciona acceso al historial de navegación del navegador.
  - Ejemplo:
    ```javascript
    history.back(); // Va a la página anterior
    ```

- **`XMLHttpRequest`**: 
  - Un objeto para realizar solicitudes HTTP asincrónicas, aunque hoy en día se usa más `fetch`.
  - Ejemplo:
    ```javascript
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'https://api.example.com/data');
    xhr.send();
    ```

---

#### 2. **Objetos Globales en Node.js**
En Node.js, el entorno de ejecución no tiene un objeto `window` como en los navegadores. En su lugar, existen otros objetos globales diseñados para trabajar con servidores, archivos, y otros aspectos del sistema operativo.

##### 2.1. **`global`**
El objeto principal en Node.js es **`global`**, que es el equivalente al objeto `window` en el navegador. Cualquier variable o función definida globalmente en un script de Node.js será accesible como propiedad de `global`.

Sin embargo, a diferencia del navegador, en Node.js las variables globales no son automáticamente parte de `global`, a menos que se declaren explícitamente.

Ejemplo:
```javascript
global.miVariableGlobal = 'Hola';
console.log(global.miVariableGlobal); // 'Hola'
```

##### 2.2. Objetos Globales Importantes en Node.js:

- **`process`**: 
  - Proporciona información y control sobre el proceso de ejecución de Node.js.
  - Ejemplo:
    ```javascript
    console.log(process.platform); // 'win32', 'linux', etc.
    ```

- **`__dirname`** y **`__filename`**:
  - Variables globales que contienen la ruta al directorio actual y al archivo actual, respectivamente.
  - Ejemplo:
    ```javascript
    console.log(__dirname); // Muestra el directorio actual
    console.log(__filename); // Muestra la ruta completa del archivo actual
    ```

- **`setTimeout()`** y **`setInterval()`**:
  - Igual que en los navegadores, estos métodos permiten programar la ejecución de funciones de manera asincrónica.
  - Ejemplo:
    ```javascript
    setTimeout(() => console.log('Mensaje después de 2 segundos'), 2000);
    ```

- **`require()`**: 
  - Un método para importar módulos en Node.js. Permite cargar bibliotecas externas o módulos internos en el archivo.
  - Ejemplo:
    ```javascript
    const fs = require('fs'); // Importa el módulo 'fs' (file system)
    ```

- **`console`**:
  - Igual que en el navegador, proporciona acceso a la consola para depuración y mensajes.
  - Ejemplo:
    ```javascript
    console.log('Mensaje en la consola de Node.js');
    ```

##### 2.3. Módulos Globales en Node.js
Node.js también incluye varios **módulos incorporados** que no necesitan ser instalados y que permiten acceder a funcionalidades del sistema operativo, como el sistema de archivos, la red, entre otros:

- **`fs`**: Módulo para trabajar con el sistema de archivos.
  ```javascript
  const fs = require('fs');
  fs.readFile('archivo.txt', 'utf8', (err, data) => {
    if (err) throw err;
    console.log(data);
  });
  ```

- **`http`**: Módulo para crear servidores HTTP.
  ```javascript
  const http = require('http');
  const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hola Mundo\n');
  });
  server.listen(3000);
  ```

- **`path`**: Módulo para manejar y transformar rutas de archivos.
  ```javascript
  const path = require('path');
  const rutaCompleta = path.join(__dirname, 'archivo.txt');
  console.log(rutaCompleta); // Devuelve la ruta completa del archivo
  ```

---

### Diferencias entre el Navegador y Node.js en términos de Objetos Globales

| **Característica**    | **Navegador**                     | **Node.js**                          |
|-----------------------|-----------------------------------|--------------------------------------|
| **Objeto Global**      | `window`                         | `global`                            |
| **Manipulación del DOM** | Disponible (a través de `document`) | No disponible                        |
| **Interacción con el sistema de archivos** | No disponible                  | Disponible a través de `fs`          |
| **Contexto de Ejecución** | Interacción con la página web y UI | Entorno del servidor, backend        |
| **Módulos Globales**   | No incluye módulos predefinidos  | Incluye módulos como `fs`, `http`, etc.|

### Conclusión
Los **objetos globales** son fundamentales para el funcionamiento tanto en el navegador como en Node.js, aunque el entorno de ejecución y las herramientas que proporcionan difieren. En el navegador, los objetos globales están más enfocados en la interacción con el DOM y la página web, mientras que en Node.js están diseñados para manejar tareas del servidor, sistema de archivos, y red.

___


# 2. Objeto global `event`
El **objeto global `event`** en JavaScript es un componente fundamental cuando se trata de la interacción entre el usuario y la página web. Se utiliza principalmente en el contexto del **Document Object Model (DOM)** y está disponible cuando ocurre un evento, como un clic de ratón, una pulsación de tecla, el envío de un formulario, entre otros.

Este objeto proporciona información y métodos sobre un evento específico que ha ocurrido, permitiendo a los desarrolladores manipular o responder a ese evento en el navegador. Aunque `event` no es estrictamente un objeto "global" en el sentido de que siempre esté disponible, es accesible en el contexto de los **manejadores de eventos**.

### Estructura del Objeto `event`
El objeto `event` contiene muchas propiedades y métodos que permiten al desarrollador interactuar con el evento, incluyendo información como el tipo de evento, el elemento que lo disparó, y la posibilidad de prevenir su comportamiento predeterminado o detener su propagación.

### Propiedades Comunes del Objeto `event`

1. **`type`**:
   - Especifica el tipo de evento que ha ocurrido, como `'click'`, `'keyup'`, `'submit'`, etc.
   - Ejemplo:
     ```javascript
     document.addEventListener('click', function(event) {
       console.log(event.type); // 'click'
     });
     ```

2. **`target`**:
   - El elemento en el que se produjo el evento.
   - Ejemplo:
     ```javascript
     document.addEventListener('click', function(event) {
       console.log(event.target); // Muestra el elemento clicado
     });
     ```

3. **`currentTarget`**:
   - El elemento actual que está manejando el evento, especialmente útil en la **propagación de eventos**.
   - Ejemplo:
     ```javascript
     document.addEventListener('click', function(event) {
       console.log(event.currentTarget); // Muestra el elemento que maneja el evento
     });
     ```

4. **`bubbles`**:
   - Indica si el evento se propaga hacia arriba en el árbol del DOM. Devuelve un valor booleano.
   - Ejemplo:
     ```javascript
     document.addEventListener('click', function(event) {
       console.log(event.bubbles); // true para eventos como click
     });
     ```

5. **`defaultPrevented`**:
   - Indica si se ha llamado a `event.preventDefault()` para evitar que ocurra la acción predeterminada del navegador.
   - Ejemplo:
     ```javascript
     document.querySelector('a').addEventListener('click', function(event) {
       event.preventDefault();
       console.log(event.defaultPrevented); // true
     });
     ```

6. **`timeStamp`**:
   - Proporciona el tiempo en milisegundos desde que se creó el evento.
   - Ejemplo:
     ```javascript
     document.addEventListener('click', function(event) {
       console.log(event.timeStamp); // Tiempo del evento
     });
     ```

### Métodos Comunes del Objeto `event`

1. **`preventDefault()`**:
   - Este método evita que ocurra la acción predeterminada asociada al evento. Por ejemplo, se puede usar para impedir que un formulario sea enviado o para desactivar el comportamiento de los enlaces.
   - Ejemplo:
     ```javascript
     document.querySelector('a').addEventListener('click', function(event) {
       event.preventDefault(); // Evita que el enlace sea seguido
     });
     ```

2. **`stopPropagation()`**:
   - Detiene la **propagación del evento** en la fase de burbujeo o captura. Útil cuando no se quiere que un evento siga propagándose hacia otros elementos padres.
   - Ejemplo:
     ```javascript
     document.querySelector('div').addEventListener('click', function(event) {
       event.stopPropagation(); // Detiene la propagación
     });
     ```

3. **`stopImmediatePropagation()`**:
   - Similar a `stopPropagation()`, pero además de detener la propagación del evento, evita que otros manejadores del mismo evento en el mismo elemento se ejecuten.
   - Ejemplo:
     ```javascript
     document.querySelector('button').addEventListener('click', function(event) {
       event.stopImmediatePropagation(); // Detiene todos los manejadores
     });
     ```

### Ejemplo Completo de `event` en Acción
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Evento Click</title>
</head>
<body>
    <div id="contenedor">
        <button id="miBoton">Haz clic aquí</button>
    </div>

    <script>
        // Manejador del evento click en el botón
        document.getElementById('miBoton').addEventListener('click', function(event) {
            console.log('Tipo de evento:', event.type); // 'click'
            console.log('Elemento objetivo:', event.target); // <button>Haz clic aquí</button>
            console.log('Evento burbujea:', event.bubbles); // true
        });

        // Manejador del evento en el contenedor
        document.getElementById('contenedor').addEventListener('click', function(event) {
            console.log('Clic en el contenedor');
        });

        // Si el botón tiene un enlace (hipotético), se podría prevenir el comportamiento predeterminado
        document.getElementById('miBoton').addEventListener('click', function(event) {
            event.preventDefault(); // Evita el comportamiento predeterminado si fuera un enlace
        });
    </script>
</body>
</html>
```

### Ejemplos de Tipos Comunes de Eventos:

1. **Eventos de ratón**:
   - `click`, `dblclick`, `mousedown`, `mouseup`, `mousemove`, `mouseover`, `mouseout`.
   - Ejemplo:
     ```javascript
     document.addEventListener('click', function(event) {
       console.log('Has hecho clic en:', event.target);
     });
     ```

2. **Eventos de teclado**:
   - `keydown`, `keyup`, `keypress`.
   - Ejemplo:
     ```javascript
     document.addEventListener('keydown', function(event) {
       console.log('Tecla presionada:', event.key);
     });
     ```

3. **Eventos de formulario**:
   - `submit`, `change`, `input`, `focus`, `blur`.
   - Ejemplo:
     ```javascript
     document.querySelector('form').addEventListener('submit', function(event) {
       event.preventDefault(); // Evita el envío del formulario
       console.log('Formulario enviado');
     });
     ```

4. **Eventos de ventana**:
   - `load`, `resize`, `scroll`, `unload`.
   - Ejemplo:
     ```javascript
     window.addEventListener('resize', function(event) {
       console.log('Tamaño de la ventana ha cambiado');
     });
     ```

---

### Conclusión

El objeto `event` en JavaScript es clave para manejar la interacción del usuario con una página web. Proporciona detalles sobre el evento que ocurrió, como el tipo de evento, el elemento que lo disparó, y ofrece métodos para controlar su comportamiento y propagación.

- **`event.preventDefault()`** permite detener el comportamiento predeterminado.
- **`event.stopPropagation()`** detiene la propagación del evento por el DOM.
  
Este objeto es crucial en la programación de eventos y es una herramienta poderosa para crear interfaces de usuario interactivas.

___


# 3. ¿Qué es el Objeto `console` en JavaScript?

El **objeto `console`** es un objeto global que proporciona métodos para acceder a la consola del navegador o del entorno de ejecución (por ejemplo, Node.js). Se utiliza principalmente para depurar código y mostrar mensajes informativos, advertencias o errores.

#### Métodos Comunes del Objeto `console`
1. **`console.log()`**: 
   - Muestra mensajes informativos en la consola.
   ```javascript
   console.log('Mensaje informativo');
   ```

2. **`console.error()`**: 
   - Muestra errores en la consola.
   ```javascript
   console.error('Esto es un error');
   ```

3. **`console.warn()`**: 
   - Muestra advertencias.
   ```javascript
   console.warn('Advertencia');
   ```

4. **`console.table()`**:
   - Muestra datos en forma de tabla, útil para arrays y objetos.
   ```javascript
   const usuarios = [{nombre: 'Juan', edad: 30}, {nombre: 'Ana', edad: 25}];
   console.table(usuarios);
   ```

5. **`console.time()`** y **`console.timeEnd()`**:
   - Permiten medir el tiempo de ejecución de un bloque de código.
   ```javascript
   console.time('Tiempo de ejecución');
   // Código a medir
   console.timeEnd('Tiempo de ejecución');
   ```

6. **`console.group()`** y **`console.groupEnd()`**:
   - Agrupan mensajes en la consola, lo que facilita la organización de la información.
   ```javascript
   console.group('Grupo 1');
   console.log('Mensaje dentro del grupo');
   console.groupEnd();
   ```

#### Ejemplo Completo del Objeto `console`:

```javascript
console.log('Esto es un mensaje informativo');
console.warn('Esto es una advertencia');
console.error('Esto es un error');

console.time('Tiempo de ejecución');
for (let i = 0; i < 1000; i++) {
  // Simulación de tarea
}
console.timeEnd('Tiempo de ejecución');

const usuarios = [{nombre: 'Juan', edad: 30}, {nombre: 'Ana', edad: 25}];
console.table(usuarios);
```

### Resumen
- **Objeto en JavaScript**: Es una colección de propiedades y métodos que encapsulan datos y comportamiento. Casi todo en JavaScript se trata como un objeto, lo que hace al lenguaje muy flexible y dinámico.
- **Objeto Literal**: Una forma de definir un objeto directamente con una lista de propiedades y valores.
- **`console`**: Es un objeto global utilizado principalmente para depuración y muestra de mensajes en la consola del navegador o Node.js.

___


# 4. ¿Por qué en JavaScript Todo es un Objeto?

En JavaScript, **casi todo es un objeto** porque es un lenguaje orientado a objetos, aunque no lo sea en el sentido clásico como otros lenguajes como Java o C++. En JavaScript, tanto los objetos como las funciones se tratan como "ciudadanos de primera clase", lo que significa que pueden ser asignados a variables, pasados como argumentos, y ser retornados por otras funciones.

Aunque no todos los tipos de datos en JavaScript son objetos, **muchos tipos de datos tienen comportamiento de objeto** o están envueltos en un objeto. Veamos algunos ejemplos:

1. **Datos Primitivos**: Tipos como cadenas, números, booleanos, `null`, y `undefined` son tipos primitivos en JavaScript, pero algunos de ellos (como cadenas y números) son "envolturas" de objetos.
   - Cuando interactúas con un número o una cadena, JavaScript temporalmente lo convierte en un **objeto envoltorio** para proporcionarte acceso a métodos (como `toUpperCase()` para cadenas).

   ```javascript
   let texto = 'Hola';
   console.log(texto.toUpperCase()); // 'HOLA'
   ```

2. **Funciones**: En JavaScript, las funciones son en realidad objetos de tipo `Function`. Esto permite asignarlas a variables o pasarlas como argumentos.

3. **Arrays**: Los arrays son también objetos en JavaScript, aunque tienen un comportamiento especial. Un array es un objeto que organiza sus datos mediante índices numerados.

4. **Objetos Globales**: Todo en el entorno de ejecución está basado en objetos globales. Por ejemplo, `window` en el navegador o `global` en Node.js.

