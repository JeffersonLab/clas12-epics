#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/wf2root_alarm.db","P=B_TORUS:,R=DAQ_REC:")

dbLoadRecords("db/liveRollAvg.db","P=B_TORUS:DAQ_REC:ctrl:file_size,I=B_TORUS:DAQ_REC:ctrl:file_size,SCAN=10,N=30"

cd ${TOP}/iocBoot/${IOC}

iocInit();

