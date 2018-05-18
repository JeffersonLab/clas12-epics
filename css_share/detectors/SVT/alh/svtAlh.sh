#!/bin/sh

noise=/usr/share/sounds/speech-dispatcher/test.wav 
logdir=/usr/clas12/DATA/logs/SVT
epics=/usr/clas12/release/pro/epics/css_share/detectors/SVT/alh

#alh -p $noise -m 1000000 -l $logdir -f $epics SVT.alhConfig
exec alh -m 1000000 -l $logdir -f $epics SVT.alhConfig

