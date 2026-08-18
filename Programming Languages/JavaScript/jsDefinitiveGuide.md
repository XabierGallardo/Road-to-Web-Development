# [JavaScript / La Guía Definitiva](https://scienceadvantage.net/wp-content/uploads/2020/08/JavaScript-The-Definitive-Guide-Master-The-Worlds-Most-Used-Programming-Language-7th-Edition-04.08-2020-.pdf)

# 0. Prefacio
Este libro cubre el lenguaje JavaScript y las APIs de JavaScript implementadas por los navegadores y por Node.


## 0.1 APIs principales de JavaScript


JavaScript cuenta con un vasto ecosistema de APIs. Dado que JavaScript fue creado originalmente para el navegador y luego fue extraído para funcionar en servidores con Node.js, hay un conjunto de APIs que comparten (definidas por el estándar ECMAScript) y otras que son exclusivas de cada entorno.

Podemos desglosar las siguientes APIs:

---

### 1. APIs Comunes (Implementadas por ambos)
Estas APIs están definidas por la especificación **ECMAScript** o por estándares universales y funcionan exactamente igual (o muy similar) tanto en el navegador como en Node.js:

*   **Manipulación de datos y sintaxis:**
    *   `String`, `Number`, `Math`, `Date`, `RegExp`, `Array`, `Object`, `JSON`.
    *   *Nota:* Históricamente hubo diferencias, pero hoy en día están totalmente estandarizadas.
*   **Estructuras de datos modernas:**
    *   `Promise`, `Map`, `Set`, `WeakMap`, `WeakSet`, `Symbol`.
*   **APIs de Iteración y Funciones:**
    *   `Array.prototype` (`.map`, `.filter`, `.reduce`), `Object.entries`, `Object.values`.
*   **Internacionalización:**
    *   `Intl` (para formatear fechas, números y monedas según la localidad).
*   **Módulos:**
    *   `import` / `export` (Sintaxis ESM). *Nota: Node lo soporta nativamente desde la versión 12+, aunque con diferencias de configuración.*
*   **APIs Web Universales (Fetch, Timers, etc.):**
    *   **`fetch`:** Node.js lo implementó de forma experimental en v18 y estable en v21.
    *   **Timers:** `setTimeout`, `setInterval`, `setImmediate` (con ligeras variaciones de rendimiento).
    *   **`console`:** Aunque la implementación interna es distinta, la API de superficie es la misma.
    *   **`URL` y `URLSearchParams`:** Disponibles globalmente en ambos.
    *   **`TextEncoder` y `TextDecoder`:** Disponibles globalmente en ambos.
    *   **`crypto.subtle` (WebCrypto):** Disponible en navegadores modernos y en Node (desde v15 globalmente).

---

### 2. APIs Exclusivas del Navegador (Web APIs)
Estas APIs están ligadas al modelo del navegador (ventanas, pestañas, interacción del usuario y seguridad del cliente).

**A. DOM (Document Object Model)**
*   **`document`:** El punto de entrada principal para manipular HTML.
    *   `document.getElementById`, `querySelector`, `createElement`, `innerHTML`, etc.
*   **Eventos:** `addEventListener`, `Event`, `MouseEvent`, `KeyboardEvent`.
*   **`MutationObserver`:** Para observar cambios en el árbol del DOM.
*   **`IntersectionObserver`:** Para saber cuándo un elemento entra o sale del viewport.

**B. BOM (Browser Object Model)**
*   **`window`:** El objeto global del navegador.
*   **`location`:** Para manipular la URL actual (redirecciones, recargar).
*   **`history`:** Para navegar entre páginas (SPA - Single Page Applications).
*   **`navigator`:** Información del navegador y del dispositivo (geolocalización, batería, conexión).
*   **`localStorage` / `sessionStorage`:** Almacenamiento síncrono clave-valor en el cliente.

**C. Renderizado y Gráficos**
*   **Canvas API:** Dibujo 2D y 3D (WebGL).
*   **WebGL / WebGPU:** Acceso a la GPU para gráficos de alto rendimiento.
*   **SVG API:** Manipulación de gráficos vectoriales.

