#!../../bin/linux-x86_64/dynapower
############################################################################
< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
############################################################################
cd "${TOP}"

dbLoadDatabase("dbd/dynapower.dbd")
dynapower_registerRecordDeviceDriver(pdbbase)

drvAsynIPPortConfigure("SER1", "hallb-moxa6:4001")
drvAsynIPPortConfigure("SER2", "hallb-moxa8:4009")

#asynSetTraceMask("SER1",-1,0x09)
#asynSetTraceIOMask("SER1",-1,0x03)

#asynSetTraceMask("SER2",-1,0x9)
#asynSetTraceIOMask("SER2",-1,0x3)

asynOctetSetOutputEos("SER2",0,"\r")
asynOctetSetInputEos("SER2",0,"\n\r")

dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")

dbLoadRecords("db/SCE410.db", "P=B_MOLLER_,R=HELMHOLTZ_,PORT=SER1,ADDR=1")

dbLoadRecords("db/asynRecord.db","P=DYNAB,R=:ASYN,PORT=SER2,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/dynapower-2022-soft.db","P=DYNAB:,PORT=SER2")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

