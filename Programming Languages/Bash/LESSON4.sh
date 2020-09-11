#!/bin/bash

# Parameters extensions & Strings
rand_str="A random string"

#Get the string length
echo "String Length : ${#rand_str}"

# Ask for an specific index
echo "${ramd_str:2}"

# Define a starting and ending index
echo "${ramd_str:2:7}"

# Get everything after letter A
echo "${rand_str#*A }"


# Looping

# While loops
num=1
# Less or equal to 10
while [ $num -le 10 ]; do
	echo $num
	num=$((num + 1))
done

num=1
while [ $num -le 20 ]; do
	if (( ((num % 2 )) == 0 )); then
		num=$((num + 1))
		continue
	fi

	if ((num > 15)); then
		break
	fi

	echo $num
	num=$((num + 1))
done


# A while-loop does something as long as the condition is true
# A until-loop is the opposite, does something until condition is true
num=1

until [ $num -gt 10 ]; do
	echo $num
	num=$((num+1))
done
