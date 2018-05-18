#!../../bin/linux-x86_64/pcMonitor

< envPaths

cd ${TOP}

dbLoadDatabase("dbd/pcMonitor.dbd",0,0)
pcMonitor_registerRecordDeviceDriver

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")
dbLoadRecords("db/pcMonitor.db","NAME=clonioc3")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

