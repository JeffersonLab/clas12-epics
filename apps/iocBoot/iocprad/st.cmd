#!../../bin/linux-x86/ioccaen

< envPaths
epicsEnvSet("IOC","iocprad")

cd ${TOP}

dbLoadDatabase("dbd/ioccaen.dbd")
ioccaen_registerRecordDeviceDriver(pdbbase)

dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

dbLoadRecords("db/crio-hycal-temps.db")
dbLoadRecords("db/crio-hycal-filter.db")
dbLoadRecords("db/prad-target.db")
dbLoadRecords("db/prad-target-status.db","P=TGT:PRad")

dbLoadRecords("db/cRIO_heartbeat.db","P=B_HW_,R=CRIO_PRAD_,DLY=60")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit()

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

