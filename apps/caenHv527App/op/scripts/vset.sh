#!/bin/bash

sector=$1
region=$2
layer=$3
voltage=$4

for ss in 1 2 3 4 5 6
do
  if [ "$sector" != "0" ] && [ "$sector" != "$ss" ]
  then
    continue
  fi
  for rr in 1 2 3
  do
    if [ "$region" != "0" ] && [ "$region" != "$rr" ]
    then
      continue
    fi
    for ll in 1 2
    do
      ll=`echo "$ll+($rr-1)*2" | bc`
      if [ "$layer" != "0" ] && [ "$layer" != "$ll" ]
      then
        continue
      fi

      for ww in 01-08 09-16 17-24 25-32 33-48 49-64 65-80 81-112
      do
        caput -w 5 B_DET_DC_HV_SEC${ss}_R${rr}_SL${ll}_S${ww}:vset $voltage
        caput -w 5 B_DET_DC_HV_SEC${ss}_R${rr}_SL${ll}_F${ww}:vset $voltage
        #caget B_DET_DC_HV_SEC${ss}_R${rr}_SL${ll}_S${ww}:${voltage}
        #caget B_DET_DC_HV_SEC${ss}_R${rr}_SL${ll}_F${ww}:${voltage}
        sleep 1
      done
      #for ww in 01-32 33-112
      #do
      #  echo caput B_DET_DC_HV_SEC${ss}_R${rr}_SL${ll}_G${ww}:vset $voltage
      #done
    
    done
  done
done

