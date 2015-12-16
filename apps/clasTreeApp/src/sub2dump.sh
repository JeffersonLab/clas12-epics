#!/bin/sh

subs=`ls ../../db/HV*_*.substitutions`

for s in $subs;
do
    msi -S $s
done
exit
