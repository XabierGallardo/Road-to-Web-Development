# JavaScript Call Stack

## Some basic concepts
The JavaScript engine (found in a hosting environment like the browser), is a single-threaded interpreter, it has a single call stack.
The browser provides web APIs like the DOM, AJAX and Timers.

The call stack is primarily used for function invocation (call). Since the call stack is single, function execution is done, one at a time, from top to bottom. It means the call stack is synchronous


## How does the call stack handle function calls?
```javascript
function firstFunction() {
	console.log("Hello from firstFunction");
}

function secondFunction() {
	firstFunction();
	console.log("The end from secondFunction");
}

// Output
// Hello from firstFunction
// The end from secondFunction
```


## The LIFO - Last In, First Out  principle
At the most basic level, a call stack is a data structure that uses the *Last In, First out* or *LIFO* principle to temporarily store and manage function invocation (call).
It means that the last function that gets pushed into the stack is the first to be pop out, when the function returns.

Same scenario as being on a queue in a grocery store cash point. You can only be attended to after the person in front of you have been ettended to. Which explains the synchronous concept on JavaScript


## What causes a stack overflow?
A stack overflow occurs when there is a recursive function (a function that calls itself) without an exit point.
The browser (hosting environment) has a maximum stack call that it can accomodate before throwing a stack error, for example:
```javascript
function callMyself() {
	callMyself();
}

callMyself();
```

The **callMyself()** will run until the browser throws a "Maximun call size exceeded", and that is a *stack overflow*


## In summary, key concepts from the call stack
1. It is single-threaded. meaning it can only do one thing at a time
2. Code execution is synchronous
3. A function invocation creates a stack frame that occupies a temporary memory
4. It works as a *LIFO* - Last In, First Out data structure
