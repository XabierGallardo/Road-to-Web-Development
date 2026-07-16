Estas son 10 pruebas técnicas muy comunes para un programador **JavaScript Junior**. Evalúan fundamentos del lenguaje, lógica y manejo de arreglos y objetos.

---

## 1. Invertir una cadena

**Enunciado**

Crea una función que reciba un string y devuelva el texto invertido.

**Ejemplo**

```javascript
reverseString("Hola");
```

Resultado:

```javascript
"aloH"
```

---

## 2. Contar vocales

**Enunciado**

Crea una función que reciba una cadena y retorne cuántas vocales contiene.

**Ejemplo**

```javascript
countVowels("JavaScript");
```

Resultado:

```javascript
3
```

---

## 3. Encontrar el número mayor

**Enunciado**

Recibe un arreglo de números y devuelve el mayor.

**Ejemplo**

```javascript
findMax([5, 12, 8, 20, 3]);
```

Resultado:

```javascript
20
```

---

## 4. Eliminar duplicados

**Enunciado**

Recibe un arreglo y devuelve otro sin elementos repetidos.

**Ejemplo**

```javascript
removeDuplicates([1, 2, 2, 3, 4, 4, 5]);
```

Resultado

```javascript
[1, 2, 3, 4, 5]
```

---

## 5. Es palíndromo

**Enunciado**

Determina si una palabra se lee igual de izquierda a derecha que de derecha a izquierda.

**Ejemplo**

```javascript
isPalindrome("reconocer");
```

Resultado

```javascript
true
```

Otro ejemplo

```javascript
isPalindrome("javascript");
```

Resultado

```javascript
false
```

---

## 6. FizzBuzz

**Enunciado**

Imprime los números del 1 al 100.

Reglas:

* múltiplo de 3 → `"Fizz"`
* múltiplo de 5 → `"Buzz"`
* múltiplo de ambos → `"FizzBuzz"`
* si no, imprime el número.

Salida parcial:

```text
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

---

## 7. Frecuencia de palabras

**Enunciado**

Recibe un texto y devuelve un objeto indicando cuántas veces aparece cada palabra.

**Ejemplo**

Entrada

```text
"hola mundo hola javascript"
```

Resultado

```javascript
{
  hola: 2,
  mundo: 1,
  javascript: 1
}
```

---

## 8. Ordenar un arreglo sin `sort()`

**Enunciado**

Implementa un algoritmo para ordenar un arreglo de menor a mayor sin utilizar `Array.prototype.sort()`.

**Ejemplo**

```javascript
sortArray([4, 1, 8, 2]);
```

Resultado

```javascript
[1, 2, 4, 8]
```

Este ejercicio evalúa conocimientos de algoritmos como Bubble Sort o Selection Sort.

---

## 9. Agrupar objetos por una propiedad

**Enunciado**

Dado un arreglo de usuarios, agrúpalos por ciudad.

**Entrada**

```javascript
const users = [
  { name: "Ana", city: "Buenos Aires" },
  { name: "Juan", city: "Córdoba" },
  { name: "Pedro", city: "Buenos Aires" }
];
```

Resultado esperado

```javascript
{
  "Buenos Aires": [
    { name: "Ana", city: "Buenos Aires" },
    { name: "Pedro", city: "Buenos Aires" }
  ],
  "Córdoba": [
    { name: "Juan", city: "Córdoba" }
  ]
}
```

---

## 10. Encontrar el primer elemento no repetido

**Enunciado**

Recibe un arreglo y devuelve el primer elemento que aparece una sola vez.

**Ejemplo**

```javascript
firstUnique([3, 5, 3, 4, 5, 6, 4]);
```

Resultado

```javascript
6
```

---

# Bonus: Preguntas frecuentes en entrevistas Junior

Además de ejercicios de código, es muy común que te hagan preguntas conceptuales como:

* ¿Cuál es la diferencia entre `==` y `===`?
* ¿Qué diferencia hay entre `let`, `const` y `var`?
* ¿Qué son el scope y el hoisting?
* ¿Qué hace `map()`, `filter()` y `reduce()`?
* ¿Qué diferencia hay entre un objeto y un arreglo?
* ¿Qué es una función flecha y en qué se diferencia de una función tradicional?
* ¿Qué es una Promise y cuándo usar `async/await`?
* ¿Qué diferencia hay entre `null` y `undefined`?
* ¿Qué es el event loop?
* ¿Qué significa que JavaScript sea de un solo hilo (single-threaded)?

Estos ejercicios y preguntas cubren gran parte de lo que suele evaluarse en entrevistas para puestos Junior. Si puedes resolverlos con soltura y explicar tus decisiones, estarás bien preparado para la mayoría de las pruebas técnicas de ese nivel.

