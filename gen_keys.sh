#!/bin/bash

teams=(1 2 3 4 5 6 7 8 9 10)

for i in "${teams[@]}"
do
	echo -e "\n\n\n" | ssh-keygen -N '' -C "team'$i'-aws" -f "team$i-aws"

done
