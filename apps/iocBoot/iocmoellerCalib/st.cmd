#!../../bin/linux-x86_64/keithley

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/keithley.dbd"
keithley_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","100000")

## Configure devices

# hallb-gpib21:
drvAsynIPPortConfigure("L0",129.57.160.166:1234,0,0,0)

asynSetTraceMask("L0",-1,0x09)
asynSetTraceIOMask("L0",-1,0x02)
#asynOctetSetOutputEos("L0",0,"\n")
#asynOctetSetInputEos("L0",0,"\n")

dbLoadRecords("db/asynRecord.db","P=moellermeter,R=:ASYN,PORT=L0,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/keithley2001.db","P=moellermeter,NPOINTS=4000,PORT=L0,PINI=0")
dbLoadRecords("db/moellermeter.db","P=moellermeter,NPOINTS=4000,PORT=L0")



cd ${TOP}/iocBoot/${IOC}

iocInit();

seq &seqMoellermeter, "P=moellermeter"

