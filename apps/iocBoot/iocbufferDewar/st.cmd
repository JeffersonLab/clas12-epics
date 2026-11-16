#!../../bin/linux-x86_64/siemens
############################################################################
< envPaths
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/siemens.dbd")
siemens_registerRecordDeviceDriver(pdbbase)

## Initialize S7 driver, define PLCs:
s7nodaveConfigureIsoTcpPort("PLC_BUFDEW", "129.57.160.84", 0,0,0)
s7nodaveConfigurePollGroup("PLC_BUFDEW", "default", 2.0, 0)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
#dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")

dbLoadRecords("db/bufdew.db","PLCID=PLC_BUFDEW")
dbLoadTemplate("db/bufdew_cpid.substitutions")

cd ${TOP}/iocBoot/${IOC}

## autosave setup
#< save_restore.cmd

dbl > pv.list

iocInit

## autosave startup
## Handle autosave 'commands' contained in loaded databases.
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=xxx:")
#create_monitor_set("info_settings.req", 30, "P=xxx:")
#create_monitor_set("torus_mps_settings.req", 30, "P=B_TORUS:,R=MPS:")

