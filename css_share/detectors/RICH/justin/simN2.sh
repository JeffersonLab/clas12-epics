#!/bin/bash
i=30
while [ 1 ]
do
    let j=i+3
    let k=i+1
    caput N2Valve1 $i
    caput N2Valve2 $j
    caput N2Valve3 $k
    let i=i+5

    sleep 1  
  done
