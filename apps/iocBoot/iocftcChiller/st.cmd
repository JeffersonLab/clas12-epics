#!../../bin/linux-x86_64/chiller
#################################################
< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
#################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/chiller.dbd")
chiller_registerRecordDeviceDriver(pdbbase)

drvAsynIPPortConfigure("SER3", "hallb-moxa1:4003")

## debugging...
#asynSetTraceMask("SER3",-1,0x09)
#asynSetTraceIOMask("SER3",-1,0x02)

## Load record instances
dbLoadRecords("db/Lauda_XT.db", "P=B_DET_FTC:,R=CHILLER:,PORT=SER3")
#
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

dbl > pv.list
iocInit

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")
create_monitor_set("Lauda_XT_settings.req", 30, "P=B_DET_FTC:,R=CHILLER:")

