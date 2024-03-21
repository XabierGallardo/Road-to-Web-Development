# Concurrency & Event Loop in JavaScript
## Some concepts
JavaScript has a **concurrency model** based on the **Event Loop**, which is responsible for executing the code, collecting and processing events and executing queued sub-tasks.

**Concurrency** means multiple computations happening at the same time or **concurrently**. Concurrency means executing multiple tasks at the same time but not necessarely simultaneously.
*Concurrency is everywhere in modern programming, whether we like it or not: Multiple computers in a network. Multiple applications running on one computer are in essence concurrent.*

**JavaScript is a single-threaded language. This thread is event-based and it responds to events when they occur**. So ho does it no block other functions form executing? Well it does, JavaScript comes with three features that allow us to run code concurrently
- **Callbacks**
- **Promises**
- **Async/Await**

*The JavaScript Event Loop relies on message passing concurrency to execute tasks present in the call stack in a non-blocking way*


## Callbacks
NodeJS is built for quick **I/O** operations. It makes heavy use of callbacks which come built in. **Callbacks are asynchronous functions** that call back after their execution completes. So in essence, the main thread receives an event which then makes it fire the handler function for the specific event.

The handler for the event delegates a task and starts procesing it while the main thread returns to listen for more events immediately. If another request comes in, the main thread will be able to intercept it even while the handler is still running its long process and the main thread will fire another handler function to execute while it listens for more events.

This makes Nodejs callback functions **non-blocking** and allows for asynchronous (concurrent) operations
```javascript
let callbackFunc = (arg, callback) => {
    let arr = [];
    for(i = 0; i < arg; i++>) {
        arr.push({name: 'User ${i+1}', id: i + 1});
    }
    callback(arr);
}

// An asynchronous callbackFunc that returns an array of 'n' objects where 'n' = arg
```


## Promises
A promise is an **object** that represents the eventual completion or failure of an asynchronous opreation like requesting data using the *fetch()* api
```javascript
let promise1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('success');
    }, 5000);
});

promise1.then(value => {
    console.log(value);
    // outputs 'success' after 5 seconds
}).catch(err => {
    console.log(err);
});

console.log(promise1);
// outputs [object Promise]
```
A promise is merely a proxy for an unkown value when the promise is created. This allows us to create statements that handle the eventual success value or failure reason of the promise.
This lets asynchronous methods values similar to synchronous methods that we can work with before the promise is returned at some point in future

A promise has 3 states
1. **Pending (pending)**: Initial state, neither fulfilled nor rejected. More of currently running at the moment
2. **Fulfilled (fulfilled)**: When the operation completes successfully
3. **Rejected (rejected)**: When the operation fails

A pending promise can either be fulfilled with a value or rejected with an error where the associated handlers queued up by a promise *then* method are called. The *catch* method can be used to call the handler when the promise is rejected where you can get the reason of failure


## Async functions (Async/Await)
The *async function()* defines an asynchronous function that returns an *AsyncFunction* object. This function operates asynchronously via the event loop using an implicit *Promise* to return a value. The only difference is that the syntax of async functions is more similar to synchronous functions than promises, so if you're more accustomed to synchronous code, async functions are the way to go for you

An async function can contain **await** expression that puases the execution of the async function and awaits for the passed promise resolution or rejection. It then resumes the *async* method and returns a resolved value
*The await keyword is only valud inside async functions, a SyntaxError will be raised if used outside async functions*
```javascript
var resolveAfter25Seconds = (func) => {
    console.log(`starting a slow promise on: ${func}`)
    return new Promise(resolve => {
        setTimeout(function() {
            resolve(25)
            console.log(`slow promise is done on: ${func}`)
        }, 25000)
    })
}

var resolveAfter1Second = (func) => {
    console.log(`Starting quick promise on: ${func}`)
    return new Promise(resolve => {
        setTimeout(function() {
            resolve(25)
            console.log(`quick promise is done on: ${func}`)
        }, 1000)
    })
}

var sequentialStart = async () => {
    console.log("---Sequential Start---")
    const slow = await resolveAfter25Seconds('sequential start')
    const fast = await resolveAfter1Second('sequential start')
    console.log(slow + ' - sequential start')
    console.log(fast + ' - sequential start')
}

var concurrentStart = async () => {
    console.log("--- Concurrent Start ---")
    const slow = resolveAfter25Seconds('concurrent start')
    const fast = resolveAfter1Second('concurrent start')
    console.log(await slow + ' - concurrent start')
    console.log(await fast + ' - concurrent start')
}

var stillSerial = () => {
    console.log("-- Concurrent with Promise.then -- ")
    Promise.all([resolveAfter25Seconds('still serial'), resolveAfter1Second('still serial')]).then(([slow, fast]) => {
        console.log(slow + ' - still serial')
        console.log(fast + ' - still serial')
    })
}

var parallel = () => {
    console.log("-- Parallel with promise.then")
    resolveAfter25Seconds('parallel').then(message => { console.log(message + ' - parallel') })
    resolveAfter1Second('parallel').then(message => { console.log(message + ' - parallel') })
}

sequentialStart()
setTimeout(function() {
    console.log('5 seconds later...')
    concurrentStart()
    }, 5000)
setTimeout(function() {
    console.log('10 seconds later...')
    stillSerial()
    }, 10000)
setTimeout(function() {
    console.log('15 seconds later...')
    parallel()
    }, 15000)


# ---Sequential Start---
# VM24:2 starting a slow promise on: sequential start
# 4
# VM24:53 5 seconds later...
# VM24:30 --- Concurrent Start ---
# VM24:2 starting a slow promise on: concurrent start
# VM24:12 Starting quick promise on: concurrent start
# VM24:16 quick promise is done on: concurrent start
# VM24:57 10 seconds later...
# VM24:38 -- Concurrent with Promise.then -- 
# VM24:2 starting a slow promise on: still serial
# VM24:12 Starting quick promise on: still serial
# VM24:16 quick promise is done on: still serial
# VM24:61 15 seconds later...
# VM24:46 -- Parallel with promise.then
# VM24:2 starting a slow promise on: parallel
# VM24:12 Starting quick promise on: parallel
# VM24:16 quick promise is done on: parallel
# VM24:48 25 - parallel
# VM24:6 slow promise is done on: sequential start
# VM24:12 Starting quick promise on: sequential start
# VM24:16 quick promise is done on: sequential start
# VM24:25 25 - sequential start
# VM24:26 25 - sequential start
# VM24:6 slow promise is done on: concurrent start
# VM24:33 25 - concurrent start
# # VM24:34 25 - concurrent start
# VM24:6 slow promise is done on: still serial
# VM24:40 25 - still serial
# VM24:41 25 - still serial
# VM24:6 slow promise is done on: parallel
# VM24:47 25 - parallel
```


