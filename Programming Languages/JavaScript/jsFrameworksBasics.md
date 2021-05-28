# JavaScript Frameworks Basics
Vanilla JavaScript concepts to understand JS Frameworks


## Modules
Modules are used to import files / pieces of code into another file
Without modules there would be no framework because it allows everything to be brought together
- ES6 Modules, TypeScript (Angular)
- Parcel, Webpack & Babel
- Export & Export Default


## Classes
Classes are used mostly in React & Angular
It's important to learn about classes & inheritance before learning a framework
- Structuring a class
- Constructors
- Methods & properties
- Instantiation
- Extending classes


## Arrow Functions
Much more compact and give advantages when it comes to scope in certain situations
- Much cleaner and short
- The standard in writing modern JS
- Scope & **"lexical this"**


## Promises / Asynchronous Requests
Many async requests/responses use promises as they are a better solution than callbacks
ES6 introduced promises as an alternative to using callbacks for asynchronous code

So if we make a request to a server or anything that could take a while, we want to do it asynchonously so that we can move on with our application and not have to stop and wait for a response

Promises do just that, they make a promise and then fulfill it when the task is done

- How to create and receive promises
- Standard **.then()** and **.catch()** syntax
- **Async / Await** is optional but recommended
- Fetch API for making HTTP requests


## Destructuring
Unpack values from objects and arrays
Used a ton in frameworks and makes for cleaner and more readable code
```sh
const { name, email } = user;

const { name, email, address: {city} } = user;
```


## Concept of Components & State
UIs are broken up into individual components of which have some sort of state associated with them
- Each component can have its own data & state of being
- We also have application level state, usually implemented using a state manager like Redux, Vuex, etc
- Nested components (Parent & children)
- Can be directly inserted or used in a router


## Spread Operator (...) 
State is usually immutable, meaning we cannot simply change it, we need to make a copy
The spread operator allows us to do that
```sh
const userState = {
	name: 'John'
}

const new UserState = {

	# Gives us whatever is inside of userState and adds the age to it
	...userState,

	age: 30
}
```


## High Order Array Functions
Functions like forEach(), map(), filter() are used all the time to iterate through and manipulate data
- **forEach()** - Basic iteration/looping
- **map()** - Manipulating the data to create a new array
- **filter()** - Used to filter out certain pieces of data. Used a lot in state reducers
