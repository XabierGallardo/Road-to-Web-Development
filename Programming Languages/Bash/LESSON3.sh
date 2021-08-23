#!/bin/bash

# Read multiple values on our shell
read -p "Enter 2 numbers to sum separated by a space: " num1 num2
sum=$((num1+num2))
echo "$num1 + $num2" = $sum


# Entering input without being displayed
read -sp "Enter the secret code: " secret
if [ "$secret" == "password" ]; then
        echo "Enter"
else
        echo "Wrong password"
fi


# In case there is a whitespace, define a separation
OIFS="$IFS"
IFS=","

read -p "Enter 2 numbers to add separated by a comma: " num1 num2

# Parameter expansion to substitute any white space or commas
num1=${num1//[[:blank:]]/}
num2=${num2//[[:blank:]]/}

sum=$((num1+num2))
echo "$num1 + $num2 = $sum"

IFS="$OIFS"


# Parameter expansion
# To print a value but immediately put some characters after
name="User"
# ${} is a character expansion
echo "${name}'s computer"

# It substitutes the word dog for cat
samp_string="The dog climbed the tree"
echo "${samp_string//dog/cat}"

# Print value name, but if its value doesn't exists, set a default value
echo "I am ${name:=User}"

# Using case inside shell scripts
read -p "How old are you? :" age

case $age in
	[0-4])
		echo "Too young for school"
		;;
	5)
		echo "Go to Kindergarten"
		;;

	[6-9] | 1[0-8])
		grade=$((age-5))
		echo "Go to grade $grade"
		;;

	*)
		echo "You are too old for school"
		;;
# End of case line, same as if-fi
esac

can_vote=0
age=18
 ((age >= 18?(can_vote=1):(can_vote=0)))
 echo "Can Vote : $can_vote"
