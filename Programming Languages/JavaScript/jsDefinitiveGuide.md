# JavaScript / La Guía Definitiva
## Capítulo 3 / Tipos, Valores y variablesTypes, Values and Variables
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

