#!/bin/sh

pre=B_DET_DC_LV_SEC

for ss in 1 2 3 4 5 6
do
    for rr in 1 2 3
    do
        caput ${pre}${ss}_R${rr}:imon.SCAN $1
        caput ${pre}${ss}_R${rr}:vmon.SCAN $1
        caput ${pre}${ss}_R${rr}:pwrbk.SCAN $1
        caput ${pre}${ss}_R${rr}:ocstat.SCAN $1
    done
done
