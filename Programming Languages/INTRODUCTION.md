# Know the logic to solve problems
It's not about an specific programming language, but its generic methodology. The most important step is to know how to solve problems using the common constructions of programming.

Programming languages are basically a way to define this constructions. Therefore it's essential to understand variables or conditional statements (if, else) and loops (for, while, do while).


## Variables
- Variables are boxes where we store values
- Every variable has a name and we'll use that name later in our program 
- Each variable can store numbers, text or another data

```sh
let variableName = 43; 		//Store value 43 on a variable called 'variableName'
let result = variableName + 30; //Call value 43 using that variable name and sum 30 (result equals 40+30)
```
Inside our variables we can store many data types. In JavaScript those types are dynamic.

```sh
var x;		//Our variable x is undefined
x = 5;		//now x is a number
x = "John";	//now x is a string

var z = true;	//Boolean variables can only have two values, true or false 
```
#### Arrays
Arrays are a collection of variables of the same type. Array items are separated by a comma:
```sh
var cars = ["Peugeot", "Ford", "Volkswagen", "Fiat"];

//In programming languages, 0 is the first number. Therefore our positions are Peugeot 0, Ford 1, Volkswagen 2, Fiat 3
var myCar = cars[2]; //I choose Volkswagen from my car collection by refering my array and that position 
``` 


## Conditionals
This allows us to control our program's execution and solve complex problems
```sh
if (result > 45) {
	console.log('execute this code only if first condition is true');
} else if (result < 25) {
	console.log('execute this code only if first condition is false and second condition is true');
} else {
	 console.log('execute this code only if first and second condition are false');
}
```


## Loops
```sh
for (let i = 0; i < 10; i++) {
	console.log('we'll repeat this code 10 times')
}
```


## Functions
When a piece of code is repeated, we can store that code onto a function, name it and use that code everytime we call to that name


## Data Structures
Fundamental concept of Computer Science. Data Structures are ways to store and manage data. 
 
An example of this data could be a thermometer, that gives us a block of data acording to an specific period of time. All this data is a set of numbers, and the way this set of numbers is organized is a data structure.

That's when we use **Arrays** or **Objects**.


*Every problem that asks us to count data repetitions or count how many elements of each type in an specific block. We'll use this data structures to solve that problems easily*.

#### Control Flow
Sometimes we want to perform two different actions in our code, depending on our decision. Or even we want to repeat an action an specific number of times. That's when we use Conditional and Loops.


## Comments
It's a part of the code that will not be executed. It represents a core part of it because we can write notes, instructions or ideas all around the code 

```sh
//This is a comment

/* This is a 
multiline
comment*/

//This function does nothing!
function nothing() {
	console.log("I do nothing!");
}
```
