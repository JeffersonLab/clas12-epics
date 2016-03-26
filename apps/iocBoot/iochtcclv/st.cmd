#!../../bin/linux-x86_64/sy2604

## You may have to change sy2604 to something else
## everywhere it appears in this file

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/sy2604.dbd"
sy2604_registerRecordDeviceDriver pdbbase

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

## Configure devices

drvAsynIPPortConfigure("1",129.57.86.129:10001,0,0,0)
#drvAsynIPPortConfigure("2",129.57.86.130:10001,0,0,0)
#drvAsynIPPortConfigure("3",129.57.86.132:10001,0,0,0)
#drvAsynIPPortConfigure("4",129.57.86.133:10001,0,0,0)
#drvAsynIPPortConfigure("5",129.57.86.134:10001,0,0,0)
#drvAsynIPPortConfigure("6",129.57.86.135:10001,0,0,0)
#drvAsynIPPortConfigure("7",129.57.86.136:10001,0,0,0)
#drvAsynIPPortConfigure("8",129.57.86.137:10001,0,0,0)

#asynSetTraceMask("1",-1,0x09)
#asynSetTraceIOMask("1",-1,0x02)
#asynOctetSetOutputEos("1",0,"\r")
#asynOctetSetInputEos("1",0,"\r")

## Load record instances
dbLoadRecords("db/sy2604.db","P=htcclv1,PORT=1,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/sy2604.db","P=htcclv2,PORT=2,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/sy2604.db","P=htcclv3,PORT=3,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/sy2604.db","P=htcclv4,PORT=4,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/sy2604.db","P=htcclv5,PORT=5,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/sy2604.db","P=htcclv6,PORT=6,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/sy2604.db","P=htcclv7,PORT=7,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/sy2604.db","P=htcclv8,PORT=8,ADDR=24,IMAX=2000,OMAX=2000")


#dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")
#dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")


cd ${TOP}/iocBoot/${IOC}

#< save_restore.cmd

iocInit();

#makeAutosaveFiles()
#create_monitor_set("sy2604_settings.req",30,"P=HPSECALLV")

