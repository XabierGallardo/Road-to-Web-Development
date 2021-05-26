# Object Oriented Programming in JavaScript Crash Course
Basis and core concepts of writing code in Object Oriented Programming

## Introduction
When it comes to objects in JavaScript
```sh
# We can access its properties
object.property

# Its functions
object.method()
```

In JavaScript almost everything is an object
We have primitive data types *strings, numbers booleans*, but we can use methods on a string

Our string is a primitive, not an object, but once we call a method on it, JavaScript adds a wrapper to it, and we can create strings as objects
```sh
const string = 'Hello';

console.log(string.toUpperCase);

console.log(typeof string);

const string2 = new String('Hello');

console.log(typeof string2)
```
All JavaScript values, except primitives, are objects

A **primitive value** is a value that has no properties or methods: *string, number, boolean, null, undefined*

- Booleans can be objects (if defined with the new keyword)
- Numbers can be objects (if defined with the new keyword)
- Strings can be objects (if defined with the new keyword)
- Dates are always objects
- Maths are always objects
- Regular expressions are always objects
- Arrays are always objects
- Functions are always objects
- Objects are always objects

We can call DOM objects like *window*
```sh
# Printing window object on console
console.log(window);

# Using a method of window
window.alert("Hi there! I'm a pop-up message")
```
Since window is the absolute parent object, there's nothing about window
So we can access its methods without typing *window.*
We can also access object *navigator*
```sh
# Gives us info on our system
console.log(navigator.appVersion);
```

## Creating objects 
We can create a new JavaScript object with four properties using different ways

#### Object Literal
Easiest way to create a JavaScript object
An object literal is a list of **name:value** pairs insided curly braces **{}**
```sh
let person = {
	firstName: "Johnny",
	lastName: "Melavo",
	age: 50,
	eyeColor: "brown"
}
```
#### Using Keyword new
```sh
let person = new Object();
person.firstName = "Johnny";
person.lastName = "Melavo";
person.age = 50;
person.eyeColor = "brown";
```


## Working with our objects
```sh
let book1 = {
	title: 'Book One',
	author: 'Tomaso Menos',
	year: 2013,

	# Adding a function as a property
	getSummary: function() {
		return `${this.title} was written by ${this.author} in ${this.year}`;
	}
};

# Printing our object on the console
console.log(book1);

# Calling a property
console.log(book1.title); # Book One

# Calling another property
console.log(book1.getSummary()); # Book One was written by Tomaso Menos in 2013

let book2 = {
	title: 'Book Two',
	author: 'Tomas Soli',
	year: 2014,

	# Adding a function as a property
	getSummary: function() {
		return `${this.title} was written by ${this.author} in ${this.year}`;
	}
};

# Calling another property
console.log(book2.getSummary()); # Book Two was written by Tomas Soli in 2014

# Printing the values of an object
console.log(Object.values(book2)); # Returns an array of the values inside

# Printing the keys of an object
console.log(Object.keys(book2)); # Returns an array of the keys inside
```

## Constructors
What if we want to create more than one book?
We don't want to repeat our code and write our property(function) getSummary twice

This is where constructors come in

A constructor it's basically a function
```sh

```