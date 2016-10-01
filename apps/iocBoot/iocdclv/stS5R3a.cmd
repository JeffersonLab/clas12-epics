#!../../bin/linux-x86_64/A6551

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/A6551.dbd"
A6551_registerRecordDeviceDriver pdbbase

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

epicsEnvSet("scan","10 second")

#drvAsynIPPortConfigure("S1R1",hallb-gpib02.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S1R2",hallb-gpib05.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S1R3",hallb-gpib08.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S2R1",hallb-gpib03.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S2R2",hallb-gpib06.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S2R3",hallb-gpib09.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S3R1",hallb-gpib19.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S3R2",hallb-gpib15.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S3R3",hallb-gpib18.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S4R1",hallb-gpib11.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S4R2",hallb-gpib14.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S4R3",hallb-gpib20.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S5R1",hallb-gpib10.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S5R2",hallb-gpib13.jlab.org:1234,0,0,0)
drvAsynIPPortConfigure("S5R3",hallb-gpib16.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S6R1",hallb-gpib01.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S6R2",hallb-gpib04.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("S6R3",hallb-gpib07.jlab.org:1234,0,0,0)

#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC1_R1,PORT=S1R1,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC1_R2,PORT=S1R2,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC1_R3,PORT=S1R3,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC2_R1,PORT=S2R1,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC2_R2,PORT=S2R2,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC2_R3,PORT=S2R3,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC3_R1,PORT=S3R1,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC3_R2,PORT=S3R2,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC3_R3,PORT=S3R3,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC4_R1,PORT=S4R1,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC4_R2,PORT=S4R2,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC4_R3,PORT=S4R3,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC5_R1,PORT=S5R1,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC5_R2,PORT=S5R2,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC5_R3,PORT=S5R3,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC6_R1,PORT=S6R1,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC6_R2,PORT=S6R2,ADDR=1,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","SCAN=${scan},P=B_DET_DC_LV_SEC6_R3,PORT=S6R3,ADDR=1,IMAX=2000,OMAX=2000")

#dbLoadRecords("db/prologix.db","P=hallb-gpib02,R=:,DESC=DCLV_S1R1,PORT=S1R1,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib05,R=:,DESC=DCLV_S1R2,PORT=S1R2,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib08,R=:,DESC=DCLV_S1R3,PORT=S1R3,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib03,R=:,DESC=DCLV_S2R1,PORT=S2R1,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib06,R=:,DESC=DCLV_S2R2,PORT=S2R2,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib09,R=:,DESC=DCLV_S2R3,PORT=S2R3,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib19,R=:,DESC=DCLV_S3R1,PORT=S3R1,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib15,R=:,DESC=DCLV_S3R2,PORT=S3R2,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib18,R=:,DESC=DCLV_S3R3,PORT=S3R3,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib11,R=:,DESC=DCLV_S4R1,PORT=S4R1,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib14,R=:,DESC=DCLV_S4R2,PORT=S4R2,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib20,R=:,DESC=DCLV_S4R3,PORT=S4R3,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib10,R=:,DESC=DCLV_S5R1,PORT=S5R1,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib13,R=:,DESC=DCLV_S5R2,PORT=S5R2,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib16,R=:,DESC=DCLV_S5R3,PORT=S5R3,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib01,R=:,DESC=DCLV_S6R1,PORT=S6R1,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib04,R=:,DESC=DCLV_S6R2,PORT=S6R2,")
#dbLoadRecords("db/prologix.db","P=hallb-gpib07,R=:,DESC=DCLV_S6R3,PORT=S6R3,")

cd ${TOP}/iocBoot/${IOC}

iocInit();

