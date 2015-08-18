#!../../bin/linux-x86/plc2epics

< envPaths

# This is a prefix for all PVs on this IOC in case we want a second instance
epicsEnvSet("PREF","HPS_SVT:PLC")

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/plc2epics.dbd"
plc2epics_registerRecordDeviceDriver pdbbase

# Initialize EtherIP driver, define PLCs
EIP_buffer_limit(450)
drvEtherIP_init()
drvEtherIP_define_PLC("${PREF}", "hpsplc", 0)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db","IOC=iocsvtPlc")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")
dbLoadRecords("db/HPS_SVT_Interlock_v5_PLCin.db","IOC=${PREF}:i,PLCID=${PREF}")
dbLoadRecords("db/HPS_SVT_Interlock_v5_PLCout.db","IOC=${PREF}:o,PLCID=${PREF}")

cd ${TOP}/iocBoot/${IOC}

## autosave setup
< save_restore.cmd

iocInit

# autosave startup
create_monitor_set("HPS_SVT_Interlocks.req", 30, "PREF=${PREF}")

# Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=xxx:")
create_monitor_set("info_settings.req", 30, "P=xxx:")
