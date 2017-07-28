#!../../bin/linux-x86_64/genFlasher

## You may have to change genFlasher to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "600000")

## Register all support components
dbLoadDatabase "dbd/genFlasher.dbd"
genFlasher_registerRecordDeviceDriver pdbbase

## Load record instances
#dbLoadRecords("db/xxx.db","user=klivHost")

## Configure devices
drvAsynIPPortConfigure("L1","fastlightpulser1:5000 UDP",0,0,0)


## Comment these for verbose output - for debugging purposes.
#asynSetTraceMask("L1", 0, 4)
#asynSetTraceIOMask("L1", 0, 6)
#asynSetTraceIOTruncateSize("L1", 0, 1000)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=$(IOC)")
dbLoadRecords("db/genFlasher.db","P=B_HW_FLASHER_HTCC-FTOF,R=:asyn,PORT=L1");
#dbLoadRecords("db/genFlasher.db","P=B_HW_GENFLASHER_HTCC-FTOF,R=:asyn,PORT=L1");

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=klivHost"

#init some values
dbpf("B_HW_FLASHER_HTCC-FTOF:F0_DATA_FILE_LOAD","/home/clasrun/htcc/flasher/HTCC_FlasherDefault.dat")
dbpf("B_HW_FLASHER_HTCC-FTOF:F0_DATA_FILE_SAVE","/home/clasrun/htcc/flasher/HTCC_FlasherDefault.dat")
dbpf("B_HW_FLASHER_HTCC-FTOF:F1_DATA_FILE_LOAD","/home/clasrun/htcc/flasher/FTOF_FlasherDefault.dat")
dbpf("B_HW_FLASHER_HTCC-FTOF:F1_DATA_FILE_SAVE","/home/clasrun/htcc/flasher/FTOF_FlasherDefault.dat")
