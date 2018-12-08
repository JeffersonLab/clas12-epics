#!../../bin/linux-x86_64/testApp

< envPaths

cd ${TOP}

dbLoadDatabase "dbd/testApp.dbd"

testApp_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/autoslope.db","P=slm_slope:calc")
dbLoadRecords("db/liveRollAvg.db","P=scaler_calc2,I=scaler_calc2,N=30,SCAN=1")

cd ${TOP}/iocBoot/${IOC}

iocInit();

