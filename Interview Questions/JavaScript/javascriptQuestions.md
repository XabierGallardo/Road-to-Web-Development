# JavaScript Questions
### What is JavaScript?
JavaScript is the most popular web scripting language, used for both client-side and server-side development. Supporting object-oriented programming abilities, the JavaScript code can be inserted into HTML pages that can be understood and executed by web browsers.

### Enumerate the differences between Java and JavaScript?
Java is a programming language, whereas JavaScript is essentially a scripting language. Developers use Java for building applications that can run in a virtual machine, an operating system, or inside a browser. Contrastingly, JS code is meant to run inside a browser only.

Nonetheless, standalone desktop applications can be built with JavaScript by using Electron and Node.js. Another important distinction between Java and JS code is that while the former requires compilation, the latter is available in a text format.

### Difference between Object Based Languages and Object Oriented Languages
**Object based languages**
- Object based languages supports the usage of object and encapsulation
- They does not support inheritance or, polymorphism or, both
- Object based languages does not supports built-in objects
- Javascript, VB are the examples of object bases languages

**Object oriented languages**
Object Oriented Languages supports all the features of Oops including inheritance and polymorphism
They support built-in objects
C#, Java, VB. Net are the examples of object oriented languages

### Could you enumerate the various features of JavaScript?
- A lightweight interpreted a programming language with some object-oriented capabilities.
- An open, cross-platform scripting language
- Complements and integrates with the Java programming language as well as other backend technologies.
- Designed especially for creating network-centric applications

### Describe the most important advantages of using JavaScript
- Enhanced interactivity – JavaScript allows creating interfaces that react when the user activates them via the keyboard or merely hovers the cursor over the same.
- Immediate feedback – Visitors need not wait for a page reload to see if they had forgotten to enter some important details.
- Low server interaction – JS allows validating user input before sending the webpage to the server. It means less server traffic and hence, less load on the server.
- Rich interfaces – JS has items like drag-and-drop components and sliders to present a richer interface to the website visitors.

### JavaScript Data Types
- Boolean – Represents true and false values.
- Null – Represents empty, nothing, and unknown type of values
- Number – Represents both integer and floating-point values.
- Object – Used for storing collections of data or more complex entities
- String – Represents single-character, multi-character, and alphanumeric values.
- Symbol – Used for creating unique identifiers for objects
- Undefined – Represents value not assigned. If a variable is only declared and not assigned in JS, it represents the undefined data type

### Explain Hoisting in javascript.
Hoisting is a default behaviour of javascript where all the variable and function declarations are moved on top

### Explain the use of debuggers in JavaScript
All modern browsers (Mozilla Firefox, Safari, Google Chrome, etc.) come with an inbuilt debugger that can be summoned by pressing the F12 key. You need to choose the Console tab to view the result. Here you can set breakpoints as well as view the value of the variables.

JavaScript also features a debugger keyword that replicates the function of using breakpoints using a debugger. However, it works only when the debugging option is enabled in the web browser settings.

### Explain the difference between function declaration and function expression
A function declared as a separate statement in the main code flow is termed the function declaration. When a function is created inside an expression or another syntax construct, it is called a function expression

### Is javascript a statically typed or a dynamically typed language?
JavaScript is a dynamically typed language. In a dynamically typed language, the type of a variable is checked during run-time in contrast to statically typed language, where the type of a variable is checked during compile-time

### Explain Higher Order Functions in javascript.
Functions that operate on other functions, either by taking them as arguments or by returning them, are called higher-order functions

### What is the use of isNaN function?
isNaN function returns true if the argument is not a number; otherwise, it is false

### What is negative Infinity?
Negative Infinity is a number in JavaScript which can be derived by dividing negative number by zero

### What are undeclared and undefined variables?
Undeclared variables are those that do not exist in a program and are not declared. If the program tries to read the value of an undeclared variable, then a runtime error is encountered

Undefined variables are those that are declared in the program but have not been given any value. If the program tries to read the value of an undefined variable, an undefined value is returned

### What are global variables? How are these variable declared?
Global variables are **available throughout the length of the code** so that **it has no scope**. The var keyword is used to declare a local variable or object. If the var keyword is omitted, a global variable is declared

The problems faced by using global variables are the clash of variable names of local and global scope. Also, it is difficult to debug and test the code that relies on global variables

### What are global variables? How are these variable declared?
Global variables are **available throughout the length of the code** so that **it has no scope**. The var keyword is used to declare a local variable or object. If the var keyword is omitted, a global variable is declared

### What are object prototypes?
All javascript objects inherit properties from a prototype.

- Date objects inherit properties from the Date prototype
- Math objects inherit properties from the Math prototype
- Array objects inherit properties from the Array prototype.

