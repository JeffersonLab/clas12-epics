#!/bin/sh

st=$EPICS/apps/iocBoot/iocdclv/st.cmd
xx=drvAsynIPPortConfigure

sr=`grep $xx $st | grep $1 | sed 's/.*("\(.*\)",.*/\1/'`

hn=`grep $xx $st | grep $1 | sed 's/.*",\(.*\):1234.*/\1/'`

ip=`nslookup $hn | grep 'Address: 129.57.160' | awk '{print$2}'`

echo $sr
echo $hn
echo $ip

