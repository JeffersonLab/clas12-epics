#!../../bin/linux-x86_64/mcc

< envPaths

epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","1000000000")

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/criowf.db")

cd ${TOP}/iocBoot/${IOC}

iocInit();

