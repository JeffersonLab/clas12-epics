//#!../../bin/linux-x86_64/A6551

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/A6551.dbd"
A6551_registerRecordDeviceDriver pdbbase

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

epicsEnvSet("SCAN","2 second")

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

drvAsynIPPortConfigure("${PORT}",${GPIB}.jlab.org:1234,0,0,0)

dbLoadRecords("db/A6551.db","SCAN=${SCAN},P=B_DET_DC_LV_${SECREG},PORT=${PORT},ADDR=1,IMAX=2000,OMAX=2000")

dbLoadRecords("db/prologix.db","P=${GPIB},R=:,DESC=DCLV_${PORT},PORT=${PORT}")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit();

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