## Some conclusions
Concurrent code is much better than sequential as its non blocking and can handle multiple users or events at the same time without any problem.
However, it is important to remember that JavaScript is only a viable option when fast input and output of data is required (gaming, social networking, videostreaming, instant messaging) and not recommended when it comes to heavy computing tasks. I would recommend Go for CPU intensive applications instead

A lot of problems arise when using sequential code, in todays world, everything is connected to the internet. This means your application might have to make some API calls every now and then. It's difficult to know how long it will take for the data to be processed and retieved, you wouldn't want your application to hang while it's loading your user's feed.

The event loop in NodeJS sort of runs your script over and over every time and event is detected. Since JS is single threaded, it offloads its operations mostly as callbacks in NodeJS thereby ensuring executions don't block each other while they are running. When a NodeJS app starts, the event loop is initialized, processes the script then begins processing the event loop


## Stack, Heap & Queue
JavaScript itself can only do one thing at one time, it can't make AJAX request while we're doing other code, it can't do a setTimeout while doing another code.

The reason why we can do things concurrently is because of the browser, which is more than just the runtime
Any of the web APIs, when they're done they push the callback on to the task queue when it's done
**Stack**
**Heap**
**Queue**

```javascript
function f(b) {
    var a = 12;
    return a + b + 35;
}

function g(x) {
    var m = 4;
    return f (m * x);
}

g(21);

// 131
```
1. When we call **g**, a first frame is created, which contains **g** arguments and local variables

2. When **g** call **f**, a second frame is created and put on top of the first, with **f** arguments and local variables

3. When **f** ends its execution, the last frame (f) is removed from the stack (leaving only g frame)

4. When **g** finish its execution, stack is empty

#### Stack
Function calls create a stack of frames. A **frame** encapsulates data such as the context and local variables of a function

#### Heap
The objects are stored in a stack, which refers to a big part of the memory

#### Queue
A program in execution in JavaScript contains a queue of messages, which is a list of messages to be processed
Every message is associated with a function
When the **stack** is **empty**, a message is removed from the queue and processed

Processing a message is basically calling the function associated with the message
The processed message ends when the stack is empty again


## Event Loop
JavaScript has a runtime model based on an **event loop**, which is responsible for executing the code, collecting and processing events, and executing queue sub-tasks.

The event loop has to wait until the stack is clear before it can push the callback onto the stack
```javascript
console.log("Hi");

setTimeout(function cb() {
    console.log("there");
});

console.log("reader!");

// Output
// Hi
// reader!
// there
```
All Web APIs works the same way, if we have an AJAX request to the URL with a callback, it will work the same way
```javascript
console.log("Hi");

$.get('url', function cb(data) {
    console.log(data);
});

console.log("reader!");

// Output
// Hi
// reader!
// { "some" : "json" }
```
This is what happens when an **async call** happen


#### setTimeout example
Let's see another example, when we write a setTimeout function is added to the queue after the specified delay in milisecs
```javascript
console.log("hello");

setTimeout(() => {
    console.log("delayed");
}, 100);
```
Hello gets logged because it's immediately added to the queue and since there is no other task waiting to be added to the queue except the one from setTimeout, which is added immediately, there is no 100ms delay guarantee that the message will be added to the queue, rather this is just a maximum delay if there are other messages in the queue waiting to be processed, however if this is not the case and there are no messages waiting in the queue, the task from the setTimeout is added immediately ignoring the delay


## The main problem of blocking the event loop
Considering the process from **Call Stack** to **Web Apis** to **Render Queue**, we must manage our JavaScript code to avoid blocking our entire app.

Basically if we write slow code on the stack, the browser can't do what it needs to do, which is create a nice fluid UI

This happens often when working with image processing or animating too many elements. We must then queue up the code

In the next example we can see how the scrolling event it's queuing up a ton of callbacks
```javascript
function animateSomething() {
    delay();
}

$.on('document', 'scroll', animateSomething);
```

Everytime we scroll, we add a ton of Callbacks to the Queue
In our **Callback Queue** we have a ton of queued events
```javascript
[scroll]
animateSomething()

[scroll]
animateSomething()

[scroll]
animateSomething()

[scroll]
animateSomething()

[scroll]
animateSomething()

// And so on
```

Our **Web API** is dealing with the event
```javascript
$.on('document','scroll', ...);
```

Our **Call Stack** is taking one by one every Callback from the queue
```javascript
// 1
[scroll]
animateSomething()

// 2
delay()
```