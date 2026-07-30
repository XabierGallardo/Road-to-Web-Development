# Event Loop y Call Stack en JavaScript

## Explicacion sencilla
Claro. Estos dos conceptos suelen ser difíciles al principio porque muchas explicaciones hablan del **Call Stack**, las **Web APIs**, las **colas** y el **Event Loop** al mismo tiempo. Vamos a construir la idea desde cero.

---

## Imagina que JavaScript es una persona

Supongamos que JavaScript es una persona trabajando en una oficina.

Sobre su escritorio tiene una lista de tareas.

```text
1. Imprimir "Hola"
2. Sumar dos números
3. Mostrar el resultado
```

La persona solo tiene **dos manos y un solo cerebro**.

No puede hacer dos tareas exactamente al mismo tiempo.

Primero hace una.

Después otra.

Después otra.

```text
Tarea 1

↓

Tarea 2

↓

Tarea 3
```

Eso significa que JavaScript es **single-threaded**.

---

## ¿Qué es un hilo (Thread)?

Un hilo es una secuencia de ejecución.

Imagina una carretera.

### Un solo carril

```text
🚗

↓

🚗

↓

🚗
```

Los coches pasan uno detrás del otro.

No pueden adelantarse.

---

### Dos carriles

```text
🚗      🚙

↓       ↓

🚕      🚓
```

Ahora sí pueden avanzar al mismo tiempo.

---

JavaScript tiene un único carril para ejecutar código JavaScript.

```text
console.log()

↓

sumar()

↓

mostrarResultado()
```

Nunca ejecuta dos funciones JavaScript simultáneamente.

---

## ¿Qué ocurre cuando encuentra una función?

Supongamos:

```javascript
function saludar() {
    console.log("Hola");
}

function despedir() {
    console.log("Adiós");
}

saludar();
despedir();
```

JavaScript hace exactamente esto:

```text
Ejecutar saludar()

↓

Terminar saludar()

↓

Ejecutar despedir()

↓

Terminar despedir()
```

Nunca hace:

```text
saludar()

despedir()

al mismo tiempo
```

---

## Entonces aparece un problema...

¿Qué ocurre con esto?

```javascript
console.log("Inicio");

setTimeout(() => {
    console.log("Hola");
}, 5000);

console.log("Fin");
```

Si JavaScript solo hace una cosa a la vez...

¿No debería quedarse esperando cinco segundos?

Muchos principiantes imaginan esto:

```text
Inicio

...

5 segundos

...

Fin

Hola
```

Pero el resultado real es

```text
Inicio

Fin

(5 segundos)

Hola
```

¿Por qué?

---

## Porque JavaScript no hace todo

Aquí está una de las ideas más importantes.

**JavaScript no controla el temporizador.**

El temporizador lo controla el navegador (o Node.js).

Imagina una oficina.

JavaScript es el empleado.

Pero también existe un asistente.

```text
Empleado (JavaScript)

+

Asistente (Navegador)
```

El empleado dice:

> "Necesito que dentro de cinco segundos hagas esto."

El asistente responde:

> "Déjamelo a mí."

Entonces el empleado sigue trabajando.

No se queda mirando el reloj.

---

## Visualicemos el ejemplo

Código

```javascript
console.log("Inicio");

setTimeout(() => {
    console.log("Hola");
}, 5000);

console.log("Fin");
```

---

### Paso 1

JavaScript ejecuta

```javascript
console.log("Inicio");
```

Salida

```text
Inicio
```

---

### Paso 2

Encuentra

```javascript
setTimeout(...)
```

JavaScript dice:

> "Navegador, guarda este temporizador."

El navegador responde:

> "Perfecto."

Entonces JavaScript continúa.

---

### Paso 3

Ejecuta

```javascript
console.log("Fin");
```

Salida

```text
Inicio

Fin
```

Mientras tanto...

El navegador está contando.

```text
5...

4...

3...

2...

1...
```

JavaScript ni siquiera está pendiente del tiempo.

---

## ¿Qué ocurre cuando terminan los cinco segundos?

El navegador dice:

> "Ya pasó el tiempo."

Pero aquí ocurre algo muy importante.

El navegador **no puede ejecutar JavaScript**.

Solo JavaScript puede ejecutar JavaScript.

Entonces hace otra cosa.

Dice:

> "Tengo una función lista para ejecutarse."

Y la deja esperando.

---

## ¿Dónde espera?

En una cola.

Imagina una fila de personas.

```text
🚶

🚶

🚶
```

Todos esperan su turno.

La función de `setTimeout` entra al final de esa cola.

---

## ¿Quién mira esa cola?

