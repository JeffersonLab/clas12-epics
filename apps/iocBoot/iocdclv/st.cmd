#!../../bin/linux-x86_64/A6551

< envPaths

< dclvAddresses.env

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/A6551.dbd"
A6551_registerRecordDeviceDriver pdbbase

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

epicsEnvSet("scan","10 second")

drvAsynIPPortConfigure("S1R1",${GPIBS1R1}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S1R2",${GPIBS1R2}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S1R3",${GPIBS1R3}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S2R1",${GPIBS2R1}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S2R2",${GPIBS2R2}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S2R3",${GPIBS2R3}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S3R1",${GPIBS3R1}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S3R2",${GPIBS3R2}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S3R3",${GPIBS3R3}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S4R1",${GPIBS4R1}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S4R2",${GPIBS4R2}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S4R3",${GPIBS4R3}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S5R1",${GPIBS5R1}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S5R2",${GPIBS5R2}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S5R3",${GPIBS5R3}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S6R1",${GPIBS6R1}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S6R2",${GPIBS6R2}.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S6R3",${GPIBS6R3}.jlab.org:1234,0,0,0)

dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC1_R1,PORT=S1R1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC1_R2,PORT=S1R2,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC1_R3,PORT=S1R3,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC2_R1,PORT=S2R1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC2_R2,PORT=S2R2,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC2_R3,PORT=S2R3,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC3_R1,PORT=S3R1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC3_R2,PORT=S3R2,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC3_R3,PORT=S3R3,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC4_R1,PORT=S4R1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC4_R2,PORT=S4R2,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC4_R3,PORT=S4R3,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC5_R1,PORT=S5R1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC5_R2,PORT=S5R2,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC5_R3,PORT=S5R3,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC6_R1,PORT=S6R1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC6_R2,PORT=S6R2,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC6_R3,PORT=S6R3,ADDR=1,IMAX=2000,OMAX=2000")

#dbLoadRecords("db/prologix.db","P=${GPIBS1R1},R=:,DESC=DCLV_S1R1,PORT=S1R1,")
#dbLoadRecords("db/prologix.db","P=${GPIBS1R2},R=:,DESC=DCLV_S1R2,PORT=S1R2,")
#dbLoadRecords("db/prologix.db","P=${GPIBS1R3},R=:,DESC=DCLV_S1R3,PORT=S1R3,")
#dbLoadRecords("db/prologix.db","P=${GPIBS2R1},R=:,DESC=DCLV_S2R1,PORT=S2R1,")
#dbLoadRecords("db/prologix.db","P=${GPIBS2R2},R=:,DESC=DCLV_S2R2,PORT=S2R2,")
#dbLoadRecords("db/prologix.db","P=${GPIBS2R3},R=:,DESC=DCLV_S2R3,PORT=S2R3,")
#dbLoadRecords("db/prologix.db","P=${GPIBS3R1},R=:,DESC=DCLV_S3R1,PORT=S3R1,")
#dbLoadRecords("db/prologix.db","P=${GPIBS3R2},R=:,DESC=DCLV_S3R2,PORT=S3R2,")
#dbLoadRecords("db/prologix.db","P=${GPIBS3R3},R=:,DESC=DCLV_S3R3,PORT=S3R3,")
#dbLoadRecords("db/prologix.db","P=${GPIBS4R1},R=:,DESC=DCLV_S4R1,PORT=S4R1,")
#dbLoadRecords("db/prologix.db","P=${GPIBS4R2},R=:,DESC=DCLV_S4R2,PORT=S4R2,")
#dbLoadRecords("db/prologix.db","P=${GPIBS4R3},R=:,DESC=DCLV_S4R3,PORT=S4R3,")
#dbLoadRecords("db/prologix.db","P=${GPIBS5R1},R=:,DESC=DCLV_S5R1,PORT=S5R1,")
#dbLoadRecords("db/prologix.db","P=${GPIBS5R2},R=:,DESC=DCLV_S5R2,PORT=S5R2,")
#dbLoadRecords("db/prologix.db","P=${GPIBS5R3},R=:,DESC=DCLV_S5R3,PORT=S5R3,")
#dbLoadRecords("db/prologix.db","P=${GPIBS6R1},R=:,DESC=DCLV_S6R1,PORT=S6R1,")
#dbLoadRecords("db/prologix.db","P=${GPIBS6R2},R=:,DESC=DCLV_S6R2,PORT=S6R2,")
#dbLoadRecords("db/prologix.db","P=${GPIBS6R3},R=:,DESC=DCLV_S6R3,PORT=S6R3,")

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

