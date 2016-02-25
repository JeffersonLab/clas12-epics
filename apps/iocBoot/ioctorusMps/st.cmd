#!../../bin/linux-x86/plc2epics

< envPaths

# This is a prefix for all PVs on this IOC in case we want a second instance
epicsEnvSet("PLC","TORUS_PLC")

cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/plc2epics.dbd")
plc2epics_registerRecordDeviceDriver(pdbbase)

# Initialize EtherIP driver, define PLCs
#EIP_buffer_limit(450)
drvEtherIP_init()
#drvEtherIP_define_PLC("${PLC}", "129.57.36.159", 0)
drvEtherIP_define_PLC("${PLC}", "129.57.96.15", 0)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")
dbLoadRecords("db/torus_mps.db","P=TORUS:,R=MPS:,PLCID=${PLC}")

cd ${TOP}/iocBoot/${IOC}

## autosave setup
< save_restore.cmd

iocInit

## autosave startup
## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=xxx:")
create_monitor_set("info_settings.req", 30, "P=xxx:")
create_monitor_set("torus_mps_settings.req", 30, "P=TORUS:,R=MPS:")

