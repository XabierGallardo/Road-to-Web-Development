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
```javascript
const { name, email } = user;

const { name, email, address: {city} } = user;
```


## Concept of Components & State
UIs are broken up into individual components of which have some sort of state associated with them
- Each component can have its own data & state of being
For example, a menu component that has a state of "open" or a state of "closed"
In a form we have a state that would be the text that is typed in, and everytime we write, it changes that state
- We also have application level state, usually implemented using a state manager like Redux, Vuex, etc
- Nested components (Parent & children)
We can nest child components wew we can nest and pass properties down
- Can be directly inserted or used in a router


## Spread Operator (...) 
State is usually immutable, meaning we cannot simply change it, we need to make a copy
The spread operator allows us to do that
```javascript
const userState = {
	name: 'John'
}

const new UserState = {

	// Gives us whatever is inside of userState and adds the age to it
	...userState,

	age: 30
}
```


## High Order Array Functions
Functions like forEach(), map(), filter() are used all the time to iterate through and manipulate data
*See highOrderFunctions.md lesson*
- **forEach()** - Basic iteration/looping, it doesn't return anything
- **map()** - Manipulating the data to create a new array from another array
- **filter()** - Used to filter out certain pieces of data. Used a lot in state reducers

```javascript
const companies = [
	{name: "Company One", category: "Finance", start: 1981, end: 2003},
	{name: "Company Two", category: "Retail", start: 1992, end: 2008},
	{name: "Company Three", category: "Auto", start: 1999, end: 2007},
	{name: "Company Four", category: "Retail", start: 1989, end: 2010},
	{name: "Company Five", category: "Technology", start: 2009, end: 2014},
	{name: "Company Six", category: "Finance", start: 1987, end: 2010},
	{name: "Company Seven", category: "Auto", start: 1986, end: 1996},
	{name: "Company Eight", category: "Technology", start: 2011, end: 2016},
	{name: "Company Nine", category: "retail", start: 1981, end: 1989}
];

const ages = [33, 12, 20, 16, 5, 54, 21, 44, 61, 13, 15, 45, 25,64, 32];
```

#### forEach()
forEach loop is a better way to loop through an array rather than using a for loop
```javascript
companies.forEach(function(company) {

	console.log(company);

});
```
**function(***currentValue, index, arr***)**

- *currentValue*: Required, the value of the current element
- *index*: Optional, the array index of the current element
- *arr*: Optional, The array object the current element belongs to

```javascript
// Another example of forEach, updating the value with 10 times the original value

let numbers = [65, 44, 12, 4];

numbers.forEach(myFunction);

function myFunction(item, index, arr) {

	arr[index] = item * 10; # 650 440 120 40

// Looking at each individual value

	console.log(item); # 65 44 12 4

	console.log(index); # 0 1 2 3

	console.log(arr); # [65,44,12,4] x 4
}
```

#### filter()
filter allows to filter things out from the array
Lets get the ages that are 21 and over
```javascript
// filter example
const canDrink = ages.filter(function(age) {

	if(age >= 21) {

		return true;
	}
});

console.log(canDrink);


// filter example using ES6 arrow functions
const canDrink = ages.filter(age => age >= 21); # Same output!
```

Now filtering retail companies
```javascript
const retailCompanies = companies.filter(function(company) {

	if(company.category === 'Retail') {

		return true;
	}
});

console.log(retailCompanies); #Returns three object in our array, Company Two, Company Four and Company Nine

// ES6 arrow function
const retailCompanies = companies.filter(company => company.category === 'Retail'); # Same result!
```

Filtering 80's companies
```javascript
const eightiesCompanies = companies.filter(company => (company.start >= 1980 && company.start < 1990));
```

Getting the companies that lasted at least 10 years
```javascript
const lastedTenYears = companies.filter(company => (company.end - company.start >= 10));

console.log(lastedTenYears);
```


#### map()
Map works differently, instead of just filtering things out, we can create new arrays of anything from a current array

We'll grab all the company names and put them into their own array
```javascript
// Create array of company names

const companyNames = companies.map(function(company) {

	return company.name; 
});

console.log(companyNames); # Returns an array of all the company names

const testMap = companies.map(function(company) {

	return `${company.name} [${company.start} - ${company.end}]`;
});

console.log(testMap); # Returns an array and each value has this format: Company One [1981 - 2003] ...


// Using ES6 arrow functions
const testMap = companies.map(company => `${company.name} [${company.start} - ${company.end}]`;);
```

An example using the ages array
```javascript
// Storing the square root values

const agesSquare = ages.map(age => Math.sqrt(age));

console.log(agesSquare);


// Multiplying each one by 2
const agesTimesTwo = ages.map(age => age * 2);

console(ageTimesTwo);


// We could square the numbers and then multiplying them by 2

const ageMap = ages

	.map(age => Math.sqrt(age))

	.map(age => age * 2);

	console.log(ageMap);
```