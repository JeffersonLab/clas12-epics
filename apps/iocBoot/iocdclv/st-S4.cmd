#!../../bin/linux-x86_64/agilent

< envPaths

< dclvAddresses.env

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/agilent.dbd"
agilent_registerRecordDeviceDriver pdbbase

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

drvAsynIPPortConfigure("S4R1",${GPIBS4R1}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S4R2",${GPIBS4R2}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S4R3",${GPIBS4R3}.jlab.org:1234,0,0,0)

dbLoadRecords("db/A6551.db","SCAN=10 second,P=B_DET_DC_LV_SEC4_R1,PORT=S4R1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=10 second,P=B_DET_DC_LV_SEC4_R2,PORT=S4R2,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=10 second,P=B_DET_DC_LV_SEC4_R3,PORT=S4R3,ADDR=1,IMAX=2000,OMAX=2000")

dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")
dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

asSetFilename("../acf/cas.acf")

iocInit();

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

