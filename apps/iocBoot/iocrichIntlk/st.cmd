#!../../bin/linux-x86_64/cRioIntlk

## You may have to change cRioIntlk to something else
## everywhere it appears in this file

< envPaths

epicsEnvSet("EPICS_CA_AUTO_ADDR_LIST","NO")
epicsEnvSet("EPICS_CA_ADDR_LIST","129.57.160.79 129.57.163.255")
epicsEnvSet("EPICS_CAS_BEACON_ADDR_LIST","129.57.163.255")

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/cRioIntlk.dbd"
cRioIntlk_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")
dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

dbLoadRecords("db/richIntlk.db")
dbLoadRecords("db/richIntlk-S1EP.db")
dbLoadRecords("db/richIntlk-sums.db")

dbLoadRecords("db/cRIO_heartbeat_bi.db","P=B_HW_, R=CRIO_RICH_, DLY=60")
dbLoadRecords("db/cRIO_heartbeat_bi.db","P=B_HW_, R=CRIO_RICH_S1_EP_, DLY=60")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit();

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list


