#!../../bin/linux-x86_64/lakeshore450

< envPaths

epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/lakeshore450.dbd"
lakeshore450_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

drvAsynIPPortConfigure("GPIB0",hallb-gpib22.jlab.org:1234,0,0,0)

#dbLoadRecords("db/prologix.db","P=GPIB0,R=:,DESC=asdf,PORT=GPIB0")
dbLoadRecords("db/lakeshore450.db","P=B_TAGGER_,R=HALLPROBE:,PORT=GPIB0")

cd ${TOP}/iocBoot/${IOC}

dbLoadRecords("alias")

< save_restore.cmd

iocInit();

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

