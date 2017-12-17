#!/bin/sh

localDir=/home/epics/DATA/HARP_SCANS
localSubdirs='harp_2c21 harp_2H01 harp_tagger'

remoteUser=hbops
remoteHost=hlbl00
remoteDir=/usr/opsdata/harpData/HallB

for dd in $localSubdirs
do
    # the trailing slash is important
    rsync -r -a -e ssh $localDir/$dd/ $remoteUser@$remoteHost:$remoteDir
done