**D. Multimedia y Dispositivos**
*   **Web Audio API:** Procesamiento y síntesis de audio.
*   **MediaDevices / getUserMedia:** Acceso a cámara y micrófono.
*   **WebRTC:** Comunicación en tiempo real (videollamadas, P2P).
*   **Web Speech API:** Reconocimiento y síntesis de voz.

**E. Red y Comunicación**
*   **XMLHttpRequest (XHR):** La forma antigua de hacer peticiones HTTP (aún soportada).
*   **WebSockets:** Comunicación bidireccional en tiempo real (también existe en Node, pero como librería externa o global reciente).
*   **Server-Sent Events (EventSource):** Recepción de eventos unidireccionales del servidor.
*   **Web Workers / Service Workers:** Multithreading y soporte offline.

---

### 3. APIs Exclusivas de Node.js
Node.js no tiene el concepto de `window` o DOM. En su lugar, se centra en el sistema operativo, archivos, procesos y servidores.

**A. Sistema de Archivos (fs)**
*   **API:** `fs.readFile`, `fs.writeFile`, `fs.readdir`, `fs.watch`, etc.
*   **Característica clave:** Ofrece versiones Síncronas (`fs.readFileSync`), Callback (`fs.readFile`) y Basadas en Promesas (`require('fs').promises.readFile`).

**B. Sistema Operativo (os) y Procesos**
*   **`process`:** El objeto global principal. Información del proceso actual.
    *   `process.argv` (argumentos), `process.env` (variables de entorno), `process.exit()`, `process.cwd()`.
*   **`os`:** Información del sistema operativo anfitrión (memoria libre, CPUs, tipo de SO).

**C. Módulos y Paquetes (CommonJS)**
*   **`require` y `module.exports`:** Aunque Node soporta ESM (`import`), la sintaxis `require` sigue siendo el estándar de facto en el ecosistema npm.

**D. Red y Servidores**
*   **`http` y `https`:** Los módulos de más bajo nivel para crear servidores web o hacer peticiones sin depender de librerías externas (como Express).
*   **`net`:** Para crear servidores y clientes TCP.
*   **`dgram`:** Para protocolo UDP.
*   **`dns`:** Resolución de nombres de dominio.

**E. Utilidades de Buffer y Streams**
*   **`Buffer`:** Clase global para manejar datos binarios crudos (muy usada al leer archivos o manejar sockets). En el navegador ahora existe `ArrayBuffer`, pero la implementación clásica de Node es `Buffer`.
*   **`Stream`:** Módulo fundamental para procesar datos en trozos (chunks) sin cargar todo en memoria (clave para el rendimiento de Node).

**F. Seguridad y Criptografía**
*   **`crypto`:** Aunque ahora comparte el estándar `WebCrypto`, Node expone una API más avanzada y de más bajo nivel para encriptación, hashing y generación de números aleatorios.

**G. Hilos y Rendimiento**
*   **`worker_threads`:** Para ejecutar JavaScript en paralelo (multi-threading real, a diferencia del event loop).
*   **`cluster`:** Para crear múltiples procesos hijos que comparten el mismo puerto de red.

---

### Resumen comparativo rápido

| Característica | Navegador | Node.js |
| :--- | :--- | :--- |
| **DOM (document, window)** | ✅ Sí | ❌ No |
| **Fetch** | ✅ Sí | ✅ Sí (desde v18+) |
| **Filesystem (fs)** | ❌ No (seguridad) | ✅ Sí |
| **Web Workers** | ✅ Sí (dedicados) | ✅ Sí (worker_threads, distinta API) |
| **localStorage** | ✅ Sí | ❌ No |
| **process.env** | ❌ No | ✅ Sí |
| **Timers** | ✅ Sí | ✅ Sí |
| **Web Audio** | ✅ Sí | ❌ No (requiere librerías nativas) |



---


# 1. Introduccion a JavaScript

