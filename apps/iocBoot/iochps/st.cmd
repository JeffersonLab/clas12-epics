#!../../bin/linux-x86_64/mpodLv

< envPaths

epicsEnvSet("EPICS_CA_ADDR_LIST", "129.57.163.255")
epicsEnvSet("EPICS_CAS_BEACON_ADDR_LIST", "129.57.163.255")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","10000000")

cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/mpodLv.dbd")
mpodLv_registerRecordDeviceDriver(pdbbase)

dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")

dbLoadRecords("db/freezer_cRIO_HPS_SVT.db")
dbLoadRecords("db/cRIO_heartbeat.db","P=B_HPS_,R=FREEZER_")

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

