# Date & Math Objects

## Creando numeros random en JavaScript con `Math.random()`

### 1. Usando `Math.random()` y `Math.floor()`
Esta es la forma más común y ampliamente usada para generar un número aleatorio entre 1 y 10.

```javascript
function numeroAleatorio1a10() {
  return Math.floor(Math.random() * 10) + 1;
}
```

#### Explicación:
- **`Math.random()`** genera un número decimal aleatorio entre 0 (inclusive) y 1 (exclusivo).
- Multiplicamos el valor generado por 10 para escalarlo al rango entre 0 y 9.999....
- **`Math.floor()`** redondea hacia abajo, eliminando los decimales, por lo que obtenemos un número entero entre 0 y 9.
- Sumamos 1 para ajustar el rango a 1-10, en lugar de 0-9.

#### Ejemplo:
Si `Math.random()` genera `0.85`, multiplicamos por 10 para obtener `8.5`, que luego se redondea a `8`, y sumando 1, obtenemos `9`.

___


### 2. Usando `Math.random()` y `Math.ceil()`
Otra forma es usar `Math.ceil()` para redondear hacia arriba, generando números en el rango 1-10.

```javascript
function numeroAleatorio1a10() {
  return Math.ceil(Math.random() * 10);
}
```

#### Explicación:
- **`Math.random()`** genera un número decimal entre 0 y 1.
- Multiplicamos por 10, lo que da un número entre 0 y 9.999... .
- **`Math.ceil()`** redondea hacia arriba, por lo que cualquier número entre 0.0001 y 9.9999 se redondeará a un valor entre 1 y 10.

#### Ejemplo:
Si `Math.random()` genera `0.85`, entonces multiplicamos por 10 para obtener `8.5`, que se redondea a `9`.

___


### 3. Usando `Math.random()` y `Math.round()`
Otra opción es usar **`Math.round()`**, que redondea al número entero más cercano. Aunque esto es menos común, también puede funcionar.

```javascript
function numeroAleatorio1a10() {
  return Math.round(Math.random() * 9) + 1;
}
```

#### Explicación:
- **`Math.random()`** genera un número decimal entre 0 y 1.
- Multiplicamos por 9, lo que da un número entre 0 y 8.999.... Esto asegura que el redondeo nos dé valores entre 0 y 9.
- **`Math.round()`** redondea el número generado al entero más cercano (redondea hacia arriba o hacia abajo según el valor decimal).
- Sumamos 1 para que el rango sea entre 1 y 10.

#### Ejemplo:
Si `Math.random()` genera `0.85`, entonces multiplicamos por 9 para obtener `7.65`, que se redondea a `8`, y luego sumamos 1 para obtener `9`.

___


### 4. Usando `Math.random()` en una expresión más directa
Es posible utilizar expresiones más cortas y directas que hacen lo mismo sin mucha variación en cuanto al rendimiento:

```javascript
let numero = ~~(Math.random() * 10) + 1;
```

#### Explicación:
- `~~` es una técnica menos común, pero interesante, que efectúa un doble complemento de bits, similar a `Math.floor()` en cuanto a redondeo hacia abajo.
- Multiplicamos por 10 para generar valores entre 0 y 9.999....
- Sumamos 1 para ajustar el rango a 1-10.

___


### 5. Usando una función de utilidad más flexible
Para generar números aleatorios en cualquier rango, se puede usar una función de utilidad más generalizada que permita cambiar el rango fácilmente:

```javascript
function numeroAleatorio(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Para obtener un número entre 1 y 10
let numero = numeroAleatorio(1, 10);
```

#### Explicación:
- Multiplicamos el valor de `Math.random()` por `(max - min + 1)` para ajustar el rango dinámicamente.
- `Math.floor()` se usa para obtener números enteros.
- Sumamos `min` para comenzar el rango desde el valor mínimo deseado.
  
### Comparación de las aproximaciones

- **`Math.floor(Math.random() * 10) + 1`** es la forma más común y eficiente de generar un número aleatorio entre 1 y 10.
- **`Math.ceil(Math.random() * 10)`** también es eficaz, aunque no tan habitual.
- **`Math.round()`** puede ser menos predecible debido a su comportamiento de redondeo hacia arriba o hacia abajo.
- **Funciones de utilidad** ofrecen flexibilidad y son útiles cuando necesitas generar números en diferentes rangos.

___


