#!/usr/bin/env bash
#HW section 2
#script will make hidden file, put variables, prints bashrc
#ver 0.0.1
#dorshamay

name=dor
lname=shamay
ID=205592512
DOB=5.6.1994
POB=Israel
touch .user_info.sh && echo "$name $lname $ID $DOB $POB" > .user_info.sh
sudo cp /$HOME/Desktop/2.12.2017/HW2.sh /etc/init.d
sudo update-rc.d HW2.sh defaults
