# Know the logic to solve problems
It's not about an specific programming language, but its generic methodology. The most important step is to know how to solve problems using the common constructions of programming.

Programming languages are basically a way to define this constructions. Therefore it's essential to understand variables or conditional statements (if, else) and loops (for, while, do while).

## Variables
- Variables are boxes where we store values
- Every box has a name and we'll use that name later in our program 
- Each box (or variable) can store numbers, text or another data

```sh
//Store value 43 on a box called 'variableName'
let variableName = 43;
//Call value 43 using that box name
let result = variableName + 30;
```

## Conditionals
This allows us to control our program's execution and solve complex problems
```sh
if (result > 45) {
	console.log('execute this code only if it fits the condition');
} else {
	 console.log('if not, execute this part');
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


