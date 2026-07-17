# 1. Ventajas de Sets sobre arrays
## Set en JavaScript

Un **Set** es una estructura de datos introducida en ES6 que permite almacenar **valores únicos** de cualquier tipo, ya sean primitivos o referencias a objetos.

### Características principales

1. **Valores únicos**: No permite duplicados
2. **Mantiene el orden de inserción**: Los elementos se iteran en el orden en que fueron agregados
3. **Sin índices**: A diferencia de los arrays, no se accede por posición
4. **Iterable**: Se puede usar con `for...of` y otros métodos de iteración

### Creación de un Set

```javascript
// Set vacío
const miSet = new Set();

// Con valores iniciales
const numeros = new Set([1, 2, 3, 4, 5]);

// Elimina duplicados automáticamente
const conDuplicados = new Set([1, 1, 2, 2, 3]);
console.log(conDuplicados); // Set(3) {1, 2, 3}
```

### Métodos principales

```javascript
const set = new Set();

// Agregar elementos
set.add(1);
set.add("texto");
set.add({nombre: "Juan"});

// Verificar si existe un elemento
console.log(set.has(1)); // true
console.log(set.has("no existe")); // false

// Eliminar un elemento
set.delete("texto");

// Tamaño del Set
console.log(set.size); // 2

// Limpiar todo el Set
set.clear();
```

### Iteración sobre un Set

```javascript
const frutas = new Set(["manzana", "pera", "uva"]);

// for...of
for (const fruta of frutas) {
    console.log(fruta);
}

// forEach
frutas.forEach((valor, clave) => {
    console.log(`${clave}: ${valor}`);
    // Nota: en Set, el valor y la clave son iguales
});

// Convertir a array
const arrayFrutas = [...frutas];
const arrayFrutas2 = Array.from(frutas);
```

### Casos de uso comunes

#### 1. **Eliminar duplicados de un array**
```javascript
const numeros = [1, 2, 2, 3, 4, 4, 5];
const unicos = [...new Set(numeros)];
console.log(unicos); // [1, 2, 3, 4, 5]
```

#### 2. **Operaciones de conjuntos**

```javascript
const setA = new Set([1, 2, 3, 4]);
const setB = new Set([3, 4, 5, 6]);

// Unión
const union = new Set([...setA, ...setB]);
console.log([...union]); // [1, 2, 3, 4, 5, 6]

// Intersección
const interseccion = new Set([...setA].filter(x => setB.has(x)));
console.log([...interseccion]); // [3, 4]

// Diferencia (elementos en A que no están en B)
const diferencia = new Set([...setA].filter(x => !setB.has(x)));
console.log([...diferencia]); // [1, 2]
```

#### 3. **Almacenar objetos únicos**
```javascript
const usuarios = new Set();

usuarios.add({id: 1, nombre: "Ana"});
usuarios.add({id: 2, nombre: "Carlos"});
// Nota: objetos diferentes con mismas propiedades se consideran únicos
usuarios.add({id: 1, nombre: "Ana"}); // Se agregará, es un objeto diferente

console.log(usuarios.size); // 3
```

### Diferencia entre Set y Array

| Característica | Set | Array |
|---------------|-----|-------|
| Duplicados | No permitidos | Permitidos |
| Acceso por índice | No | Sí |
| Búsqueda | `has()` - O(1) | `includes()` - O(n) |
| Uso principal | Valores únicos | Listas ordenadas |

### WeakSet

Existe también **WeakSet**, una variante donde solo se pueden almacenar objetos y las referencias son débiles (no impiden la recolección de basura):

```javascript
const weakSet = new WeakSet();
const obj = {dato: "importante"};

weakSet.add(obj);
// Solo acepta objetos
// No es iterable
// No tiene .size
```

Los Sets son especialmente útiles cuando necesitas garantizar unicidad, realizar búsquedas rápidas o trabajar con conjuntos de datos sin duplicados.

---

# 2. Ventajas de un Set iterando elementos comunes en un array
`Set` es una estructura de datos introducida en **ES6 (ECMAScript 2015)** cuya principal característica es que **solo puede almacenar valores únicos**.

```javascript
const vocales = new Set(["a", "e", "i", "o", "u"]);
```

Visualmente podrías imaginarlo así:

```
Set
┌─────┐
│ "a" │
│ "e" │
│ "i" │
│ "o" │
│ "u" │
└─────┘
```

No tiene índices como un array.

---

# Array vs Set

Con un array:

```javascript
const vocales = ["a", "e", "i", "o", "u"];
```

Si preguntas:

```javascript
vocales.includes("i")
```

JavaScript hace algo parecido a esto internamente:

```javascript
if ("a" === "i")
if ("e" === "i")
if ("i" === "i") // Encontró el elemento
```

Va comparando uno por uno hasta encontrarlo.

Si no existe:

```javascript
vocales.includes("x")
```

Debe revisar todo el array:

```
a
e
i
o
u
```

Eso es una búsqueda **lineal**.

Complejidad:

```
O(n)
```

donde `n` es el número de elementos del array.

---

## ¿Qué hace un Set?

