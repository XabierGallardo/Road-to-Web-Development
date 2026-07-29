# Comparación de bucles en JavaScript

## Tabla comparativa rápida

| Bucle | Tipo | Iteración | Uso recomendado | Performance |
|-------|------|-----------|-----------------|-------------|
| **for clásico** | Estructurado | Indexada | Arrays, control preciso | ⭐⭐⭐⭐⭐ |
| **for...of** | Iterador | Valores | Arrays, iterables modernos | ⭐⭐⭐⭐ |
| **for...in** | Enumeración | Propiedades | Objetos (con cuidado) | ⭐⭐ |
| **forEach** | Funcional | Valores | Arrays, operaciones simples | ⭐⭐⭐ |
| **while** | Estructurado | Condicional | Bucles indeterminados | ⭐⭐⭐⭐ |
| **do...while** | Estructurado | Condicional | Al menos una ejecución | ⭐⭐⭐⭐ |
| **map/filter/reduce** | Funcional | Valores | Transformaciones funcionales | ⭐⭐⭐ |

---

## 1. FOR CLÁSICO

```javascript
const array = ['a', 'b', 'c', 'd', 'e'];

// Sintaxis básica
for (let i = 0; i < array.length; i++) {
  console.log(i, array[i]);
}

// Con control de salto
for (let i = 0; i < array.length; i += 2) {
  console.log(array[i]); // a, c, e
}

// Bucle inverso
for (let i = array.length - 1; i >= 0; i--) {
  console.log(array[i]); // e, d, c, b, a
}
```

**Ventajas:**
- ✅ Máximo control (índice, salto, dirección)
- ✅ Mejor rendimiento (más rápido)
- ✅ Funciona en todos los navegadores
- ✅ Permite `break` y `continue`

**Desventajas:**
- ❌ Sintaxis verbosa
- ❌ Propenso a errores (off-by-one)
- ❌ No es funcional

---

## 2. FOR...OF (ES6)

```javascript
const array = ['a', 'b', 'c'];
const string = 'hola';
const set = new Set([1, 2, 3]);
const map = new Map([['a', 1], ['b', 2]]);

// Arrays
for (const valor of array) {
  console.log(valor); // a, b, c
}

// Strings (itera caracteres)
for (const char of string) {
  console.log(char); // h, o, l, a
}

// Sets
for (const valor of set) {
  console.log(valor); // 1, 2, 3
}

// Maps (obtiene [clave, valor])
for (const [clave, valor] of map) {
  console.log(clave, valor); // a 1, b 2
}

// Con índice usando entries()
for (const [index, valor] of array.entries()) {
  console.log(index, valor);
}

// Break y continue funcionan
for (const valor of array) {
  if (valor === 'b') continue;
  if (valor === 'c') break;
  console.log(valor); // a
}
```

**Ventajas:**
- ✅ Simple y legible
- ✅ Funciona con cualquier **iterable**
- ✅ Obtiene valores directamente
- ✅ Permite `break` y `continue`

**Desventajas:**
- ❌ No da acceso directo al índice (usar `.entries()`)
- ❌ No funciona con objetos planos (no son iterables)

---

## 3. FOR...IN

```javascript
const objeto = { 
  nombre: 'Ana', 
  edad: 25, 
  ciudad: 'Madrid' 
};

// Objetos
for (const clave in objeto) {
  console.log(clave, objeto[clave]); 
  // nombre Ana, edad 25, ciudad Madrid
}

// ⚠️ CUIDADO: También itera propiedades del prototipo
Array.prototype.customMethod = function() {};

const arr = [1, 2, 3];
for (const key in arr) {
  console.log(key, arr[key]); 
  // 0 1, 1 2, 2 3, customMethod ƒ...
}

// Solución: usar hasOwnProperty
for (const key in arr) {
  if (arr.hasOwnProperty(key)) {
    console.log(key, arr[key]);
  }
}

// ⚠️ Para arrays, el orden NO está garantizado
```

**Ventajas:**
- ✅ Itera sobre propiedades de objetos
- ✅ Obtiene claves fácilmente

**Desventajas:**
- ❌ Itera propiedades del prototipo
- ❌ Orden no garantizado
- ❌ Lento para arrays
- ❌ Incluye propiedades no numéricas en arrays
- ❌ No recomendado para arrays

---

## 4. FOR EACH

```javascript
const array = ['a', 'b', 'c'];

// Sintaxis básica
array.forEach((valor, indice, arrayCompleto) => {
  console.log(valor, indice);
});

// Con thisArg (contexto)
function Procesador() {
  this.prefijo = 'Item: ';
  array.forEach(function(valor) {
    console.log(this.prefijo + valor);
  }, this); // <-- thisArg
}

// Con arrow function (hereda this)
const procesador = {
  prefijo: 'Item: ',
  procesar() {
    array.forEach(valor => {
      console.log(this.prefijo + valor);
    });
  }
};

// ⚠️ NO permite break o continue (solo con excepciones)
try {
  array.forEach(valor => {
    if (valor === 'b') throw new Error('break');
    console.log(valor);
  });
} catch (e) {
  // Simula break
}
```

**Ventajas:**
- ✅ Sintaxis funcional y legible
- ✅ Acceso a índice y array original
- ✅ Bueno para operaciones simples

**Desventajas:**
- ❌ No soporta `break` o `continue` nativamente
- ❌ Performance ligeramente menor
- ❌ No funciona con await (problemas con async)

---

## 5. WHILE

