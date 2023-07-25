#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("0","test1")

## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

callbackSetQueueSize(5000)
scanOnceSetQueueSize(5000)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")

dbLoadTemplate("db/jscalers_86.substitutions")

cd ${TOP}/iocBoot/${IOC}

iocInit

dbl > pv.list
