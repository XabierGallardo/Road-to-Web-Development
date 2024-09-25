## Convertir a number en JavaScript
En JavaScript, hay varias formas de convertir un valor a un número. Algunas de estas formas son explícitas (cuando usas una función o un método específico para realizar la conversión) y otras son implícitas (cuando JavaScript convierte automáticamente un valor a un número en determinadas situaciones). Aquí te explico las principales maneras de convertir valores a números:

### 1. **Uso de la función `Number()`**

La función global `Number()` convierte el valor pasado como argumento a un número. Este es el método más directo para convertir un valor a un número, y puede manejar varios tipos de entrada, incluidos strings, booleanos y `null`.

#### Ejemplo:
```javascript
Number('42');      // 42
Number('3.14');    // 3.14
Number('');        // 0 (una cadena vacía se convierte en 0)
Number('abc');     // NaN (cadena no numérica)
Number(true);      // 1
Number(false);     // 0
Number(null);      // 0
Number(undefined); // NaN
```

### 2. **Uso de `parseInt()`**

`parseInt()` convierte una cadena a un número entero. Solo considera la parte inicial de la cadena hasta que encuentra un carácter no numérico. Puedes especificar una base (radix) para convertir números en otros sistemas, como binario o hexadecimal.

#### Ejemplo:
```javascript
parseInt('42');       // 42
parseInt('3.14');     // 3 (solo la parte entera)
parseInt('100', 2);   // 4 (en binario)
parseInt('abc');      // NaN
```

### 3. **Uso de `parseFloat()`**

`parseFloat()` es similar a `parseInt()`, pero permite convertir cadenas que representan números decimales.

#### Ejemplo:
```javascript
parseFloat('3.14');   // 3.14
parseFloat('42.98abc'); // 42.98 (ignora el texto después del número)
parseFloat('abc');    // NaN
```

### 4. **Operador Unario `+`**

El operador unario `+` convierte el valor a un número de manera rápida y sencilla. Si el valor no se puede convertir a un número, devuelve `NaN`.

#### Ejemplo:
```javascript
+'42';      // 42
+'3.14';    // 3.14
+true;      // 1
+false;     // 0
+null;      // 0
+undefined; // NaN
+'';        // 0 (cadena vacía se convierte en 0)
```

### 5. **Multiplicación por `1`**

Multiplicar un valor por 1 es una forma implícita de forzar la conversión a número. Esto también devuelve `NaN` si el valor no es convertible.

#### Ejemplo:
```javascript
'42' * 1;      // 42
'3.14' * 1;    // 3.14
true * 1;      // 1
false * 1;     // 0
null * 1;      // 0
undefined * 1; // NaN
```

### 6. **Uso de `Math.floor()`, `Math.ceil()`, `Math.round()`**

Aunque no están diseñadas específicamente para conversión, estas funciones pueden convertir otros tipos de datos (como cadenas o booleanos) a números enteros antes de aplicar sus operaciones de redondeo.

#### Ejemplo:
```javascript
Math.floor('3.9');    // 3
Math.ceil('3.1');     // 4
Math.round('3.5');    // 4
Math.floor(true);     // 1
Math.ceil(false);     // 0
```

### 7. **`parseInt()` con `toString()` para convertir bases**

Si necesitas convertir un número en una cadena a un número de una base específica, `parseInt()` combinado con `toString()` te permite convertir entre bases numéricas.

#### Ejemplo:
```javascript
parseInt('ff', 16);  // 255 (base hexadecimal)
parseInt('100', 2);  // 4 (base binaria)
```

### 8. **Conversión Implícita en Operaciones Aritméticas**

JavaScript a menudo convierte valores automáticamente a números cuando se usan en operaciones aritméticas como suma, resta, multiplicación o división. Esta conversión es implícita y depende del contexto de la operación.

#### Ejemplo:
```javascript
'42' - 0;        // 42 (se convierte a número para la resta)
'3.14' * 2;      // 6.28 (se convierte a número para la multiplicación)
true + false;    // 1 (true es 1 y false es 0)
null + 10;       // 10 (null se convierte a 0)
```

### 9. **Uso del Objeto `Date` (con `getTime()` o `valueOf()`)**

Los objetos `Date` pueden ser convertidos a números usando `getTime()` o `valueOf()`. Esto es útil si necesitas trabajar con marcas de tiempo (timestamps).

