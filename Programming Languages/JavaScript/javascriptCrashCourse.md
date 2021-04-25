# What is Javascript?

### High level, interpreted programming language
**High level** means that there are a lot of abstractions, so we don't have to deal with things like memory management like we would do with a low leve language like C or C++

**Interpreted** means that the program is executed directly without having to run through a compiler
Languages like Java need to run the code through a compiler (that transforms our human readable code into machine language)

### Conforms to the ECMAScript specification

### Multi-paradigm
This means that you can write your code in many different ways, like object-oriented code or functional code

### Runs on the client/browser as well as on the server (Node.js)
JavaScript is the language of the browser or the client, this means it's the language of the front end
But JavaScript also runs on the server for more powerful options like interacting with a database, this is done using a JavaScript runtime known as **Node.js**


# Why learn JavaScript?
It's the programming language of the browser
Build very interactive user interfacecs with frameworks like React
Used in building very fast server-side and full stack applications
Used in mobile development (React Native, NativeScript, Ionic)
Used in desktop application development (Electron JS)


# Index
- Variables
- Data Types
- Arrays
- Object Literals
- Methods for strings, arrays, objects, etc
- Loops -for, while, for...of, forEach, map
- Conditionals (if, ternary & switch)
- Functions (normal & arrow)
- OOP (prototypes & classes)
- DOM Selection
- DOM manipulation


# Variables
### Printing messages on the screen
```sh
# Displays Hello World on the screen
alert("Hello World");

# Prints Hello World on the browser console (F12 -> Console)
console.log("Hello World");
```

### var, let & const variables & Data Types
**var** has been used since the beginning of javascript, but isn't used anymore because and its global scoped
This means that if we use the same variable name outside of its block, it can cause a conflict and cause problems

**let** and **const** were added with ES6 (ECMAScript 6) in 2015 and both have a block-level scope

**let** variables allow us to reassing values
**const** variables are short for constant, which means that variable cannot be changed or reassigned
```sh
# let example
let age = 30;
age = 31;
console.log(age); # outputs 31

# const example
const age = 30;
age = 31;
console.log(age); # outputs an error message (assignment to constant variable)
```
There are different approaches about when to use let or const variables, some people just uses let
Some other people prefers to use only const, except when you know you're going to reassingn the value


# Data Types

### Primitive data types
We have **primitive data types**, which means that the data is directly assigned to memory
Examples of primitive data types are *String, Numbers, Boolean, null, undefined*

```sh
# String
const name = "John";
# Number
const age = 30;
# Numbers also include decimals
const rating = 4.5;
# Boolean (either true or false only)
const isCool = true;
# Null is basically empty, it's a variable with nothing on it
const x = null;

# Undefined variable
const y = undefined;
# Another example of undefined variable
let z;

# To test the type
console.log(typeof name); # returns string

# Concatenation
console.log("My name is " + name + " and I am " + age); # My name is John and I am 30

# Template String or Template literals (ES6 concatenation)
const hello = `My name is ${name} and I am ${age}`;
console.log(hello); # # My name is John and I am 30
```

### String properties & methods
A **property** doesn't have parenthesis, if not, it's a method
A **method** is basically a function that is associated with an object
```sh
const s = "Hello World";
console.log(s.length); # 11
console.log(s.toUpperCase()); # HELLO WORLD
console.log(s.toLowerCase); # hello world
console.log(s.substring(0, 6).toUpperCase()); # HELLO W

# to split a string onto an array
console.log(s.split('')); # ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"]

const x = 'technology, computers, it, code';
console.log(s.split(', ')); # ["technology", "computers", "it", "code"]
```
With those split() examples, now we could insert each specific word onto a database and search to it and stuff like that


# Arrays
**Arrays** are variables that hold multiple values
With JavaScript we can have multiple data types within the same array
*const fruits = ['apples', 'oranges', 'pears', 10, true];*
```sh
const fruits = ['apples', 'oranges', 'pears'];

console.log(fruits[1]); # oranges

# Adding a new value to the end
fruits.push('mangos');

# Adding a new value to the beginning
fruits.unshift('straberries');

# Deleting the last element
fruits.pop();

# Deleting the first element
fruits.shift();

# Check if something is an array
console.log(Array.isArray(fruits)); # true
console.log(Array.isArray('hello')); # false

# Getting an index of a certain value
console.log(fruits.indexOf('oranges')); # 2
```


# Object Literals
