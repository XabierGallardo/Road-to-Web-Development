# What is Javascript?

##### High level, interpreted programming language
**High level** means that there are a lot of abstractions, so we don't have to deal with things like memory management like we would do with a low leve language like C or C++

**Interpreted** means that the program is executed directly without having to run through a compiler
Languages like Java need to run the code through a compiler (that transforms our human readable code into machine language)

##### Conforms to the ECMAScript specification

##### Multi-paradigm
This means that you can write your code in many different ways, like object-oriented code or functional code

##### Runs on the client/browser as well as on the server (Node.js)
JavaScript is the language of the browser or the client, this means it's the language of the front end
But JavaScript also runs on the server for more powerful options like interacting with a database, this is done using a JavaScript runtime known as **Node.js**


## Why learn JavaScript?
- It's the programming language of the browser
- Build very interactive user interfacecs with frameworks like React
- Used in building very fast server-side and full stack applications
- Used in mobile development (React Native, NativeScript, Ionic)
- Used in desktop application development (Electron JS)


## Index
- Variables & Data Types
- Arrays
- Object Literals
- Methods for strings, arrays, objects, etc
- Loops -for, while, for...of, forEach, map
- Conditionals (if, ternary & switch)
- Functions (normal & arrow)
- OOP (prototypes & classes)
- DOM Selection
- DOM manipulation

## Variables & Data Types
##### Printing messages on the screen
```sh
//Displays Hello World on the screen
alert("Hello World");

//Prints Hello World on the browser console (F12 -> Console)
console.log("Hello World");
```

##### var, let & const variables
**var** has been used since the beginning of javascript, but isn't used anymore because and its global scoped
This means that if we use the same variable name outside of its block, it can cause a conflict and cause problems

**let** and **const** were added with ES6 (ECMAScript 6) in 2015 and both have a block-level scope

**let** variables allow us to reassing values
**const** variables are short for constant, which means that variable cannot be changed or reassigned
