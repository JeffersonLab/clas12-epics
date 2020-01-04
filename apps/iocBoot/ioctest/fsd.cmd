#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

cd ${TOP}/iocBoot/${IOC}

dbLoadRecords("fsd.db","P=B_FSD2")


iocInit();

