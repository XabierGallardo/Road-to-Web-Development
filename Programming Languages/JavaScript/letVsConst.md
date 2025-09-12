# Entendiendo `const`en arrays y objetos

## 1. Qué significa `const`

Cuando declarás algo con `const`, lo que se vuelve **constante** es **la referencia** al valor almacenado en memoria, no el valor en sí.

```js
const x = 10;
x = 20; // ❌ Error: no se puede reasignar
```

En este caso, `x` apuntaba a la dirección de memoria con el valor `10`. Si intentás que `x` apunte a otro valor (`20`), no está permitido.

---

## 2. Caso de objetos y arrays

Un objeto o array en JavaScript no es el valor en sí, sino una **referencia a una estructura en memoria**.

```js
const arr = [1, 2, 3];
```

Aquí lo que es **constante** es la **referencia a ese array en memoria**, no el contenido del array.
Por eso:

```js
arr.push(4); // ✅ permitido → mutación del array
arr[0] = 99; // ✅ permitido → cambio de un elemento
```

Pero:

```js
arr = [9, 8, 7]; // ❌ Error → intento de reasignar la referencia
```

Lo mismo aplica a objetos:

```js
const obj = { a: 1 };
obj.a = 2;   // ✅ permitido
obj.b = 3;   // ✅ permitido
obj = {};    // ❌ Error
```

---

## 3. Ejemplo gráfico

* `const arr = [1,2,3]`

  * `arr` (la **referencia**) 👉 🔗 \[ 1, 2, 3 ] en memoria
  * La referencia es **inmutable**, pero lo que está dentro de esa caja en memoria **sí puede cambiar**.

---

## 4. Cómo congelar valores de verdad

Si querés que el contenido de un objeto/array no pueda cambiar, además de usar `const`, tenés que usar métodos como:

```js
const obj = Object.freeze({ a: 1 });
obj.a = 2; // ❌ no cambia
```

O para arrays:

```js
const arr = Object.freeze([1, 2, 3]);
arr.push(4); // ❌ TypeError en modo estricto
```

---

✅ En resumen:

* `const` fija la **referencia**, no el contenido.
* Objetos y arrays son **mutables** aunque su referencia esté bloqueada.
* Si querés inmutabilidad real, necesitás `Object.freeze` o librerías de estructuras inmutables.


---

# 2. Que priorizar? `let` vs `const`

**Usar `const` por defecto y `let` solo cuando sea necesario** es la práctica recomendada en JavaScript moderno. No es solo cuestión de estilo, sino de **buenas prácticas y principios de programación**.

## 📌 Regla general:

### ✅ **Usa `const` por defecto** (80-90% de los casos)
### 🔁 **Usa `let` solo cuando necesites reasignar** (10-20% de los casos)
### ❌ **Evita `var`** (solo en código legacy)

## ¿Por qué preferir `const`?

### 1. **Mayor seguridad y predictibilidad**
```javascript
// Con const - No se puede reasignar (más seguro)
const PI = 3.1416;
// PI = 3.15; // ❌ Error: Assignment to constant variable

// Con let - Se puede reasignar (menos predecible)
let counter = 0;
counter = 1; // ✅ Funciona
```

### 2. **Código más claro y mantenible**
```javascript
// Mal - No queda claro si se reasignará
let user = getUser();
// ... 50 líneas después ...
user = updateUser(user); // ¿Es intencional?

// Bien - La intención es clara
const user = getUser();
// user no cambiará en todo el scope
```

### 3. **Mejor scope management**
```javascript
// const y let tienen block scope ({}), no function scope como var
{
    const message = "Hola";
    console.log(message); // ✅ "Hola"
}
console.log(message); // ❌ ReferenceError
```

## Casos donde SÍ usar `let`:

### 1. **Contadores y acumuladores**
```javascript
// ✅ Necesitas reasignar
let count = 0;
count += 1;

let total = 0;
for (let i = 0; i < array.length; i++) {
    total += array[i];
}
```

### 2. **Bucles donde reasignas la variable**
```javascript
// ✅ En bucles tradicionales
for (let i = 0; i < 10; i++) {
    console.log(i);
}

// ✅ Reasignación condicional
let result;
if (condition) {
    result = "valor A";
} else {
    result = "valor B";
}
```

### 3. **Reasignaciones necesarias**
```javascript
// ✅ Cuando necesitas modificar el valor
let isLoading = false;

function fetchData() {
    isLoading = true;
    // llamada API...
    isLoading = false;
}
```

## ⚠️ Importante: `const` no hace inmutables los objetos

```javascript
const user = { name: "Juan", age: 30 };

// ✅ Esto SÍ funciona (modificación de propiedades)
user.age = 31;
user.city = "Madrid";

// ❌ Esto NO funciona (reasignación)
// user = { name: "Pedro" }; // Error

// Para objetos inmutables, usar Object.freeze()
const config = Object.freeze({ apiUrl: "https://api.com" });
// config.apiUrl = "nueva-url"; // ❌ Error en modo estricto
```

## 🎯 Buenas prácticas:

### 1. **Declarar variables lo más cerca posible de su uso**
```javascript
// Bien
function calculateTotal(items) {
    const taxRate = 0.21;
    
    let total = 0;
    for (const item of items) {
        total += item.price;
    }
    
    return total * (1 + taxRate);
}
```

### 2. **Usar nombres descriptivos**
```javascript
// Mal
let x = 10;

// Bien
const MAX_USERS = 10;
let currentUserCount = 0;
```

### 3. **Preferir const incluso en bucles modernos**
```javascript
// ✅ Mejor - const en for...of
const numbers = [1, 2, 3];
for (const number of numbers) {
    console.log(number);
}

// ✅ También válido - let si necesitas modificar
for (let i = 0; i < numbers.length; i++) {
    numbers[i] *= 2;
}
```

## 📊 Resumen:

| Situación | Recomendación |
|-----------|---------------|
| Valores que no cambian | `const` |
| Contadores, acumuladores | `let` |
| Variables en bucles tradicionales | `let` |
| Variables en bucles for...of | `const` |
| Resultados condicionales | `let` |
| Configuraciones, constantes | `const` |

**No es solo estilo personal**: Usar `const` por defecto hace tu código más robusto, predecible y fácil de debuggear. Los linters modernos como ESLint incluso tienen reglas para forzar esta práctica (`prefer-const`).