#!../../bin/linux-x86_64/pcMonitor

< envPaths

cd ${TOP}

dbLoadDatabase("dbd/pcMonitor.dbd",0,0)
pcMonitor_registerRecordDeviceDriver

dbLoadRecords("db/pcMonitor.db","NAME=clonpc11")

cd ${TOP}/iocBoot/${IOC}

iocInit

