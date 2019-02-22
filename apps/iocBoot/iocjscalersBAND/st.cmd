#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("5","ADCBAND1")
Start_SCALERS_CRATE("6","TDCBAND1")

## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

dbLoadTemplate("db/jscalers_BAND_FADC.substitutions")
dbLoadTemplate("db/jscalers_BAND_DISC.substitutions")

dbLoadRecords("db/waveformApp.db","P=B_DET_BAND_,R=FADC:, NELM=256,FTVL=FLOAT,PERIOD=1, FNAME=bandfadc.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_BAND_,R=DISC:, NELM=256,FTVL=FLOAT,PERIOD=1, FNAME=banddisc.txt")

dbLoadRecords("db/jscalers_BAND_sums.db")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

seq waveform, "P=B_DET_BAND_,R=FADC:"
seq waveform, "P=B_DET_BAND_,R=DISC:"

dbl > pv.list

