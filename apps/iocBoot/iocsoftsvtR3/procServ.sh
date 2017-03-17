#!/bin/sh

ioc=iocsoftsvtR3
port=20004
logdir=/usr/clas12/DATA/logs
epics=/home/baltzell/clas12-epics-svtiocs

procServ -n $ioc -i^D^C --logfile $logdir/$ioc.log --logstamp -c $epics/apps/iocBoot/$ioc $port ./st.cmd

