#!/bin/bash

# Define and calling a function
getDate() {
	date
	return
}
getDate


# Global & Local variables example
name="Derek"

demLocal(){
	local name="Paul"
	return
}
demLocal
echo "$name"


#Example of command and receiving values
getSum(){
	local num3=$1
	local num4=$2

	local sum=$((num3+num4))

	echo $sum
}
num1=5
num2=6

sum=$(getSum num1 num2)
echo "The sum is $sum"


# Read input from the user
# read -p "What is your name? " name
# echo "Hello $name"

# Conditionals (if)
read -p "How old are you? " age
if [ $age -ge 16 ]
then
	echo "You can drive"
elif [ $age -eq 15 ]
then
	echo "You can drive next year"
else
	echo "You can't drive"
fi

# eq= equal to / ne= not equal / le= less or equal to/ lt= less than / ge= greater or equal to/ gt= greater than


# Conditionals
read -p "Enter a number " num
if((num == 10)); then
	echo "Your number equals 10"
fi

if ((num >= 10)); then
	echo "It's greater than 10"
else
	echo "It is less than ten"
fi

if (( ((num % 2)) == 0)); then
	echo "It is even"
fi


# Logical Operators
if (( ((num > 0)) && ((num < 11)) ));
then
	echo "$num is between 1 and 10"
fi


# Comparisons
string_a="UNIX"
string_b="GNU"

echo "Are $string_a and $string_b strings equal?"
[ $string_a = $string_b ]
echo $?

num_a=100
num_b=100

echo "Is $num_a equal to $num_b?"
[ $num_a -eq $num_b ]
echo $?
