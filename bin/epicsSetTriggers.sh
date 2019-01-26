#!/bin/sh

d=$CLON_PARMS/trigger/vpk/trigger_scalers

p=$1

if [ ! -e $d/${p}.txt ]
then
    echo ABORTED:  MISSING FILE: $d/${p}.txt
    exit
fi

if [ ! -e $d/${p}_stage2.txt ]
then
    echo ABORTED:  MISSING FILE: $d/${p}_stage2.txt
    exit
fi

$d/setTrigDescPrescaleStatus.sh $d/$p.txt
$d/setTrigDesc-stage2.sh $d/${p}_stage2.txt

