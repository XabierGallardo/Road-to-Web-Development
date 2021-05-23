# JavaScript High Order Functions & Arrays
```sh
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


## forEach()
forEach loop is a better way to loop through an array rather than using a for loop
```sh
# Printing every iteration with a for loop

for(let i = 0; i < companies.length; i++) {

	console.log(companies[i]); # Returning the objects

	console.log(companies.name); #Company One Company Two...
}

# Using forEach
companies.forEach(function(company) {

	console.log(company);

});
```

**function(***currentValue, index, arr***)**

- *currentValue*: Required, the value of the current element
- *index*: Optional, the array index of the current element
- *arr*: Optional, The array object the current element belongs to

```sh
# Another example of forEach, updating the value with 10 times the original value

let numbers = [65, 44, 12, 4];

numbers.forEach(myFunction);

function myFunction(item, index, arr) {

	arr[index] = item * 10; # 650 440 120 40

# Looking at each individual value

	console.log(item); # 65 44 12 4

	console.log(index); # 0 1 2 3

	console.log(arr); # [65,44,12,4] x 4
}
```


## filter()
filter allows to filter things out from the array

Lets get the ages that are 21 and over
```sh
# for loop example
let canDrink = [];

for (let i = 0; i < ages.length; i++) {
	
	if(ages[i] >= 21) {
		
		canDrink.push(ages[i]);
	}
}

# filter example
const canDrink = ages.filter(function(age) {

	if(age >= 21) {

		return true;
	}
});

console.log(canDrink);


# filter example using ES6 arrow functions
const canDrink = ages.filter(age => age >= 21); # Same output!
```

Now filtering retail companies
```sh
const retailCompanies = companies.filter(function(company) {

	if(company.category === 'Retail') {

		return true;
	}
});

console.log(retailCompanies); #Returns three object in our array, Company Two, Company Four and Company Nine

# ES6 arrow function
const retailCompanies = companies.filter(company => company.category === 'Retail'); # Same result!
```

Filtering 80's companies
```sh
const eightiesCompanies = companies.filter(company => (company.start >= 1980 && company.start < 1990));
```

Getting the companies that lasted at least 10 years
```sh
const lastedTenYears = companies.filter(company => (company.end - company.start >= 10));

console.log(lastedTenYears);
```


## map()
Map works differently, instead of just filtering things out, we can create new arrays of anything from a current array

We'll grab all the company names and put them into their own array
```sh
# Create array of company names

const companyNames = companies.map(function(company) {

	return company.name; 
});

console.log(companyNames); # Returns an array of all the company names

const testMap = companies.map(function(company) {

	return `${company.name} [${company.start} - ${company.end}]`;
});

console.log(testMap); # Returns an array and each value has this format: Company One [1981 - 2003] ...


# Using ES6 arrow functions
const testMap = companies.map(company => `${company.name} [${company.start} - ${company.end}]`;);
```

An example using the ages array
```sh
# Storing the square root values

const agesSquare = ages.map(age => Math.sqrt(age));

console.log(agesSquare);


# Multiplying each one by 2
const agesTimesTwo = ages.map(age => age * 2);

console(ageTimesTwo);


# We could square the numbers and then multiplying them by 2

const ageMap = ages

	.map(age => Math.sqrt(age))

	.map(age => age * 2);

	console.log(ageMap);
```


## sort()
We'll sort the companies by the start year
```sh
const sortedCompanies = companies.sort(function(c1, c2) {
	
	if(c1.start > c2.start) {
	
		return 1;
	
	} else {
	
		return -1;
	}
});

console.log(sortedCompanies);


# Shorter form

const sortedCompanies = companies.sort((a, b) => (a.start > b.start ? 1 : -1))

console.log(sortedCompanies);
```
Sorting ages
```sh
# Sorting in ascending order

const sortAges = ages.sort((a, b) => a - b);

# Sorting in descending order

const sortAges = ages.sort((a, b) => b - a);

console.log(sortAges);
```


## reduce()
Adding all of the ages together
```sh
# for loop example
let ageSum = 0;

for(let i = 0; i < ages.length; i++) {

	ageSum += ages[i];
}

# Using reduce

const ageSum = ages.reduce(function(total, age) {

	return total + age;

}, 0);


# Shorter version

const ageSum = ages.reduce((total, age) => total + age, 0);

console.log(ageSum);
```
Get the total years for all companies
The range of all companies will add all those up

```sh
const totalYears = companies.reduce(function(total, company) {
	
	return total + (company.end - company.start);

	# We'll have to add that second parameter of zero
}, 0);


# Shorter way
const totalYears = companies.reduce((total, company) => total + (company.end - company.start), 0);

console.log(totalYears); # 119
```


## Combine Methods
```sh
const combined = ages
	
	.map(age => age * 2) # Returns an array of all the ages times 2

	# Now we have an unsorted array of all the ages

	.filter(age => age >= 40) # Filters anything that was under 40

	.sort((a, b) => a - b) # Sorts the results

	# Now we'll reduce to sort them all together
	
	.reduce((a, b) => a + b, 0); # Returns 798
```