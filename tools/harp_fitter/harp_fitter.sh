#!/bin/sh
motorName=$1
fitterExe=/usr/clas12/release/pro/epics/tools/harp_fitter/Fitter.exe
dataDir=/home/epics/DATA/HARP_SCANS
lastFile=`ls -lht $dataDir | grep $motorName | awk '{print$9}' | heaed -n1`
$fitterExe $motorName/$lastFile
