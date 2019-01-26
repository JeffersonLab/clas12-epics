#!../../bin/linux-x86_64/testApp

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/testApp.dbd"
testApp_registerRecordDeviceDriver pdbbase

#dbLoadRecords("db/soeTimestamp.db","P=soe,R=,UPPER=358651,LOWER=-1426734475")

dbLoadRecords("db/soeTimestamp-sim.db","P=soe,R=,UVAL=358651,LVAL=-1426734475")
dbLoadRecords("db/soeTimestamp.db","P=soe,R=,UPPER=soe:upper,LOWER=soe:lower")

cd ${TOP}/iocBoot/${IOC}

iocInit();

