#!../../bin/linux-x86_64/keysight

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/keysight.dbd"
keysight_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","100000")

## Configure devices

drvAsynIPPortConfigure("L0",hallb-rasterdriver-1:5025,0,0,0)
drvAsynIPPortConfigure("L1",hallb-moxa6:4007,0,0,0)
drvAsynIPPortConfigure("L2",hallb-moxa6:4008,0,0,0)

#asynSetTraceMask("L2",-1,0x09)
#asynSetTraceIOMask("L2",-1,0x02)

asynOctetSetOutputEos("L0",0,"\n")
asynOctetSetInputEos( "L0",0,"\n")
asynOctetSetOutputEos("L1",0,"\r")
asynOctetSetInputEos( "L1",0,"\n\r")
asynOctetSetOutputEos("L2",0,"\r")
asynOctetSetInputEos( "L2",0,"\n\r")

dbLoadRecords("db/asynRecord.db","P=B_RASTER:DRV, R=:ASYN,PORT=L0,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/asynRecord.db","P=B_RASTER:PS:X,R=:ASYN,PORT=L1,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/asynRecord.db","P=B_RASTER:PS:Y,R=:ASYN,PORT=L2,ADDR=1,IMAX=2000,OMAX=2000")

dbLoadRecords("db/A33500.db","TAG=B_RASTER:DRV:,PORT=L0,L=HB"))

dbLoadTemplate("db/raster-magnets.substitutions")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

dbpf("B_RASTER:DRV:WG_XAMPL.DRVL","-4.5")
dbpf("B_RASTER:DRV:WG_XAMPL.DRVH", "4.5")
dbpf("B_RASTER:DRV:WG_YAMPL.DRVL","-4.5")
dbpf("B_RASTER:DRV:WG_YAMPL.DRVH", "4.5")

dbpf("B_RASTER:DRV:WG_XVOFF.DRVL","-1.0")
dbpf("B_RASTER:DRV:WG_XVOFF.DRVH", "1.0")
dbpf("B_RASTER:DRV:WG_YVOFF.DRVL","-1.0")
dbpf("B_RASTER:DRV:WG_YVOFF.DRVH", "1.0")

