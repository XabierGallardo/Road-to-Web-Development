# Destructuring assignment
Destructuring consists in taking **values from arrays** or **properties from objects** and set them as **local variables**

JavaScript Destructuring is a technique that can make your javascript more concise and readable
```sh
# Old way
const arr = [1,2,3];
const one = arr[0];
const two = arr[1];

# New way
const [one, two] = [1,2,3];
```

### Array Destructuring
```sh
const arr = [':pizza:', ':hamburger:', ':fries:'];

const [pizza, hamburger, fries] = arr;


# Ommiting variables by adding a comma without a variable name
const [,, fries] = arr;


# Adding first couple variables, then putting a remainder in their own array
# We do this by adding ... in front of the variable name
const [pizza, ...rest] = arr; 


# Setting a default value in case the value is undefined
const arr = [undefined, ':hamburger:', ':fries:'];
# Using =
const [spaghetti=':spaghetti:', pizza, fries] = arr;
```

### Object Destructuring
```sh
const obj = {
	banana: ':banana:',
	strawberry: ':strawberry:',
	pineapple: ':pineapple:'
}


# We're dupplication the object's propery name as a variable with . notation
const banana = obj.banana;
const strawberry = obj.strawberry;
const pineapple = obj.pineapple;

# By putting {} after const, we can reference propery names which will automatically become local variables
const { banana, strawberry, pineapple } = obj;


# As we do with arrays, we can set a default value with =
const { banana=':palm_tree:'} = obj;


# In some cases we may want to use a different name than what's provided on the object itself
# We do this by using a : after property name allows to rename it, which is super useful when dealing with name collisions
const { banana: platano} = obj;

# Even with objects that use property names that are not valid variable names


# We can also use : to access nested properties
const obj = {
	parent: {
		child: 'baby'
	},
}

const { parent: { child } } = obj;
# Setting a variable from an object within an object
```


### Loops
In addition to destructuring top level variables, we can also use the syntax in for loops
which is specially useful when dealing with an array of objects
```sh
const users = [
	{ id: 1 },
	{ id: 2 },
	{ id: 3 }
];

for (const { id } of users) {

}
```

### Function args
We can destructure arrays and objects passed as arguments
```sh
const user = { id: 0, username: 'jeff' }

function haveFun( {id, username}) {
	console.log(`hi ${username}`);
}
```


### REGEX
We can also use destruturing with regular expressions REGEX
```sh
# When using the match function on a string it returns an array of results
var re = /\w+\s/g;

var str = "fee fi fo fum";

# We can provide descriptive variable names for the regular expression matches
const [fee, fi, fo] = str.match(re);
```


### Dynamic Properties
In cases in which we want to destructure an object but we don't know the propery name until runtime
We can use computed propery names in destructuring just like we can with object literals
```sh
const rando = randomKey();

const obj = {
	[rando]: 23
}

# By wrapping a propery name in brackets [] it now takes a variable as its value instead of a static name
const { [rando]: myKey } = obj;

# It's computed as runtime!
```