#!/bin/bash

USAGE="Usage:\n\tsetdc.sh sector region layer"

SFWIRES=(01-08 09-16 17-24 25-32 33-48 49-64 65-80 81-112)
GWIRES=(01-32 33-112)

SVOLTS=(10 20 30 40 50 45 35 25)
FVOLTS=(15 25 35 45 50 40 30 20)
GVOLTS=(30 50)

# PV PREFIX FOR THE DC HV:
P=B_DET_DC_HV

# PAUSE OCCAISONALLY FOR BETTER PERFORMANCE:
NCAPUTS=0
function CAPUT {
  pv=$1
  value=$2
  #caget $pv
  caput -w 2 $pv $value
  let NCAPUTS=$NCAPUTS+1
  # this is the parameter to tune
  if [ $NCAPUTS -gt 5 ]; then
    NCAPUTS=0
    sleep 1
  fi
}

# CHECK #ARGUMENTS:
if [ -z $3 ]; then
  echo -e "Missing Argments.\n$USAGE" ; exit
elif ! [ -z $4 ]; then
  echo -e "Extra Arguments.\n$USAGE" ;  exit
fi

sector=$1
region=$2
layer=$3

# CHECK ARGUMENT VALUES:
if [ "$sector" != "0" ] && [ "$sector" != "1" ] && [ "$sector" != "2" ] && [ "$sector" != "3" ] && [ "$sector" != "4" ] && [ "$sector" != "5" ] && [ "$sector" != "6" ]; then
  echo -e "\nInvalid Sector:  $sector\n\n$USAGE" ; exit
fi
if [ "$region" != "0" ] && [ "$region" != "1" ] && [ "$region" != "2" ] && [ "$region" != "3" ]; then
  echo -e "\nInvalid Region:  $region\n\n$USAGE" ; exit
fi
if [ "$layer" != "0" ] && [ "$layer" != "1" ] && [ "$layer" != "2" ] && [ "$layer" != "3" ] && [ "$layer" != "4" ] && [ "$layer" != "5" ] && [ "$layer" != "6" ]; then
  echo -e "\nInvalid Layer:  $layer\n\n$USAGE" ; exit
fi
if [ "$layer" != "0" ]; then
  if [ "$region" == "1" ]; then
    if [ "$layer" != "1" ] && [ "$layer" != "2" ]; then
      echo -e "\nInvalid Region/Layer Combination:  $region/$layer\n\n$USAGE" ; exit
    fi
  elif [ "$region" == "2" ]; then
    if [ "$layer" != "3" ] && [ "$layer" != "4" ]; then
      echo -e "\nInvalid Region/Layer Combination:  $region/$layer\n\n$USAGE" ; exit
    fi
  elif [ "$region" == "3" ]; then
    if [ "$layer" != "5" ] && [ "$layer" != "6" ]; then
      echo -e "\nInvalid Region/Layer Combination:  $region/$layer\n\n$USAGE" ; exit
    fi
  fi
fi

# PRINT CONFIG:
echo
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
      prefix=${P}_SEC${ss}_R${rr}_SL${ll}
      ii=0
      while [[ $ii < 8 ]]
      do
        CAPUT ${prefix}_S${SFWIRES[$ii]}:vset ${SVOLTS[$ii]}
        let ii=ii+1
      done
      ii=0
      while [[ $ii < 8 ]]
      do
        CAPUT ${prefix}_F${SFWIRES[$ii]}:vset ${FVOLTS[$ii]}
        let ii=ii+1
      done
      ii=0
      while [[ $ii < 2 ]]
      do
        CAPUT ${prefix}_G${GWIRES[$ii]}:vset ${GVOLTS[$ii]}
        let ii=ii+1
      done
    done
  done
done

