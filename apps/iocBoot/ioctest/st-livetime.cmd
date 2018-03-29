#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

#dbLoadRecords("db/tsBusy.db")
dbLoadRecords("db/daq2epics.db","P=B_DAQ")

dbLoadRecords("db/liveRollAvg.db","P=B_DAQ:livetime,I=B_DAQ:livetime,N=15,SCAN=2")
dbLoadRecords("db/liveRollAvg.db","P=B_IPM2C21A,I=IPM2C21A,  N=30,SCAN=1")
dbLoadRecords("db/tsBusy-alarm.db")

cd ${TOP}/iocBoot/${IOC}

iocInit();

dbpf("B_DAQ:livetime:rms.HIGH","0.3")
dbpf("B_DAQ:livetime:rms.HSV","MAJOR")
dbpf("B_DAQ:livetime:mean.LOW","75")
dbpf("B_DAQ:livetime:mean.LSV","MAJOR")

dbpf("B_IPM2C21A:rms.HIGH","2")
dbpf("B_IPM2C21A:mean.LOW","5")

