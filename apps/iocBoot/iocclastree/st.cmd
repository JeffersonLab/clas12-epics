#!../../bin/linux-x86/clasTree

< envPaths
cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/clasTree.dbd")
ioccaen_registerRecordDeviceDriver(pdbbase)

dbLoadTemplate("db/clas12Nodes.substitutions");

cd ${TOP}/iocBoot/${IOC}
iocInit

