
## Top 20 coding exercises for a JR JavaScript developer
### 1. Write a function that takes in an array of numbers and returns the sum of all the numbers.
```js
// 1. Write a function that takes an array of numbers and returns the sum of all the numbers
let arr1 = [1,2,3,4,5];

// Solution 1, for loop
let result = 0;
function for1(arr) {
	for(let i = 0; i < arr.length; i++) {
		result += arr[i];
	}
	return result;	// 15
}

// Solution 2, forEach
arr1.forEach(function (item) {
	result += item;	//15
});


// Solution 3, map
let result2 = 0;
arr1.map( n => result2 += n); // result2 = 15


// Solution 4, for of
let result3 = 0
for (let number of arr1) {
	result3 += number;	// result3 = 15
}
```

### 2. Write a function that takes in a string and returns the string reversed.
```js
// 2. Write a function that takes in a string and returns the string reversed
let str2 = "Hello world!";
let finalStr2 = str2.split('').reverse().join(''); // !dlrow olleH
```

### 3. Write a function that takes in an array of numbers and returns the largest number in the array.
```js
// 3. Write a function that takes in an array of numbers and returns the largest number in the array
let arr3 = [1,2,11,34,65,25,43,17];

// Solution 1, Math.max()
let res3 = Math.max(...arr3);	// 65


// Solution 2, for lop
function max3(arr) {
	let maxNum = 0;
	for(let i = 0; i < arr.length; i++) {
		if(arr[i] > maxNum) {
			maxNum = arr[i];
		}
	}
	return maxNum;	// 65
}
```

4. Write a function that takes in an array of numbers and returns a new array with only the even numbers.

5. Write a function that takes in a string and counts the number of vowels in the string.

6. Write a function that takes in an array of strings and returns a new array with only the strings that have more than 5 characters.

7. Write a function that takes in an array of numbers and returns the average of all the numbers.

8. Write a function that takes in a number and returns true if the number is prime, false otherwise.

9. Write a function that takes in an array of strings and returns the longest string in the array.

10. Write a function that takes in an array of numbers and returns a new array with the numbers sorted in ascending order.

11. Write a function that takes in a string and returns true if the string is a palindrome, false otherwise.

12. Write a function that takes in an array of numbers and returns the sum of all the positive numbers in the array.

13. Write a function that takes in a string and removes all whitespace from the string.

14. Write a function that takes in an array of numbers and returns the product of all the numbers.

15. Write a function that takes in two arrays and returns a new array with the elements that are common to both arrays.

16. Write a function that takes in a string and returns the string with all the vowels removed.

17. Write a function that takes in an array of numbers and returns the median of the numbers.

18. Write a function that takes in a string and returns the most common character in the string.

19. Write a function that takes in an array of numbers and returns a new array with only the numbers that are multiples of 3.

20. Write a function that takes in a string and returns the string with the characters in reverse order.


## Top 30 coding exercises for a SSR JavaScript developer
1. Write a function that takes in an array of numbers and returns the sum of all the numbers.

2. Create a function that sorts an array of numbers in ascending order.

3. Implement a function that returns the factorial of a given number.

4. Write a function that checks if a given number is a prime number.

5. Implement a function that finds the maximum number in an array.

6. Create a function that removes duplicates from an array.

7. Write a function that converts a string to uppercase.

8. Implement a function that reverses a string.

10. Write a function that checks if a string is a palindrome.

11. Create a function that finds the longest word in a string.

12. Implement a function that counts the number of vowels in a string.

13. Write a function that converts a number to its Roman numeral equivalent.

14. Create a function that calculates the area of a triangle.

15. Implement a function that checks if a given year is a leap year.

16. Write a function that sorts an array of strings in alphabetical order.

17. Create a function that generates a random number between two given numbers.

18. Implement a function that checks if a string contains a specific substring.

19. Write a function that capitalizes the first letter of each word in a sentence.

20. Create a function that calculates the average of an array of numbers.

21. Implement a function that converts a number to a binary number.

22. Write a function that generates a Fibonacci sequence up to a given number.

23. Create a function that finds the median of an array of numbers.

24. Implement a function that checks if a given string is an anagram.

25. Write a function that converts a string to camel case.

26. Create a function that checks if a number is a perfect square.

27. Implement a function that calculates the distance between two points on a coordinate plane.

28. Write a function that checks if a given string is a valid email address.

29. Create a function that sorts an array of objects based on a specific property.

30. Implement a function that calculates the factorial of a given number using recursion.