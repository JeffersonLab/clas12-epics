#!../../bin/linux-x86_64/cRioIntlk

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

dbLoadRecords("db/ftIntlkHard.db")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit();

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list