## 1.1 JavaScript como lenguaje multiparadigma
Los **estilos de programación** (también llamados **paradigmas de programación**) son formas fundamentales de estructurar y organizar el código para resolver problemas. No son lenguajes en sí, sino "filosofías" o enfoques que puedes aplicar al escribir código.

Aquí tienes los principales estilos, divididos en dos grandes categorías: **Paradigmas principales** y **Paradigmas de especialidad**.

---

### 1. Paradigmas Principales

Estos son los estilos más comunes que encontrarás en la industria y en la mayoría de los lenguajes populares (JavaScript, Python, Java, C++, etc.).

#### A. Programación Imperativa
Es el estilo más antiguo y básico. Consiste en darle a la computadora una secuencia exacta de pasos (comandos) para cambiar el estado del programa.

-   **Concepto clave:** "¿CÓMO se hace?" (paso a paso).
-   **Elementos:** Bucles (`for`, `while`), condicionales (`if`), variables que se reasignan constantemente.
-   **Ejemplo (JavaScript):**
    ```javascript
    let total = 0;
    let numeros = [1, 2, 3, 4];
    for (let i = 0; i < numeros.length; i++) {
        total = total + numeros[i]; // Cambiando el estado de 'total'
    }
    console.log(total); // 10
    ```

#### B. Programación Declarativa
Es el concepto opuesto al imperativo. En lugar de decir "cómo" hacer las cosas, le dices al programa "qué" quieres obtener. El "cómo" se abstrae.

-   **Concepto clave:** "¿QUÉ quiero obtener?".
-   **Ejemplo:** SQL (bases de datos), HTML, o funciones de alto nivel en JS.
    ```javascript
    let numeros = [1, 2, 3, 4];
    let total = numeros.reduce((acumulador, numero) => acumulador + numero, 0);
    // No le dije que hiciera un bucle, le dije que "redujera" el array a una suma.
    ```

#### C. Programación Orientada a Objetos (POO / OOP)
Este estilo modela el código basándose en "objetos" del mundo real. Cada objeto tiene **propiedades** (datos) y **métodos** (funciones que actúan sobre esos datos).

-   **Conceptos clave:** Clases, Herencia, Encapsulamiento, Polimorfismo.
-   **Ideal para:** Videojuegos, interfaces gráficas, sistemas empresariales complejos.
-   **Ejemplo (JavaScript moderno):**
    ```javascript
    class Coche {
        constructor(marca) {
            this.marca = marca;
            this.velocidad = 0;
        }
        acelerar() {
            this.velocidad += 10;
        }
    }
    const miCoche = new Coche("Toyota");
    miCoche.acelerar();
    ```

#### D. Programación Funcional (PF)
Trata la programación como si fuera matemática. Se basa en "funciones puras" (sin efectos secundarios) y en tratar los datos como **inmutables** (no se modifican, se crean copias).

-   **Conceptos clave:** Funciones puras, inmutabilidad, recursión, funciones de orden superior (`.map`, `.filter`, `.reduce`), composición de funciones.
-   **Ideal para:** Ciencia de datos, procesamiento de grandes flujos de datos, sistemas que requieren alta confiabilidad.
-   **Ejemplo (JavaScript):**
    ```javascript
    const numeros = [1, 2, 3];
    // No modificamos 'numeros', creamos un array nuevo
    const dobles = numeros.map(n => n * 2); 
    ```

#### E. Programación Orientada a Eventos (Event-Driven)
El flujo del programa no sigue una línea recta, sino que reacciona a "eventos" (clics del usuario, respuestas de un servidor, timers). Es el estilo dominante en el desarrollo web frontend.

-   **Concepto clave:** Event Loop, Listeners (escuchadores), Callbacks.
-   **Ejemplo (JavaScript en el navegador):**
    ```javascript
    // No sabemos cuándo el usuario hará clic, pero definimos qué pasará cuando lo haga.
    document.getElementById("boton").addEventListener("click", () => {
        console.log("¡Me hicieron clic!");
    });
    ```

