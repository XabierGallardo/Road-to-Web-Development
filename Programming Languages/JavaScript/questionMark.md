# ? The question mark
One of the most powerful characters in JavaScript
Providing syntactic sugar in three great ways

### Ternary Operator
Ternary means that it's composed of three parts
Using the ? as our strating place

*condition* **?** *true* **:** *false*

condition to test **?** value if true **:** value if false  

The operator if often used to replace a traditional if statement
```sh
(condition) ? truthyValue : falsyValue

# instead of
if (condition) {

	# Truthy value

} else {
	# Falsy value
}
```
As we see, the ternary expression is concise, but less readable than an if statement

But this changes when we need to assign a variable
A statement like **if** is imperative, it does something
```sh
# It begins with a state
let status;

# Then, as the program's is executed, it mutates the state
if (bankAccount > 100) {

	status = 'rich';

} else {

	status = 'poor';

}
# Takes multiple lines of code just to assign a variable based on a simple condition
```

The **ternary operator** creates an expression, which means that it produces a value that we can then assign to a variable
```sh
const status = bankAccount > 100 ? 'rich' : 'poor';
```
This code is declarative, it describes the state of a variable as opossed to mutating it
This is why we use *let* in the if example and *const* in the ternary operator example

**Declarative code** is great because it can also be used in function arguments and in array and object literals
```sh
# Functions
fun(cond ? a : b);

# Objects
const obj = {
	prop: cond ? a : b;
}

# Arrays
const arr = [
	cond ? a : b;
];
```


### Optional ? Chaining
In 2020 a new feature landed in JavaScript called optional chaining
This is very useful in cases when we call an object property that does not exists and then, it triggers an error
```sh
const user = {
	name: 'jeff'
}

user.write.code(); # Uncaugh TypeError

# This could be changed by adding

user && user.write && user.write.code();
```
But this is simplified just adding a **?** between the property name and the period between the next property
```sh
const user = {
	name: 'jeff'
}

user.write?.code(); # If it's undefined it'll return just undefined, it doesn't throw an error
```


### Nullish ?? Coalescing
In many cases, we want to set a default value for a missing variable or property name
We can do that with a **||** (logical OR operator) 
But to avoid errors with **||** because of JavaScript rules
```sh
const order = {

	amount: undefined || 23.99, # may return 0

	description: undefined || 'some product', # may return ''

# This sometimes may return an empty string or 0 being set to a default value
}
```

To avoid this error, we can substitute *||* with **??**
```sh
const order = {

	amount: 0 ?? 23.99,

	description: '' ?? 'some product',

	# It works like || except undefined null are the only values that short circuit to the right side
}
```

**value** ?? *default*

**preferred value** ?? *fallback value*

This makes our code much more predictable!