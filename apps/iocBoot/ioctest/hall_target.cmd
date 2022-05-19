#!../../bin/linux-x86_64/amq

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

cd ${TOP}/iocBoot/${IOC}

dbLoadRecords("hall_target.db")

iocInit();

