#!/bin/sh
motorName=$1
dataDir=/home/epics/DATA/HARP_SCANS
lastFile=`ls -lht $dataDir/$motorName | grep $motorName | awk '{print$9}' | head -n1`
harp_fitter $motorName/$lastFile
