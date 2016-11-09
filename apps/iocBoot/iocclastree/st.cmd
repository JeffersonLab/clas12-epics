#!../../bin/linux-x86/clasTree

< envPaths
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "1000000")

cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/clasTree.dbd")
clasTree_registerRecordDeviceDriver(pdbbase)

dbLoadTemplate("db/clas12Nodes.substitutions");

cd ${TOP}/iocBoot/${IOC}
#dbLoadRecords("test.db")
iocInit

