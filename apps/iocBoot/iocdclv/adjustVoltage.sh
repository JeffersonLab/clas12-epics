#!/bin/sh

pre=B_DET_DC_LV_SEC

for ss in 1 2 3 4 5 6
do
    for rr in 1 2 3
    do
        v1=`caget ${pre}${ss}_R${rr}:vsetrbk | awk '{print$2}'`
        v2=`echo $v1 $1 1 | bc`
        caput ${pre}${ss}_R${rr}:vset $v2
    done
done
