#!../../bin/linux-x86_64/fthDivider

## You may have to change fthDivider to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "600000")

## Register all support components
dbLoadDatabase "dbd/fthDivider.dbd"
fthDivider_registerRecordDeviceDriver pdbbase

## Configure devices
drvAsynIPPortConfigure("L1","ftvdivider:9764",0,0,0)

## Comment these for verbose output - for debugging purposes.
asynSetTraceMask("L1", 0, 4)
asynSetTraceIOMask("L1", 0, 6)
asynSetTraceIOTruncateSize("L1", 0, 1000)

## Load record instances
#dbLoadRecords("db/xxx.db","user=klivHost")

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=$(IOC)")
dbLoadRecords("db/fthDivider.db","P=B_DET_FTH_DIVIDER,R=:asyn,PORT=L1,NCHAN=240");
dbLoadTemplate("db/fthDividerChan.substitutions")
dbLoadTemplate("db/fthDividerBoard.substitutions")

cd "${TOP}/iocBoot/${IOC}"
#dbLoadRecords("test.db")

iocInit

## Run the command to init the ioc
system ./initFthDivider.sh

