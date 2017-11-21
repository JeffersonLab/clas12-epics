#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("0","ADCCTOF1")
Start_SCALERS_CRATE("1","ADCFT1")
Start_SCALERS_CRATE("2","ADCFT2")
Start_SCALERS_CRATE("3","ADCFT3")
Start_SCALERS_CRATE("4","ADCCND1")


## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

dbLoadTemplate("db/jscalers_CTOF_FADC.substitutions")
dbLoadTemplate("db/jscalers_HTCC_FADC.substitutions")

dbLoadTemplate("db/jscalers_FTC_FADC.substitutions")
dbLoadTemplate("db/jscalers_FTH_FADC.substitutions")

dbLoadTemplate("db/jscalers_CND_FADC.substitutions")

dbLoadRecords("db/jscalers_wfC.db")
dbLoadRecords("db/jscalers_wf_averagesC.db")

dbLoadRecords("db/waveformApp.db","P=B_DET_FTC_,R=FADC:,  NELM=332,FTVL=FLOAT,PERIOD=1, FNAME=ftcfadc.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_FTC_,R=FADC:t:,NELM=332,FTVL=FLOAT,PERIOD=30,FNAME=ftcfadcT.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_FTH_,R=FADC:,  NELM=232,FTVL=FLOAT,PERIOD=1, FNAME=fthfadc.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_FTH_,R=FADC:t:,NELM=232,FTVL=FLOAT,PERIOD=30,FNAME=fthfadcT.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_CND_,R=FADC:,  NELM=144,FTVL=FLOAT,PERIOD=1, FNAME=cndfadc.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_CND_,R=FADC:t:,NELM=144,FTVL=FLOAT,PERIOD=1, FNAME=cndfadcT.txt")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

seq seqJscalersC

seq waveform, "P=B_DET_FTC_,R=FADC:"
seq waveform, "P=B_DET_FTC_,R=FADC:t:"
seq waveform, "P=B_DET_FTH_,R=FADC:"
seq waveform, "P=B_DET_FTH_,R=FADC:t:"
seq waveform, "P=B_DET_CND_,R=FADC:"
seq waveform, "P=B_DET_CND_,R=FADC:t:"

dbl > pv.list

