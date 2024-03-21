# What is Javascript?

### Basic Concepts
**JavaScript is a**

- **High level language**: Strong abstraction from the details of the computer, including natural language elements, which means that it's easier to use


- **Single threaded, Asynchronous language**: Single threaded means that it contains the execution of instructions in a single sequence, which means that one command is processed at a time. Asynchronous means that instead of waiting for the response before executing the next bit of code, we declare what we want to happen once we receive our response.

The *Non-blocking event loop* can queue up work in the background without blocking the main thread	


- **Interpreted | JIT Compiled**: Instead of being a compiled language that needs to converting the program source code into machine-readable binary code before execution. It is interpreted, which executes the program instructions without requiring them to be precompiled. Javascript engines are designed leveraging best of the both approaches & developed the Just In Time (JIT) Compilation model.
Some of the popular engines are *V8 from Google* (enables Node.js, Chrome & chromium-based browsers), *SpiderMonkey* (enables Firefox & its fork implementations) and *JavaScriptCode* (enables Safari & other WebKit based browsers).

*Just-In-Time* or *JIT* Compiler means that all code coverts to machine code in parallel, then executed immediately


- **Prototyped based**: Prototype-based programming is a style of object-oriented programming in which classes are not explicitly defined, but rather derived by adding properties and methods to an instance of another class, which means that this style allows the creation of an object without first defining its class.
This prototype-based programming style means that inheritance is performed via a process of reusing existing objects that serve as prototypes


- **Multi-paradigm**: In JavaScript we can use multiple programming paradigms, from imperative, reactive, functional or object-oriented


- **Dynamic**: JavaScript uses a loosely typed data structure, which means that it is possible to use any of the declaration (var, let, const) without specifying the variable type


### What can you do with JavaScript?
- **Front-end** applications
- **Server-side/Back-end** applications with *Node.js*
- **Mobile** applications with *React Native* or *Ionic*
- **Desktop** apps with *Electron*


### High level, interpreted programming language
*High level* means that there are a lot of abstractions, so we don't have to deal with things like memory management like we would do with a low level language like C or C++

*Interpreted* means that the program is executed directly without having to run through a compiler
Languages like Java need to run the code through a compiler (that transforms our human readable code into machine language)

### Conforms to the ECMAScript specification

### Multi-paradigm
This means that you can write your code in many different ways, like object-oriented code or functional code

### Runs on the client/browser as well as on the server (Node.js)
JavaScript is the language of the browser or the client, this means it's the language of the front end
But JavaScript also runs on the server for more powerful options like interacting with a database, this is done using a JavaScript runtime known as *Node.js*


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
- Loops (for, while, for...of, forEach, map)
- Conditionals (if, ternary & switch)
- Functions (normal & arrow)
- OOP (prototypes & classes)
- DOM Selection
- DOM manipulation


# Variables
### Printing messages on the screen
```javascript
// Displays Hello World on the screen
alert("Hello World");

// Prints Hello World on the browser console (F12 -> Console)
console.log("Hello World");
```

### var, let & const variables
**var** has been used since the beginning of javascript, but isn't used anymore because and its global scoped
This means that if we use the same variable name outside of its block, it can cause a conflict and cause problems

**let** and **const** were added with ES6 (ECMAScript 6) in 2015 and both have a block-level scope

**let** variables allow us to reassing values
**const** variables are short for constant, which means that variable cannot be changed or reassigned
```javascript
// let example
let age = 30;
age = 31;
console.log(age); // outputs 31

// const example
const age = 30;
age = 31;
console.log(age); // outputs an error message (assignment to constant variable)
```
There are different approaches about when to use let or const variables, some people just uses let
Some other people prefers to use only const, except when you know you're going to reassingn the value


# Data Types
### Primitive data types
We have **primitive data types**, which means that the data is directly assigned to memory
Examples of primitive data types are *String, Numbers, Boolean, null, undefined*
```javascript
// String
const name = "John";

v Number
const age = 30;

// Numbers also include decimals
const rating = 4.5;

// Boolean (either true or false only)
const isCool = true;

// Null is basically empty, it's a variable with nothing on it
const x = null;

// Undefined variable
const y = undefined;
//Another example of undefined variable
let z;

// To test the type
console.log(typeof name); //returns string

// Concatenation
console.log("My name is " + name + " and I am " + age); //My name is John and I am 30

//Template String or Template literals (ES6 concatenation)
const hello = `My name is ${name} and I am ${age}`;
console.log(hello); //My name is John and I am 30
```

