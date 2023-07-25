#!../../bin/linux-x86_64/dynapower
< envPaths

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES",1000000)

cd "${TOP}"

dbLoadDatabase("dbd/dynapower.dbd")
dynapower_registerRecordDeviceDriver(pdbbase)

drvAsynIPPortConfigure("SER1", "hallb-keithley2470:5025")

#asynSetTraceMask("SER1",-1,0x09)
#asynSetTraceIOMask("SER1",-1,0x03)
asynOctetSetOutputEos("SER1",0,"\n")
asynOctetSetInputEos("SER1",0,"\n")

dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db", "IOC=${IOC}")

dbLoadRecords("db/asynRecord.db","P=B_uRWell,R=:ASYN,PORT=SER1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/keithley2470.db","P=B_uRWell,R=:,PORT=SER1,ADDR=1")

cd "${TOP}/iocBoot/${IOC}"

iocInit

dbl > pv.list

