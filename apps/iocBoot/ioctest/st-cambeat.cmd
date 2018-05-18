#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","1000000")

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/heartbeatProc.db","P=hallbcam07:,I=cctv6:image5:ArrayData")

cd ${TOP}/iocBoot/${IOC}

iocInit();

