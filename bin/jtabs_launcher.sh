#!/bin/bash
#
# Wrap this with xterm -e for use from MEDM.  Set remote hostname below.
#

host=hlbl00
user=hbops

#echo "Running JTabs from $host..."
#read -p "Enter your username [$user]: " INPUT_STRING
#if [ "$INPUT_STRING" != "" ]; then
#	user=$INPUT_STRING
#fi

#ssh $host -l $user jtabs
ssh -i ~/.ssh/id_rsa_hpsrun $host -l $user jmenu

