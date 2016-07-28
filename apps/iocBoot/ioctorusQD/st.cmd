#!../../bin/linux-x86_64/plc2epics
############################################################################
< envPaths
epicsEnvSet("EPICS_CA_ADDR_LIST", "129.57.96.26")
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/plc2epics.dbd")
plc2epics_registerRecordDeviceDriver(pdbbase)

## Initialize EtherIP driver, defined PLCs
drvEtherIP_init()
drvEtherIP_define_PLC("PLC_TORUS", "129.57.96.15", 0)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")
dbLoadTemplate("db/torus_quench.substitutions")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

dbl > pv.list
iocInit

## autosave startup
## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

