//#!../../bin/linux-x86_64/agilent

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/agilent.dbd"
agilent_registerRecordDeviceDriver pdbbase

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

drvAsynIPPortConfigure("${PORT}",${GPIB}.jlab.org:1234,0,0,0)

dbLoadRecords("db/A6551.db","SCAN=${SCAN},P=B_DET_DC_LV_${SECREG},PORT=${PORT},ADDR=${ADDR},IMAX=2000,OMAX=2000")

dbLoadRecords("db/prologix.db","P=${GPIB},R=:,DESC=DCLV_${PORT},PORT=${PORT}")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

asSetFilename("../acf/cas.acf")

iocInit();

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

