# Node.js Basics
## What is Node.js?
Node.js is an open-source web development framework written in JavaScript
Node.js is a runtime that allows JavaScript running on the server
Used to build powerful, fast & scalable web apps
Uses an event-driven, non-blocking I/O model

Now it's possible to write a full stack in a single language!

#### Non-blocking I/O
When using traditional server-side technologies, like PHP and Apache
Each connection or request spawns a new thread which takes up system memory and eventually maxes out the memory load
So it needs to wait for one process to finish before starting and this works in it asynchronous way

Node.js operates on a single thread and uses non-bloking i/o calls which allows it to support tens of thousands of concurrent connections, held in an event loop, this is why it's called an event-driven system

- Works on a single thread using non-blocking I/O calls
- Support tens of thousands concurrent connections
- Optimizes throughput and scalability in web apps with many I/O operations
- This makes Node.js apps extremely fast and efficient


#### Event Loop
- Single-threaded
- Supports concurrency via events and callbacks
- **EventEmitter** class is used to bind events and event listeners
<p align="center">
        <img src="../../../Images/eventloop.png" alt="Event Loop">
</p>

The main idea is that with traditional server-side programming you would have to just wait for one task to finish before you can start the next
With Node.js it's on a single thread and you can have tens of thousands connections at once


## What can we build with Node.js?
- REST APIs & Backend apps
- Real-time services (chats, games, etc)
- Blogs, CMS, Social apps
- Utilities & Tools
- Anything that is not CPU-intensive


## What it is NPM / Node Package Manager?
- Node.js Package Manager
- Used to install node programs/modules
- Easy to specify and link dependencies
- Modules get installed into the "node_modules" folder
```sh
# It will install the Express module into a node modules folder
npm install express

# Installing modules globally, not only in just one directory
npm install -g express
```

## Popular Modules
- **Express** - Web development framework
- **Connect** - Extensible HTTP server framework
- **Socket.io** - Server side component for websockets
- **Pug/Jade** - Template engine inspired by HAML
- **Mongo/Mongoose** - Wrappers to interact with MongoDB
- **Coffee-Script** - CoffeeScript compiler
- **Redis** - Redis client library


## package.json
**package.json** is a really important file that is used in node packages and applications
- It goes in the root of your package/application
- Tells npm how your package is structured and what will do to install it
```sh
{
	"name": "mytasklist",
	"version": "1.0.0",
	"description": "Simple task manager",
	# main describes the file that it's the entry point of our application like index.js
	"main": "server.js",
	"author": "Johnny Melavo",
	"license": "ISC",
	"dependencies": {
		"body-parser": "^1.15.2",
		"express": "^4.14.0",
		"mongojs": "^2.4.0"
	}
}
```
We can create a package.json manually or we can run
```sh
npm init
```
With Node.js we can run the JavaScript files from the command line!


## Creating a basic web server
When we upload our PHP file to Apache, this takes care of all the requests
With Node.js is a little different, you have to create your own server

So we're gount yo build a simple server that's on the node.js website
```sh
# We're including a Node module that it's already including in the system (no need to install it)
const http = require('http');

# We're bringing the filesystem module
const fs = require('fs');

# We're working on our localhost so we'll use the loopback address
const hostname = '127.0.0.1'
const port = 3000;

fs.readFile('index.html', (err, html) => {

	if(err) {
		throw err;
	}

	const server = http.createServer((req, res) => {

		res.statusCode = 200;
		res.setHeader('Content-type', 'text/html');
		res.write(html);
		res.end();
	});

	server.listen(port, hostname, () => {

		console.log('Server started on port ' + port);
	});
});
```

**Now our server is running and parsing the HTML!**


# Understanding Node.js

## Step 1 Introduction
When we visit a URL on the internet, it points to your server
When the request is received we can use node to handle the requests and read a file from the server's filesystem
Then responds back to the client so they can view the HTML in the browser


## Step 2 Install Node
On a terminal
```sh
# Checking in node is installed
node -v

# If not, install it with NVM (Node Version Manager) github.com/nvm-sh/nvm
nvm install  12.16.3 #example
```


## Step 3 Hello World
One way to start our first steps in Node is with REPL
**REPL** stands for Read Eval Print Loop
When we type node into the command line, it allows us to run JavaScript code and will print out the results
```sh
node

> console.log("Hello World") # Hello World
```

But mostly we'll want to execute JavaScript code that lives in an actual file
The default entry point into a node.js app is the index.js file

On index.js
```sh
console.log("Hello World");
```

Now we can run from the terminal
```sh
node index.js # Hello World

# And because it's an index file, we can actually point to the parent directory
node . # Hello World
```


## Step 4 Events
Node.js is defined as an *asynchronous event-driven JavaScript runtime*
The runtime implements a thing called **event loop** just like a web browser does

This allows node to push intensive operations off to a separate thread, so only very fast non-blocking operations happen on the main thread

This is why  people call Node,  non-blocking, it's a design choice that makes node.js very suitable for things that require high throughput like real time apps, web servers, etc

So without a depper knowledge of those low-level details, we need to know how **events** and **callbacks** work

In most cases, we'll listen to events, events can come in many forms, but one example is on the process global
Before a node process finishes, it emits an event named exit, we can listen to this event using on an then register a callback function as the second argument

Where the event is exit and the callback is the function associated with it
When the exit event occurs node.js will run this function
```sh
process.on('exit', function(){

	// do something!
});
```

The functions isn't called the first time node.js sees it
Its only called after the exit event occurs at some point in the future

