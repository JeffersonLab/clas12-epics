#!../../bin/linux-x86_64/A6551

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/A6551.dbd"
A6551_registerRecordDeviceDriver pdbbase

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

## Configure devices


#OLD:
#drvAsynIPPortConfigure("L0",129.57.160.95:1234,0,0,0)
#drvAsynIPPortConfigure("L0",129.57.160.108:1234,0,0,0)
#asynSetTraceMask("L0",-1,0x09)
#asynSetTraceIOMask("L0",-1,0x02)
#asynOctetSetOutputEos("L0",0,"\r\n")
#asynOctetSetInputEos("L0",0,"\n")
#dbLoadRecords("db/A6551.db","S=1,L=1,PORT=L0,ADDR=24,IMAX=2000,OMAX=2000")


# TEMPORARY in EEL125:
#drvAsynIPPortConfigure("L0",129.57.86.140:1234,0,0,0)
#dbLoadRecords("db/A6551.db","P=B_DET_DC_LV_SEC5_R1,PORT=L0,ADDR=24,IMAX=2000,OMAX=2000")
#asynOctetSetOutputEos("L0",0,"\r\n")
#asynOctetSetInputEos("L0",0,"\n")



## Call one for each with sector, layer and GPIB ID

drvAsynIPPortConfigure("L0",hallb-gpib04.jlab.org:1234,0,0,0)

#dbLoadRecords("db/asynRecord.db","P=DCLV,R=:ASYN,PORT=L0,ADDR=1,IMAX=2000,OMAX=2000")

dbLoadRecords("db/A6551.db","P=DCLV,PORT=L0,ADDR=1,IMAX=2000,OMAX=2000")

#asynOctetSetOutputEos("L0",0,"\r\n")
asynOctetSetOutputEos("L0",0,"\r")
asynOctetSetInputEos("L0",0,"\n")
asynSetTraceMask("L0",-1,0x09)
asynSetTraceIOMask("L0",-1,0x02)



##drvAsynIPPortConfigure("00",hallb-gpib00.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("01",hallb-gpib01.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("02",hallb-gpib02.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("03",hallb-gpib03.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("04",hallb-gpib04.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("05",hallb-gpib05.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("06",hallb-gpib06.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("07",hallb-gpib07.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("08",hallb-gpib08.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("09",hallb-gpib09.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("10",hallb-gpib10.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("11",hallb-gpib11.jlab.org:1234,0,0,0)
##drvAsynIPPortConfigure("12",hallb-gpib12.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("13",hallb-gpib13.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("14",hallb-gpib14.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("15",hallb-gpib15.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("16",hallb-gpib16.jlab.org:1234,0,0,0)
##drvAsynIPPortConfigure("17",hallb-gpib17.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("18",hallb-gpib18.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("19",hallb-gpib19.jlab.org:1234,0,0,0)
#drvAsynIPPortConfigure("20",hallb-gpib20.jlab.org:1234,0,0,0)
##drvAsynIPPortConfigure("21",hallb-gpib21.jlab.org:1234,0,0,0)

#dbLoadTemplate("db/dclv.substitutions")

#dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")
#dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

cd ${TOP}/iocBoot/${IOC}

iocInit();

#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=${IOC}:")
#create_monitor_set("info_settings.req", 30, "P=${IOC}:")
#create_monitor_set("dclv_settings.req",30,"P=HPSECALLV")

