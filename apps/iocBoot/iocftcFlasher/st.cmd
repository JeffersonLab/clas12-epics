#!../../bin/linux-x86_64/ftcFlasher

## You may have to change ftcFlasher to something else
## everywhere it appears in this file

< envPaths
cd "${TOP}"

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "600000")

## Register all support components
dbLoadDatabase "dbd/ftcFlasher.dbd"
ftcFlasher_registerRecordDeviceDriver pdbbase

## Configure devices
drvAsynIPPortConfigure("L1","ftflash:9764",0,0,0)


## Comment these for verbose output - for debugging purposes.
#asynSetTraceMask("L1", 0, 4)
#asynSetTraceIOMask("L1", 0, 6)
#asynSetTraceIOTruncateSize("L1", 0, 1000)

## Load record instances
#dbLoadRecords("db/iocAdminSoft.db", "IOC=$(IOC)")
dbLoadRecords("db/ftcFlasher.db","P=B_DET_FTC_FLASHER,R=:asyn,PORT=L1,NCHAN=336");


cd "${TOP}/iocBoot/${IOC}"
iocInit


## Run the command to init the ioc
system ./initFtcFlasher.sh