### String properties & methods
A **property** doesn't have parenthesis, if not, it's a method
A **method** is basically a function that is associated with an object
```javascript
const s = "Hello World";

console.log(s.length); //11

console.log(s.toUpperCase()); //HELLO WORLD

console.log(s.toLowerCase); //hello world

console.log(s.substring(0, 6).toUpperCase()); //HELLO W

//to split a string onto an array
console.log(s.split('')); //["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"]

const x = 'technology, computers, it, code';

console.log(s.split(', ')); //["technology", "computers", "it", "code"]
```
With those split() examples, now we could insert each specific word onto a database and search to it and stuff like that


# Arrays
**Arrays** are variables that hold multiple values
With JavaScript we can have multiple data types within the same array
*const fruits = ['apples', 'oranges', 'pears', 10, true];*
```javascript
const fruits = ['apples', 'oranges', 'pears'];

console.log(fruits[1]); //oranges

//Adding a new value to the end
fruits.push('mangos');

//Adding a new value to the beginning
fruits.unshift('straberries');

//Deleting the last element
fruits.pop();

//Deleting the first element
fruits.shift();

//Check if something is an array
console.log(Array.isArray(fruits)); //true
console.log(Array.isArray('hello')); //false

//Getting an index of a certain value
console.log(fruits.indexOf('oranges')); //2
```


# Object Literals
Object literals are basically just key-value pairs
```javascript
const person = {
	firstName: 'John',
	lastName: 'Doe',
	age: 30,
	hobbies: ['music', 'movies', 'sports'],

	//We can also do embedded objects (an object within an object)
	address: {
		street: '50 main st',
		city: 'Boston',
		state: 'MA'
	}
}

//To access a single value we can use the dot syntax
console.log(person.firstName, person.lastName); //John Doe

console.log(person.hobbies[1]); //movies

console.log(person.address.city); //Boston

//We can also use destructuring, it's part of ES6
const { firstName, lastName, address: { city} } = person;

//We can add properties
person.email = 'john@gmail.com';
```

### Arrays of objects
In JavaScript we'll be dealing with tons of arrays of objects
```javascript
const todos = [
	{
		id: 1,
		text: 'Take out trash',
		isCompleted: true
	},
	{
		id: 2,
		text: 'Meeting',
		isCompleted: true
	},
	{
		id: 3,
		text: 'Dentist',
		isCompleted: true
	}
];

console.log(todos[1].text); //Meeting

//To convert this array of objects into JSON within our script to send it to a server
const todoJSON = JSON.stringify(todos);
console.log(todoJSON); //Returns a JSON string
```

### JSON or JavaScript Object Notation
JSON is a lightweight data interchange formata data
It's commonly used to send and receive data in web apps

**JSON Syntax Rules**
- Data is in name/value pairs
- Data is separated by commas
- Curly braces hold objects
- Square brackets hold arrays

The JSON format is syntactically identical to the code for creating JavaScript objects
Because of this similarity, a JavaScript program can easily convert JSON data into native JavaScript objects
*JSON names require double quotes. JavaScript names do not*
```javascript
{
"employees":[
  {"firstName":"John", "lastName":"Doe"},
  {"firstName":"Anna", "lastName":"Smith"},
  {"firstName":"Peter", "lastName":"Jones"}
]
}
```
**Converting a JSON text to a JavaScript Object**
A common use of JSON is to read data from a web server, and display the data in a web page
For simplicity, this can be demonstrated using a string as input
First, let's create a JavaScript string containing JSON syntax
Then, we'll use the JavaScript built-in function JSON.parse() to convert the string into a JavaScript object
```javascript
let text = '{ "employees" : [' +
'{ "firstName":"John" , "lastName":"Doe" },' +
'{ "firstName":"Anna" , "lastName":"Smith" },' +
'{ "firstName":"Peter" , "lastName":"Jones" } ]}'; 

let object = JSON.parse(text);

console.log(obj.employees[1].firstName + " " + obj.employees[1].lastName');
// Anna Smith
```


# Loops (for, while, for...of, forEach, map)
### for
```javascript
//This function will be executed until the condition i < 10 is true
for(let i = 0; i < 10; i++) {
	console.log(`For Loop Number: ${i}`); //For Loop Number: 0 For Loop Number: 1 ...
}
```

### while
```javascript
let i = 0;
while (i < 10) {
	console.log(`While Loop Number: ${i}`);
	i++;
}
```

An example looping through arrays
```javascript
const todos = [
	{
		id: 1,
		text: 'Take out trash',
		isCompleted: true
	},
	{
		id: 2,
		text: 'Meeting',
		isCompleted: true
	},
	{
		id: 3,
		text: 'Dentist',
		isCompleted: false
	}
];

//length will give us the number of items in the array
for(let i = 0; i < todos.length; i++) {
	console.log(todo[i].text); //Take out trash		Meeting		Dentist
}
```

