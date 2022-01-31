# Concurrency & Event Loop in JavaScript
JavaScript itself can only do one thing at one time, it can't make AJAX request while we're doing other code, it can't do a setTimeout while doing another code.

The reason why we can do things concurrently is because of the browser, which is more than just the runtime.
Any of the web APIs, when they're done they push the callback on to the task queue when it's done

## Event Loop
JavaScript has a runtime model based on an **event loop**, which is responsible for executing the code, collecting and processing events, and executing queue sub-tasks.

The event loop has to wait until the stack is clear before it can push the callback onto the stack
```sh
console.log("Hi");

setTimeout(function cb() {
    console.log("there");
});

console.log("reader!");

# Output
# Hi
# reader!
# there
```
All Web APIs works the same way, if we have an AJAX request to the URL with a callback, it will work the same way
```sh
console.log("Hi");

$.get('url', function cb(data) {
    console.log(data);
});

console.log("reader!");

# Output
# Hi
# reader!
# { "some" : "json" }
```
This is what happens when an **async call** happen


##  