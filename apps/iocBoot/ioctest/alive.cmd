#!../../bin/linux-x86_64/testApp

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/testApp.dbd"
testApp_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/misc-crate-alive.db","P=B_HW_camac1:ALIVE")

cd ${TOP}/iocBoot/${IOC}

iocInit();

