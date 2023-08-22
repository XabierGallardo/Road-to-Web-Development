# [ES TypeScript](https://ed.team/cursos/typescript)
## Lenguajes dinámicos vs lenguajes tipados
Al no ser un lenguaje tipado, JavaScript puede traer problemas a veces, si sumamos un entero con un string, JavaScript simplemente suma:
```js
let sum = (a,b) => a+b;
suma(3, "test"); // 3test
``` 
En JavaScript los parámetros de las funciones y las variables no tienen ningún tipo de información! De manera que los desarrolladores tienen que recurrir a la documentación o adivinar basándose en la implementación.

En un lenguaje tipado como GO, especificamos que tanto a como b son números enteros, y el resultado también será entero.
Así se asegura los datos de entrada y de salida:
```go
func sum(a, b int) int{
    return a + b
}
```
Esto es porque JavaScript es un lenguaje dinámicamente tipado, por tanto asigna el tipo de dato según las circunstancias. Por tanto permite que un tipo de dato se convierta a otro tipo de dato.
A esto se le llama **casting**.

JavaSript puede castear un texto a un número, un número a un boolean, un boolean a un texto, etc, según el flujo del programa.

Esto quiere decir que no lo controla el programador. Por ahí ese dato viene de una función anterior y no sabemos qué devuelve. JavaScript no lanza alertas de error y acepta todo lo que venga, esos errores se ven en producción cuando es tarde.

Por eso JavaScript no suele gustar mucho a los programadores y siempre buscaron reemplazaron por opciones que compilen a JavaScript. Por tanto, ante la imposibilidad de sustituír JavaScript, se hizo necesario **extender JavaScript**.

## Qué es TypeScript?
**TypeScript extiende a JavaScript agregandole tipos**.
Por tanto cada vez que usamos un dato, le decimos si el dato es un número, un texto o un boolean, etc.
Así el programa sabe qué dato se recibe, qué dato se devuelve y el flujo del programa está en orden.
 
De ahí el nombre **type / script**

Volviendo al ejemplo anterior, nos devolveria un error:
```ts
let sum = (a:number, b:number) => {
    return a + b
}
sum(3 + "test"); // ERROR Argument of type 'string' is not assignable to parameter of type 'number'.
```
Además no tenemos que esperar a que la aplicación esté en producción para darnos cuenta de que algo falla, los errores saltan ya desde el editor.

## Ventajas de TypeScript sobre JavaScript
1. No hace falta aprender un lenguaje nuevo
2. No hay que esperar a que la aplicación esté en producción. TypeScript alerta desde el propio editor mientras escribimos el código.
3. Las tecnologías de frontend funcionan con TypeScript. React, Angular, Vue, etc
4. Se puede usar TypeScript en el backend, así como en cualquier lugar donde se puede utilizar JavaScript
5. TypeScript le agrega funciones adicionales a JavaScript, como clases e interfaces

## TypeScript behaves like a compiled language
- TypeScript extends JavaScript by adding **static typing**
- TypeScript behaves like a compiled language
- A common way to use TypeScript is to use the official TypeScript compiler, which transpiles TypeScript code into JavaScript
- Some popular code editors, such as Visual Studio Code, have built-in TypeScript support and can show errors as you write code
- TypeScript has an official compiler which can be installed using npm.
- We can run the typescript compiler using the **tsc command**, it will take the .ts file and transpile it into vanilla JS

## [About TypeScript](https://www.w3schools.com/typescript/index.php)
- We can choose any flavour of JS we want to target acient browsers, from ES1, ES3, ES5, ES6
- Therefore we can use the latest syntax of JavaScript without having to worry if they'll be supported in an older environment
- The TypeScript compiler can be configured using a tsconfig.json
- Our TypeScript project will have a **tsconfig.json** file which provides an infinite number of ways to customize the behaviour of the compiler

*tsconfig.json*
```json
{
"compilerOptions" : {
    "module" : "system",
    "noImplicityAny" : true,
    "removeComments" : true,
    "preserveConstEnums" : true,
    "outFile" : "../dist/bundle.js",
    "sourceMap" : true
    },
    "include": ["src/**/*"],
    "exclude" : ["node_modules"]
}
```

