# String methods JavaScript
## Comparacion entre `slice()`, `substring()`, y `substr()`
En JavaScript, las funciones `slice()`, `substring()`, y `substr()` son métodos de cadena que se utilizan para extraer partes de una cadena. Aunque realizan funciones similares, tienen diferencias clave en cuanto a cómo trabajan con los índices y cómo manejan los parámetros que se les pasan.

### 1. **`slice()`**
El método `slice()` devuelve una nueva cadena que extrae una porción de la cadena original, según los índices que le pasemos. Este método es flexible y funciona con índices negativos.

#### Sintaxis:
```javascript
str.slice(startIndex, endIndex);
```

- **startIndex**: El índice de inicio (incluido).
- **endIndex**: El índice final (no incluido). Este parámetro es opcional, y si se omite, `slice()` extrae desde `startIndex` hasta el final de la cadena.

- Si `startIndex` es negativo, cuenta desde el final de la cadena.
- Si `endIndex` es negativo, cuenta desde el final de la cadena.

#### Ejemplos:
```javascript
let texto = "JavaScript";

// Extraer desde el índice 4 hasta el final
console.log(texto.slice(4)); // "Script"

// Extraer desde el índice 0 al 4 (sin incluir el 4)
console.log(texto.slice(0, 4)); // "Java"

// Índices negativos (comienza a contar desde el final)
console.log(texto.slice(-6)); // "Script"
console.log(texto.slice(-9, -6)); // "Jav"
```

### 2. **`substring()`**
El método `substring()` devuelve una nueva cadena entre dos índices, o desde el índice de inicio hasta el final de la cadena. A diferencia de `slice()`, no admite índices negativos y, si `startIndex` es mayor que `endIndex`, intercambia los valores.

#### Sintaxis:
```javascript
str.substring(startIndex, endIndex);
```

- **startIndex**: El índice de inicio (incluido).
- **endIndex**: El índice final (no incluido). Este parámetro es opcional, y si se omite, `substring()` extrae desde `startIndex` hasta el final de la cadena.

- No admite índices negativos, si se pasa un índice negativo, lo considera como `0`.
- Si `startIndex` es mayor que `endIndex`, intercambia los valores.

#### Ejemplos:
```javascript
let texto = "JavaScript";

// Extraer desde el índice 4 hasta el final
console.log(texto.substring(4)); // "Script"

// Extraer desde el índice 0 al 4 (sin incluir el 4)
console.log(texto.substring(0, 4)); // "Java"

// Intercambia los índices si el inicio es mayor que el final
console.log(texto.substring(5, 0)); // "JavaS"

// No soporta índices negativos, lo trata como 0
console.log(texto.substring(-3)); // "JavaScript"
```

### 3. **`substr()`** (obsoleto)
El método `substr()` extrae una parte de la cadena comenzando en el índice especificado y tomando un número específico de caracteres. Este método está obsoleto y su uso no es recomendado, aunque sigue siendo compatible en muchos navegadores.

#### Sintaxis:
```javascript
str.substr(startIndex, length);
```

- **startIndex**: El índice de inicio (puede ser negativo, y empezará a contar desde el final de la cadena si lo es).
- **length**: La cantidad de caracteres a extraer. Este parámetro es opcional, y si se omite, `substr()` extrae desde `startIndex` hasta el final de la cadena.

- Si `startIndex` es negativo, cuenta desde el final de la cadena.
- `length` es el número de caracteres a extraer a partir de `startIndex`.

#### Ejemplos:
```javascript
let texto = "JavaScript";

// Extraer desde el índice 4, con una longitud de 6 caracteres
console.log(texto.substr(4, 6)); // "Script"

// Extraer desde el índice -6 (desde el final), con una longitud de 6 caracteres
console.log(texto.substr(-6, 6)); // "Script"

// Extraer desde el índice 4 hasta el final, sin longitud especificada
console.log(texto.substr(4)); // "Script"
```

### Diferencias clave:

1. **`slice()` vs `substring()`**:
   - Ambos métodos funcionan de manera similar en la mayoría de los casos.
   - **Soporte para índices negativos**: `slice()` admite índices negativos, mientras que `substring()` no.
   - **Intercambio de valores**: Si el `startIndex` es mayor que el `endIndex`, `substring()` intercambia los valores, mientras que `slice()` no.

2. **`slice()` vs `substr()`**:
   - **Parámetros**: `slice()` utiliza un índice de inicio y un índice de final, mientras que `substr()` usa un índice de inicio y una longitud.
   - **Soporte para índices negativos**: Ambos admiten índices negativos para el índice de inicio.
   - **Obsolescencia**: `substr()` está obsoleto y su uso no es recomendado en proyectos modernos.

3. **`substring()` vs `substr()`**:
   - **Parámetros**: `substring()` utiliza dos índices (inicio y final), mientras que `substr()` usa un índice de inicio y la longitud de la subcadena a extraer.
   - **Intercambio de valores**: `substring()` intercambia `startIndex` y `endIndex` si `startIndex` es mayor que `endIndex`, mientras que `substr()` no lo hace.

### ¿Cuál usar?

- **`slice()`** es generalmente el más flexible y poderoso debido a su soporte para índices negativos y su comportamiento predecible, por lo que es la opción más recomendada en la mayoría de los casos.
- **`substring()`** es útil si prefieres que los valores de los índices se intercambien automáticamente en caso de error.
- **`substr()`** es obsoleto y se recomienda evitarlo en nuevos proyectos.

### Ejemplo comparativo:

```javascript
let texto = "JavaScript";

// Usando slice (índices negativos permitidos)
console.log(texto.slice(4, 10)); // "Script"
console.log(texto.slice(-6));    // "Script"

// Usando substring (sin índices negativos)
console.log(texto.substring(4, 10)); // "Script"
console.log(texto.substring(-6));    // "JavaScript" (negativos no permitidos)

// Usando substr (longitud, método obsoleto)
console.log(texto.substr(4, 6)); // "Script"
```

En resumen, **`slice()`** es la opción más recomendable para trabajar con subcadenas en JavaScript debido a su versatilidad y manejo de índices negativos.