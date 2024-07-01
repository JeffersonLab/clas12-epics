#!../../bin/linux-x86/ioccaen

< envPaths
epicsEnvSet("IOC","ioctest")

cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/ioccaen.dbd")
ioccaen_registerRecordDeviceDriver(pdbbase)

cd ${TOP}/iocBoot/${IOC}

dbLoadRecords("seq-test.db")

iocInit()