---

### 2. Paradigmas Secundarios o Derivados

Estos estilos a menudo se mezclan con los anteriores o están ganando popularidad recientemente.

#### F. Programación Procedural
Es un subconjunto de la Programación Imperativa. Consiste en agrupar el código imperativo en "procedimientos" o "funciones" reutilizables para evitar repetir código. (Muchos lenguajes como C usan este estilo).

-   **Diferencia con POO:** No usa clases ni objetos, solo funciones sueltas.

#### G. Programación Reactiva
Es una evolución de la Programación Funcional y Orientada a Eventos. Se centra en "flujos de datos" (streams) y en la propagación automática del cambio. Si una variable cambia, todo lo que depende de ella se actualiza solo.

-   **Ejemplos modernos:** Librerías como RxJS, o frameworks de UI como React, Vue o Svelte (el "estado" cambia y la "vista" reacciona).

#### H. Programación Genérica (Metaprogramación)
Consiste en escribir código que puede funcionar con cualquier tipo de dato sin necesidad de reescribirlo. Es muy común en lenguajes fuertemente tipados como C++ o TypeScript (usando *Genéricos* `<T>`).

#### I. Programación Lógica
Se basa en definir un conjunto de hechos y reglas lógicas. El programa "infiere" las respuestas. Es muy usada en Inteligencia Artificial.

-   **Lenguaje representativo:** Prolog.

#### J. Programación Concurrente y Paralela
Estilo enfocado en ejecutar múltiples tareas "al mismo tiempo". Puede ser real (multihilos en CPUs de varios núcleos) o simulada (como el Event Loop de JavaScript o los async/await).

---

### Resumen en JavaScript: ¿Cuál deberías usar?

JavaScript es un lenguaje **multiparadigma**, lo que significa que puedes mezclar todos estos estilos en un mismo proyecto:

1.  **Orientado a Objetos (POO):** Usado mucho en el Backend (Node.js con TypeScript) y en aplicaciones grandes empresariales (Angular).
    *   *Estilo:* `class`, `new`, `this`, `extends`.
2.  **Funcional (PF):** Es el estilo dominante en el Frontend moderno (React, Redux).
    *   *Estilo:* Funciones flecha, `.map`, `.filter`, `...spread`, evitando mutar variables.
3.  **Orientado a Eventos:** Es el corazón de JavaScript tanto en el navegador (clics) como en Node.js (el patrón `EventEmitter`).
4.  **Imperativo:** Es como todo el mundo empieza a programar, y lo usas para escribir la lógica básica dentro de tus funciones.

**La clave:** Un buen programador no se casa con un solo estilo; elige el que mejor resuelve el problema específico que tiene delante.


---


## 1.2 JavaScript como lenguaje de proposito general
Cuando decimos que JavaScript es un **lenguaje de propósito general (General-Purpose Language)**, significa que **no fue diseñado para resolver un único tipo de problema o funcionar en un solo entorno**, sino que es lo suficientemente flexible y completo como para usarse en casi cualquier ámbito del desarrollo de software.

Esto contrasta con los **lenguajes de dominio específico (DSL - Domain-Specific Languages)**, que están creados para hacer una sola cosa muy bien.

---

### La metáfora perfecta: La Navaja Suiza vs. El Taladro

*   **Lenguaje de dominio específico (DSL):** Es como un taladro. Es perfecto para hacer agujeros (ej. SQL para bases de datos, o HTML para estructurar páginas web), pero no sirve para cortar madera o apretar tornillos.
*   **Lenguaje de propósito general (JavaScript):** Es una navaja suiza. Puedes cortar, abrir botellas, usar el destornillador y hasta limarte las uñas. No será el mejor taladro del mundo, pero puede hacer un agujero si es necesario.

---

### ¿En qué áreas se puede usar JavaScript hoy en día?

Para justificar su título de "propósito general", JavaScript salió del navegador y conquistó prácticamente todas las capas del desarrollo de software:

