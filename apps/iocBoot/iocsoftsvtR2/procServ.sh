#!/bin/sh

ioc=iocsoftsvtR2
port=20003
logdir=/usr/clas12/DATA/logs
epics=/usr/clas12/release/pro/epics

procServ -n $ioc -i^D^C --logfile $logdir/$ioc.log --logstamp -c $epics/apps/iocBoot/$ioc $port ./st.cmd

