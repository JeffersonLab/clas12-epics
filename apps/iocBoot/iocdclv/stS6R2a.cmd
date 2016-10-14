#!../../bin/linux-x86_64/A6551

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/A6551.dbd"
A6551_registerRecordDeviceDriver pdbbase

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

epicsEnvSet("scan","2 second")

drvAsynIPPortConfigure("S6R2",hallb-gpib04.jlab.org:1234,0,0,0)

dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC6_R2,PORT=S6R2,ADDR=1,IMAX=2000,OMAX=2000")

dbLoadRecords("db/asynRecord.db","P=asdf,PORT=S6R2,R=:,ADDR=1,IMAX=2000,OMAX=2000")
asynOctetSetOutputEos("S6R2",0,"\r\n")
asynOctetSetInputEos("S6R2",0,"\n")
asynSetTraceMask("S6R2",-1,0x09)
asynSetTraceIOMask("S6R2",-1,0x02)

#dbLoadRecords("db/prologix.db","P=hallb-gpib04,R=:,DESC=DCLV_S6R2,PORT=S6R2")

cd ${TOP}/iocBoot/${IOC}

iocInit();