On top of the chain is Object.prototype. Every prototype inherits properties and methods from the Object.prototype.

A prototype is a blueprint of an object. Prototype allows us to use properties and methods on an object even if the properties and methods do not exist on the current object

### What is the use of a constructor function in javascript?
Constructor functions are used to create objects in javascript.
If we want to create multiple objects having similar properties and methods, constructor functions are used

### What is 'this' keyword in JavaScript?
'This' keyword refers to the object from where it was called
The value of “this” keyword will always depend on the object that is invoking the function. 

### What is the working of timers in JavaScript?
Timers are used to execute a piece of code at a set time or repeat the code in a given interval. This is done by using the functions **setTimeout**, **setInterval**, and **clearInterval**

The setTimeout(function, delay) function is used to start a timer that calls a particular function after the mentioned delay. The setInterval(function, delay) function repeatedly executes the given function in the mentioned delay and only halts when canceled. The clearInterval(id) function instructs the timer to stop

Timers are operated within a single thread, and thus events might queue up, waiting to be executed

### What is === operator?
=== is called a strict equality operator, which returns true when the two operands have the same value without conversion

### Difference between "==" and "==="?
"==" checks only for equality in value, whereas "===" is a stricter equality test and returns false if either the value or the type of the two variables are different

###  How you can submit a form using JavaScript?
To submit a form using JavaScript use
```sh
document.form[0].submit();
document.form[0].submit();
```

### Does JavaScript support automatic type conversion?
Yes, JavaScript does support automatic type conversion. It is the common way of type conversion used by JavaScript developers

### How to read and write a file using JavaScript?
There are two ways to read and write a file using JavaScript
Using JavaScript extensions
Using a web page and Active X objects

### What are all the looping structures in JavaScript?
For, while, do-while loops

### What is called Variable typing in Javascript?
Variable typing is used to assign a number to a variable. The same variable can be assigned to a string
```sh
i = 10;
i = "string"
```

### How can you convert the string of any base to an integer in JavaScript?
The **parseInt()** function is used to convert numbers between different bases. parseInt() takes the string to be converted as its first parameter. The second parameter is the base of the given string

### What is the function of the delete operator?
The delete keyword is used to delete the property as well as its value.
```sh
var student= {age:20, batch:"ABC"};
Delete student.age
```

### What is recursion in a programming language?
Recursion is a technique to iterate over an operation by having a function call itself repeatedly until it arrives at a result. 

### What is an undefined value in JavaScript?
- Variable used in the code doesn't exist
- Variable is not assigned to any value
- Property does not exist

### What are all the types of Pop up boxes available in JavaScript?
Alert, confirm, prompt

### What is the use of Void (0)?
Void(0) is used to prevent the page from refreshing, and parameter "zero" is passed while calling

### What is the data type of variables in JavaScript?
All variables in JavaScript are object data types

### What do you understand by cookies? How will you create, read, and delete a cookie using JavaScript?
A cookie is simply data, usually small, sent from a website and stored on the user’s computer by the web browser used to access the website. It is a reliable way for websites to remember stateful information and record the user's browsing activity.

The most basic way of **creating a cookie** using JS is to assign a string value to the document. Cookie object. The general syntax is:
```sh
document.cookie = “key1 = value1; key2 = value2; … ; keyN= valueN; expires = date”;
```
**Reading a cookie** using JS is as simple as creating the same. As the value of the document. Cookie object is the cookie, use this string whenever you wish to access the cookie.

The document.cookie string keeps a list of name = value pairs, where a semicolon separates each pair. The name represents a cookie's name, and the value represents the respective cookie’s string value. For breaking the string into key and value, you can use the split() method.

**Deleting a cookie** using JavaScript, simply set the expiration date (expires) to a time that’s already past. Some web browsers don’t let you delete a cookie unless you don’t specify the cookie's path. Hence, defining the cookie path is important to ensure that the right cookie is deleted

### What is a pop()method in JavaScript?
The pop() method is similar to the shift() method, but the difference is that the Shift method works at the array's start. The pop() method takes the last element off of the given array and returns it

### What are the disadvantages of using innerHTML in JavaScript?
innerHTML content is refreshed every time and thus is slower. There is no scope for validation in innerHTML. Therefore, it is easier to insert rogue code in the document and make the web page unstable

### What is break and continue statements?
Break statement exits from the current loop
Continue statement continues with next statement of the loop

### What are the two basic groups of data types in JavaScript?
- They are as—Primitive
- Reference types
Primitive types are number and Boolean data types. Reference types are more complex types like strings and dates

### How can generic objects be created?
```sh
var i = new Object()
```

