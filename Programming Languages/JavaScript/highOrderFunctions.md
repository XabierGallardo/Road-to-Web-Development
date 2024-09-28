# Programacion funcional
La **programación funcional** es un paradigma de programación en el que las funciones son tratadas como ciudadanos de primera clase. Esto significa que las funciones pueden ser asignadas a variables, pasadas como argumentos a otras funciones, y devueltas como resultados de otras funciones. En JavaScript, la programación funcional se basa en el uso de funciones puras, la inmutabilidad de datos y la evitación de efectos secundarios.

### Características clave de la programación funcional

1. **Funciones puras**:
   Una función pura es aquella que, dado el mismo conjunto de argumentos, siempre devuelve el mismo resultado y no tiene efectos secundarios. Es decir, no modifica variables externas, ni realiza operaciones que alteren el estado del programa (como modificar archivos o interactuar con bases de datos).

   **Ejemplo de una función pura**:
   ```javascript
   function suma(a, b) {
       return a + b;
   }
   console.log(suma(2, 3)); // 5
   ```

   Esta función siempre devolverá `5` si se le pasan los argumentos `2` y `3`.

2. **Inmutabilidad**:
   En la programación funcional, los datos no cambian una vez que han sido creados. En lugar de modificar estructuras de datos (como objetos o arrays), se crean nuevas estructuras con los cambios aplicados. Esto garantiza que los datos sean consistentes a lo largo del programa y ayuda a evitar errores difíciles de rastrear.

   **Ejemplo de inmutabilidad**:
   ```javascript
   const array = [1, 2, 3];
   const nuevoArray = array.map(elemento => elemento * 2);
   console.log(array); // [1, 2, 3] (no cambia)
   console.log(nuevoArray); // [2, 4, 6] (nuevo array)
   ```

3. **Funciones como ciudadanos de primera clase**:
   Las funciones pueden ser tratadas como valores, lo que significa que pueden ser asignadas a variables, pasadas como parámetros y devueltas desde otras funciones. Esto permite la composición de funciones y facilita la reutilización de código.

   **Ejemplo**:
   ```javascript
   function saludo(nombre) {
       return `Hola, ${nombre}!`;
   }

   function ejecutaFuncion(funcion, valor) {
       return funcion(valor);
   }

   console.log(ejecutaFuncion(saludo, "Ana")); // "Hola, Ana!"
   ```

4. **Funciones de orden superior (High-order functions)**:
   Las funciones de orden superior son funciones que reciben una o más funciones como argumento o devuelven una función como resultado. Esto es fundamental en la programación funcional, ya que permite crear abstracciones y manipular el comportamiento de otras funciones.

   **Ejemplo**:
   ```javascript
   const numeros = [1, 2, 3, 4, 5];
   const dobles = numeros.map(numero => numero * 2); // `map` es una high-order function
   console.log(dobles); // [2, 4, 6, 8, 10]
   ```

5. **Composición de funciones**:
   La composición de funciones es el proceso de combinar múltiples funciones pequeñas para crear una nueva función. El resultado de una función es pasado como entrada a la siguiente, formando una cadena de procesamiento.

   **Ejemplo**:
   ```javascript
   const agregar = x => x + 1;
   const multiplicar = x => x * 2;

   const agregarYMultiplicar = x => multiplicar(agregar(x));

   console.log(agregarYMultiplicar(5)); // 12
   ```

6. **Evitar efectos secundarios**:
   Un efecto secundario es cualquier interacción de una función con el "mundo exterior", como modificar variables globales, realizar lecturas o escrituras en archivos, o modificar datos fuera del ámbito local de la función. En la programación funcional, se trata de minimizar estos efectos para que el comportamiento del programa sea más predecible y controlable.

   **Ejemplo de una función con efectos secundarios**:
   ```javascript
   let contador = 0;
   function incrementar() {
       contador++;
   }
   ```

   En este caso, la función `incrementar` modifica una variable global, lo que introduce un efecto secundario. Esto puede llevar a problemas si diferentes partes del programa dependen del valor de `contador`.

### Ventajas de la programación funcional en JavaScript

1. **Código más fácil de razonar**: Al minimizar los efectos secundarios y trabajar con funciones puras, es más fácil predecir y comprender cómo se comporta el código.
   
2. **Facilita la prueba de código (testing)**: Las funciones puras son más fáciles de probar porque no dependen del estado externo, lo que las hace ideales para pruebas unitarias.

3. **Reutilización y composición de funciones**: La programación funcional permite componer funciones pequeñas y específicas para crear soluciones más grandes y complejas. Esto fomenta la reutilización del código.

