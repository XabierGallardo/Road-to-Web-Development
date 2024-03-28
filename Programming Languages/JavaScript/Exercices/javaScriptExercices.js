/*1.	Given a positive integer, write a function to check if it's a power of 2:
 * Examples: 8=>true, 15=>false, 32=>true*/

//Solution 1
function isPowerOfTwo(x) {
	if(x === 0) {
		return false;
	} if(x%2 === 0) {
		return true;
	} else {
		return false;
	}
}

//Solution 2
function isPowerOfTwo(x) {
	var division = x/2;
	var solution = Number.isInteger(division);
	if(solution === true) {
		return true;
	}else{
		return false;
	}
}


/////////////////////////////////////////////////////////////////////

/*2.	Write a function to print the first 100 elements of the sequence 1, 3, 4, 13, 53, 690*/
var sequence = [1,3];

function mySequence() {
	for (var i = 0; i < 101	; i++) {
        var a = sequence[sequence.length -2];
        var b = sequence[sequence.length -1];
        var c = (a * b) + 1;
        sequence.push(c);
        console.log(sequence[i]);
    }
}

mySequence();


/////////////////////////////////////////////////////////////////////

/*3.	Given a string, write a function to print all possible permutations.
Example: ABC => ABC ACB BAC BCA CAB CBA*/
function permut(string) {
	var results = [];

	if(string.length < 2) {
		return string;
	}

	for(var i = 0; i < string.length; i++) {
		var firstChar = string[i];
		var charsLeft = string.substring(0,i) + string.substring(i+1);
		var innerPermutations = permut(charsLeft);

		for(var j = 0; j < innerPermutations.length; j++) {
			results.push(firstChar + innerPermutations[j]);
		}
	}
	return results;
}

permut("ABC"); // "ABC", "ACB", "BAC", "BCA", "CAB", "CBA" ]



/////////////////////////////////////////////////////////////////////

/*4.	Given a String, reverse the whole string without reversing the individual words in it.
 * Example: "my favourite film is the lord of the rings" => "rings the of lord the is film favourite my"*/
var string = "my favourite film is the lord of the rings";

var separate = string.split(" ");

var reverse = separate.reverse();

console.log(reverse); //"rings", "the", "of", "lord", "the", "is", "film", "favourite", "my"


/////////////////////////////////////////////////////////////////////

/*5.	Remove Duplicates 	*/


function findDuplicates(text) {
  
  let formated = text.toLowerCase().split('');
  console.log(formated); //["t","e","s","t"]
  
  let unique = formated.filter((value, index) => {
    return formated.indexOf(value) === index;
  });
  console.log(unique); //Tes
}
findDuplicates("Test");


/////////////////////////////////////////////////////////////////////

/*6.	Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice*/


/////////////////////////////////////////////////////////////////////

/*7.	ATM machines allow 4 or 6 digit PIN codes
PIN codes cannot contain anything but exactly 4 digits or exactly 6 digis
Is the function is passed a valid PIN string return true, else return false*/

function validatePIN (pin) {

  if(typeof(pin) !== 'number' && isNaN(pin[0]) === true) {
    return false;
  } else if (pin.length === 4 || pin.length === 6) {
    return true;
  } else {
    return false;
  }
}


/////////////////////////////////////////////////////////////////////

/*8.	PALINDROMES
Create an algorith to return if an string is a palindrome	*/

function palindrome(palabra) { 
  //split: sofa -> s, o, f, a
  //reverse: a, f, o, s
  //join: afos
  let reverse = palabra.split('').reverse().join('');
  if(palabra == reverse) {
    console.log('It\'s a palindrome: ' + palabra + " = " + reverse); 
  } else {
    console.log('It\'s not a palindrome: ' + palabra + " = " + reverse);
  }
}
palindrome("oso");


/////////////////////////////////////////////////////////////////////

/*9.	JavaScript 6 / 1 of 5
What would be the output of the code given below?
True, False, TypeError, SyntaxError*/
const plus =+0;
const minus = -0;
const result = plus === minus;

//Returns TRUE


/////////////////////////////////////////////////////////////////////

/*10.	JavaScript 6 / 2 of 5
You have an array of strings as shown.
How will you create a new array with no duplicates?

- sports.filter(sp => sp.unique())	// sp.unique is not a function
- [...sports]												// Copy the same array
- [...new Set(sports)] 							// Removes duplicates!
- Array.from(new Set(sports))				// Removes duplicates!
*/

var sports = ["baseball", "basketball", "hockey", "baseball", "running", "basketball"];

// The object Set allows to store unique values of any kind, even primitive values or references to objects!