1.  **Desarrollo Web Frontend (El origen):**
    *   Manipular el DOM, animaciones, lógica de interfaces, frameworks como React, Vue o Angular.

2.  **Desarrollo Backend (Servidores):**
    *   Gracias a **Node.js**, **Deno** o **Bun**, JavaScript corre fuera del navegador. Puedes crear APIs REST, manejar bases de datos, gestionar autenticación y manejar miles de conexiones simultáneas (como hace Netflix o PayPal).

3.  **Aplicaciones de Escritorio:**
    *   Con frameworks como **Electron** (usado por VS Code, Slack, Discord) o **Tauri**, puedes construir aplicaciones nativas para Windows, Mac y Linux usando solo JavaScript, HTML y CSS.

4.  **Aplicaciones Móviles:**
    *   Con **React Native** o **Ionic**, escribes el código una vez en JavaScript y generas aplicaciones nativas o híbridas para iOS y Android (Facebook, Instagram y Airbnb usan esto en parte).

5.  **Internet de las Cosas (IoT) y Robótica:**
    *   Frameworks como **Johnny-Five** o **Cylon.js** permiten programar microcontroladores (como Arduino o Raspberry Pi) para encender luces, leer sensores o mover motores usando JavaScript.

6.  **Inteligencia Artificial y Ciencia de Datos:**
    *   Aunque Python es el rey aquí, JavaScript tiene librerías potentes como **TensorFlow.js** para entrenar y ejecutar redes neuronales directamente en el navegador o en Node.

7.  **Bases de Datos:**
    *   Bases de datos NoSQL como **MongoDB** utilizan JavaScript como su lenguaje de consulta interno.

8.  **Automatización de Tareas (Scripting):**
    *   Puedes escribir un script en Node.js para renombrar cientos de archivos en tu computadora, descargar información de internet automáticamente (Web Scraping con Puppeteer) o publicar posts en redes sociales.

---

### ¿Por qué JavaScript logró ser de "Propósito General"?

Originalmente (1995), JavaScript era un lenguaje de scripting *solo* para el navegador, muy limitado. Se convirtió en un lenguaje de propósito general gracias a tres factores clave:

1.  **El Event Loop (Programación Asíncrona):** JavaScript fue diseñado para no bloquearse. Esto lo hace ideal para manejar muchas tareas a la vez (como leer un archivo mientras responde a un chat), lo cual es vital para servidores modernos.
2.  **El motor V8 (de Google Chrome):** En 2008, Google creó un motor increíblemente rápido para ejecutar JavaScript. Un programador llamado Ryan Dahl tomó ese motor, lo sacó del navegador, le añadió APIs para leer archivos y crear servidores, y nació **Node.js**.
3.  **Una comunidad gigante y NPM:** Al ser el único lenguaje que entienden los navegadores, millones de programadores ya lo sabían. Al sacarlo del navegador, toda esa gente pudo aplicar su conocimiento para crear herramientas para otras áreas, llenando el registro de paquetes (NPM) con soluciones para casi todo.

**En resumen:** Ser un lenguaje de propósito general significa que con JavaScript no solo haces páginas web; puedes crear el servidor que las alimenta, la base de datos que las guarda, la app móvil que las consume y el robot que te trae un café mientras programas.


---


