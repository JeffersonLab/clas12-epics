#!/bin/sh
P=$1
infile=`caget -S -t ${1}:DATA_FILE_LOAD`

while read line; do
    caput  $line
done < $infile

exit
