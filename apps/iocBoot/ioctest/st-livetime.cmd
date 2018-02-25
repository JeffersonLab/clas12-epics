#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/tsBusy.db")
dbLoadRecords("db/liveRollAvg.db","P=B_livetime,I=B_livetime,N=15,SCAN=2")
dbLoadRecords("db/liveRollAvg.db","P=B_IPM2C21A,I=IPM2C21A,  N=30,SCAN=1")
dbLoadRecords("db/tsBusy-alarm.db")

cd ${TOP}/iocBoot/${IOC}

iocInit();

dbpf("B_livetime:rms.HIGH","2")
dbpf("B_livetime:rms.HSV","MAJOR")
dbpf("B_livetime:mean.LOW","75")
dbpf("B_livetime:mean.LSV","MAJOR")

dbpf("B_IPM2C21A:rms.HIGH","2")
dbpf("B_IPM2C21A:mean.LOW","5")

