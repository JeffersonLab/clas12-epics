#!/bin/sh

export MIBDIRS=${MIBDIRS}:${EPICS}/apps/mibs

while [ 1 ]
do
  date
  snmpget -v1 -c public 129.57.160.153 SPAGENT-MIB::sensorProbeTempDegree.0 
  sleep 10
done

