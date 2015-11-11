#!../../bin/linux-x86_64/prologix
################################################################################
< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")
################################################################################
cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/prologix.dbd")
prologix_registerRecordDeviceDriver(pdbbase)

drvAsynIPPortConfigure("ETH1",  "hallb-gpib01:1234")
drvAsynIPPortConfigure("ETH2",  "hallb-gpib02:1234")
drvAsynIPPortConfigure("ETH3",  "hallb-gpib03:1234")
drvAsynIPPortConfigure("ETH4",  "hallb-gpib04:1234")
drvAsynIPPortConfigure("ETH5",  "hallb-gpib05:1234")
drvAsynIPPortConfigure("ETH6",  "hallb-gpib06:1234")
drvAsynIPPortConfigure("ETH7",  "hallb-gpib07:1234")
drvAsynIPPortConfigure("ETH8",  "hallb-gpib08:1234")
drvAsynIPPortConfigure("ETH9",  "hallb-gpib09:1234")
drvAsynIPPortConfigure("ETH10", "hallb-gpib10:1234")
drvAsynIPPortConfigure("ETH11", "hallb-gpib11:1234")
drvAsynIPPortConfigure("ETH12", "hallb-gpib12:1234")
drvAsynIPPortConfigure("ETH13", "hallb-gpib13:1234")
drvAsynIPPortConfigure("ETH14", "hallb-gpib14:1234")
drvAsynIPPortConfigure("ETH15", "hallb-gpib15:1234")
drvAsynIPPortConfigure("ETH16", "hallb-gpib16:1234")
drvAsynIPPortConfigure("ETH17", "hallb-gpib17:1234")
drvAsynIPPortConfigure("ETH18", "hallb-gpib18:1234")

## debugging...
#asynSetTraceMask("ETH1",-1,0x09)
#asynSetTraceIOMask("ETH1",-1,0x02)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")

cd ${TOP}/iocBoot/${IOC}
dbLoadTemplate("prologix.substitutions")

## autosave setup
< save_restore.cmd

dbl > pv.list
iocInit

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")
create_monitor_set("prologixAll_settings.req", 30, "P=HB:GPIB:")

