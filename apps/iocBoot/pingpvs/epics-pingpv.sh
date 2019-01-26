#!/bin/sh

host=$1
hbeat=B_HW_$host:ALIVE

while [ 1 ]
do
    ping -c 1 -w 5 $host >& /dev/null
    if [ $? == "0" ]
    then
        caput $hbeat 1
    else
        caput $hbeat 0
    fi
    sleep 10
done

