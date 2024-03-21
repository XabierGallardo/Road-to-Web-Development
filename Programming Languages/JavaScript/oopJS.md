# Object Oriented Programming in JavaScript Crash Course
Basis and core concepts of writing code in Object Oriented Programming


## Introduction
When it comes to objects in JavaScript
```javascript
//We can access its properties
object.property

//Its functions
object.method()
```

In JavaScript almost everything is an object
We have primitive data types *strings, numbers booleans*, but we can use methods on a string

Our string is a primitive, not an object, but once we call a method on it, JavaScript adds a wrapper to it, and we can create strings as objects
```javascript
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
```javascript
//Printing window object on console
console.log(window);

//Using a method of window
window.alert("Hi there! I'm a pop-up message")
```
Since window is the absolute parent object, there's nothing about window
So we can access its methods without typing *window.*
We can also access object *navigator*
```javascript
//Gives us info on our system
console.log(navigator.appVersion);
```


## Creating objects 
We can create a new JavaScript object with four properties using different ways

#### Object Literal
Easiest way to create a JavaScript object
An object literal is a list of **name:value** pairs insided curly braces **{}**
```javascript
let person = {
	firstName: "Johnny",
	lastName: "Melavo",
	age: 50,
	eyeColor: "brown"
}
```
#### Using Keyword new
```javascript
let person = new Object();
person.firstName = "Johnny";
person.lastName = "Melavo";
person.age = 50;
person.eyeColor = "brown";
```


## Working with our objects
```javascript
let book1 = {

	title: 'Book One',
	author: 'Tomaso Menos',
	year: 2013,

	//Adding a function as a property
	getSummary: function() {

		return `${this.title} was written by ${this.author} in ${this.year}`;

	}
};

//Printing our object on the console
console.log(book1);

//Calling a property
console.log(book1.title); //Book One

//Calling another property
console.log(book1.getSummary()); //Book One was written by Tomaso Menos in 2013

let book2 = {
	title: 'Book Two',
	author: 'Tomas Soli',
	year: 2014,

	//Adding a function as a property
	getSummary: function() {

		return `${this.title} was written by ${this.author} in ${this.year}`;

	}
};

//Calling another property
console.log(book2.getSummary()); //Book Two was written by Tomas Soli in 2014

//Printing the values of an object
console.log(Object.values(book2)); //Returns an array of the values inside

//Printing the keys of an object
console.log(Object.keys(book2)); //Returns an array of the keys inside
```

## Constructors
What if we want to create more than one book?
We don't want to repeat our code and write our property(function) getSummary twice

This is where constructors come in

A constructor it's basically a function
```javascript
//Constructor (with Uppercase)
function Book() {

	console.log('Book Instantiated');

}

//Instantiate an Object
const book1 = new Book(); //Book Instantiated
```
When a new object is instantiated, it will run the code is defined on the constructor
```javascript
function Book(title, author, year) {

	this.title = title;
	this.author = author;
	this.year = year;

	this.getSummary = function() {

		return `${this.title} was written by ${this.author} in ${this.year}`;

	}
}

const book1 = new Book('Book One', 'Johnny Melavo', '2014');
const book2 = new Book('Book Two', 'Johnny Escuccio', '2015');

console.log(book2.getSummary()); //Book Two was written by Johnny Escuccio in 2015
```


## Prototype
All JavaScript objects inherit properties and methods from a prototype
- **Date** objects inherit from **Date.prototype**
- **Array** objects inherit from **Array.prototype**
- **Person** objects inherit from **Person.prototype**

The **Object.prototype** is on the top of the prototype inheritance chain:

**Date** objects, **Array** objects and **Person** objects inherit from **Object.prototype**

The JavaScript prototype property allows us to add new properties to object constructors
It also allows us to add new methods to object constructors

Now we're getting rid of the getSummary function from the constructor
The idea is to store the function into the prototype, we don't want that function for every book object
```javascript
function Book(title, author, year) {

	this.title = title;
	this.author = author;
	this.year = year;

}

//getSummary
Book.prototype.getSummary = function() {

	return `${this.title} was written by ${this.author} in ${this.year}`;

}

//getAge
Book.prototype.getAge = function() {

	const years = new Date().getFullYear() - this.year;

	return `${this.title} is ${years} years old`;
}

//Same result
console.log(book2.getSummary()); //Book Two was written by Johnny Escuccio in 2015

//Now the object doesn't have the method, now it's stored in the prototype
console.log(book2);

console.log(book2.getAge()); //Book Two is 2 years old
```
Now we'll manipulate the data
```javascript
//Revise / change the year
Book.prototype.revise = function(newYear) {

	this.year = newYear;

	this.revised = true;

}