## Explicit, Implicit and Special Types
```ts
// EXPLICIT TYPE
// We can strongly type a variable using a colon followed by its type
// string, boolean or number
let appName: string;
appName = 23; // ERROR Type 'number is not assignable (...)


// IMPLICIT TYPE
// If we set an initial value, it will implicitly infer the type
let appName = 'test';


// ANY TYPE for Opt Out type checking
// There may be cases when we want to opt out of this behaviour
// We use the any type for a loosely type or opt out type checking
let appName: any = 'test';
appName = 23;


// UNKNOWN TYPE, similar to ANY but safer
// TypeScript will prevent unknown types from being used
// unknown is best used when you don't know the type of data being typed
// To add a type later, you'll need to cast it
// Casting is when we use the "as" keyword to say property or variable is of the casted type
let w: unknown = 1;
w = "string"; // no error


// ARRAYS
// We use brackets in an array to strongly type a list
let list: number[] = [1,2,3];


// CUSTOM TYPES AND INTERFACES
// We can define our own custom types and iterfaces
// We can then apply the interface to a plain JavaScript Object
interface Car {
    year: number;
    model: string;
    electric: boolean;
}

let myCar: Car;
```
With our stongly typed code, we get **autocomplete** on our IDE!
<p>
    <img src="tsIntellisense.png" alt="TypeScript Autocomplete">
</p>

## TS Simple Types
There are 3 main primitives in JavaScript and TypeScript
- **boolean**: true or false values
- **number**: whole numbers and floating point values
- **string**: text values

There are also 2 less common primitives used in later versions of JS and TS
- **bigint**: whole numbers and floating point values, but allows larger negative and positive numbers than *number* type
- **symbol**: used to create a globally unique identifier

## TS Arrays
```ts
const names: string[] = [];
names.push["tony"]; // no error
names.push(3); // ERROR: Argument of type 'number' is not assignable to aprameter of type 'string'


// The readonly keyword can prevent arrays from being changed
const names2: readonly string[] = ["Dylan"];
names.push("Jack"); // ERROR: Property 'push does not exist on type 'readonly string[]'


// TypeScript can infer the type of an array if it has values
const numbers = [1, 2, 3]; // inferred to type number[]
numbers.push(4); // no error
// comment line below out to see the successful assignment
numbers.push("2"); // Error: Argument of type 'string' is not assignable to parameter of type 'number'.
```
## TS Tuples
- **A tuple is a typed array with a pre-defined length and types** for each index.
- Tuples are great because they allow each element in the array to be a known type of value.
```ts
// Define our tuple
let ourTuple: [number, boolean, string];

// Initialize correctly
ourTuple = [5, false, 'hello world'];

// the order matters in our tuple and will throw an error
// initialized incorrectly which throws an error
ourTuple = [false, 'Coding God was mistaken', 5];

// A good practice is to make your tuple readonly
const ourReadonlyTuple: readonly [number, boolean, string] = [5, true, 'The Real Coding God'];
// throws error as it is readonly.
ourReadonlyTuple.push('Coding God took a day off');
```

## TS Object Types
```ts
const car: {type: string, model: string, year: number} ={
    type: "Toyota",
    model: "Corolla",
    year: 2009
};


// Type inference
// TS can infer the types of properties based on their values
const car = {
  type: "Toyota",
};
car.type = "Ford"; // no error
car.type = 2; // Error: Type 'number' is not assignable to type 'string'.


// Optional property
// Properties that don't have to be defined in the object definition
const car: { type: string, mileage?: number } = { // no error
  type: "Toyota"
};
car.mileage = 2000;
```

## TS Enums
- An **enum is a special class that represents a group of constants** (unchangeable variables)
- **Enums come in two flavors, string and numeric**
- By default, enums will initialize the first value to 0 and add 1 to each additional value
```ts
enum CardinalDirections {
    North,
    East,
    South,
    West
}
let currentDirection = CardinalDirections.North; 
console.log(currentDirection);  // Logs 0


//Numeric Values Initialized
// You can set the value of the first numeric enum and have it auto increment from that:
enum CardinalDirections {
  North = 1,
  East,
  South,
  West
}
console.log(CardinalDirections.North);  // logs 1
console.log(CardinalDirections.West);   // logs 4


// Numeric Values Fully Initialized
enum StatusCodes {
  NotFound = 404,
  Success = 200,
  Accepted = 202,
  BadRequest = 400
}
console.log(StatusCodes.NotFound);  // logs 404
console.log(StatusCodes.Success);   // logs 200


// String Enums
// Enums can also contain strings. This is more common than numeric enums, because of their readability
enum CardinalDirections {
  North = 'North',
  East = "East",
  South = "South",
  West = "West"
};
console.log(CardinalDirections.North);  // logs "North"
console.log(CardinalDirections.West);   // logs "West"
```