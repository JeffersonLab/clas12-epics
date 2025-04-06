#!/bin/sh
export JAVA_HOME=/usr/clas12/offline/jdk/21.0.2
export PATH=$JAVA_HOME/bin:$PATH
motorName=$1
dataDir=/home/epics/DATA/HARP_SCANS
lastFile=`ls -lht $dataDir/$motorName | grep $motorName | awk '{print$9}' | head -n1`
$EPICS/tools/harp_fitter/harp_fitter $motorName/$lastFile
