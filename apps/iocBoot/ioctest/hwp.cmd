#!../../bin/linux-x86_64/testApp

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/testApp.dbd"
testApp_registerRecordDeviceDriver pdbbase

#dbLoadRecords("db/alarm-on-change.db","INP=doggy,P=bobcat")
dbLoadRecords("db/alarm-on-change.db","INP=IGL1I00OD16_16,P=B_HWP:")

cd ${TOP}/iocBoot/${IOC}

iocInit();

