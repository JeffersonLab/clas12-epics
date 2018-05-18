#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/mcc_fsdGlobal.db")

cd ${TOP}/iocBoot/${IOC}

iocInit();

