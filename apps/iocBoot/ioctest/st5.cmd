#!../../bin/linux-x86_64/testApp
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/testApp.dbd")
testApp_registerRecordDeviceDriver pdbbase

#epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","1000000")

dbLoadRecords("db/dt_test.db","P=B_XXX,DT=1")

dbLoadRecords("db/timeDerivative.db","P=CLL6763A,DT=10")

cd "${TOP}/iocBoot/${IOC}"

iocInit


dbl > pv.list

