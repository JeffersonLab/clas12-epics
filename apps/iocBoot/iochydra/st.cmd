#!../../bin/linux-x86_64/amq

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

dbLoadRecords("db/waveformApp.db","P=HB:monitoring:ai:,R=,FNAME=./waveform.txt,PERIOD=10,NELM=87,FTVL=DOUBLE")
dbLoadTemplate("db/hydra.substitutions")

cd ${TOP}/iocBoot/${IOC}

< ../save_restore.cmd

iocInit();

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

seq waveform, "P=HB:monitoring:ai:,R="

dbl > pv.list

