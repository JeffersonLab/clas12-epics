#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/scaler-ped.db","OUT=fcup_offset,P=fcup_offset,RAW=scalerS2b, REF=IPM2C21A,REFMAX=0.1,RAWMAX=500,N=5")
dbLoadRecords("db/scaler-ped.db","OUT=slm_offset, P=slm_offset, RAW=scalerS16b,REF=IPM2C21A,REFMAX=0.1,RAWMAX=500,N=5")

#dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit();

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

