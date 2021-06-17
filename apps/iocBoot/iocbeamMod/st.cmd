#!../../bin/linux-x86/caen1190App

epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","1000000000")

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/caen1190App.dbd"
caen1190App_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db","IOC=iocbeamMod")

dbLoadRecords("db/caen1190.db","P=beamMod")

dbLoadTemplate("db/caen1190.substitutions")

cd ${TOP}/iocBoot/${IOC}

iocInit();

seq caen1190seq, "P=beamMod"

dbl > pv.list

