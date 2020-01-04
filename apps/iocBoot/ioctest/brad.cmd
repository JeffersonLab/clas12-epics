#!../../bin/linux-x86_64/testApp

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/testApp.dbd"
testApp_registerRecordDeviceDriver pdbbase

#dbLoadRecords("db/heartbeatUpdate.db","INP=C1068_QDAC11r.RVAL,P=asdf,HIHI=10")
#dbLoadRecords("db/heartbeatUpdate.db","INP=scaler_calc1,P=asdf,HIHI=10")
dbLoadRecords("db/heartbeatUpdate.db","INP=asdf,P=asdf,HIHI=10")

cd ${TOP}/iocBoot/${IOC}

iocInit();