console.log(book2); //Book { ... year: "2016" }

book2.revise('2018');

console.log(book2); //Book { ... year: "2018", revised: true }
```


## Inheritance
We'll create a magazine object, but this magazine will inherit the properties of the book
```javascript
//Book constructor
function Book(title, author, year) {

	this.title = title;
	this.author = author;
	this.year = year;

}

//getSummary
Book.prototype.getSummary = function() {

	return `${this.title} was written by ${this.author} in ${this.year}`;

}

function Magazine(title, author, year, month) {

	//We'll call the Book object and get its properties
	Book.call(this, title, author, year);
	
	this.month = month;

}

//Instantiate Magazine object
const mag1 = new Magazine('Mag One', 'John Jackson', '2018', 'January');

//In order to inherit the prototype methods of Book
Magazine.prototype = Object.create(Book.prototype);

console.log(mag1); //Prints the Magazine object

console.log(mag1.getSummary()); //Mag One was written by John jackson in 2018

//Now if we look at the proto object, we'll see that it uses the Book constructor
console.log(mag1);

//To change the constructor to the magazine
Magazine.prototype.constructor = Magazine;

//Now it will show that the constructor is Magazine
console.log(mag1); //constructor: Magazine(title, author, year, month)
```


## Different ways to create objects
Object of Protos
```javascript
const bookProtos = {

	getSummary: function() {
		return `${this.title} was written by ${this.author} in ${this.year}`;
	},

	getAge: function() {
		const years = new Date().getFullYear() - this.year;
		return `${this.title} is ${years} years old`;
	}
};

//Object creation 1
const book1 = Object.create(bookProtos);
book1.title = 'Book One';
book1.author = 'Johnny Melavo';
book1.year = '2013';

//Object creation 2
const book1 = Object.create(bookProtos, {
	title: {value: 'Book One'},
	author: {value: 'Johnny Melavo'},
	year: {value: '2013'},
});
```
Creating objects using classes, much easier for those familiar with object-oriented programming languages
```javascript
class Book {
	constructor(title, author, year) {
		this.title = title;
		this.year = author;
		this.year = year;
	}

	getSummary() {
		return `${this.title} was written by ${this.author} in ${this.year}`;
	}

	getAge() {
		const years = new Date().getFullYear() - this.year;
		return `${this.title} is ${years} years old`;
	}

	revise(newYear) {
		this.year = newYear;
		this.revised = true;
	}

	//Static methods allows us to have a method in our class that we can use without instatiate an object

	//Defining an static method
	static topBookStore() {
		return 'Barnes & noble';
	}
}

//Instantiating an object
const book1 = new Book('Book One', 'Johnny Melavo', '2013');

console.log(book1); //Now we can see printed our objects with the methods below the prototype arrow

//To use our static method, we must call it on the actual class

book1.topBookStore(); //Uncaugh TypeError: is not a function

console.log(Book.topBookStore());
```
Working with subclasses
Our subclass magazine will have everything a book has but also have a month
```javascript
//Magazine subclass
class Magazine extends Book() {

	constructor(title, author, year, month) {

		//In order to call the parent constructor we will use super
		super(title, author, year);
		this.month = month;

	}
}

//Instantiate Magazine
const mag1 = new Magazine('Mag One', 'John Johnson', '2018', 'Jan');

//We can access getSummary
console.log(mag1.getSummary());
```


# More about Classes
ES6 introduces JavaScript Classes
JavaScript Classes are templates for JavaScript Objects

We'll create a class with the keyword **class**
We always add a method named constructor()
```javascript
class Car {

	constructor(name, year) {

		this.name = name;
		this.year = year;

	}
}
```
Now we'll use the **Car class** to create **Car objects**
```javascript
let myCar1 = new Car("Ford", 2014);
let myCar2 = new Car("Audi", 2016);
```
The constructor method is called automatically when a new object is created

## The Constructor Method
The constructor method is a special method
- It has to have the exact name "constructor"
- It is executed automatically when a new object is created
- It is used to initialize object properties

If we don't defined a constructor method, JavaScript will add an empty constructor method

## Class Methods
Class methods are created with the same syntax as object methods
Using the keyword **class** to create a class
Add a **constructor()** method
Then adding any number of methods
```javascript
class ClassName {
	constructor() { ... }
	method_1() { ... }
	method_2() { ... }
	method_3() { ... }
}
```
We'll create a class method named "age" that returns the Car age
```javascript
class Car {

	constructor (name, year) {
		this.name = name;
		this.year = year;
	}

	age() {
		let date = new Date().getFullYear() - this.year;
		return `This car is ${date} years old`;
	}
}

let myCar = new Car("Ford", 2014);

console.log(myCar.age()); //This car is 7 years old
```