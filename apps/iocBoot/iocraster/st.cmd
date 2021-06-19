#!../../bin/linux-x86_64/keysight

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/keysight.dbd"
keysight_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","100000")

## Configure devices

drvAsynIPPortConfigure("L0",129.57.86.49:5025,0,0,0)
#drvAsynIPPortConfigure("L1",129.57.86.49:5026,0,0,0)
#drvAsynIPPortConfigure("L2",129.57.86.49:5027,0,0,0)

#asynSetTraceMask("L0",-1,0x09)
#asynSetTraceIOMask("L0",-1,0x02)
#asynOctetSetOutputEos("L0",0,"\n")
#asynOctetSetInputEos("L0",0,"\n")

dbLoadRecords("db/asynRecord.db","P=B_RASTER:DRV,R=:ASYN,PORT=L0,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A33500.db","TAG=B_RASTER:DRV,PORT=L0,L=HB"))

dbLoadRecords("db/asynRecord.db","P=B_RASTER:PS:X,R=:ASYN,PORT=L1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/asynRecord.db","P=B_RASTER:PS:Y,R=:ASYN,PORT=L2,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadTemplate("db/danfysik-8500.substitutions")

cd ${TOP}/iocBoot/${IOC}

iocInit();

