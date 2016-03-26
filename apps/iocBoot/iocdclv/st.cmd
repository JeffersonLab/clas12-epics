#!../../bin/linux-x86_64/A6551

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/A6551.dbd"
A6551_registerRecordDeviceDriver pdbbase

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

## Configure devices
#drvAsynIPPortConfigure("L0",129.57.160.95:1234,0,0,0)
drvAsynIPPortConfigure("L0",129.57.160.108:1234,0,0,0)

#asynSetTraceMask("L0",-1,0x09)
#asynSetTraceIOMask("L0",-1,0x02)
#asynOctetSetOutputEos("L0",0,"\r\n")
#asynOctetSetInputEos("L0",0,"\n")

dbLoadRecords("db/A6551.db","S=1,L=1,PORT=L0,ADDR=24,IMAX=2000,OMAX=2000")




## Call one for each with sector, layer and GPIB ID
#drvAsynIPPortConfigure("00",129.57.160.95:1234,0,0,0)
#drvAsynIPPortConfigure("01",129.57.160.96:1234,0,0,0)
#drvAsynIPPortConfigure("02",129.57.160.97:1234,0,0,0)
#drvAsynIPPortConfigure("03",129.57.160.98:1234,0,0,0)
#drvAsynIPPortConfigure("04",129.57.160.99:1234,0,0,0)
#drvAsynIPPortConfigure("05",129.57.160.100:1234,0,0,0)
#drvAsynIPPortConfigure("06",129.57.160.101:1234,0,0,0)
#drvAsynIPPortConfigure("07",129.57.160.102:1234,0,0,0)
#drvAsynIPPortConfigure("08",129.57.160.103:1234,0,0,0)
#drvAsynIPPortConfigure("09",129.57.160.104:1234,0,0,0)
#drvAsynIPPortConfigure("10",129.57.160.105:1234,0,0,0)
#drvAsynIPPortConfigure("11",129.57.160.106:1234,0,0,0)
#drvAsynIPPortConfigure("12",129.57.160.107:1234,0,0,0)
#drvAsynIPPortConfigure("13",129.57.160.108:1234,0,0,0)
#drvAsynIPPortConfigure("14",129.57.160.109:1234,0,0,0)
#drvAsynIPPortConfigure("15",129.57.160.110:1234,0,0,0)
#drvAsynIPPortConfigure("16",129.57.160.111:1234,0,0,0)
#drvAsynIPPortConfigure("17",129.57.160.112:1234,0,0,0)
##drvAsynIPPortConfigure("18",129.57.160.113:1234,0,0,0)
##drvAsynIPPortConfigure("19",129.57.160.114:1234,0,0,0)
##drvAsynIPPortConfigure("20",129.57.160.115:1234,0,0,0)


#dbLoadRecords("db/A6551.db","S=1,L=1,PORT=00,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=1,L=2,PORT=01,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=1,L=3,PORT=02,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=2,L=1,PORT=03,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=2,L=2,PORT=04,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=2,L=3,PORT=05,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=3,L=1,PORT=06,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=3,L=2,PORT=07,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=3,L=3,PORT=08,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=4,L=1,PORT=09,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=4,L=2,PORT=10,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=4,L=3,PORT=11,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=5,L=1,PORT=12,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=5,L=2,PORT=13,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=5,L=3,PORT=14,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=6,L=1,PORT=15,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=6,L=2,PORT=16,ADDR=24,IMAX=2000,OMAX=2000")
#dbLoadRecords("db/A6551.db","S=6,L=3,PORT=17,ADDR=24,IMAX=2000,OMAX=2000")

#dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")
#dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

cd ${TOP}/iocBoot/${IOC}

iocInit();

#makeAutosaveFiles()
#create_monitor_set("A6551_settings.req",30,"P=HPSECALLV")

