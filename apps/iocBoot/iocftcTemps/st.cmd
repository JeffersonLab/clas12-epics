#!../../bin/linux-x86_64/OmegaCYD218
#################################################
< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
#################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/OmegaCYD218.dbd")
OmegaCYD218_registerRecordDeviceDriver(pdbbase)

drvAsynIPPortConfigure("SER1", "hallb-moxa2:4001")
drvAsynIPPortConfigure("SER2", "hallb-moxa2:4002")

## debugging...
#asynSetTraceMask("SER1",-1,0x09)
#asynSetTraceIOMask("SER1",-1,0x02)
#asynSetTraceMask("SER2",-1,0x09)
#asynSetTraceIOMask("SER2",-1,0x02)

cd "${TOP}/iocBoot/${IOC}"

## Load record instances
dbLoadTemplate("OmegaCYD218.substitutions")

## autosave setup
< save_restore.cmd

dbl > pv.list
iocInit

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")
create_monitor_set("OmegaCYD218_All_settings.req", 30)

