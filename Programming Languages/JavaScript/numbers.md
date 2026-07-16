# Entendiendo `Number` en JavaScript y sus formatos

En JavaScript, el tipo **`Number`** representa prácticamente **todos los números**, tanto enteros como decimales. A diferencia de otros lenguajes (como Java, C# o C++), JavaScript **no tiene tipos separados como `int`, `float` o `double`** para los números normales.

---

# 1. El tipo `Number`

Todos estos valores son del mismo tipo:

```javascript
let edad = 25;
let precio = 19.99;
let negativo = -100;
let cero = 0;

console.log(typeof edad);      // "number"
console.log(typeof precio);    // "number"
console.log(typeof negativo);  // "number"
```

Aunque uno sea entero y otro decimal, ambos son:

```
number
```

Internamente JavaScript usa el estándar **IEEE 754 Double Precision (64 bits)**.

Eso significa que un `Number` puede almacenar:

* enteros
* decimales
* números muy grandes
* números muy pequeños

---

# 2. ¿Existen Integer y Float?

Sí existen **como concepto**, pero **no como tipos diferentes**.

Por ejemplo:

```javascript
10
```

es un entero (integer).

Mientras que:

```javascript
10.5
```

es un decimal (floating point).

Pero ambos siguen siendo:

```javascript
typeof 10      // number

typeof 10.5    // number
```

No existe:

```javascript
int
float
double
```

como tipos separados.

---

# 3. Integer (Enteros)

Son números sin parte decimal.

```javascript
1
25
100
-30
5000000
```

Ejemplo:

```javascript
let personas = 150;

console.log(Number.isInteger(personas));
```

Resultado:

```
true
```

Otro ejemplo:

```javascript
Number.isInteger(10.5)
```

Resultado:

```
false
```

---

# 4. Float (Decimales)

Son números con parte decimal.

```javascript
3.14
10.8
100.99
```

Ejemplo:

```javascript
let pi = 3.14159;

console.log(Number.isInteger(pi));
```

Resultado

```
false
```

---

# 5. ¿Por qué se llaman Floating Point?

Porque el punto decimal "flota".

Por ejemplo

```
12345

1.2345 × 10⁴
```

o

```
0.000123

1.23 × 10⁻⁴
```

La posición del decimal puede cambiar.

De ahí el nombre:

```
Floating Point
```

---

# 6. Precisión de los decimales

Aquí aparece uno de los problemas famosos de JavaScript.

```javascript
0.1 + 0.2
```

Esperaríamos

```
0.3
```

Pero devuelve

```
0.30000000000000004
```

¿Por qué?

Porque los números decimales se almacenan en binario y algunos no pueden representarse exactamente.

---

# 7. Números muy grandes

Existe un límite para representar enteros con precisión.

```javascript
Number.MAX_SAFE_INTEGER
```

Resultado

```
9007199254740991
```

Después de ese número puede haber errores.

```javascript
9007199254740992 === 9007199254740993
```

Da

```
true
```

Por eso existe **`BigInt`**.

```javascript
let numero = 9007199254740993n;
```

Ahora sí conserva toda la precisión.

---

# 8. Valores especiales de Number

## Infinity

```javascript
1 / 0
```

Resultado

```
Infinity
```

---

## -Infinity

```javascript
-1 / 0
```

Resultado

```
-Infinity
```

---

## NaN

Significa

```
Not a Number
```

Ejemplo

```javascript
Number("Hola")
```

Resultado

```
NaN
```

Otro

```javascript
0 / 0
```

Resultado

```
NaN
```

---

# 9. Conversión a Number

```javascript
Number("25")
```

Resultado

```
25
```

```javascript
Number("25.6")
```

Resultado

```
25.6
```

Pero

```javascript
Number("abc")
```

Da

```
NaN
```

---

# 10. Formato de números

Aquí es donde mucha gente se confunde.

Una cosa es **el valor**.

Otra distinta es **cómo se muestra**.

El número

```javascript
1234567.89
```

Siempre vale exactamente eso.

Lo que cambia es la presentación.

---

# 11. `toLocaleString()`

JavaScript puede mostrar el mismo número según la configuración regional (locale).

Ejemplo:

```javascript
let numero = 1234567.89;

console.log(numero.toLocaleString("en-US"));
```

Resultado

```
1,234,567.89
```

En Estados Unidos:

* coma → separador de miles
* punto → decimal

---

Ahora Argentina:

```javascript
console.log(numero.toLocaleString("es-AR"));
```

Resultado

```
1.234.567,89
```

Aquí:

* punto → separador de miles
* coma → decimal

El valor **no cambió**.

Solo cambió su representación.

---

# 12. ¿Por qué ocurre esto?

Porque cada país tiene convenciones distintas para escribir números.

Por ejemplo:

| País           | Miles      | Decimal            |
| -------------- | ---------- | ------------------ |
| Estados Unidos | `1,234.56` | punto decimal      |
| Argentina      | `1.234,56` | coma decimal       |
| España         | `1.234,56` | coma decimal       |
| Alemania       | `1.234,56` | coma decimal       |
| Francia        | `1 234,56` | espacio para miles |

El método `toLocaleString()` aplica automáticamente estas convenciones según el locale indicado.

---

# 13. Formato de moneda

Ejemplo:

```javascript
let precio = 1234567.89;

console.log(
  precio.toLocaleString("es-AR", {
    style: "currency",
    currency: "ARS"
  })
);
```

Resultado

```
$ 1.234.567,89
```

Estados Unidos:

```javascript
precio.toLocaleString("en-US", {
    style: "currency",
    currency: "USD"
});
```

Resultado

```
$1,234,567.89
```

Europa:

```javascript
precio.toLocaleString("de-DE", {
    style: "currency",
    currency: "EUR"
});
```

Resultado

```
1.234.567,89 €
```

---

# 14. ¿Qué significa `"es-AR"`?

Es un **locale**, un identificador de idioma y región.

Está compuesto por:

* `es` → idioma (español)
* `AR` → país (Argentina)

Otros ejemplos:

| Locale  | Idioma    | País           |
| ------- | --------- | -------------- |
| `es-AR` | Español   | Argentina      |
| `es-ES` | Español   | España         |
| `es-MX` | Español   | México         |
| `en-US` | Inglés    | Estados Unidos |
| `en-GB` | Inglés    | Reino Unido    |
| `fr-FR` | Francés   | Francia        |
| `de-DE` | Alemán    | Alemania       |
| `pt-BR` | Portugués | Brasil         |

Cada locale define reglas para:

* Separadores de miles.
* Separadores decimales.
* Formato de moneda.
* Formato de fechas.
* Nombres de meses y días.
* Convenciones de porcentajes y otros formatos.

---

# Resumen

| Concepto           | Explicación                                                                |
| ------------------ | -------------------------------------------------------------------------- |
| `Number`           | Único tipo numérico estándar para enteros y decimales en JavaScript.       |
| Integer            | Número sin decimales (concepto, no un tipo distinto).                      |
| Float              | Número con decimales (también representado como `Number`).                 |
| `BigInt`           | Tipo especial para enteros muy grandes, con precisión arbitraria.          |
| `NaN`              | Resultado de una operación que no produce un número válido.                |
| `Infinity`         | Representa un valor mayor que cualquier número finito.                     |
| `toLocaleString()` | Formatea un número según las convenciones de un idioma y región.           |
| `es-AR`            | Locale para español de Argentina: usa `.` para miles y `,` para decimales. |

La idea clave es distinguir **el valor** de **su representación**: un `Number` como `1234567.89` es el mismo en cualquier lugar; lo que cambia con `toLocaleString("es-AR")`, `toLocaleString("en-US")` o cualquier otro locale es únicamente la forma en que se presenta al usuario según las convenciones culturales de cada región.

