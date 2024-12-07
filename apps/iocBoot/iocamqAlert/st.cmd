#!../../bin/linux-x86_64/amq
< envPaths
cd ${TOP}
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.scalers.HallB_DAQ")

dbLoadTemplate("db/amq-atof.substitutions")
dbLoadRecords("db/amq-atof-aliases.db")
dbLoadRecords("db/amq-atof-scalers.db")

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

cd ${TOP}/iocBoot/${IOC}

< ../save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

StartMQ()

dbl > pv.list

seq atof

