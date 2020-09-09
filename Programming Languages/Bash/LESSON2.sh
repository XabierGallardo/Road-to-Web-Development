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


# Welcoming and calling to date function
greeting="Welcome"
user=$(whoami)
day=$(date +%A)

echo "$greeting back $user! Today is $day";
echo "Your Bash shell version is: $BASH_VERSION. Enjoy!";


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


# Create a file and then write onto that file
touch samp_file && vim samp_file

# Checks if directory exists, if not, create it
[ -d samp_dir ] || mkdir samp_dir


# Test some strings
str1=""
str2="Sad"
str3="Happy"
# Check if str1 is null
if [ "$str1" ]; then
	echo "$str1 is not null"
fi
# Check if string has a value or not
if [ -z "$str1" ]; then
	echo "str1 has no value"
fi
# Check two strings
if [ "$str2" == "$str3" ]; then
	echo "$str2 equals $str3"
elif [ "$str2" != "$str3" ]; then
	echo "$str2 is not equal to $str3"
fi

if [ "$str2" > "$str3" ]; then
	echo "$str2 is greater than $str3"
elif [ "$str2" < "$str3" ]; then
	echo "$str2 is less than $str3"
fi

# Another example
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


# Check files
file1="./test_file1"
file2="./test_file2"
# Check if exists
if [ -e "$file1" ]; then
	echo "$file1 exists"
fi
# Check if it's a normal file
if [ -f "$file1" ]; then
	echo "$file1 is a normal file"
fi
# Check if it's readable
if [ -r "$file1" ]; then
	echo "$file1 is readable"
fi
# Check if it's writable
if [ -w "$file1" ]; then
	echo "$file1 is writable"
fi
# Check if it's executable
if [ -x "$file1" ]; then
	echo "$file1 is executable"
fi
# Check if it's a directory
if [ -d "$file1" ]; then
	echo "$file1 is a directory"
fi
# Check if it's a symbolic line
if [ -L "$file1" ]; then
	echo "$file1 is a symbolic line"
fi
# Check if it's a named pipe
if [ -p "$file1" ]; then
	echo "$file1 is a named pipe"
fi
# Check if it's a network socket
if [ -S "$file1" ]; then
	echo "$file1 is a network socket"
fi
# Check if it's owned by the group
if [ -G "$file1" ]; then
	echo "$file1 is owned by the group"
fi
# Check if it's owned by the  user
if [ -O "$file1" ]; then
	echo "$file1 is owned by the user"
fi
