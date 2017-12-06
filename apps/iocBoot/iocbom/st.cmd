#!../../bin/linux-x86_64/iocbom
< envPaths
cd ${TOP}

Init_BOM()

Start_BOM_CRATE("3","SCALER9")

## Register all support components
dbLoadDatabase("dbd/iocbom.dbd")
iocbom_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

#dbLoadTemplate("db/jscalers_TRIG.substitutions")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

