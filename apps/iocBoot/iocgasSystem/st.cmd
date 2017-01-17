#!../../bin/linux-x86_64/cRio

## You may have to change bom to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/cRio.dbd")
cRio_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")
## cRIO heartbeat alarms
dbLoadRecords("db/cRIO_heartbeat.db",   "P=B_HW_, R=CRIO_FC_,   DLY=60")
dbLoadRecords("db/cRIO_heartbeat.db",   "P=B_HW_, R=CRIO_GS_,   DLY=60")
dbLoadRecords("db/cRIO_heartbeat.db",   "P=B_HW_, R=CRIO_SF_,   DLY=60")
# dbLoadRecords("db/cRIO_heartbeat.db",   "P=B_HW_, R=CRIO_DEV_,  DLY=60")
# dbLoadRecords("db/cRIO_heartbeat.db",   "P=B_HW_, R=CRIO_HTCC_, DLY=60")
# dbLoadRecords("db/cRIO_heartbeat.db",   "P=B_HW_, R=CRIO_SVT_,  DLY=60")
## Detector Systems
dbLoadRecords("db/gas_cRIO_DC.db",      "P=B_DET_,R=DC_GAS_")
dbLoadRecords("db/gas_cRIO_FTC.db",     "P=B_DET_,R=FTC_GAS_")
# dbLoadRecords("db/gas_cRIO_HTCC.db",    "P=B_DET_,R=HTCC_GAS_")
dbLoadRecords("db/gas_cRIO_LTCC.db",    "P=B_DET_,R=LTCC_GAS_")
dbLoadRecords("db/gas_cRIO_LTCC_SEC.db","P=B_DET_,R=LTCC_GAS_,SEC=S1_")
dbLoadRecords("db/gas_cRIO_LTCC_SEC.db","P=B_DET_,R=LTCC_GAS_,SEC=S2_")
dbLoadRecords("db/gas_cRIO_LTCC_SEC.db","P=B_DET_,R=LTCC_GAS_,SEC=S3_")
dbLoadRecords("db/gas_cRIO_LTCC_SEC.db","P=B_DET_,R=LTCC_GAS_,SEC=S4_")
dbLoadRecords("db/gas_cRIO_LTCC_SEC.db","P=B_DET_,R=LTCC_GAS_,SEC=S5_")
dbLoadRecords("db/gas_cRIO_LTCC_SEC.db","P=B_DET_,R=LTCC_GAS_,SEC=S6_")
dbLoadRecords("db/gas_cRIO_RICH.db",    "P=B_DET_,R=RICH_GAS_")
# dbLoadRecords("db/gas_cRIO_SVT.db",     "P=B_DET_,R=SVT_GAS_")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

dbl > pv.list
iocInit

## autosave startup
## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=xxx:")
create_monitor_set("info_settings.req", 30, "P=xxx:")

