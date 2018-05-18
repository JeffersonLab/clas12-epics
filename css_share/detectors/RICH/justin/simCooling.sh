#!/bin/bash
i =30
while [ 1 ]
do
    let j=i+3
    let k=i+1
    caput CoolingValve1 $i
    caput CoolingValve2 $j
    caput CoolingValve3 $k
    caput CoolingValve4 $k
    let i=i+5

    sleep 1  
  done
