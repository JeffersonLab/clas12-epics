#!/bin/sh

app=/usr/clas12/release/pro/epics/apps/keithley2001App
syn=/usr/clas12/R3.14.12.5/synApps_5_8/asyn-4-26/

medm $app/op/medm/moellermeter.adl >& /dev/null &

medm -x -macro P=moellermeter,R=:ASYN $syn/opi/medm/asynOctet.adl >& /dev/null &

echo setenv EPICS_CA_MAX_ARRAY_BYTES 100000

#SYST:KEY
#"Enter" = 18
#"Trig" = 30