### What is the use of a type of operator?
'Typeof' is an operator used to return a string description of the type of a variable

### Which keywords are used to handle exceptions?
Try… Catch---finally is used to handle exceptions in the JavaScript

```sh
Try{
    Code
}
Catch(exp){
    Code to throw an exception.
}
Finally{
    Code runs either it finishes successfully or after catch
}

```

### What are the different types of errors in JavaScript?
There are three types of errors:

- Load time errors: Errors that come up when loading a web page, like improper syntax errors, are known as Load time errors and generate the errors dynamically
- Runtime errors: Errors that come due to misuse of the command inside the HTML language
- Logical Errors: These are the errors that occur due to the bad logic performed on a function with a different operation

### What is the use of the Push and Unshift methods in JavaScript?
The **push** method is used to **add** or append one or more **elements to an Array end**. Using this method, we can append multiple elements by passing multiple arguments.

**Unshift** method is like the push method, which **works at the beginning of the array**. This method is used to prepend one or more elements to the beginning of the array

### How are object properties assigned?
```sh
obj ["class"] = 12;
or
obj.class = 12;
```

### What do you understand by Closures in JavaScript?
Closures provide a better, concise, creative, and expressive writing code for JavaScript developers and programmers. Technically speaking, closures are a combination of lexical environment and function.

In other words, a closure is a locally declared variable that is related to a function and stays in the memory when the related function has returned. The closure contains all local variables that were in-scope at the time of the closure creation

### How can you import all exports of a file as an object in JavaScript?
To import all exported members of an object, one can use:

*import * as object name from ‘./file.js.’*

The exported methods or variables can be easily accessed by using the dot (.) operator

### How can the OS of the client machine be detected?
The **navigator.appVersion** string can be used to detect the operating system on the client machine

### What is a window.onload and onDocumentReady?
The **onload** function is **not run until all the information on the page is loaded**. This leads to a substantial delay before any code is executed

**onDocumentReady loads the code just after the DOM is loaded**. This allows early manipulation of the code

### What is for-in loop in Javascript?
The for-in loop is used to loop through the properties of an object

The for-in loop is meant to be used for looping through the properties of a JavaScript object—every iteration of the loop results in a property of the object getting associated with the variable name. The loop continues until all the object properties are exhausted
```sh
for (variable name in object){
    statement or block to execute
} 
```
In each repetition, one property from the object is associated with the variable name. The loop is continued till all the properties of the object are depleted

### What is event bubbling?
JavaScript allows DOM elements to be nested inside each other. In such a case, if the handler of the child is clicked, the handler of the parent will also work as if it were clicked too

There are two ways for accomplishing event propagation and the order in which an event is received in the HTML DOM API.

These are Event Bubbling and Event Capturing. The event is directed towards its intended target in the former, whereas the event goes down to the latter element.

- Event Capturing – Also known as trickling, Event Capturing is rarely used. The process starts with the outermost element capturing the event and then propagating it to the innermost element.
- Event Bubbling – In this process, the event gets handled by the innermost element first and then propagated to the outermost element

### Is JavaScript case sensitive? Give its example.
Yes, JavaScript is case-sensitive

### What boolean operators can be used in JavaScript?
The 'And' Operator (&&), 'Or' Operator (||), and the 'Not' Operator (!) can be used in JavaScript

### How are DOM utilized in JavaScript?
DOM stands for Document Object Model and is responsible for how various objects in a document interact with each other. DOM is required for developing web pages, which includes objects like paragraphs, links, etc. These objects can be operated to include actions like add or delete. DOM is also required to add extra capabilities to a web page

DOM is a programming interface for HTML and XML documents.

When the browser tries to render a HTML document, it creates an object based on the HTML document called DOM. Using this DOM, we can manipulate or change various elements inside the HTML document

### How are event handlers utilized in JavaScript?
Events are the actions that result from activities, such as clicking a link or filling a form by the user. An event handler is required to manage the proper execution of all these events. Event handlers are an extra attribute of the object. This attribute includes the event's name and the action taken if the event takes place

### How can JavaScript codes be hidden from old browsers that do not support JavaScript?
```sh
Add "<!--" without the quotes in the code just after the <script> tag.
Add "//-->" without the quotes in the code just before the <script> tag
```

### JavaScript Array Methods
The Array object has many properties and methods which help developers to handle arrays easily and efficiently. You can get the value of a property by specifying arrayname.property and the output of a method by specifying arrayname.method().
- length property --> If you want to know the number of elements in an array, you can use the length property.
- prototype property --> If you want to add new properties and methods, you can use the prototype property.
- reverse method --> You can reverse the order of items in an array using a reverse method.
- sort method --> You can sort the items in an array using sort method.
- pop method --> You can remove the last item of an array using a pop method.
- shift method --> You can remove the first item of an array using shift method.
- push method --> You can add a value as the last item of the array.

