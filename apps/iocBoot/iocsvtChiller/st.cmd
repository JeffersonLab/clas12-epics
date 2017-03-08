#!../../bin/linux-x86_64/svtChiller

< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/svtChiller.dbd")
svtChiller_registerRecordDeviceDriver(pdbbase)

drvAsynIPPortConfigure("L0",svtchiller1.acc.jlab.org:10001,0,0,0)

## debugging...
#asynSetTraceMask("SER3",-1,0x09)
#asynSetTraceIOMask("SER3",-1,0x02)

## Load record instances
dbLoadRecords("db/svtChiller.db")

dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

iocInit

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

