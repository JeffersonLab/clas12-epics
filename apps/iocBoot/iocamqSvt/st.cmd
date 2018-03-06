#!../../bin/linux-x86_64/amq
#This file was created by using the command "awk -f makeIocs.gk clasrun.clasprod.daq.HallB_DAQ.dat" on Wed Dec  6 17:35:35 EST 2017

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.daq.HallB_DAQ")


dbLoadTemplate("db/amqSvt.substitutions")

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

#Need this to start responding to messages after all records are defined
StartMQ()

dbl > pv.list