### What is OOPS Concept in JavaScript?
Many times, variables or arrays are not sufficient to simulate real-life situations. JavaScript allows you to create objects that act like real-life objects. A student or a home can be an object that has many unique characteristics of its own. You can create properties and methods for your objects to make programming easier. If your object is a student, it will have properties like the first name, last name, id, etc., and methods like calculating rank, change address, etc. If your object is a home, it will have properties like a number of rooms, paint color, location, etc. The methods like to calculate area, change owner, etc

### What is JavaScript Unit Testing, and what are the challenges in JavaScript Unit Testing?
JavaScript Unit Testing is a testing method in which JavaScript tests code written for a web page or web application module. It is combined with HTML as an inline event handler and executed in the browser to test if all functionalities work fine. These unit tests are then organized in the test suite

Every suite contains several tests designed to be executed for a separate module. Most importantly, they don't conflict with any other module and run with fewer dependencies on each other (some critical situations may cause dependencies)

### What is the rest parameter and spread operator?
Both rest parameter and spread operator were introduced in the ES6 version of javascript.

**Rest parameter**
It provides an improved way of handling parameters of a function.
Using the rest parameter syntax, we can create functions that can take a variable number of arguments.
Any number of arguments will be converted into an array using the rest parameter.
It also helps in extracting all or some parts of the arguments.
Rest parameter can be used by applying three dots (...) before the parameters.
```sh
function extractingArgs(...args){
  return args[1];
}
```
**Spread operator**
Although the syntax of spread operator is exactly the same as the rest parameter, spread operator is used to spread an array, and object literals. We also use spread operators where one or more arguments are expected in a function call
The … spread operator is useful for many different routine tasks in JavaScript, including the following:
- Copying an array
- Concatenating or combining arrays
- Using Math functions
- Using an array as arguments
- Adding an item to a list
- Adding to state in React
- Combining objects
- Converting NodeList to an array

### What is the use of promises in javascript?
Promises are used to handle asynchronous operations in javascript.

Before promises, callbacks were used to handle asynchronous operations. But due to limited functionality of callback, using multiple callbacks to handle asynchronous code can lead to unmanageable code.

Promise object has four states
- Pending - Initial state of promise. This state represents that the promise has neither been fulfilled nor been rejected, it is in the pending state.
- Fulfilled - This state represents that the promise has been fulfilled, meaning the async operation is completed.
- Rejected - This state represents that the promise has been rejected for some reason, meaning the async operation has failed.
- Settled - This state represents that the promise has been either rejected or fulfilled.

A promise is created using the Promise constructor which takes in a callback function with two parameters, resolve and reject respectively

**resolve** is a function that will be called, when the async operation has been successfully completed.
**reject** is a function that will be called, when the async operation fails or if some error occurs.

Promises are used to handle asynchronous operations like server requests, for the ease of understanding, we are using an operation to calculate the sum of three elements

**then()** method is used to access the result when the promise is fulfilled.
**catch()** method is used to access the result/error when the promise is rejected

### What are classes in javascript?
Introduced in the ES6 version, classes are nothing but syntactic sugars for constructor functions.
They provide a new way of declaring constructor functions in javascript

Unlike functions, classes are not hoisted. A class cannot be used before it is declared.
A class can inherit properties and methods from other classes by using the extend keyword.
All the syntaxes inside the class must follow the strict mode(‘use strict’) of javascript. Error will be thrown if the strict mode rules are not followed.

### What is Object Destructuring?
Object destructuring is a new way to extract elements from an object or an array
```sh
const arr = [1, 2, 3, 4];
const [first,second,third,fourth] = arr;

console.log(first); // Outputs 1
console.log(second); // Outputs 2
console.log(third); // Outputs 3
console.log(fourth); // Outputs 4
```

### JavaScript Objects
JavaScript objects are containers for named values called properties or methods.
**Objects are variables too. But objects can contain many values.
The values are written as name : value pairs**

**The name:values pairs in JavaScript objects are called properties**

**Objects can also have methods. Methods are actions that can be performed on objects.
Methods are stored in properties as function definitions**


*In JavaScript, objects are king. If you understand objects, you understand JavaScript.*
*A JavaScript object is a collection of named values*

### Prototypes
All JavaScript objects inherit properties and methods from a prototype
- Date objects inherit from Date.prototype
- Array objects inherit from Array.prototype
- Person objects inherit from Person.prototype
The Object.prototype is on the top of the prototype inheritance chain