## 1.3 Nombres, versiones y modos en JavaScript
JavaScript fue creado por Netscape en los primeros años de la web, denominado "JavaScript", Netscape delegó la estandarizacion del lenguaje a ECMA (European Computer Manufacturer's Association). Como JavaScript era una marca registrada de Sun Microsystems (ahora Oracle), debido a cuestiones relativas a esta marca registrada, la versión estandarizada de JavaScript fue registrada como ECMAScript.

Desde el estandar ES6 en 2015, donde se implementaron grandes cambios que hicieron que JavaScript pasara de ser un lenguaje de scripting a un lenguaje serio de proposito general para proyectos complejos de ingenieria de software. Desde entonces, a partir de ES6, los lanzamientos y las nuevas implementaciones en JavaScript son anuales (ES2016, ES2017, ES2020,ES2025, etc)


## 1.4 Como funciona JavaScript?
La idea central es esta:

> **JavaScript como lenguaje define las herramientas fundamentales para manipular datos, pero necesita un entorno que le proporcione herramientas para interactuar con el mundo exterior.**

### 1. ¿Qué es el lenguaje JavaScript?

El lenguaje JavaScript, por sí mismo, define cosas como:

```js
let nombre = "Juan";
let numeros = [1, 2, 3];

console.log(numeros.length);

let persona = {
    nombre: "Juan",
    edad: 30
};
```

También define:

* variables
* funciones
* objetos
* arrays
* strings
* números
* `Map`
* `Set`
* `Promise`
* `Date`
* operadores
* estructuras `if`, `for`, `while`
* clases
* módulos, etc.

Estas características forman parte de la **especificación del lenguaje JavaScript** (ECMAScript).

Pero hay una pregunta importante:

**¿Cómo hago para leer un archivo?**

```js
leerArchivo("datos.txt");
```

¿Quién implementa `leerArchivo()`?

JavaScript como lenguaje no lo define.

Lo mismo ocurre con:

```js
enviarDatosPorInternet(...)
crearVentana(...)
dibujarEnPantalla(...)
leerTeclado(...)
accederAlGPS(...)
```

Todas esas cosas dependen del **entorno donde se ejecuta JavaScript**.

---

### 2. ¿Qué es una librería estándar?

Una **librería estándar (standard library)** es un conjunto de funcionalidades que vienen asociadas oficialmente a un lenguaje y que permiten hacer tareas comunes sin tener que implementarlas desde cero.

Por ejemplo, JavaScript tiene funcionalidades estándar para trabajar con texto:

```js
"Hola".toUpperCase();
```

Arrays:

```js
[1, 2, 3].map(x => x * 2);
```

Sets:

```js
let conjunto = new Set([1, 2, 3]);
```

Mapas:

```js
let mapa = new Map();
mapa.set("nombre", "Juan");
```

Y objetos como:

```js
Math
JSON
Date
Promise
RegExp
Map
Set
```

Todo eso forma parte de las APIs que proporciona el ecosistema estándar de JavaScript/ECMAScript.

Por eso el libro dice:

> "The core JavaScript language defines a minimal API for working with numbers, text, arrays, sets, maps, and so on"

Es decir:

**el núcleo de JavaScript trae herramientas básicas para trabajar con datos.**

---

### 3. Entonces, ¿qué es una "plataforma"?

Aquí está la parte que puede resultar confusa.

Una **plataforma** es el entorno completo que proporciona JavaScript para poder hacer cosas útiles.

Por ejemplo, cuando ejecutás JavaScript en un navegador, tenés:

```text
JavaScript
    │
    ▼
Navegador
    │
    ├── DOM
    ├── Web APIs
    ├── fetch()
    ├── localStorage
    ├── Canvas
    ├── WebSockets
    ├── Geolocation
    └── etc.
```

El navegador es el **host environment** (entorno anfitrión) de JavaScript.

JavaScript proporciona:

```js
let numeros = [1, 2, 3];

numeros.map(x => x * 2);
```

Pero el navegador proporciona cosas como:

```js
document.querySelector("button");

fetch("https://example.com");

localStorage.setItem("nombre", "Juan");

navigator.geolocation.getCurrentPosition(...);
```

Estas APIs **no son simplemente "el lenguaje JavaScript"**.

Son APIs proporcionadas por el navegador.

---

### 4. Y Node.js es otro host environment

Esto es especialmente importante si estás aprendiendo Node.js.

Podemos pensar:

```text
                    JavaScript
                        │
             ┌──────────┴──────────┐
             │                     │
         Navegador               Node.js
             │                     │
        Web APIs              APIs de Node
             │                     │
       ┌─────┼─────┐        ┌──────┼──────┐
       │     │     │        │      │      │
      DOM  fetch  Canvas    fs    http   process
```

Por ejemplo:

#### JavaScript estándar

```js
const numeros = [1, 2, 3];

console.log(numeros.map(n => n * 2));
```

Esto pertenece al ecosistema estándar del lenguaje.

#### Node.js

```js
import fs from "fs";

fs.readFileSync("archivo.txt", "utf8");
```

`fs` no es una característica del lenguaje JavaScript.

Es una API proporcionada por **Node.js**.

Por eso:

```js
fs.readFileSync(...)
```

funciona en Node.js, pero no podés asumir que funciona directamente en un navegador.

---

### 5. Un ejemplo todavía más claro

Imaginá que JavaScript es un idioma.

El idioma te permite formar frases:

> "Quiero abrir el archivo."

Pero saber decir esa frase **no significa que tengas la capacidad física de abrir el archivo**.

Necesitás un entorno que te dé esa capacidad.

En programación:

```text
Lenguaje JavaScript
        │
        │ define
        ▼
Sintaxis + tipos + estructuras + operaciones básicas
        │
        │ se ejecuta dentro de
        ▼
Host Environment
        │
        ├── Browser
        │      ├── DOM
        │      ├── fetch
        │      ├── Canvas
        │      └── Web Storage
        │
        └── Node.js
               ├── fs
               ├── http
               ├── net
               ├── process
               └── streams
```

El **host environment** le proporciona a JavaScript las capacidades para interactuar con el exterior.

---

### 6. ¿Y por qué el texto menciona "input/output"?

Porque un lenguaje necesita alguna forma de interactuar con el exterior.

Por ejemplo:

**Input:**

```text
teclado → programa
archivo → programa
red → programa
cámara → programa
```

**Output:**

```text
programa → pantalla
programa → archivo
programa → red
programa → impresora
```

JavaScript no define por sí mismo cosas como:

```js
leerTeclado()
leerArchivo()
mostrarVentana()
enviarPorRed()
```

El entorno donde se ejecuta JavaScript decide cómo ofrecer esas capacidades.

---

### 7. La diferencia entre JavaScript, Web APIs y Node.js

Esta distinción te va a resultar muy útil:

| Cosa                             | ¿Quién la proporciona? | Ejemplo                             |
| -------------------------------- | ---------------------- | ----------------------------------- |
| Lenguaje JavaScript              | ECMAScript             | `let`, `if`, `Array`, `Map`         |
| Standard library / APIs estándar | ECMAScript             | `JSON`, `Math`, `Promise`, `Map`    |
| Web APIs                         | Navegador              | `document`, `fetch`, `localStorage` |
| APIs de Node.js                  | Node.js                | `fs`, `http`, `process`             |
| Librerías externas               | terceros               | Express, Axios, Lodash              |

Por ejemplo:

```js
const express = require("express");
```

`express` **no es JavaScript**.

Tampoco es parte de la librería estándar de JavaScript.

Es una **librería externa** que alguien instaló, normalmente mediante npm.

---

### 8. Una distinción importante: librería vs plataforma

Una **librería** es normalmente un conjunto de código que te proporciona funcionalidades.

Por ejemplo:

```text
Express
Axios
React
Lodash
```

Una **plataforma/entorno** es mucho más grande. Incluye el motor que ejecuta JavaScript y numerosas APIs y servicios.

Por ejemplo:

```text
Node.js
```

incluye:

```text
JavaScript engine (V8)
        +
Node.js APIs
        +
módulos
        +
event loop
        +
sistema de módulos
        +
herramientas
```

Por eso Node.js se considera un **runtime/environment** para JavaScript, mientras que Express es una **librería/framework** que corre encima de Node.js.

---

### En una frase

El párrafo quiere decir:

> **JavaScript define principalmente cómo escribir y manipular datos dentro de un programa; el entorno en el que JavaScript se ejecuta —por ejemplo un navegador o Node.js— le proporciona las herramientas necesarias para comunicarse con archivos, redes, pantalla, sistema operativo, etc.**

Y esto explica por qué **JavaScript en el navegador y JavaScript en Node.js tienen el mismo lenguaje, pero APIs disponibles diferentes**.


## 1.5 Expresiones, Sentencias y Funciones

Si las **expresiones** en JavaScript fuesen frases, las **sentencias** serian oraciones completas.
- Una expresion es algo que computa un valor, nada mas, no alteran el estado del programa de ninguna manera
- Las sentencias por otra parte no tienen un valor pero alteran el estado.

Una funcion es un bloque nombrado de JavaScript que se define una vez y se invoca cuantas veces se quiera.



---



# 2. Estructura lexica

*-- pp 33*



---



# 3. Tipos, Valores y variables
### 3.1 Tipos de datos en JavaScript
Los tipos de datos en JavaScript se pueden dividir en 2 categorías, tipos de datos primitivos y objetos

#### Tipos de datos primitivos
En JavaScript, los tipos de datos primitivos son valores que no son objetos y no tienen métodos. Estos son los tipos de datos más básicos y fundamentales que se pueden usar para almacenar y manipular datos en JavaScript. Los principales tipos de datos primitivos son:

1. **`String`**:
   - Representa una cadena de caracteres, por ejemplo, `"Hola"`, `'Mundo'`.
   - Se puede definir con comillas simples (`'...'`), comillas dobles (`"..."`), o backticks para strings de plantilla (`` `...` ``).

2. **`Number`**:
   - Representa tanto números enteros como de punto flotante, por ejemplo, `42`, `3.14`.
   - En JavaScript, no existe una distinción entre enteros y decimales; ambos son considerados de tipo `Number`.

3. **`Boolean`**:
   - Representa un valor lógico que puede ser `true` o `false`.
   - Se utiliza comúnmente en operaciones condicionales y control de flujo.

4. **`Undefined`**:
   - Es el valor que se le asigna a una variable que ha sido declarada pero no inicializada.
   - También es el valor devuelto por funciones que no especifican un valor de retorno.

5. **`Null`**:
   - Representa la ausencia intencional de cualquier objeto o valor.
   - Es un tipo especial que indica que una variable se ha establecido en "ningún valor" o "vacío".

6. **`Symbol`** (introducido en ECMAScript 6):
   - Representa un valor único e inmutable que se utiliza como identificador de propiedades de objetos.
   - Cada valor de tipo `Symbol` es único y se puede crear usando `Symbol()`.

7. **`BigInt`** (introducido en ECMAScript 2020):
   - Se utiliza para representar números enteros que son demasiado grandes para ser representados por el tipo `Number`.
   - Se define agregando una `n` al final de un número entero, por ejemplo, `123n`.

### Ejemplo de Uso:
```javascript
let name = "Alice";       // String
let age = 30;             // Number
let isAdult = true;       // Boolean
let x;                    // Undefined
let y = null;             // Null
let uniqueId = Symbol();  // Symbol
let bigNumber = 1234567890123456789012345678901234567890n; // BigInt
```

### Notas Adicionales:
- **`Undefined`** y **`Null`** son similares pero diferentes; `undefined` indica una variable no inicializada, mientras que `null` se utiliza intencionalmente para denotar "sin valor".
- **`Symbol`** es útil cuando se necesita una clave única en un objeto que no colisionará con ninguna otra clave.
- **`BigInt`** permite trabajar con números enteros más allá del rango seguro de los números `Number`.

Estos tipos de datos son fundamentales para entender cómo funciona la gestión de memoria y el manejo de valores en JavaScript.


---


# 4. Expresiones y operadores

---


# 5. Declaraciones

---

# 6. Objetos

---

# 7. Arrays

---

# 8. Funciones

---

# 9. Clases

---

# 10.Modulos

---

# 11. La Libreria estandar de JavaScript

---

# 12. Generadores e iteradores

---

# 13. JavaScript asincrono

---

# 14. Metaprogramacion

---

# 15. JavaScript en navegadores web

---

# 16. JavaScript en el servidor con Node

---

# 17. Herramientas de JavaScript y Extensiones