4. **Inmutabilidad**: Al evitar la mutación de datos, se reduce la posibilidad de errores relacionados con el cambio de estado.

### Desventajas y limitaciones

1. **Curva de aprendizaje**: Para desarrolladores acostumbrados a paradigmas como la programación orientada a objetos, la programación funcional puede tener una curva de aprendizaje más empinada.

2. **Rendimiento**: A veces, la creación de nuevas estructuras de datos en lugar de modificar las existentes puede ser menos eficiente en términos de rendimiento, especialmente en aplicaciones con gran cantidad de datos.

### Ejemplo completo de programación funcional en JavaScript:

```javascript
const productos = [
    { nombre: 'Camisa', precio: 20 },
    { nombre: 'Pantalón', precio: 40 },
    { nombre: 'Zapatos', precio: 50 },
    { nombre: 'Sombrero', precio: 15 }
];

// Filtrar productos que cuestan más de 20
const productosCaros = productos.filter(producto => producto.precio > 20);

// Obtener los nombres de los productos filtrados
const nombresProductosCaros = productosCaros.map(producto => producto.nombre);

// Sumar los precios de los productos caros
const precioTotal = productosCaros.reduce((total, producto) => total + producto.precio, 0);

console.log(nombresProductosCaros); // ['Pantalón', 'Zapatos']
console.log(precioTotal); // 90
```

En este ejemplo, utilizamos varias high-order functions (`filter`, `map`, `reduce`) para procesar la lista de productos de manera funcional, sin modificar la lista original ni crear efectos secundarios.

### Conclusión

La **programación funcional en JavaScript** promueve el uso de funciones puras, inmutabilidad y la composición de funciones para resolver problemas de forma más clara y predecible. Este paradigma puede mejorar la calidad del código, hacerlo más fácil de mantener y probar, aunque con una curva de aprendizaje que puede requerir adaptación para aquellos acostumbrados a otros paradigmas como la programación orientada a objetos.

___


# High Order Functions en JavaScript
Las **high-order functions** (funciones de orden superior) en JavaScript son funciones que cumplen al menos una de estas dos condiciones:

1. **Reciben una o más funciones como argumento(s)**.
2. **Devuelven una función** como resultado.

Esto las convierte en herramientas clave para la programación funcional, ya que permiten manipular el comportamiento de otras funciones y facilitan la composición y reutilización de código.

En JavaScript, muchos métodos integrados de arrays como `map`, `filter`, `reduce`, `forEach`, `every`, `some`, entre otros, son ejemplos de high-order functions, ya que aceptan funciones como parámetros para procesar cada elemento del array.

### 1. **Método `forEach()`**
El método `forEach()` ejecuta una función proporcionada para cada elemento del array. No devuelve un nuevo array, sino que se usa cuando solo queremos realizar una acción con cada elemento, sin modificarlo ni crear un nuevo array.

**Sintaxis:**
```javascript
array.forEach(function(elemento, indice, array) {
    // hacer algo con cada elemento
});
```

**Ejemplo:**
```javascript
const numeros = [1, 2, 3, 4, 5];
numeros.forEach((numero) => {
    console.log(numero * 2); // Imprime el doble de cada número
});
```

### 2. **Método `map()`**
`map()` crea un nuevo array aplicando una función a cada uno de los elementos del array original. Es decir, transforma los elementos y devuelve un nuevo array con los valores transformados.

**Sintaxis:**
```javascript
const nuevoArray = array.map(function(elemento, indice, array) {
    // retornar nuevo valor para cada elemento
});
```

**Ejemplo:**
```javascript
const numeros = [1, 2, 3, 4, 5];
const dobles = numeros.map(numero => numero * 2);
console.log(dobles); // [2, 4, 6, 8, 10]
```

### 3. **Método `filter()`**
`filter()` crea un nuevo array que contiene solo los elementos que cumplen con la condición especificada en la función que le pasamos.

**Sintaxis:**
```javascript
const nuevoArray = array.filter(function(elemento, indice, array) {
    // retornar true o false para cada elemento
});
```

**Ejemplo:**
```javascript
const numeros = [1, 2, 3, 4, 5];
const mayoresQueTres = numeros.filter(numero => numero > 3);
console.log(mayoresQueTres); // [4, 5]
```

### 4. **Método `reduce()`**
`reduce()` aplica una función a un acumulador y a cada elemento del array para reducir el array a un solo valor (por ejemplo, la suma o producto de todos los elementos).

**Sintaxis:**
```javascript
const resultado = array.reduce(function(acumulador, elemento, indice, array) {
    // lógica para acumular valor
}, valorInicial);
```

