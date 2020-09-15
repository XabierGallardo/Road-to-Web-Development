#!/bin/bash

# Read, loop through and output information from a file 

# while loop
while read avg rbis hrs; do
	printf "Avg: ${avg}\nRBIs: ${rbis}\nHRs: ${hrs}\n"


done < barry_bonds.txt

# for loop
for (( i=0; i<=10; i=i+1)); do
	echo $i
done

# ranges of for loops
for i in {A..Z}; do
	echo $i
done


# Unidimensional arrays
# Don't put commas
fav_nums=(3.14 2.718 .57721 4.6692)
echo "Pi :  ${fav_nums[0]}"

# Add a value to an array
fav_nums[4]=1.618
echo "GR : ${fav_nums[4]}"

# Add a group of values to an array
fav_nums+=(1 7)
for i in ${fav_nums[*]}; do
	echo $i
done


# Output indexes
for i in ${fav_nums[@]}; do
	echo $i
done

# Get the number of items stored inside an array
echo "Array Length : ${#fav_nums[@]}"

# Get the length of an array individual element
echo "Index 3 Length : ${#fav_nums[3]}"

# Sort an array
sorted_nums=($(for i in "${fav_nums[@]}"; do
echo $i
done | sort))

for i in ${sorted_nums[*]}; do
	echo $i
done

# Delet an array element
unset 'sorted_nums[1]'

# Delete the whole array
unset sorted_nums


# Positional Parameters and how to set the values from the command line
# Pos Par are variables that can store data on the command line in variables names 0 to 9

# The variable 0 will contain path to current script
echo  "1st Argument : $1"

sum=0

# $# give the number of arguments
while [[ $# -gt 0 ]]; do
	num=$1
	sum=$((sum+num))
	# shift will move the value on the 2nd argument into 1 position
	shift
done

echo "Sum : $sum"

# ./LESSON5.sh 1 2 3 4 5
# 1st Argument : 1
# Sum : 15
