#!../../bin/linux-x86_64/srsApp

< envPaths

epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES",1000000)
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/srsApp.dbd"
srsApp_registerRecordDeviceDriver pdbbase

dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db", "IOC=${IOC}")
#dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")

drvAsynIPPortConfigure("L0","htcc-rga:818",0,0,0)

asynSetTraceMask("L0",-1,0x9)
asynSetTraceIOMask("L0",-1,0x4)

asynOctetSetOutputEos("L0",-1,"\r\n")
asynOctetSetInputEos("L0",-1,"\n\r")

epicsThreadSleep(1)

dbLoadRecords("db/asynRecord.db","P=B_HTCC:,R=RGA,PORT=L0,ADDR=1,IMAX=2000,OMAX=2000")
dbLoadRecords("db/srs-rga.db","P=B_HTCC:,R=RGA,NANA=991,NHIST=100,MODEL=100,PORT=L0")
dbLoadRecords("db/timer.db","P=B_HTCC:,R=RGA")

cd ${TOP}/iocBoot/${IOC}

#< save_restore.cmd

iocInit

#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=${IOC}:")
#create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