### for of
```javascript
for(let todo of todos) {
	console.log(todo.text); //Take out trash		Meeting		Dentist
}
```

### High order array methods: forEach, map, filter
Best way to do any kind of iteration with arrays

**forEach** loops through the array

**map** will allow us to create a new array from an array

**filter** will allow us to create a new array based on a condition
```javascript
//forEach
todos.forEach(function(todo) {
	console.log(todo.text); //Take out trash		Meeting		Dentist
});

//map
const todoText = todos.map(function(todo) {
	 //Loop through and return an array of just the text values
	return todo.text;
});
console.log(todoText);  //["Take out trash", "Meeting", "Dentist"]

//filter
const todoCompleted = todos.filter(function(todo) {
	 //Similar to map, but filtering only those which are completed
	return todo.isCompleted === true;
});
//Returns an array of 2 values and both of them are completed (true)
console.log(todoCompleted); 

//We can even combine both filter and map loops
//filter
const todoCompleted = todos.filter(function(todo) {
	return todo.isCompleted === true;
}).map(function(todo) {
	return todo.text;
});

console.log(todoCompleted);  //["Take out trash", "Meeting"]
```


# Conditionals (if, ternary & switch)
### if else, else if, &&, ||
```javascript
const x = 10;
const y = 10;

if(x === 10) {
	console.log("x is 10");
}
else if (x > 10) {
	console.log("x is greater than 10")
} 
else {
	console.log("x is less than 10");
}

//Multiple conditions, && and, || or
//if x > 5 and y > 10
if(x > 5 && y > 10) {} 

# if x > 5 or y > 10
if(x > 5 || y > 10) {} 
```

### Ternary Operator
Is basically a shorthand if statement
It's used a lot to assign variables based on a condition
```javascript
const x = 10;
//if x > 10 is true, then (?), color value is red, else (:) color value is blue
const color = x > 10 ? 'red' : 'blue';
```

### Switch
Switch conditionals allow us to uses cases
```javascript
switch(color) {
	case 'red':
		console.log('color is red');
		break;
	
	case 'blue':
		console.log('color is blue');
		break;

		default:
		console.log('color is not red or blue');
		break;
}
```


# Functions
A function is a block of code designed to perform a particular task
It is executed when "something" invokes it (calls it)
We can create a function with the **function** keyword
```javascript
//Adding default values for num1 and num2 parameters
function addNums(num1 = 1, num2 = 2) {
	//for the most part we won't console log a function
	//console.log(num1 + num2);

	//We'll want to return something from instead
	return num1 + num2;
}

console.log(addNums(5,4)); //9
console.log(addNums()); //2
```

### Arrow functions
Introduced in ES6, arrow functions are very handy and help a lot to clean things up
instead of using the keyword **function** we would name it as a variable
```javascript
const addNums = (num1 = 1, num2 = 2) => {
	return num1 + num2;
}

//We don't even need to use the return keyword when the function only has one statement and it returns a value
const addNums = (num1 = 1. num2 = 1) => num1 + num2;

//Even when we only have a parameter, no () are needed
const addNums = num1 => num1 + 5;

//A great option with forEach
todos.forEach((todo) => console.log(todo));
```


# OOP or Object Oriented Programming
We've already looked at object literals, however we can construct objects using a *constructor function*

### Constructor Function
We can use constructor functions with prototypes
and we can also sue ES6 classes
```javascript
//A constructor function should start with a capital
function Person(firstName, lastName, dob) {
	this.firstName = firstName;
	this.lastName = lastName;

	//We can create a Date object
	this.dob = new Date(dob);

	//We can also create methods (functions to this person object)
	this.getBirthYear = function() {
		return this.dob.getFullYear();
	}

	this.getFullName = function() {
		return `${this.firstName} ${this.lastName}`;
	}
}

//Instantiate object
const person1 = new Person('John', 'Doe', '4-3-1980');
const person2 = new Person('Mary', 'Smith', '3-6-1970');

console.log(person1); //Returns object Person John Doe 4-3-1980
console.log(person2.firstName); //Mary
console.log(person2.dob.getFullYear()); //1970
console.log(person1.getBirthYear()); //1980
console.log(person1.getFullName()); //John Doe
```

### Prototypes
All JavaScript objects inherit properties and methods from a prototype
- Date objects inherit from Date.prototype
- Array objects inherit from Array.prototype
- Person objects inherit from Person.prototype

