#!../../bin/linux-x86_64/monitor

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/monitor.dbd"
monitor_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

dbLoadTemplate("db/hydra.substitutions")
dbLoadRecords("db/hydra-sum.db")

cd ${TOP}/iocBoot/${IOC}

< ../save_restore.cmd

iocInit();

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