#### Ejemplo:
```javascript
let date = new Date();
date.getTime();    // devuelve el número de milisegundos desde el 1 de enero de 1970
+date;             // lo mismo que getTime(), ya que `+` llama implícitamente a valueOf()
```

### 10. **Convertir Arrays a Números**

Cuando intentas convertir un array a un número, JavaScript primero intenta convertir el array a una cadena. Si el array está vacío o contiene solo un elemento numérico, este será convertido a un número. Si contiene múltiples elementos, la conversión resulta en `NaN`.

#### Ejemplo:
```javascript
Number([42]);    // 42
Number(['42']);  // 42
Number([1, 2]);  // NaN
```

### 11. **`Boolean` a Número**

Los valores booleanos `true` y `false` pueden ser convertidos a números fácilmente:
- `true` se convierte en `1`.
- `false` se convierte en `0`.

#### Ejemplo:
```javascript
Number(true);   // 1
Number(false);  // 0
```

### Tabla Resumen de Resultados

| Entrada          | `Number()`  | `parseInt()`  | `parseFloat()` | `+`     | Multiplicación por `1` |
|------------------|-------------|---------------|----------------|---------|------------------------|
| `'42'`           | 42          | 42            | 42.0           | 42      | 42                     |
| `'3.14'`         | 3.14        | 3             | 3.14           | 3.14    | 3.14                   |
| `'10px'`         | NaN         | 10            | NaN            | NaN     | NaN                    |
| `'abc'`          | NaN         | NaN           | NaN            | NaN     | NaN                    |
| `true`           | 1           | NaN           | NaN            | 1       | 1                      |
| `false`          | 0           | NaN           | NaN            | 0       | 0                      |
| `null`           | 0           | NaN           | NaN            | 0       | 0                      |
| `undefined`      | NaN         | NaN           | NaN            | NaN     | NaN                    |
| `''` (cadena vacía) | 0        | NaN           | NaN            | 0       | 0                      |
| `[42]` (array)   | 42          | NaN           | NaN            | 42      | 42                     |
| `[1, 2]`         | NaN         | NaN           | NaN            | NaN     | NaN                    |

### Conclusión

JavaScript ofrece múltiples formas de convertir un valor a un número, cada una con sus características y usos adecuados. En general, si necesitas convertir un valor a número de manera segura, **`Number()`** es el enfoque más común y directo. Sin embargo, en casos específicos, como cuando trabajas con cadenas que contienen números decimales o cuando necesitas convertir números en diferentes bases, **`parseInt()`**, **`parseFloat()`**, o incluso operaciones aritméticas implícitas como multiplicar por `1` pueden ser útiles.


___



## `parseInt()`

`parseInt()` es una función global en JavaScript que convierte una cadena de texto en un número entero. Es especialmente útil cuando necesitas transformar una cadena que contiene dígitos numéricos en un valor numérico para realizar cálculos u operaciones aritméticas.

### Sintaxis

```javascript
parseInt(string, radix)
```

- **`string`**: La cadena que deseas convertir a un número entero.
- **`radix`** (opcional): La base numérica (o sistema numeral) que indica cómo interpretar los caracteres de la cadena. El valor del `radix` puede estar entre 2 y 36.

### Funcionamiento

La función `parseInt()` lee la cadena `string` carácter por carácter y convierte la secuencia inicial de caracteres que representan un número en un entero. Si encuentra un carácter que no es un dígito válido en el sistema numeral especificado por el `radix`, deja de analizar la cadena en ese punto.

Si no se puede analizar ningún número válido en la cadena, devuelve `NaN` (Not-a-Number).

### Ejemplos Básicos

```javascript
parseInt('42');     // 42
parseInt('3.14');   // 3  (solo considera la parte entera)
parseInt('100', 10); // 100 (base 10)
parseInt('100', 2);  // 4   (base 2 - binario)
parseInt('10a');     // 10  (deja de convertir en 'a')
parseInt('abc');     // NaN (no hay número al principio)
```

### Detalles Importantes

1. **Parte Entera**: `parseInt()` solo extrae la parte entera de una cadena. Si la cadena contiene decimales, los ignorará.
   ```javascript
   parseInt('3.14'); // 3
   ```

