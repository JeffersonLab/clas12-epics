#!../../bin/linux-x86_64/cRio
############################################################################
< envPaths
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/cRio.dbd")
cRio_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")
## Detector Systems 
dbLoadRecords("db/gas_cRIO_HTCC.db",    "P=B_DET_,R=HTCC_")
dbLoadRecords("db/gas_cRIO_SVT.db",     "P=B_DET_,R=SVT_")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

iocInit

## export pv list
dbl > pv.list

## autosave startup
## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=xxx:")
create_monitor_set("info_settings.req", 30, "P=xxx:")
create_monitor_set("gas_cRIO_SVT.req",  30, "P=B_DET_,R=SVT_")
