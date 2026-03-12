#!../../bin/linux-x86/ioccaen

< envPaths
epicsEnvSet("IOC","iocprad")

cd ${TOP}

dbLoadDatabase("dbd/ioccaen.dbd")
ioccaen_registerRecordDeviceDriver(pdbbase)

dbLoadRecords("db/crio-hycal-temps.db")
dbLoadRecords("db/crio-hycal-filter.db")
dbLoadRecords("db/cRIO_heartbeat.db","P=B_HW_,R=CRIO_PRAD_,DLY=60")

cd ${TOP}/iocBoot/${IOC}

iocInit()