2. **Radix (Base numérica)**: El `radix` define en qué sistema numérico se interpretará la cadena. Si no se especifica el `radix`, JavaScript intentará inferirlo de la cadena:
   - Si la cadena empieza con `'0x'`, `parseInt` asume que es hexadecimal (base 16).
   - Si no se proporciona el `radix`, y la cadena no empieza con `'0x'`, se asumirá que es decimal (base 10).
   
   Es recomendable **siempre especificar el `radix`** para evitar comportamientos inesperados:
   ```javascript
   parseInt('10', 10); // 10 (decimal)
   parseInt('10', 2);  // 2  (binario)
   parseInt('10', 16); // 16 (hexadecimal)
   ```

3. **`NaN` (Not-a-Number)**: Si la cadena no comienza con caracteres válidos en el sistema numeral especificado, `parseInt()` devolverá `NaN`.
   ```javascript
   parseInt('abc'); // NaN
   ```

4. **Espacios en blanco**: Los espacios en blanco al principio de la cadena se ignoran, pero si hay caracteres no numéricos al principio, el resultado será `NaN`.
   ```javascript
   parseInt('   42'); // 42
   parseInt('   abc'); // NaN
   ```

5. **Valores especiales**: Si se le pasa un valor que no es una cadena, como `null`, `undefined`, o un objeto, `parseInt()` intentará convertirlo a una cadena primero.
   ```javascript
   parseInt(null);       // NaN
   parseInt(undefined);  // NaN
   parseInt(true);       // NaN
   ```

### Ejemplos con `radix`

El `radix` determina la base numérica que se utiliza para interpretar la cadena de texto. Aquí hay algunos ejemplos que demuestran cómo el uso del `radix` afecta el resultado:

- **Base 2 (binaria)**: Cada dígito puede ser 0 o 1.
   ```javascript
   parseInt('101', 2); // 5
   ```

- **Base 8 (octal)**: Los dígitos válidos son del 0 al 7.
   ```javascript
   parseInt('77', 8); // 63
   ```

- **Base 16 (hexadecimal)**: Los dígitos válidos son del 0 al 9 y de la 'a' a la 'f' (minúsculas o mayúsculas).
   ```javascript
   parseInt('ff', 16); // 255
   ```

- **Base 36**: Utiliza los números del 0 al 9 y las letras de la 'a' a la 'z'. El número más grande posible en base 36 es `z`, que representa el número decimal 35.
   ```javascript
   parseInt('z', 36); // 35
   parseInt('10', 36); // 36
   ```

### Ejemplos Avanzados

1. **Combinando con otras funciones**: `parseInt()` puede ser usado junto con otras funciones como `map()` para convertir una lista de cadenas en números enteros.
   ```javascript
   let numbers = ['10', '20', '30'].map(num => parseInt(num, 10));
   console.log(numbers); // [10, 20, 30]
   ```

2. **Trabajando con valores hexadecimales**:
   ```javascript
   let hexColor = '#ff5733';
   let red = parseInt(hexColor.substring(1, 3), 16);
   let green = parseInt(hexColor.substring(3, 5), 16);
   let blue = parseInt(hexColor.substring(5, 7), 16);
   console.log(red, green, blue); // 255, 87, 51
   ```

### Errores Comunes

1. **No especificar el `radix`**: A menudo, los desarrolladores olvidan especificar el `radix`, lo que puede llevar a resultados inesperados, especialmente cuando se trabaja con cadenas que comienzan con `'0x'` (hexadecimal).

   ```javascript
   parseInt('010'); // 10 (se trata como decimal, pero en algunos entornos podría ser octal)
   ```

   Para evitar estos problemas, siempre es recomendable definir el `radix`.

2. **Asumir que `parseInt()` maneja decimales**: Recuerda que `parseInt()` **no** maneja decimales, solo trabaja con la parte entera de una cadena.
   ```javascript
   parseInt('3.99'); // 3
   ```

### Alternativas

- **`Number()`**: Si necesitas convertir una cadena en un número, incluidas las fracciones decimales, es preferible usar `Number()` o `parseFloat()`.

   ```javascript
   Number('3.14'); // 3.14
   parseFloat('3.14'); // 3.14
   ```

- **`parseFloat()`**: Convierte una cadena a un número flotante.
   ```javascript
   parseFloat('3.14'); // 3.14
   ```

### Conclusión

`parseInt()` es una herramienta muy útil para convertir cadenas a enteros, especialmente cuando se trabaja con diferentes sistemas numéricos (binario, octal, hexadecimal). Sin embargo, debe ser utilizado con cuidado, especialmente respecto al manejo del `radix` y su limitación para trabajar solo con la parte entera de las cadenas.