## Estudiando en detalle el ejemplo 5: `numeroAleatorio()`
```js
// Funcion numeroAleatorio
function numeroAleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
console.log(numeroAleatorio(1, 10)); // Numero aleatorio entre 1 y 10


// Practicando ejemplo, siguiendo ejemplo de arriba max 10, minimo 1
let numbers = "";
for (let i = 0; i < 10; i++) {
  numbers += Math.floor(Math.random() * (10 - 1 + 1)) + 1 + " ";
}

console.log(numbers); // "10 9 3 9 5 3 2 5 8 6 "
```

### Explicación paso a paso:

1. **Parámetros `min` y `max`:**
   - Esta función toma dos parámetros: `min` y `max`. Estos parámetros representan el rango en el cual deseas que se genere el número aleatorio.
   - El valor mínimo será el más bajo que puede generar, y el máximo será el más alto posible dentro del rango (inclusivo).

2. **`Math.random()`**
   - `Math.random()` es un método de JavaScript que devuelve un número decimal aleatorio (un número en punto flotante) entre 0 (inclusive) y 1 (exclusivo), es decir, nunca devuelve exactamente 1, pero puede devolver valores muy cercanos.
   - Ejemplo de salida: `0.4234`, `0.9283`, `0.1542`.

3. **`Math.random() * (max - min + 1)`**
   - Se multiplica el valor aleatorio entre 0 y 1 (generado por `Math.random()`) por `(max - min + 1)`. 
   - Esto ajusta el valor aleatorio para que esté dentro del rango que va desde 0 hasta el tamaño total del rango de números que queremos.
   - `max - min + 1`: Esto se utiliza para asegurarse de que el valor generado pueda incluir tanto el valor mínimo como el valor máximo, ya que sin el `+1`, el valor máximo no sería incluido.

   **Ejemplo:**
   - Si `min` es 1 y `max` es 10, el rango de números enteros es de 1 a 10 (un total de 10 números).
   - Multiplicando el valor aleatorio por `(10 - 1 + 1)`, o sea, `10`, escalamos el valor aleatorio para que esté entre 0 y 9.999... Esto se aproxima a un número entero en ese rango.

4. **`Math.floor()`**
   - `Math.floor()` es un método que redondea hacia abajo cualquier número decimal, devolviendo siempre el número entero más cercano que sea menor o igual al valor dado.
   - Aplicamos `Math.floor` a la expresión anterior para eliminar los decimales, redondeando hacia abajo.
   - Esto asegura que el resultado sea un número entero dentro del rango de 0 a `(max - min)`.

   **Ejemplo:**
   - Si `Math.random() * (max - min + 1)` da `7.42`, `Math.floor(7.42)` será `7`.
   - Si da `3.99`, será redondeado a `3`.

5. **`+ min`:**
   - Finalmente, sumamos `min` al resultado para desplazar el valor al rango deseado. Sin esta suma, estaríamos obteniendo un número entre 0 y `(max - min)` en lugar de entre `min` y `max`.
   - Esto ajusta el valor obtenido tras el redondeo para que comience en `min` en lugar de en 0.

   **Ejemplo:**
   - Si `min` es 5 y `Math.floor(Math.random() * (max - min + 1))` genera `2`, sumando `min` (5), obtenemos `7`.

### Ejemplo completo:

Si llamamos a la función así:

```javascript
numeroAleatorio(5, 10);
```

1. `Math.random()` podría devolver, por ejemplo, `0.67`.
2. Multiplicamos por `(10 - 5 + 1)`, que es `6`. Entonces, `0.67 * 6 = 4.02`.
3. Aplicamos `Math.floor(4.02)`, que da `4`.
4. Sumamos `min` (5): `4 + 5 = 9`.

El resultado final de esta llamada sería `9`.

### Resumen:
- **`Math.random()`**: genera un número aleatorio entre 0 y 1.
- **Multiplicación por `(max - min + 1)`**: escala ese valor para que esté dentro del rango deseado.
- **`Math.floor()`**: redondea hacia abajo para obtener un número entero.
- **Suma de `min`**: ajusta el valor al rango correcto empezando desde `min` hasta `max`.

### Ejemplos adicionales:

```javascript
numeroAleatorio(1, 5); // Podría devolver 1, 2, 3, 4 o 5.
numeroAleatorio(10, 20); // Podría devolver un número entre 10 y 20, inclusive.
numeroAleatorio(-5, 5); // Podría devolver un número entre -5 y 5, inclusive.
```
