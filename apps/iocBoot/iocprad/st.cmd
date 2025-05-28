#!../../bin/linux-x86/ioccaen

< envPaths
epicsEnvSet("IOC","iocprad")

cd ${TOP}

dbLoadDatabase("dbd/ioccaen.dbd")
ioccaen_registerRecordDeviceDriver(pdbbase)

dbLoadRecords("db/crio-hycal-temps.db")

cd ${TOP}/iocBoot/${IOC}

iocInit()

