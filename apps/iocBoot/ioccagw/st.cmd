#!../../bin/linux-x86_64/cagw
#################################################
< envPaths
epicsEnvSet("EPICS_CA_ADDR_LIST","129.57.167.43")
#################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/cagw.dbd")
cagw_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")
dbLoadRecords("db/cagw.db", "P=B_CAGW:")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

dbl > pv.list
iocInit

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

