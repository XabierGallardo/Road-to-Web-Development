#!/bin/bash

# Variable declaration
myName="Xabier";

# Constant declaration
declare -r NUM1=5

num2=4

# Basic arithmetics and print info, using python
num3=$((NUM1+num2))
num4=$((NUM1-num2))
num5=$((NUM1*num2))
num6=$((NUM1/num2))

echo "5 + 4 = $num3"
echo "5 - 4 = $num4"
echo "5 * 4 = $num5"
echo "5 / 4 = $num6"

echo $((5**2))
echo $((5%4))

rand=5
let rand+=4
echo "$rand"

echo "rand++ = $((rand++))"
echo "++rand = $((++rand))"
echo "rand-- = $((rand--))"
echo "--rand = $((--rand))"

num7=1.2
num8=3.4
num9=$(python -c "print $num7+$num8")
echo $num9

# Print out info over multiple lines
cat<< END
This text
prints on
many lindes
END