Un `Set` está implementado internamente mediante una **tabla hash (hash table)** en la mayoría de motores de JavaScript (como V8 en Chrome y Node.js).

Cuando haces:

```javascript
const vocales = new Set(["a", "e", "i", "o", "u"]);
```

Internamente ocurre algo parecido a esto (simplificado):

```
Hash("a") → posición 2

Hash("e") → posición 15

Hash("i") → posición 7

Hash("o") → posición 20

Hash("u") → posición 9
```

Cuando preguntas:

```javascript
vocales.has("i")
```

No busca elemento por elemento.

Hace:

```
Hash("i")
↓

posición 7

↓

¿Hay algo aquí?

Sí

↓

true
```

No necesita recorrer toda la colección.

---

# Comparación visual

## Array

```
["a", "e", "i", "o", "u"]

buscar "u"

↓

a ❌

e ❌

i ❌

o ❌

u ✔
```

Cinco comparaciones.

---

## Set

```
Set

Hash("u")

↓

posición 9

↓

✔ Encontrado
```

Una sola búsqueda.

---

# Complejidad

## Array

```javascript
includes()
indexOf()
find()
findIndex()
```

Son:

```
O(n)
```

porque pueden recorrer todos los elementos.

---

## Set

```javascript
has()
```

Es aproximadamente

```
O(1)
```

Tiempo constante.

Da igual si hay:

* 5 elementos
* 500 elementos
* 5 millones de elementos

El tiempo de búsqueda suele mantenerse prácticamente constante.

---

# Ejemplo

Supongamos un millón de elementos.

Array:

```javascript
const numeros = [1,2,3,...,1000000];

numeros.includes(1000000);
```

Debe revisar:

```
1

2

3

...

999999

1000000 ✔
```

---

Con un Set:

```javascript
const numeros = new Set([1,2,3,...,1000000]);

numeros.has(1000000);
```

Va directamente a la posición correspondiente mediante el hash.

---

# Operaciones principales

Crear:

```javascript
const colores = new Set();
```

Agregar:

```javascript
colores.add("rojo");
colores.add("azul");
```

Eliminar:

```javascript
colores.delete("rojo");
```

Buscar:

```javascript
colores.has("azul");
```

Cantidad:

```javascript
colores.size;
```

Vaciar:

```javascript
colores.clear();
```

---

# No admite duplicados

```javascript
const numeros = new Set();

numeros.add(5);
numeros.add(5);
numeros.add(5);

console.log(numeros);
```

Resultado:

```
Set(1) {5}
```

Solo existe un `5`.

Con un array:

```javascript
[5,5,5]
```

sí existirían los tres.

---

# ¿Por qué en tu ejercicio mejora el rendimiento?

Tu código original era:

```javascript
const vocales = ["a", "e", "i", "o", "u"];

for (const letra of str) {
    if (vocales.includes(letra)) {
        contador++;
    }
}
```

Cada llamada a `includes()` recorre el array de vocales.

Con un `Set`:

```javascript
const vocales = new Set(["a", "e", "i", "o", "u"]);

for (const letra of str) {
    if (vocales.has(letra)) {
        contador++;
    }
}
```

La búsqueda es directa.

### ¿Se nota la diferencia?

En este caso concreto, **no demasiado**, porque el conjunto de vocales siempre tiene solo 5 elementos. La ventaja práctica es pequeña.

Sin embargo, el uso de `Set` refleja una buena elección de estructura de datos. Si el conjunto creciera a cientos o miles de elementos (por ejemplo, una lista de palabras permitidas, códigos, identificadores o usuarios), `Set` ofrecería una mejora significativa en las búsquedas.

**Regla general:**

* Usa un **Array** cuando el orden y los índices importan o necesitas acceder por posición (`arr[0]`, `arr[1]`, etc.).
* Usa un **Set** cuando lo importante es saber rápidamente si un valor existe y garantizar que no haya duplicados.


---


## Comparar dos arrays idénticos en JavaScript
Comparar si dos arrays son idénticos en JavaScript no es tan sencillo como usar el operador `===` o `==`, ya que estos operadores comparan referencias de objetos, no su contenido. Para determinar si dos arrays son idénticos (es decir, tienen los mismos elementos en el mismo orden), debes comparar sus elementos uno por uno. A continuación, te explico varias formas de hacerlo:

---

### 1. **Comparación Manual con un Bucle**
Puedes recorrer ambos arrays y comparar cada elemento en la misma posición.

#### Ejemplo:
```javascript
function arraysSonIdenticos(arr1, arr2) {
    // Si las longitudes son diferentes, no son idénticos
    if (arr1.length !== arr2.length) {
        return false;
    }

    // Compara cada elemento
    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) {
            return false;
        }
    }

    return true;
}

const array1 = [1, 2, 3];
const array2 = [1, 2, 3];
const array3 = [1, 2, 4];

console.log(arraysSonIdenticos(array1, array2)); // true
console.log(arraysSonIdenticos(array1, array3)); // false
```

#### Ventajas:
- Fácil de entender y personalizar.
- Funciona para arrays de tipos primitivos (números, strings, booleanos).

