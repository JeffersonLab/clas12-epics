#!/bin/sh

for xx in 01 02 03 04 05 06 07 08 09 10 11 13 14 15 16 18 19 20
do
    echo $xx
    hallb-gpib-reset.sh $xx
done

