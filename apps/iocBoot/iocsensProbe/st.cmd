#!../../bin/linux-x86_64/sensProbe

#############################################################################
< envPaths
epicsEnvSet("MIBDIRS", "$(TOP)/mibs")
#############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/sensProbe.dbd")
sensProbe_registerRecordDeviceDriver(pdbbase)

## IOC monitoring, etc
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")

## Load record instances 
dbLoadRecords("db/sensProbe.db", "P=sensProbe:,R=01:,HOST=129.57.160.77")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
#< save_restore.cmd

dbl > pv.list
iocInit

## Handle autosave 'commands' contained in loaded databases.
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=${IOC}:")
#create_monitor_set("info_settings.req", 30, "P=${IOC}:")

