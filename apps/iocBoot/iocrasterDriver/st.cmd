#!../../bin/linux-x86_64/keithley2001

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/keithley2001.dbd"
keithley2001_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","100000")

## Configure devices

drvAsynIPPortConfigure("L0",129.57.86.49:5025,0,0,0)

asynSetTraceMask("L0",-1,0x09)
asynSetTraceIOMask("L0",-1,0x02)
asynOctetSetOutputEos("L0",0,"\n")
asynOctetSetInputEos("L0",0,"\n")

dbLoadRecords("db/asynRecord.db","P=rasterdriver,R=:ASYN,PORT=L0,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/keysight33X00.db","P=rasterdriver,R=:,PORT=L0,SCAN1=2 second,SCAN2=5 second")

cd ${TOP}/iocBoot/${IOC}

iocInit();

