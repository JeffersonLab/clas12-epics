#!/bin/bash
P=B_DET_DC_HV
USAGE="Usage:\n\tsetdc.sh sector region layer wires setter value"

if [ -z $6 ]; then
  echo -e "Missing Argments.\n$USAGE" ; exit
elif ! [ -z $7 ]; then
  echo -e "Extra Arguments.\n$USAGE" ;  exit
fi

sector=$1
region=$2
layer=$3
wires=$4
setter=$5
value=$6

# CHECK ARGUMENTS:
if [ "$setter" != "vset" ] && [ "$setter" != "iset" ] && [ "$setter" != "pwonoff" ] && [ "$setter" != "rup" ] && [ "$setter" != "rdn" ] && [ "$setter" != "trip" ] && [ "$setter" != "vmax" ]; then
  echo -e "\nInvalid setter:  $setter\n\n$USAGE" ; exit
fi
if [ "$sector" != "0" ] && [ "$sector" != "1" ] && [ "$sector" != "2" ] && [ "$sector" != "3" ] && [ "$sector" != "4" ] && [ "$sector" != "5" ] && [ "$sector" != "6" ]; then
  echo -e "\nInvalid Sector:  $sector\n\n$USAGE" ; exit
fi
if [ "$region" != "0" ] && [ "$region" != "1" ] && [ "$region" != "2" ] && [ "$region" != "3" ]; then
  echo -e "\nInvalid Region:  $region\n\n$USAGE" ; exit
fi
if [ "$layer" != "0" ] && [ "$layer" != "1" ] && [ "$layer" != "2" ] && [ "$layer" != "3" ] && [ "$layer" != "4" ] && [ "$layer" != "5" ] && [ "$layer" != "6" ]; then
  echo -e "\nInvalid Layer:  $layer\n\n$USAGE" ; exit
fi
if [ "$wires" != "0" ] && [ "$wires" != "S" ] && [ "$wires" != "F" ] && [ "$wires" != "G" ]; then
  echo -e "\nInvalid Wires:  $wires\n\n$USAGE" ; exit
fi
if [ "$region" == "1" ]; then
  if [ "$layer" != "1" ] && [ "$layer" != "2" ]; then
    echo -e "\nInvalid Region/Layer Combination:  $region/$layer\n\n$USAGE" ; exit
  fi
elif [ "$region" == "2" ]; then
  if [ "$layer" != "3" ] && [ "$layer" != "4" ]; then
    echo -e "\nInvalid Region/Layer Combination:  $region/$layer\n\n$USAGE" ; exit
  fi
elif [ "$region" == "3" ]; then
  if [ "$layer" != "4" ] && [ "$layer" != "5" ]; then
    echo -e "\nInvalid Region/Layer Combination:  $region/$layer\n\n$USAGE" ; exit
  fi
fi

# PRINT CONFIG:
echo
echo "Setting $setter = $value"
if [ "$sector" == "0" ]; then
  echo "All Sectors"
else
  echo "Sector $sector"
fi
if [ "$region" == "0" ]; then
  echo "All Regions"
else
  echo "Region $region"
fi
if [ "$layer" == "0" ]; then
  echo "All Layers"
else
  echo "Layer $layer"
fi
if [ "$wires" == "0" ]; then
  echo "All Wires"
else
  echo "$wires Wires"
fi
echo

# LOOP OVER SECTOR/REGION/LAYER/WIRES AND CAPUT:
for ss in 1 2 3 4 5 6
do
  if [ "$sector" != "0" ] && [ "$sector" != "$ss" ]; then
    continue
  fi
  for rr in 1 2 3; do
    if [ "$region" != "0" ] && [ "$region" != "$rr" ]; then
      continue
    fi
    for ll in 1 2; do
      ll=`echo "$ll+($rr-1)*2" | bc`
      if [ "$layer" != "0" ] && [ "$layer" != "$ll" ]; then
        continue
      fi
      for wt in S F G; do
        if [ "$wires" != "0" ] && [ "$wires" != "$wt" ]; then
          continue
        fi
        if [ "$wt" == "S" ] || [ "$wt" == "F" ]; then
          for wn in 01-08 09-16 17-24 25-32 33-48 49-64 65-80 81-112; do
            caput ${P}_SEC${ss}_R${rr}_SL${ll}_${wt}${wn}:${setter} ${value}
          done
        elif [ "$wt" == "G" ]; then
          for wn in 01-32 33-112; do
            caput ${P}_SEC${ss}_R${rr}_SL${ll}_${wt}${wn}:${setter} ${value}
          done
        fi
        sleep 1
      done
    done
  done
done