#### Desventajas:
- No funciona correctamente para arrays que contienen objetos o arrays anidados (ya que compara referencias, no contenido).

---

### 2. **Usar `JSON.stringify`**
Puedes convertir ambos arrays a strings usando `JSON.stringify` y luego comparar los strings resultantes.

#### Ejemplo:
```javascript
function arraysSonIdenticos(arr1, arr2) {
    return JSON.stringify(arr1) === JSON.stringify(arr2);
}

const array1 = [1, 2, 3];
const array2 = [1, 2, 3];
const array3 = [1, 2, 4];

console.log(arraysSonIdenticos(array1, array2)); // true
console.log(arraysSonIdenticos(array1, array3)); // false
```

#### Ventajas:
- Simple y conciso.
- Funciona para arrays que contienen objetos o arrays anidados (siempre que los objetos tengan el mismo orden de propiedades).

#### Desventajas:
- No es eficiente para arrays muy grandes.
- Depende del orden de las propiedades en los objetos.
- No funciona correctamente si los arrays contienen valores especiales como `undefined`, `NaN`, o funciones.

---

### 3. **Usar `every` y `indexOf`**
Puedes usar el método `every` para verificar si cada elemento de un array coincide con el elemento correspondiente en el otro array.

#### Ejemplo:
```javascript
function arraysSonIdenticos(arr1, arr2) {
    return (
        arr1.length === arr2.length && // Compara longitudes
        arr1.every((elemento, indice) => elemento === arr2[indice]) // Compara elementos
    );
}

const array1 = [1, 2, 3];
const array2 = [1, 2, 3];
const array3 = [1, 2, 4];

console.log(arraysSonIdenticos(array1, array2)); // true
console.log(arraysSonIdenticos(array1, array3)); // false
```

#### Ventajas:
- Más moderno y funcional.
- Fácil de leer y entender.

#### Desventajas:
- No funciona correctamente para arrays que contienen objetos o arrays anidados.

---

### 4. **Comparación Profunda (Deep Comparison)**
Si los arrays contienen objetos o arrays anidados, necesitas una comparación profunda que verifique el contenido de los objetos y arrays recursivamente.

#### Ejemplo:
```javascript
function arraysSonIdenticos(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return false;
    }

    for (let i = 0; i < arr1.length; i++) {
        if (Array.isArray(arr1[i]) && Array.isArray(arr2[i])) {
            if (!arraysSonIdenticos(arr1[i], arr2[i])) {
                return false;
            }
        } else if (typeof arr1[i] === 'object' && typeof arr2[i] === 'object') {
            if (JSON.stringify(arr1[i]) !== JSON.stringify(arr2[i])) {
                return false;
            }
        } else if (arr1[i] !== arr2[i]) {
            return false;
        }
    }

    return true;
}

const array1 = [1, { a: 1 }, [2, 3]];
const array2 = [1, { a: 1 }, [2, 3]];
const array3 = [1, { a: 2 }, [2, 3]];

console.log(arraysSonIdenticos(array1, array2)); // true
console.log(arraysSonIdenticos(array1, array3)); // false
```

#### Ventajas:
- Funciona para arrays con objetos o arrays anidados.
- Compara el contenido de los objetos y arrays.

#### Desventajas:
- Más complejo de implementar.
- Puede ser menos eficiente para estructuras muy grandes o profundas.

---

### 5. **Usar Librerías Externas**
Si necesitas una solución robusta y no quieres implementar la comparación manualmente, puedes usar librerías como **Lodash**, que proporcionan funciones para comparaciones profundas.

#### Ejemplo con Lodash:
```javascript
const _ = require('lodash');

const array1 = [1, { a: 1 }, [2, 3]];
const array2 = [1, { a: 1 }, [2, 3]];
const array3 = [1, { a: 2 }, [2, 3]];

console.log(_.isEqual(array1, array2)); // true
console.log(_.isEqual(array1, array3)); // false
```

#### Ventajas:
- Muy robusto y probado.
- Funciona para cualquier tipo de estructura de datos.

#### Desventajas:
- Requiere instalar una librería externa.

---

### Resumen de Métodos

| Método                     | Ventajas                                                                 | Desventajas                                                          |
|----------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------|
| **Bucle manual**           | Simple, funciona para tipos primitivos                                   | No funciona para objetos o arrays anidados                           |
| **`JSON.stringify`**       | Simple, funciona para objetos y arrays anidados                          | No funciona con valores especiales como `undefined` o `NaN`          |
| **`every` e `indexOf`**    | Moderno y funcional                                                      | No funciona para objetos o arrays anidados                           |
| **Comparación profunda**   | Funciona para objetos y arrays anidados                                  | Complejo de implementar, menos eficiente                             |
| **Librerías externas**     | Robusto, funciona para cualquier estructura                              | Requiere instalar una librería                                       |

---

### Conclusión
- Si los arrays contienen solo tipos primitivos, un **bucle manual** o `every` es suficiente.
- Si los arrays contienen objetos o arrays anidados, usa **`JSON.stringify`** o una **comparación profunda**.
- Para una solución robusta y sin complicaciones, considera usar una librería como **Lodash**.