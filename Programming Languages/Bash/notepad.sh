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

