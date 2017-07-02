#!../../bin/linux-x86_64/cRio
############################################################################
< envPaths
epicsEnvSet("EPICS_CA_ADDR_LIST", "129.57.163.255")
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/cRio.dbd")
cRio_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")
## cRIO heartbeat alarms
dbLoadRecords("db/cRIO_heartbeat.db",   "P=B_HW_, R=CRIO_DEV_,  DLY=60")
# dbLoadRecords("db/cRIO_heartbeat.db",   "P=B_HW_, R=CRIO_HTCC_, DLY=60")
dbLoadRecords("db/cRIO_heartbeat.db",   "P=B_HW_, R=CRIO_SVT_,  DLY=60")
## Detector Systems 
#dbLoadRecords("db/gas_cRIO_HTCC.db",    "P=B_DET_, R=HTCC_GAS_")
dbLoadRecords("db/gas_cRIO_SVT.db",     "P=B_DET_, R=SVT_GAS_")

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