Aquí aparece el famoso **Event Loop**.

El Event Loop no ejecuta código.

Su único trabajo es preguntar constantemente:

```text
¿JavaScript terminó?

↓

No

↓

Espero.

--------------------

¿JavaScript terminó?

↓

Sí

↓

¿Hay funciones esperando?

↓

Sí

↓

Dáselas a JavaScript.
```

Hace esta comprobación miles de veces por segundo.

---

## Pongamos todo junto

```javascript
console.log("A");

setTimeout(() => {
    console.log("B");
}, 2000);

console.log("C");
```

Paso a paso.

---

## JavaScript ejecuta

```javascript
console.log("A");
```

Resultado

```text
A
```

---

## Encuentra

```javascript
setTimeout(...)
```

Se lo entrega al navegador.

El navegador empieza el contador.

JavaScript sigue trabajando.

---

## Ejecuta

```javascript
console.log("C");
```

Resultado

```text
A

C
```

---

## Dos segundos después

El navegador termina.

Dice

> "Ya está."

Coloca la función aquí.

```text
Cola

↓

console.log("B")
```

---

## El Event Loop pregunta

```text
¿JavaScript sigue ocupado?
```

Respuesta

```text
No.
```

Entonces mueve la función hacia JavaScript.

JavaScript ejecuta

```javascript
console.log("B");
```

Resultado

```text
A

C

B
```

---

## Entonces...

¿Qué hace realmente el Event Loop?

Muchísima gente cree que el Event Loop ejecuta el código.

No.

Su trabajo es mucho más simple.

Hace esto continuamente:

```text
¿El motor de JavaScript está libre?

↓

Sí

↓

¿Hay tareas esperando?

↓

Sí

↓

Entrégaselas.
```

Nada más.

Es como el recepcionista de una consulta médica.

No atiende pacientes.

Solo dice:

```text
"Siguiente."
```

---

## ¿Qué pasa si JavaScript está ocupado?

Supongamos

```javascript
console.log("Inicio");

setTimeout(() => {
    console.log("Hola");
}, 1000);

for (let i = 0; i < 10000000000; i++) {
}

console.log("Fin");
```

El bucle tarda unos segundos.

Durante ese tiempo

```text
JavaScript

↓

ocupado

↓

ocupado

↓

ocupado
```

Mientras tanto el navegador ya terminó el temporizador.

La función está esperando.

```text
Cola

↓

console.log("Hola")
```

Pero el Event Loop pregunta

```text
¿JavaScript está libre?

↓

No.
```

Entonces no puede hacer nada.

Debe esperar.

Cuando termina el `for`

```text
¿Está libre?

↓

Sí.
```

Ahora sí entrega la función.

Por eso el resultado será

```text
Inicio

(espera varios segundos)

Fin

Hola
```

Aunque el temporizador fuera de un segundo.

---

## Una analogía completa

Imagina un restaurante.

* **JavaScript** → el cocinero.
* **Navegador** → los camareros.
* **Event Loop** → el jefe de cocina.

Llega un pedido.

```text
🍔
```

El cocinero empieza.

Mientras cocina, un camarero dice:

> "Dentro de cinco minutos tengo que servir un postre."

El cocinero responde:

> "Perfecto."

Y sigue cocinando.

Cinco minutos después.

El camarero dice:

> "El postre está listo."

Pero el cocinero sigue ocupado.

Entonces el jefe de cocina espera.

Cuando el cocinero termina el plato actual, el jefe dice:

> "Ahora haz el postre."

Eso es exactamente el Event Loop.

---

## Resumen visual

```text
Tu código JavaScript

        │
        ▼
JavaScript ejecuta instrucciones
        │
        ▼
¿Necesita esperar? (temporizador, petición HTTP, evento...)
        │
      Sí
        │
        ▼
El navegador se encarga de esa tarea
        │
        ▼
Cuando termina, coloca la función en una cola
        │
        ▼
El Event Loop observa constantemente:
"¿JavaScript está libre?"
        │
        ├── No → sigue esperando
        └── Sí → entrega la siguiente función a JavaScript
```

## Qué debes recordar

Hay tres ideas clave:

1. **JavaScript es single-threaded**: solo ejecuta una instrucción de JavaScript a la vez, en un único hilo.

2. **El navegador o Node.js realizan las operaciones asíncronas** (como temporizadores, peticiones de red o eventos). JavaScript simplemente les pide que las gestionen.

3. **El Event Loop coordina el momento en que esas tareas vuelven a JavaScript**. No ejecuta el código por sí mismo; solo espera a que el motor de JavaScript quede libre y entonces le entrega la siguiente tarea pendiente. Si JavaScript está ocupado con una operación larga, las tareas deben esperar en la cola aunque ya hayan terminado externamente.