```javascript
// Bucle básico
let i = 0;
while (i < 5) {
  console.log(i);
  i++;
}

// Bucle con condición compleja
let encontrado = false;
let contador = 0;
while (!encontrado && contador < 100) {
  if (contador === 42) encontrado = true;
  contador++;
}

// Bucle infinito (cuidado!)
// while (true) { /* ... */ }

// Procesar elementos hasta agotar
const pila = [1, 2, 3, 4];
while (pila.length > 0) {
  console.log(pila.pop()); // 4, 3, 2, 1
}
```

**Ventajas:**
- ✅ Flexible
- ✅ Útil para condiciones complejas
- ✅ Buen rendimiento

**Desventajas:**
- ❌ Riesgo de bucles infinitos
- ❌ Puede ser menos legible

---

## 6. DO...WHILE

```javascript
// Se ejecuta AL MENOS una vez
let i = 5;
do {
  console.log(i); // Se ejecuta aunque i >= 5
  i++;
} while (i < 5);

// Ejemplo práctico: menú
let opcion;
do {
  opcion = prompt('Elige 1, 2 o 3 (0 para salir)');
  console.log('Elegiste:', opcion);
} while (opcion !== '0');
```

**Ventajas:**
- ✅ Garantiza una ejecución
- ✅ Útil para menús y validaciones

**Desventajas:**
- ❌ Menos común
- ❌ Puede ser confuso

---

## 7. MÉTODOS FUNCIONALES

```javascript
const numeros = [1, 2, 3, 4, 5];

// map - transforma
const duplicados = numeros.map(n => n * 2);
// [2, 4, 6, 8, 10]

// filter - filtra
const pares = numeros.filter(n => n % 2 === 0);
// [2, 4]

// reduce - acumula
const suma = numeros.reduce((acc, n) => acc + n, 0);
// 15

// some - ¿algún elemento cumple?
const hayPares = numeros.some(n => n % 2 === 0);
// true

// every - ¿todos cumplen?
const todosPares = numeros.every(n => n % 2 === 0);
// false

// find - encuentra primero
const primerPar = numeros.find(n => n % 2 === 0);
// 2

// findIndex - índice del primero
const indicePar = numeros.findIndex(n => n % 2 === 0);
// 1
```

---

## 8. COMPARATIVA DE PERFORMANCE

```javascript
// Prueba de velocidad (100,000 elementos)
const arr = Array.from({ length: 100000 }, (_, i) => i);

console.time('for clásico');
for (let i = 0; i < arr.length; i++) {
  arr[i] * 2;
}
console.timeEnd('for clásico'); // ~2-3ms

console.time('for...of');
for (const val of arr) {
  val * 2;
}
console.timeEnd('for...of'); // ~3-5ms

console.time('forEach');
arr.forEach(val => val * 2);
console.timeEnd('forEach'); // ~5-8ms

console.time('for...in');
for (const key in arr) {
  if (arr.hasOwnProperty(key)) {
    arr[key] * 2;
  }
}
console.timeEnd('for...in'); // ~15-20ms (el más lento)
```

---

## 9. CASOS DE USO RECOMENDADOS

### ✅ Cuándo usar cada uno:

| Bucle | Mejor para |
|-------|-----------|
| **for clásico** | Rendimiento crítico, loops grandes, control preciso |
| **for...of** | La mayoría de casos modernos, iterables, legibilidad |
| **for...in** | **SOLO** para objetos (con hasOwnProperty) |
| **forEach** | Operaciones simples sin break, código funcional |
| **while** | Condiciones complejas, cuando no se sabe cuántas iteraciones |
| **map/filter/reduce** | Transformaciones de datos, programación funcional |

### ❌ Qué evitar:

```javascript
// ❌ NO usar for...in en arrays
const arr = [1, 2, 3];
for (const key in arr) { /* MAL */ }

// ❌ NO usar forEach para async/await
await arr.forEach(async (item) => { /* NO funciona bien */ });

// ✅ Usar for...of para async
for (const item of arr) {
  await procesar(item);
}

// ❌ NO modificar el array mientras se itera con forEach
arr.forEach((item, index) => {
  arr.splice(index, 1); // MAL
});

// ✅ Usar for clásico o while para modificaciones
for (let i = arr.length - 1; i >= 0; i--) {
  arr.splice(i, 1); // BIEN
}
```

---

## 10. EJEMPLOS PRÁCTICOS COMPARADOS

```javascript
const usuarios = [
  { id: 1, nombre: 'Ana', activo: true },
  { id: 2, nombre: 'Juan', activo: false },
  { id: 3, nombre: 'María', activo: true }
];

// 1. Filtrar y transformar (mejor con métodos funcionales)
const nombresActivos = usuarios
  .filter(u => u.activo)
  .map(u => u.nombre);
// ['Ana', 'María']

// 2. Buscar y modificar (for...of con break)
let encontrado = null;
for (const usuario of usuarios) {
  if (usuario.id === 2) {
    usuario.activo = true;
    encontrado = usuario;
    break;
  }
}

// 3. Acumular valores (reduce)
const total = usuarios.reduce((sum, u) => sum + (u.activo ? 1 : 0), 0);

// 4. Bucle con condición compleja (while)
let intentos = 0;
let exito = false;
while (intentos < 3 && !exito) {
  exito = intentarConexion();
  intentos++;
}
```

---

## Resumen final

- **Rendimiento**: `for clásico` > `for...of` > `forEach` > `for...in`
- **Legibilidad**: `for...of` > `forEach` > `for clásico`
- **Flexibilidad**: `while` > `for clásico` > `for...of`
- **Funcional**: `map/filter/reduce` para transformaciones

**Recomendación moderna**: Usa `for...of` por defecto, `forEach` para operaciones simples, y métodos funcionales para transformaciones de datos. Reserva `for...in` solo para objetos y `for clásico` cuando necesites máximo rendimiento o control fino.