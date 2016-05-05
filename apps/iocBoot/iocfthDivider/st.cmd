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

## Load record instances
#dbLoadRecords("db/xxx.db","user=klivHost")

## Load record instances
#dbLoadRecords("db/iocAdminSoft.db", "IOC=$(IOC)")
dbLoadRecords("db/fthDivider.db","P=B_DET_FTC_FLASHER,R=:asyn,PORT=L1,NCHAN=336");


cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=klivHost"
