#!../../bin/linux-x86_64/prologix
################################################################################
< envPaths
################################################################################
cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/prologix.dbd")
prologix_registerRecordDeviceDriver(pdbbase)

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

#drvAsynIPPortConfigure("ETH1", "hallb-gpib01:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib02:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib03:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib04:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib05:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib06:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib07:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib08:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib09:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib10:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib11:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib12:1234")
drvAsynIPPortConfigure("ETH1", "hallb-gpib13:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib14:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib15:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib16:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib17:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib18:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib19:1234")
#drvAsynIPPortConfigure("ETH1", "hallb-gpib20:1234")

## debugging...
# GPIB:01
#asynSetTraceMask("ETH1",-1,0x09)
#asynSetTraceIOMask("ETH1",-1,0x02)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")
dbLoadRecords("db/prologix.db", "P=GPIB:,R=01:,PORT=ETH1")

cd ${TOP}/iocBoot/${IOC}

## autosave setup
< save_restore.cmd

dbl > pv.list
iocInit

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")
create_monitor_set("prologix_settings.req", 30, "P=GPIB:,R=01:")

