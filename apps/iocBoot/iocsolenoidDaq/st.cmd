#!../../bin/linux-x86_64/wf2root
############################################################################
< envPaths
# TODO: set IP
epicsEnvSet("EPICS_CA_ADDR_LIST", "129.57.96.18")
# for 10K long arrays:
#epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES", "40000")
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/wf2root.dbd")
wf2root_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")
#
dbLoadTemplate("iocBoot/${IOC}/wf2root.substitutions")
#dbLoadTemplate("iocBoot/${IOC}/wf2root-10K.substitutions")

dbLoadRecords("db/cRIO_heartbeat.db","P=B_HW_,R=CRIO_SOLDAQ_,DLY=60")

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
create_monitor_set("wf2root_settings.req", 30, "P=B_SOL:DAQ_REC:")

