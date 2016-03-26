#!../../bin/linux-x86_64/sy2604

## You may have to change sy2604 to something else
## everywhere it appears in this file

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/sy2604.dbd"
sy2604_registerRecordDeviceDriver pdbbase

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

## Configure devices

drvAsynIPPortConfigure("L0",129.57.86.129:10001,0,0,0)

#asynSetTraceMask("L0",-1,0x09)
#asynSetTraceIOMask("L0",-1,0x02)
asynOctetSetOutputEos("L0",0,"\r")
asynOctetSetInputEos("L0",0,"\r")

## Load record instances
## Call one for each with sector, layer and GPIB ID
dbLoadRecords("db/sy2604.db","P=htcclv,PORT=L0,ADDR=24,IMAX=2000,OMAX=2000")

cd ${TOP}/iocBoot/${IOC}
iocInit();

