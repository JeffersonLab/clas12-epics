#!../../bin/linux-x86/A6551

## You may have to change A6551 to something else
## everywhere it appears in this file

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/A6551.dbd"
A6551_registerRecordDeviceDriver pdbbase

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

## Configure devices
drvAsynIPPortConfigure("L0",129.57.160.95:1234,0,0,0)

#asynSetTraceMask("L0",-1,0x09)
#asynSetTraceIOMask("L0",-1,0x02)
asynOctetSetOutputEos("L0",0,"\r\n")
asynOctetSetInputEos("L0",0,"\n")

## Load record instances
## Call one for each with sector, layer and GPIB ID
dbLoadRecords("db/A6551.db","S=1,L=1,PORT=L0,ADDR=24,IMAX=2000,OMAX=2000")

cd ${TOP}/iocBoot/${IOC}
iocInit();

