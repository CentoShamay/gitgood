#!/usr/bin/env bash
#dorshamay
#0.0.1
#list all the processes by your user.

read -p "Please put your username here" var
	if [ $var == dorshamay ]
		then
			ps -u $var;
        else
			echo "Please enter diffrent user";
fi