**Ejemplo:**
```javascript
const numeros = [1, 2, 3, 4, 5];
const suma = numeros.reduce((acumulador, numero) => acumulador + numero, 0);
console.log(suma); // 15
```

### 5. **Método `every()`**
`every()` devuelve `true` si todos los elementos del array cumplen con la condición dada. Si al menos un elemento no cumple, devuelve `false`.

**Sintaxis:**
```javascript
const resultado = array.every(function(elemento, indice, array) {
    // retornar true o false
});
```

**Ejemplo:**
```javascript
const numeros = [1, 2, 3, 4, 5];
const todosSonPositivos = numeros.every(numero => numero > 0);
console.log(todosSonPositivos); // true
```

### 6. **Método `some()`**
`some()` devuelve `true` si al menos un elemento del array cumple con la condición. Si ninguno cumple, devuelve `false`.

**Sintaxis:**
```javascript
const resultado = array.some(function(elemento, indice, array) {
    // retornar true o false
});
```

**Ejemplo:**
```javascript
const numeros = [1, 2, 3, 4, 5];
const hayMayoresQueTres = numeros.some(numero => numero > 3);
console.log(hayMayoresQueTres); // true
```

### Comparación rápida entre `every()` y `some()`:

- **`every()`**: Todos los elementos deben cumplir la condición.
- **`some()`**: Solo un elemento necesita cumplir la condición.

### Ejemplo completo utilizando varias high-order functions:

```javascript
const estudiantes = [
    { nombre: "Ana", nota: 8 },
    { nombre: "Luis", nota: 5 },
    { nombre: "Carlos", nota: 7 },
    { nombre: "María", nota: 9 }
];

// Obtener todos los estudiantes aprobados (nota >= 6)
const aprobados = estudiantes.filter(estudiante => estudiante.nota >= 6);
console.log(aprobados);

// Obtener un array con solo los nombres de los estudiantes
const nombres = estudiantes.map(estudiante => estudiante.nombre);
console.log(nombres);

// Verificar si todos los estudiantes tienen una nota mayor o igual a 5
const todosAprobados = estudiantes.every(estudiante => estudiante.nota >= 5);
console.log(todosAprobados); // true

// Verificar si algún estudiante tiene una nota perfecta (10)
const algunPerfecto = estudiantes.some(estudiante => estudiante.nota === 10);
console.log(algunPerfecto); // false

// Sumar todas las notas de los estudiantes
const sumaNotas = estudiantes.reduce((acumulador, estudiante) => acumulador + estudiante.nota, 0);
console.log(sumaNotas); // 29
```

### Ventajas del uso de high-order functions

1. **Código más limpio y conciso**: Evitan la necesidad de escribir bucles manualmente.
2. **Reutilización de funciones**: Puedes pasar funciones reutilizables como argumentos.
3. **Abstracción de comportamiento**: Facilitan la separación entre el "qué hacer" y el "cómo hacerlo".

### Conclusión

Las **high-order functions** permiten escribir código más expresivo y funcional en JavaScript. Métodos como `map`, `filter`, `reduce`, `forEach`, `every` y `some` son poderosos porque permiten trabajar con arrays de manera más eficiente y declarativa, sin necesidad de escribir bucles explícitos.


___


# JavaScript High Order Functions & Arrays
```javascript
const companies = [
	{name: "Company One", category: "Finance", start: 1981, end: 2003},
	{name: "Company Two", category: "Retail", start: 1992, end: 2008},
	{name: "Company Three", category: "Auto", start: 1999, end: 2007},
	{name: "Company Four", category: "Retail", start: 1989, end: 2010},
	{name: "Company Five", category: "Technology", start: 2009, end: 2014},
	{name: "Company Six", category: "Finance", start: 1987, end: 2010},
	{name: "Company Seven", category: "Auto", start: 1986, end: 1996},
	{name: "Company Eight", category: "Technology", start: 2011, end: 2016},
	{name: "Company Nine", category: "retail", start: 1981, end: 1989}
];

const ages = [33, 12, 20, 16, 5, 54, 21, 44, 61, 13, 15, 45, 25,64, 32];
```


## forEach()
forEach loop is a better way to loop through an array rather than using a for loop
```javascript
// Printing every iteration with a for loop

for(let i = 0; i < companies.length; i++) {

	console.log(companies[i]); // Returning the objects

	console.log(companies.name); //Company One Company Two...
}

// Using forEach
companies.forEach(function(company) {

	console.log(company);

});
```

**function(***currentValue, index, arr***)**

