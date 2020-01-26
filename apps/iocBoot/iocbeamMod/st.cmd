#!../../bin/linux-x86/caen1190App

epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","1000000000")

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/caen1190App.dbd"
caen1190App_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db","IOC=iocbeamMod")

dbLoadRecords("db/caen1190.db","P=beamMod")

#dbLoadRecords("db/array-to-scalar-4.db","INP=beamMod:power:maxes:amp:0, P=beamMod:power:maxes:amp:, R=0:")
#dbLoadRecords("db/array-to-scalar-4.db","INP=beamMod:power:maxes:amp:0, P=beamMod:power:maxes:amp:, R=1:")
#dbLoadRecords("db/array-to-scalar-4.db","INP=beamMod:power:maxes:amp:0, P=beamMod:power:maxes:amp:, R=2:")
#dbLoadRecords("db/array-to-scalar-4.db","INP=beamMod:power:maxes:amp:0, P=beamMod:power:maxes:amp:, R=3:")
#dbLoadRecords("db/array-to-scalar-4.db","INP=beamMod:power:maxes:freq:0,P=beamMod:power:maxes:freq:,R=0:")
#dbLoadRecords("db/array-to-scalar-4.db","INP=beamMod:power:maxes:freq:0,P=beamMod:power:maxes:freq:,R=1:")
#dbLoadRecords("db/array-to-scalar-4.db","INP=beamMod:power:maxes:freq:0,P=beamMod:power:maxes:freq:,R=2:")
#dbLoadRecords("db/array-to-scalar-4.db","INP=beamMod:power:maxes:freq:0,P=beamMod:power:maxes:freq:,R=3:")

cd ${TOP}/iocBoot/${IOC}

iocInit();

seq caen1190seq, "P=beamMod"

dbl > pv.list

