#!/bin/bash

pre=B_DET_RICH_TEMP_SEC1

i=10

while [ 1 ]
do
  
  let j=i+10
  let k=i+20
  
  caput $pre\_ROW6_PANEL4 $i

  caput $pre\_ROW7_PANEL3 $i
  caput $pre\_ROW7_PANEL4 $i
  caput $pre\_ROW7_PANEL5 $i

  caput $pre\_ROW8_PANEL2 $i
  caput $pre\_ROW8_PANEL3 $j
  caput $pre\_ROW8_PANEL4 $j
  caput $pre\_ROW8_PANEL5 $i
  
  caput $pre\_ROW9_PANEL2 $i
  caput $pre\_ROW9_PANEL3 $j
  caput $pre\_ROW9_PANEL4 $k
  caput $pre\_ROW9_PANEL5 $j
  caput $pre\_ROW9_PANEL6 $i
  
  caput $pre\_ROW10_PANEL2 $i
  caput $pre\_ROW10_PANEL3 $j
  caput $pre\_ROW10_PANEL4 $k
  caput $pre\_ROW10_PANEL5 $j
  caput $pre\_ROW10_PANEL6 $i
  
  caput $pre\_ROW11_PANEL2 $i
  caput $pre\_ROW11_PANEL3 $j
  caput $pre\_ROW11_PANEL4 $j
  caput $pre\_ROW11_PANEL5 $i

  caput $pre\_ROW12_PANEL3 $i
  caput $pre\_ROW12_PANEL4 $i

  let i=i+5
  sleep 1

done

