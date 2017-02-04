#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")
dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

dbLoadRecords("db/mcc_vacuum.db")
dbLoadRecords("db/mcc_bpm.db")
dbLoadRecords("db/mcc_cryo.db")
dbLoadRecords("db/mcc_tagger.db")

dbLoadTemplate("db/alarm_bpm.substitutions")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit();

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

#dbl > pv.list

