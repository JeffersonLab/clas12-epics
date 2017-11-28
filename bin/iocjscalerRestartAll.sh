#!/bin/sh

for ss in 1 2 3 4 5 6
do
  softioc_console -R iocjscalers${ss}
done

softioc_console -R iocjscalersC
softioc_console -R iocjscalersT
#softioc_console -R iocjscalersRICH

