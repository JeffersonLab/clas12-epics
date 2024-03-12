#!../../bin/linux-x86_64/dcPower

< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

cd "${TOP}"

dbLoadDatabase("dbd/dcPower.dbd")
dcPower_registerRecordDeviceDriver(pdbbase)

drvAsynIPPortConfigure("L2",hallb-moxa6.jlab.org:4002)

#asynSetTraceMask("L2",-1,0x9)
#asynSetTraceIOMask("L2",-1,0x3)

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", "IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:"

dbLoadRecords("db/asynRecord.db","P=NABO,R=:ASYN,PORT=L2,ADDR=1,IMAX=2000,OMAX=2000")

dbLoadTemplate("db/magflow.substitutions")

cd "${TOP}/iocBoot/${IOC}"

< ../save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