---


# Entendiendo mejor el callstack y el event loop
Muy buena pregunta. Aquí es donde suele producirse la mayor confusión. La respuesta corta es:

> **Nadie "llama" al Event Loop.** El Event Loop forma parte del entorno de ejecución (el navegador o Node.js) y está funcionando continuamente desde que comienza el programa.

Veámoslo paso a paso.

---

## ¿Quién ejecuta el código JavaScript?

Cuando abres una página web, ocurre algo parecido a esto:

```text
Navegador

↓

Carga el archivo .js

↓

Motor de JavaScript (V8, SpiderMonkey...)

↓

Empieza a ejecutar la primera línea
```

Por ejemplo:

```javascript
console.log("Hola");

console.log("Mundo");
```

El motor empieza por la primera línea y continúa hasta el final.

---

## ¿Quién crea el Call Stack?

El propio motor de JavaScript.

Imagina que el código es:

```javascript
function saludar() {
    console.log("Hola");
}

saludar();
```

Al comenzar:

```text
Call Stack

(vacío)
```

---

Cuando encuentra

```javascript
saludar();
```

la función entra en el Call Stack.

```text
┌────────────┐
│ saludar()  │
└────────────┘
```

Dentro de `saludar()` encuentra

```javascript
console.log("Hola");
```

Entonces entra otra llamada.

```text
┌────────────────────┐
│ console.log()      │
├────────────────────┤
│ saludar()          │
└────────────────────┘
```

Cuando termina `console.log()` sale.

```text
┌────────────┐
│ saludar()  │
└────────────┘
```

Después termina `saludar()`.

```text
(vacío)
```

Siempre funciona como una **pila (Stack)**.

**Último en entrar → primero en salir (LIFO).**

---

## Veamos un ejemplo más profundo

```javascript
function A() {
    B();
}

function B() {
    C();
}

function C() {
    console.log("Hola");
}

A();
```

El Call Stack evoluciona así.

---

Primero

```text
A()
```

```text
┌─────┐
│ A() │
└─────┘
```

---

A llama a B.

```text
┌─────┐
│ B() │
├─────┤
│ A() │
└─────┘
```

---

B llama a C.

```text
┌─────┐
│ C() │
├─────┤
│ B() │
├─────┤
│ A() │
└─────┘
```

---

C llama a `console.log()`.

```text
┌────────────────┐
│ console.log()  │
├────────────────┤
│ C()            │
├────────────────┤
│ B()            │
├────────────────┤
│ A()            │
└────────────────┘
```

---

Ahora empiezan a salir.

```text
console.log()

↓

C()

↓

B()

↓

A()
```

Hasta quedar vacío.

---

## ¿Y el Event Loop?

Mientras todo esto ocurre...

El Event Loop está haciendo esto:

```text
¿El Stack está vacío?

↓

No

↓

Espero
```

Y vuelve a preguntar.

```text
¿El Stack está vacío?

↓

No

↓

Espero
```

Miles de veces por segundo.

No interrumpe a JavaScript.

Nunca mete una función "a la fuerza".

---

## Ahora aparece un `setTimeout`

```javascript
console.log("A");

setTimeout(() => {
    console.log("B");
}, 1000);

console.log("C");
```

Veamos quién hace cada cosa.

---

### Primera línea

```javascript
console.log("A");
```

Entra al Stack.

```text
Stack

console.log()
```

Sale.

---

### Segunda línea

```javascript
setTimeout(...)
```

Entra al Stack.

```text
setTimeout()
```

Pero `setTimeout` no espera.

Hace algo parecido a esto:

```text
JavaScript

↓

Navegador

"Ejecuta esto dentro de 1 segundo"
```

Y sale inmediatamente del Stack.

---

### Tercera línea

```javascript
console.log("C");
```

Entra al Stack.

Sale.

---

Ahora el Stack está vacío.

---

## Mientras tanto...

El navegador lleva un segundo contando.

```text
1...

0...
```

Cuando termina hace esto:

```text
Callback Queue

↓

() => console.log("B")
```

Todavía **no entra al Stack**.

Solo espera.

---

## ¿Cuándo entra al Stack?

Aquí trabaja el Event Loop.

Pregunta

```text
¿Stack vacío?

↓

Sí
```

Entonces toma la primera función de la cola.

```text
Cola

↓

console.log("B")
```

Y la mueve al Stack.

```text
Stack

↓

console.log()
```

Después se ejecuta.

---

## ¿Qué pasa si hay muchas tareas esperando?

