#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("3","SCALER1")
#Start_SCALERS_CRATE("4","CLASSCHV1")
Start_SCALERS_CRATE("5","CLASSC10")

## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

dbLoadTemplate("db/jscalers_TRIG.substitutions")
#dbLoadTemplate("db/jscalers_NEUTRON.substitutions")
dbLoadTemplate("db/jscalers_BLINE.substitutions")

dbLoadRecords("db/jscaler_TRIG_alias.db")
dbLoadRecords("db/jscaler_RUN_alias.db")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

