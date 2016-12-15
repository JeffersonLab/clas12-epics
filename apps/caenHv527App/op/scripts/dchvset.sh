#!/bin/bash

USAGE="Usage:\n\tsetdc.sh sector region layer wires setter value"

##########################################################################
#
# Loops over channels and caputs.
# 
# All arguments must be supplied and in the correct order.
# Argument values are checked for validity.
#
# Interactive user input is requested for confirmation after printing the
# given configuration.  To override this, one can pipe a 'y' to this script,
# e.g. `echo y | dchvset.sh`.
#
# Valid argment values:
#
# Detector Components
# sector = 1,2,3,4,5,6
# region = 1,2,3
# layer  = 1,2,3,4,5,6 (depends on region)
# wires  = S,F,G
# all    = 0 (loops over all possibilities given above)
#
# Setter:
# pwonoff, vset, iset, rup, rdn, vmax, trip
#
#
#
# This script exists because:
# 1. Mass caputs occaisonally timeout on the ioc for CEAN 527
#    e.g. hundreds of successive caputs without any delays
# 2. High speed writes (e.g. via burt) occaisonally result in the
#    CAENET v288 cards failing to succesfully transmit to the HV
#    board.  And currently our driver does not check whether the
#    transmission failed and retry (and that would be pretty
#    complicated in its current design).
# On #2, records to compare inputs and outputs work to fix the
#    issue, but could be risky if a bad readback exists.  And also
#    this will get more complicated when we introduce group writes.
# Group output operations fully get rid of both #1 and #2, but
#    introduce the additional issue that single channel output
#    records do not update after a group output operation.
# 
#########################################################################

STARTTIME=`date`

# PV PREFIX FOR THE DC HV:
P=B_DET_DC_HV

# PAUSE OCCAISONALLY FOR BETTER PERFORMANCE:
NCAPUTS=0
function CAPUT {
  pv=$1
  value=$2
  caput -w 2 $pv $value
  let NCAPUTS=$NCAPUTS+1
  # this is the parameter to tune
  if [ $NCAPUTS -gt 5 ]; then
    NCAPUTS=0
    sleep 1
  fi
}

# CHECK #ARGUMENTS:
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

# CHECK ARGUMENT VALUES:
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
    if [ "$layer" != "4" ] && [ "$layer" != "5" ]; then
      echo -e "\nInvalid Region/Layer Combination:  $region/$layer\n\n$USAGE" ; exit
    fi
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

# USER CONFIRMATION
echo "Enter 'Y' or 'y' to confirm..."
read answer
if [ "$answer" != "y" ] && [ "$answer" != "Y" ]; then
  exit
fi

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
            CAPUT ${P}_SEC${ss}_R${rr}_SL${ll}_${wt}${wn}:${setter} ${value}
          done
        elif [ "$wt" == "G" ]; then
          for wn in 01-32 33-112; do
            CAPUT ${P}_SEC${ss}_R${rr}_SL${ll}_${wt}${wn}:${setter} ${value}
          done
        fi
      done
    done
  done
done

ENDTIME=`date`

echo StartTime: $STARTTIME
echo EndTime:   $ENDTIME

