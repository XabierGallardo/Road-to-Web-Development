# ES6 Spread Operator & Rest Operator

This operator allows expressions to be expanded in places where multiple arguments, elements or variables are expected

### Add the elements of an existing array into a new array
```javascript
var certsToAdd = ["Algorithms and Data Structures", "Front End Libraries"];
var certifications = ["Responsive Web Design", ...certsToAdd, "Data Visualization", "APIs and Microservices", "Quality Assurance and Information Security"];
console.log(certifications);
```

### Pass elements of an array as arguments to a function
```javascript
function addThreeNumbers(x, y, z) {
	console.log(x + y + z);
}
var args = [0, 1, 2];
addThreeNumbers(...args); //It'll ignore more than 3 args
```

### Copy arrays
```javascript
var arr = [1, 2, 3];
var arr2 = [...arr]; //copy previous array into a different one

arr2.push(4);
console.log(arr); //[1, 2, 3]
console.log(arr2); //[1, 2, 3, 4]
```

### Concatenate arrays
```javascript
var arr = [0, 1, 2];
var arr2 = [3, 4, 5];
arr1 = [...arr1, "This is a string", ...arr2]; // == arr1.concat(arr2)
console.log(arr1); //[0, 1, 2, "This is a string", 3, 4, 5]
```

### REST: condense multiple elements into an array
The rest operator collects multiple elements and condenses into a single array element

```javascript
function multiply(multiplier, ...theArgs) {
	return theArgs.map(function(element) {
		return multiplier * element; //multiplies each element of the args
	});
}
var arr = multiply(2, 1, 2, 3);
console.log(arr); //[2, 4, 6]
```
