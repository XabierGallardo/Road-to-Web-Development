/*1.	Given a positive integer, write a function to check if it's a power of 2:
 * Examples: 8=>true, 15=>false, 32=>true*/

//Solution 1
function isPowerOfTwo(x) {
	if(x == 0) {
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




/*3.	Given a string, write a function to print all possible permutations.
 * Example: ABC=> ABC ACB BAC BCA CAB CBA*/