- *currentValue*: Required, the value of the current element
- *index*: Optional, the array index of the current element
- *arr*: Optional, The array object the current element belongs to

```javascript
// Another example of forEach, updating the value with 10 times the original value

let numbers = [65, 44, 12, 4];

numbers.forEach(myFunction);

function myFunction(item, index, arr) {

	arr[index] = item * 10; // 650 440 120 40

// Looking at each individual value

	console.log(item); // 65 44 12 4

	console.log(index); // 0 1 2 3

	console.log(arr); // [65,44,12,4] x 4
}
```


## filter()
filter allows to filter things out from the array

Lets get the ages that are 21 and over
```javascript
// for loop example
let canDrink = [];

for (let i = 0; i < ages.length; i++) {
	
	if(ages[i] >= 21) {
		
		canDrink.push(ages[i]);
	}
}

// filter example
const canDrink = ages.filter(function(age) {

	if(age >= 21) {

		return true;
	}
});

console.log(canDrink);


// filter example using ES6 arrow functions
const canDrink = ages.filter(age => age >= 21); // Same output!
```

Now filtering retail companies
```javascript
const retailCompanies = companies.filter(function(company) {

	if(company.category === 'Retail') {

		return true;
	}
});

console.log(retailCompanies); //Returns three object in our array, Company Two, Company Four and Company Nine

// ES6 arrow function
const retailCompanies = companies.filter(company => company.category === 'Retail'); // Same result!
```

Filtering 80's companies
```javascript
const eightiesCompanies = companies.filter(company => (company.start >= 1980 && company.start < 1990));
```

Getting the companies that lasted at least 10 years
```javascript
const lastedTenYears = companies.filter(company => (company.end - company.start >= 10));

console.log(lastedTenYears);
```


## map()
Map works differently, instead of just filtering things out, we can create new arrays of anything from a current array

We'll grab all the company names and put them into their own array
```javascript
// Create array of company names

const companyNames = companies.map(function(company) {

	return company.name; 
});

console.log(companyNames); // Returns an array of all the company names

const testMap = companies.map(function(company) {

	return `${company.name} [${company.start} - ${company.end}]`;
});

console.log(testMap); // Returns an array and each value has this format: Company One [1981 - 2003] ...


// Using ES6 arrow functions
const testMap = companies.map(company => `${company.name} [${company.start} - ${company.end}]`;);
```

An example using the ages array
```javascript
// Storing the square root values

const agesSquare = ages.map(age => Math.sqrt(age));

console.log(agesSquare);


// Multiplying each one by 2
const agesTimesTwo = ages.map(age => age * 2);

console(ageTimesTwo);


// We could square the numbers and then multiplying them by 2

const ageMap = ages

	.map(age => Math.sqrt(age))

	.map(age => age * 2);

	console.log(ageMap);
```


## sort()
We'll sort the companies by the start year
```javascript
const sortedCompanies = companies.sort(function(c1, c2) {
	
	if(c1.start > c2.start) {
	
		return 1;
	
	} else {
	
		return -1;
	}
});

console.log(sortedCompanies);


// Shorter form

const sortedCompanies = companies.sort((a, b) => (a.start > b.start ? 1 : -1))

console.log(sortedCompanies);
```
Sorting ages
```javascript
// Sorting in ascending order

const sortAges = ages.sort((a, b) => a - b);

// Sorting in descending order

const sortAges = ages.sort((a, b) => b - a);

console.log(sortAges);
```


## reduce()
Adding all of the ages together
```javascript
// for loop example
let ageSum = 0;

for(let i = 0; i < ages.length; i++) {

	ageSum += ages[i];
}

// Using reduce

const ageSum = ages.reduce(function(total, age) {

	return total + age;

}, 0);


// Shorter version

const ageSum = ages.reduce((total, age) => total + age, 0);

console.log(ageSum);
```
Get the total years for all companies
The range of all companies will add all those up

```javascript
const totalYears = companies.reduce(function(total, company) {
	
	return total + (company.end - company.start);

	// We'll have to add that second parameter of zero
}, 0);


// Shorter way
const totalYears = companies.reduce((total, company) => total + (company.end - company.start), 0);

console.log(totalYears); // 119
```


## Combine Methods
```javascript
const combined = ages
	
	.map(age => age * 2) // Returns an array of all the ages times 2

	// Now we have an unsorted array of all the ages

	.filter(age => age >= 40) // Filters anything that was under 40

	.sort((a, b) => a - b) // Sorts the results

	// Now we'll reduce to sort them all together
	
	.reduce((a, b) => a + b, 0); // Returns 798
```