This event is built-int in node, but we can also create our own from scratch
```sh
# Importing an event emitter from the events module that is built into node
const { EventEmitter } = require('events');

# We can create a custom event emitter by instantiating the class
const eventEmitter = new EventEmitter();

# Then we'll register a callback that fires on the lunch event
eventEmitter.on('lunch', () => {

	console.log("I'm having a lunch!");
});

# Now the callback is registered, we can call it. This triggers our callback function
eventEmitter.emit('lunch'); # I'm having a lunch!
```

This event-driven style of programming is extremely useful when we have something that is CPU intensive


## Step 5 File System
Node has a built-int file system module called fs
It can read, write and delete files on the file system among other things
It also can do things in a blocking or non-blocking way

We'll create a *hello.txt* file
```sh
This is a text example!
```

In our JavaScript code, we'll import two functions from the file system module, **readFile** and **readFileSync**

**sync === blocking**
Anytime we see a function that ends in sync, think blocking, because it will need to finish all of its work before any of our other code can run

#### Blocking example
```sh
const { readFile, readFileSync } = require('fs');

# We can read a text file on node by passing the path to that file, then we'll specify the enconding as UTF-8
const txt = readFileSync('./hello.txt', 'utf8');

console.log(txt);

# This console.log won't run until after that file has been read
console.log("do this ASAP");

# RESULTS
# This is a text example!
# do this ASAP
```

#### Non-blocking example
Luckily we can make our code non-blocking by refactoring this to a callback

Inside the callback function we can access an error object if the operation fails, or when successful, the actual text from the file
```sh
const { readFile, readFileSync } = require('fs');


# We just add a callback function as the 3rd argument
const txt = readFileSync('./hello.txt', 'utf8', (err, txt) => {

	console.log(txt);
});

console.log("do this ASAP");

# RESULTS
# do this ASAP
# This is a text example!
```

The good thing about this is that even though the console log to the text file comes first in our script, it's not the thing that gets executed first

Node registers the callback, executes the rest of the script and then finally runs the callback when the file has been read

#### Promise example
Promises are also asynchronous and non-blocking and they tend to produce much cleaner code when compared to callbacks

We're importing read file from the promises namespace, this gives us a function that returns a promise when called

This code is much easier to read specially with many async calls in the same function
```sh
const { readFile } = require('fs').promises;

async function hello() {
	const file = await readFile('./hello.txt', 'utf8');
}
```

#### Modules & NPM
A module is nothing more than a JavaScript file that exports its code
Node has a bunch of built-in modules like **fs** and **events**
And there's a long list of other modules beyond that

The traditional way to import a module is tu use a **require()** function
Node also has a support for ES6 modules which use the import-export syntax (but most Node modules written in Vanilla JavaScript still use require)

We'll create a new file called *my-module.js*
We'll reference this module with module.exports and whatever we add inside, it will be available to use in the other file
```sh
# 
module.exports = {
	science: 'sociology'
}
```

On *index.js*
```sh
# We'll import our mode
const myModule = require('./my-module')
```

The primary place to use somebody else's code will be using NPM (Node Package Manager)
NPM is installed with Node and it's a tool we can use to install remote packages to use in our own code

On the terminal, we'll write **npm init** to create a **package.json file in the root of the application**
```sh
npm init -y
```

This **package.json** file contains metadata about our project, but most importantly, it keeps track of the dependencies that we use here

Now we'll use npm to install **express**
```sh
npm install express
```

Express is a minimal web application framework and one of the most popular third-party modules

Now, in our *package.json* file, it added Express to the dependencies and pegged to a specific version
This dependencies object allows us to manage multiple dependencies in a project and then reinstall them all at once on a different system

With this package installed, we can import it by name in our js code
With express, now we're ready to build a real full-stack application and deploy it to the cloud

Our server will live in a url, and when an user makes a request to this url in the browser the server will respond with some HTML

In our code, we'll first create an instance of an express app
**An express app allows us to create different URLs and endpoints that a user can navigate to in the browser**, and then we define code for the server to handle those requests

When an user navigates to a URL in the browser, it's what's known as a get request
This means they're requesting some data on the server and not trying to modify or update anything on the server

With express we can set up an endpoint by calling **app.get()**
```sh
const express = require('express');

const app = express();

# The first argument is the URL that the user will navigate to
# The second argument is the callback function
app.get('/foo/bar', (request, response) => {

	# We need to read some HTML from our file system and then send it back to the browser
	readFile('./home.html', 'utf8', (err, html) => {

		# If theres an error, we can handle that by sending a response
		if (err) {
			response.status(500).send('sorry out of order!')
		}

		# Now we send the response back down to the client
		response.send(html)
	});
});
```

We can think of every request to a URL as an event and then we handle that event with the function
- **request** - user's incoming data
- **response** - our outgoing data

Now we just need to tell our Express app to start listening to incoming requests
We do that by defining a port which will normally come from a node environment variable
```sh
app.listen(process.env.PORT || 3000, () => console.log('App available on http://localhost:3000'));
```

Now we can start it up on the terminal
```sh
node . # App available on http://localhost:3000
```

To avoid nested callbacks, it's recommended to use promises instead of callbacks
Instead of importing readFile from fs, we'll import it from fs.promises
```sh
const { readFile } = require('fs').promises;
```

We can make our callback function async and then we can write the response in a single line of code by saying response.send and then await the operation to read file

```sh
const { readFile } = require('fs').promises;

app.get('/', async (request, response) => {

	response.send( await readFile('./home.html', 'utf8') );

});
```