Supongamos

```javascript
setTimeout(() => console.log(1), 0);

setTimeout(() => console.log(2), 0);

setTimeout(() => console.log(3), 0);
```

La cola queda

```text
1

↓

2

↓

3
```

El Event Loop nunca hace

```text
3

↓

2

↓

1
```

Respeta el orden de llegada (FIFO, **First In, First Out**).

---

## Entonces, ¿qué orden sigue todo?

Supongamos este código:

```javascript
function uno() {
    console.log("Uno");
}

function dos() {
    console.log("Dos");
}

console.log("Inicio");

uno();

dos();

console.log("Fin");
```

La secuencia es:

```
1. console.log("Inicio")
```

Stack

```text
console.log()
```

Sale.

---

```
2. uno()
```

Stack

```text
uno()
```

Dentro

```text
console.log()
```

Stack

```text
console.log()

↓

uno()
```

Sale.

Después sale `uno()`.

---

```
3. dos()
```

Exactamente igual.

---

```
4. console.log("Fin")
```

Y termina.

---

## ¿Quién decide el orden?

El motor de JavaScript.

Simplemente lee el archivo **de arriba hacia abajo**.

Cada vez que encuentra una llamada a una función:

```javascript
miFuncion();
```

la coloca encima del Stack.

Si esa función llama a otra:

```javascript
function A() {
    B();
}
```

B entra encima de A.

Si B llama a C.

C entra encima de B.

Por eso el Stack siempre parece una torre.

```text
console.log()

↓

C()

↓

B()

↓

A()
```

Cuando termina la función de arriba...

La quita.

Y continúa con la siguiente.

---

## Resumen

Piensa en cuatro "actores":

```text
1. Motor de JavaScript
```

Lee el código línea por línea y coloca las llamadas a funciones en el **Call Stack**.

---

```text
2. Call Stack
```

Guarda las funciones que se están ejecutando.

Funciona como una pila (**LIFO**):

* Última función en entrar.
* Primera en salir.

---

```text
3. Navegador (o Node.js)
```

Se encarga de tareas como:

* `setTimeout()`
* `fetch()`
* eventos del ratón.
* eventos del teclado.

Cuando terminan, coloca sus callbacks en una cola.

---

```text
4. Event Loop
```

No ejecuta código ni crea funciones.

Solo observa continuamente:

```text
¿El Call Stack está vacío?

↓

Sí

↓

¿Hay tareas esperando?

↓

Sí

↓

Pasa la primera al Call Stack.
```

Una buena analogía es una recepción médica:

* El **motor de JavaScript** es el médico que atiende pacientes.
* El **Call Stack** es la consulta donde solo cabe un paciente a la vez.
* La **cola** es la sala de espera.
* El **Event Loop** es el recepcionista que mira si el médico quedó libre y, cuando lo está, llama al siguiente paciente. Nunca interrumpe una consulta en curso; simplemente espera a que termine la actual antes de hacer pasar al siguiente.



---


## Some basic concepts
The JavaScript engine (found in a hosting environment like the browser), is a single-threaded interpreter, it has a single call stack.
The browser provides web APIs like the DOM, AJAX and Timers.

The call stack is primarily used for function invocation (call). Since the call stack is single, function execution is done, one at a time, from top to bottom. It means the call stack is synchronous


## How does the call stack handle function calls?
```javascript
function firstFunction() {
	console.log("Hello from firstFunction");
}

function secondFunction() {
	firstFunction();
	console.log("The end from secondFunction");
}

// Output
// Hello from firstFunction
// The end from secondFunction
```


## The LIFO - Last In, First Out  principle
At the most basic level, a call stack is a data structure that uses the *Last In, First out* or *LIFO* principle to temporarily store and manage function invocation (call).
It means that the last function that gets pushed into the stack is the first to be pop out, when the function returns.

Same scenario as being on a queue in a grocery store cash point. You can only be attended to after the person in front of you have been ettended to. Which explains the synchronous concept on JavaScript


## What causes a stack overflow?
A stack overflow occurs when there is a recursive function (a function that calls itself) without an exit point.
The browser (hosting environment) has a maximum stack call that it can accomodate before throwing a stack error, for example:
```javascript
function callMyself() {
	callMyself();
}

callMyself();
```

The **callMyself()** will run until the browser throws a "Maximun call size exceeded", and that is a *stack overflow*


## In summary, key concepts from the call stack
1. It is single-threaded. meaning it can only do one thing at a time
2. Code execution is synchronous
3. A function invocation creates a stack frame that occupies a temporary memory
4. It works as a *LIFO* - Last In, First Out data structure
