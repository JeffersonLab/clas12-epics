#!../../bin/linux-x86_64/amq
#This file was created by using the command "awk -f makeIocs.gk clasrun.clasprod.daq.HallB_DAQ.dat" on Wed Dec  6 17:35:35 EST 2017

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.daq.HallB_DAQ")


dbLoadTemplate("db/amqSvt.substitutions")

dbLoadRecords("db/waveformApp.db","P=B_SVT_DAQ_,R=STRIPRATE_R1:topAvg:,NELM=42,FTVL=FLOAT,PERIOD=5,FNAME=wflist-r1-top.txt")
dbLoadRecords("db/waveformApp.db","P=B_SVT_DAQ_,R=STRIPRATE_R1:botAvg:,NELM=42,FTVL=FLOAT,PERIOD=5,FNAME=wflist-r1-bot.txt")
dbLoadRecords("db/waveformApp.db","P=B_SVT_DAQ_,R=STRIPRATE_R2:topAvg:,NELM=42,FTVL=FLOAT,PERIOD=5,FNAME=wflist-r2-top.txt")
dbLoadRecords("db/waveformApp.db","P=B_SVT_DAQ_,R=STRIPRATE_R2:botAvg:,NELM=42,FTVL=FLOAT,PERIOD=5,FNAME=wflist-r2-bot.txt")
dbLoadRecords("db/waveformApp.db","P=B_SVT_DAQ_,R=STRIPRATE_R3:topAvg:,NELM=42,FTVL=FLOAT,PERIOD=5,FNAME=wflist-r3-top.txt")
dbLoadRecords("db/waveformApp.db","P=B_SVT_DAQ_,R=STRIPRATE_R3:botAvg:,NELM=42,FTVL=FLOAT,PERIOD=5,FNAME=wflist-r3-bot.txt")
dbLoadRecords("db/waveformApp.db","P=B_SVT_DAQ_,R=STRIPRATE:chip:max:,NELM=168,FTVL=FLOAT,PERIOD=5,FNAME=wflist-max.txt")

dbLoadRecords("db/amqSvt-calc-slot.db","CRATE=SVT1,SUFFIX=SEMERROR")
dbLoadRecords("db/amqSvt-calc-slot.db","CRATE=SVT2,SUFFIX=SEMERROR")
dbLoadRecords("db/amqSvt-calc-slot.db","CRATE=SVT1,SUFFIX=SEMSTATE")
dbLoadRecords("db/amqSvt-calc-slot.db","CRATE=SVT2,SUFFIX=SEMSTATE")

dbLoadRecords("db/amqSvt-rate-alarm.db")

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

#Need this to start responding to messages after all records are defined
StartMQ()

seq waveform, "P=B_SVT_DAQ_,R=STRIPRATE_R1:topAvg:"
seq waveform, "P=B_SVT_DAQ_,R=STRIPRATE_R1:botAvg:"
seq waveform, "P=B_SVT_DAQ_,R=STRIPRATE_R2:topAvg:"
seq waveform, "P=B_SVT_DAQ_,R=STRIPRATE_R2:botAvg:"
seq waveform, "P=B_SVT_DAQ_,R=STRIPRATE_R3:topAvg:"
seq waveform, "P=B_SVT_DAQ_,R=STRIPRATE_R3:botAvg:"
seq waveform, "P=B_SVT_DAQ_,R=STRIPRATE:chip:max:"

dbl > pv.list
