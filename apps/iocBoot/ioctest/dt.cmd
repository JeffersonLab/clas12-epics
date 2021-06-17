#!../../bin/linux-x86_64/testApp

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/testApp.dbd"
testApp_registerRecordDeviceDriver pdbbase

#dbLoadRecords("db/timeDerivative2.db","P=fcup_offset,R=:a,DT=2")
dbLoadRecords("db/timeDerivative2.db","INP=tiger,P=bobcat,NSEC=2,N=5")

cd ${TOP}/iocBoot/${IOC}

#dbLoadRecords("deriv.db")

iocInit();

