#!../../bin/linux-x86_64/A6551

< envPaths

< dclvAddresses.env

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/A6551.dbd"
A6551_registerRecordDeviceDriver pdbbase

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

drvAsynIPPortConfigure("S1R2",${GPIBS1R1}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S2R2",${GPIBS2R1}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S3R2",${GPIBS3R1}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S4R2",${GPIBS4R1}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S5R2",${GPIBS5R1}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S6R2",${GPIBS6R1}.jlab.org:1234,0,0,0)

dbLoadRecords("db/A6551.db","SCAN=10 second,P=B_DET_DC_LV_SEC1_R2,PORT=S1R1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=10 second,P=B_DET_DC_LV_SEC2_R2,PORT=S2R1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=10 second,P=B_DET_DC_LV_SEC3_R2,PORT=S3R1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=10 second,P=B_DET_DC_LV_SEC4_R2,PORT=S4R1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=10 second,P=B_DET_DC_LV_SEC5_R2,PORT=S5R1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=10 second,P=B_DET_DC_LV_SEC6_R2,PORT=S6R1,ADDR=1,IMAX=2000,OMAX=2000")

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

