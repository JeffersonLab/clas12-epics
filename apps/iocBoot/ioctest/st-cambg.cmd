#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/liveRollAvg.db","I=IPM2C21A,P=B_IPM2C21A:avg20s,N=20,SCAN=1"))
dbLoadRecords("db/camera-bg.db","P=cctv6")

cd ${TOP}/iocBoot/${IOC}

iocInit();