The Object.prototype is on the top of the prototype inheritance chain:
*Date objects, Array objects, and Person objects inherit from Object.prototype*

Sometimes you want to add new properties (or methods) to all existing objects of a given type
Sometimes you want to add new properties (or methods) to an object constructor
The JavaScript prototype property allows you to add new properties to object constructors:

**We can attach objects and methods to the prototype**
Because we don't want to have the functions with every object instance, we may not need to use this
that's why we want to put these in the prototype
```javascript
function Person(firstName, lastName, dob) {
	this.firstName = firstName;
	this.lastName = lastName;
	this.dob = new Date(dob);
}

Person.prototype.getBirthYear = function() {
	return this.dob.getFullYear();
}

Person.prototype.getFullName = function() {
	return `${this.firstName} ${this.lastName}`;
}

console.log(person2.getFullName()); //Mary Smith
```
Now we can also console.log the object person and don't see its methods attached

### ES6 Classes
ES6 classes do the exact same thing under the hood, it adds the methods to the prototype
Everything will look the same, however it's syntatic sugar (just a prettier way to write it)
```javascript
class Person {

	//Constructor
	constructor(firstName, lastName, dob) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.dob = new Date(dob);
	}

	//Methods
	getBirthYear() {
		return this.dob.getFullYear();
	}

	getFullName() {
		return `${this.firstName} ${this.lastName}`;
	}
}

//Same results!
const person1 = new Person('John', 'Doe', '4-3-1980');
const person2 = new Person('Mary', 'Smith', '3-6-1970');

console.log(person1); //Returns object Person John Doe 4-3-1980
console.log(person2.firstName); //Mary
console.log(person2.dob.getFullYear()); //1970
console.log(person1.getBirthYear()); //1980
console.log(person1.getFullName()); //John Doe
```
It does the same thing than the previous example, but in a prettier and easier way!


# DOM or Document Object Model
DOM is the tree structure of our HTML website

### Window object
The Window object is the parent object of the browser
It does includes functions like alert() or localStorage()
The window object is supported by all browsers. It represents the browser's window.
```javascript
console.log(window); //It includes functions like alert() or localStorage()
window.alert("hello"); //Same result as alert("hello")
```

### document
We also find the **document**
The document is what we want to use to select things from the document
```javascript
//Single element
const form = document.getElementById("my-form"); 
console.log(form); //prints the element with that id

//Query selector method
console.log(document.querySelector("h1")); //Gives us the first h1 element

console.log(document.querySelectorAll(".item")); //Gives the node list of the elements with that class

console.log(document.getElementsByClassName("h1")); //Gives the html selection

console.log(document.getElementsByTagName("li")); //Gives the html selection
```

### DOM Manipulation
```javascript
const ul = document.querySelector('.items');

ul.remove(); //Remove all elements with class items

ul.lastElementChild.remove(); //Remove last element of the list

ul.firstElementChild.textContent = 'Hello'; //Changing the text content to Hello

ul.children[1].innerText = 'Ted';

ul.lastElementChild.innerHTML = '<h1>Hello</h1>';

const btn = document.querySelector('.btn');
btn.style.background = 'red'; //Changing the background of the element with that class
```

### Event Listener
HTML events are actions that happen to HTML elements
When JavaScript is used in HTML pages, JavaScript can *react* on these events, for example
	- An HTML web page has finished loading
	- An HTML input field has changed
	- An HTML button was clicked

```javascript
const btn = document.querySelector('.btn');

btn.addEventListener('click', (e) => {
	e.preventDefault(); //Prevent default behavior clicking the submit button
	
	console.log('click');
	
	document.querySelector('#my-form').style.background = "#ccc"; //Adding a dark background

	document.querySelector('body').classList.add)'bg-dark';

	document.querySelector('.items').lastElementChild.innerHTML = '<h1>Hello</h1>';
});
```
```javascript
const myForm = document.querySelector('#my-form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const msg = document.querySelector('.msg');
const userList = document.querySelector('#users');

//When submiting, do the function onSubmit()
myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {

	e.preventDefault();

	console.log(nameInput.value); //Getting the value from the field

	if(nameInput.value === '' || emailInput.value === '') {

		msg.classList.add('error');
		msg.innerHTML = 'Please enter all fields';

		setTimeout(() => msg.remove(), 3000); //After 3 seconds the error message goes away
	} else {
		console.log('success');

		//Creating a text node with the input values
		const li = document.createElement('li');

		li.appendChild(document.createTextNode(`${nameInput.value} : ${emailInput.value}`));

		userList.appendChild(li);

		//Clear fields
		nameInput.value = '';
		emailInput.value = '';
	}
}
```
