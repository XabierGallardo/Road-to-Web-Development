# Programming Questions

### Can you enumerate and explain the various types of errors that can occur during the execution of a computer program?
- **Logical errors**: This occurs in the scenario of a computer program implementing the wrong logic. There are no reports generated for these types of programming errors and they are the most difficult ones to dealt with

- **Runtime errors**: Occurs when the program contains an illegal operation (dividing a number by 0). These are the only errors that are displayed instantly during the program execution. The program execution is stopped and a diagnostic message is displayed

- **Syntax errors**: Occurs when one or more grammatical rules of the pgoramming language being used is violated, such errors are detected during compile time

### Explain an algorithm
An algorithm can be defined as a set of finite steps that when followed helps in accomplishing a particular task
Important features of an algorighm are clarity, efficiency and finiteness

### What do you understand by maintaining and updating a computer program?
The maitenance and updating process of a computer program starts post its succesful installation
While program maintenance is the continuous process of monitoring the computer program for bugs and errors, updating the computer program means making it better with minor and major changes over time

### Provide a brief explanation on variables
Variables are used for storing the input of a program as well as the computational results during program execution
These are actually named memory locations, the value stored in a variable can change during the program execution

### Every programming language has reserved words, what are they?
Reserved word, also known as keywords are the words that have predefined meaning in a particular programming language
These reserved words can't be used for redefined for serving other purposes
In **Java** we have *abstract, boolean, catch, class, const, double, enum, finally, implements*

### What do you understand by loops?
A loops is a structure in programming that can repeat a defined set of statements for a set of number of times or untila a particular condition is satisfied

### Explain program documentation, why is it important?
Program documentation is the written description of the algorighm, coding method, design, testing and proper use of a particular computer program
It is valiable for those who use the program on a day-to-day basis and also for the programmers who are meant to corrent, modify and update the computer program

The main focus of program documentation is development, maintenance and knowledge transfer to other developers

### What are constants?
A constant is a programming entity whose value can't be changed or modified during program execution

### Explain the operators
Operators are used for performing certain operations on data in a computer program
These are represented by symbols
- **Arithmetic**: Used for carrying out mathematical operations
- **Assignment**: Used for storing computational results, strings and values in variables
- **Logical**: Used for allowing a computer program to make a decision based on multiple conditionals. Logical operators allow combining simple conditions to form more complex conditions
- **Relational**: Used for defining or testing some kind of relation between two entities. These operators evaluate to either true or false and produce a non-zero value

### Explain arrays
Arrays are programming structures that are a collection of several data values

### Explain program execution
Program execution is the process of carrying out instructions innate to the program by the computer
Before execution, the computer program is required to be loaded into the memory (RAM) of the computer

### What do you understand by program implementation?
Post the successful completion of software testing of a computer program, it needs to be installed and put into operation on the targeted computer
This process of installing and setting up the computer program to be used by end-users is termed as program implementation

### What is debugging?
During the testing of a computer program, a number of issues are discovered, these are called errors and bugs
Debugging is teh process of correcting them, in other words, debugging is the process of correcting the failures discovered in the implemented code

### What is a recursive function?
A function that calls itself is called a recursive function
It's based on a terminating condition and uses a stack, the phenomenon is called recursion

### What is functional programming?
Functional programming is a way of thinking about software construction by creating pure functions. It avoid concepts of shared state, mutable data observed in Object Oriented Programming. 

### What is Gitflow?
Gitflow is an abstract idea of a workflow in git, it assigns specific functions to different branches and defines how and when they have to interact

### What is Pipeline?
Pipelines are the top-level component of continuous integration, delivery and deployment. There are two main parts
- Jobs, which define what to do (jobs that compile or test code)
- Stages, which define when to run the jobs

### Differences between High level and Low level languages
**High level**
- Programmer friendly language
- Less memory efficient
- Easier to understand
- Simpler to debug and maintain
- Portable
- Can run on any platform
- It needs compiler or interpreter for translation
- Used widely for programming
- C, C++, Java, Python

**Low level**
- Machine friendly language
- High memory efficient
- Tough to understand
- Complex to debug and maintain
- Non-portable
- Machine dependent
- Needs assembler for translation
- Machine code and Assembly Language

### Differences between Strong, Weak and Dynamic typing
A **strongly typed language** has stricter rules at compile time, which implies that errors and exceptions are more likely to happend during compilation
Most of these rules affect variable assignment, function return values, procedure arguments and function calling

A **weakly typed language** has looser typing rules and may produce unpredictable or even erroneous results or may perform implicit type conversion at runtime

A **Dynamic typed language** allows variables to be changed in its type with no problems

Weak or dynamic type normally depends on the point where the compilation phase is done.
If the compilation is done normally is a static type, but if this is done on the execution, is normally a dynamic type

<hr>

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
