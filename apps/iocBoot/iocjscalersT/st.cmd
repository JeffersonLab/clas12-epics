#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("3","TRIG2")

## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

dbLoadTemplate("db/jscalers_TRIG.substitutions")

cd ${TOP}/iocBoot/${IOC}

#< save_restore.cmd

iocInit

#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=${IOC}:")
#create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

