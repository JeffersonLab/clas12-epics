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
dbLoadRecords("db/mcc_fsd.db")
dbLoadRecords("db/hall_target.db")

dbLoadTemplate("db/alarm_bpm.substitutions")

dbLoadTemplate("db/hallb_ia.substitutions")
dbLoadRecords("db/hallb_ia.db")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit();

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

epicsThreadSleep(2)
dbpf "B_IA_C1068_QDAC07:init.PROC", "1"
dbpf "B_IA_C1068_QDAC08:init.PROC", "1"
dbpf "B_IA_C1068_QDAC09:init.PROC", "1"
dbpf "B_IA_C1068_QDAC10:init.PROC", "1"

