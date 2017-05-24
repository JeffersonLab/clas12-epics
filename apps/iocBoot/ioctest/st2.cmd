#!../../bin/linux-x86_64/testApp
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/testApp.dbd")
testApp_registerRecordDeviceDriver pdbbase
#dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")

epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","10000000")

#dbLoadRecords("db/test.db")
dbLoadRecords("db/svt-sums-global.db")

cd "${TOP}/iocBoot/${IOC}"

iocInit


dbl > pv.list