/////////////////////////////////////////////////////////////////////

/*11.	JavaScript 6 / 3 of 5
ES6 Arrow functions are best used as non-method functions
Explain why they aren't very useful when used as method functions, like in the example below

- They don't have their own bindings to this or super
- They don't have their own scope
- They can't be results
- They can't be defined inside an object
*/

var object = { x:1,
	printXarrow: () => console.log(this.i, this);
};
printXarrow logs(undefined, window);


/////////////////////////////////////////////////////////////////////

/*12.	JavaScript 6 / 4 of 5
Given the next code snippet*/
let target = {
	qux: "Welcome, qux"
}

let proxy = new Proxy(target, {
	get(receiver, name) {
		return name in receiver ? receiver[name]: `Hello, ${name}`
	}
})

proxy.qux === "Welcome, qux"
proxy.world === "Hello, world"

/*There are two statements
S1: This snipped is used for hooking into runtime-level object meta-operations
s2: There is no equivalent in ES5 for this operation

s1 is correct and s2 is correct
s1 is correct and s2 is incorrect
s1 is incorrect and s2 is correct
s1 is incorrect and s2 is incorrect*/


/////////////////////////////////////////////////////////////////////

/*13.	JavaScript 6 / 5 of 5
We have declared a data array in the below code
Choose the missing code to search the "7" number using the below code*/
let data = [10,20,7,50,1,100];
let result = (item) {
	return item < 10;
}
console.warn(result);

//data.find(function
//data.search(function
//data.find
//data.find(7)


/////////////////////////////////////////////////////////////////////

/*14. Write the FizzBuzz algorith which returns an array of strings from 1 to N, but
	- For multiples of 3, prints "Fizz"
	- For multiples of 5, prints "Buzz"
	- For multiples of both 3 and 5 prints "FizzBuzz"
The function takes an integer N as a parameter and returns the FizzBuzz sequence as an array os strings up to index N.Examples:

Input: 2
Output: 1,2

Input: 5
Output: 1,2,Fizz,4,Buzz

Input: 9
Output: 1,2,Fizz,4,Buzz,Fizz,7,8,Fizz

Input: 15
Output: 1,2,Fizz,4,Buzz,Fizz,Bizz,11,Fizz,13,15,FizzBuzz*/

function fizzbuzz(input) {
	let result = [];
	for(let i = 1; i <= input; i++) {
	
		if (i % 3 === 0 && i % 5 === 0) {
			result.push("FizzBuzz");
		} else if (i % 3 === 0) {
			result.push("Fizz");
		} else if (i % 5 === 0) {
			result.push("Buzz");
		} else {
			result.push(i);
		}
	}
	console.log(result);
}

fizzbuzz(2);
fizzbuzz(5);
fizzbuzz(9);
fizzbuzz(15);


/////////////////////////////////////////////////////////////////////


/*15. Export a list of student records in comma separated values (CSV) format.
The student records are imported from a database in JSON format. It contains student details such as studentID, name, etc.

The function formatRecords parses the students records and returns a comma separated string to be subsequently exported to CSVa. The function accepts an array containing a JSON encoded list of student objects. It should return a list of only graduating students for whom the student IDs are available.
Each item in the list should be separated from th enex item by a comma followed by a space, like:

Input:
[
	'{
		"studentId": 20,
		"name": "chad west",
		"graduating": true
	}',
	'{
		"studentId": 23,
		"name": "jake paul",
		"graduating": true
	}',
	'{
		"studentId": 21,
		"name": "brad stanly",
		"graduating": false
	}',
]

Output: "chad west, jake paul"

The function uses the map, reduce and filter functions*/

let receivedData = `
	[
		{
			"studentId": 20,
			"name": "chad west",
			"graduating": true
		},
		{
			"studentId": 23,
			"name": "jake paul",
			"graduating": true
		},
		{
			"studentId": 21,
			"name": "brad stanly",
			"graduating": false
		},
		{
			"studentId": 7530,
			"name": "Robert Lee",
			"graduating": true
		},
		{
			"name": "Carli B.",
			"graduating": false
		},
		{
			"studentId": 6679,
			"name": "Jacqui Ostermann",
			"graduating": true
		},
		{
			"studentId": 8357,
			"name": "Abeke Teka",
			"graduating": true
		}
	]
`;

let myJson = JSON.parse(receivedData);

function formatRecords(studentsRecords) {
	let graduating = myJson
		.filter(student => student.hasOwnProperty("studentId") && student.graduating === true)
		.map(student => student.name)
		.toString();

	
	return console.log(graduating)
}

formatRecords()
