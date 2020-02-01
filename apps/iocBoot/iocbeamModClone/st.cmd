#!../../bin/linux-x86_64/testApp

epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","1000000000")

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/testApp.dbd"
testApp_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/caen1190clone.db","IN=beamMod,OUT=B_beamMod")

cd ${TOP}/iocBoot/${IOC}

iocInit();

