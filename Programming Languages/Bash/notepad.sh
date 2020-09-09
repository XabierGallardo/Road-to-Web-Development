#!/bin/bash
# To print a value but immediately put some characters after
name="Derek"
# ${} is a character expansion
echo "${name}'s toy"
samp_string="The dog climbed the tree"
echo "${samp_string//dog/cat}"

