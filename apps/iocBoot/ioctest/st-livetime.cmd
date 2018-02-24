#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/tsBusy.db")
dbLoadRecords("db/liveRollAvg.db","P=B_livetime,I=B_livetime,N=15,SCAN=2")
        
cd ${TOP}/iocBoot/${IOC}

iocInit();

