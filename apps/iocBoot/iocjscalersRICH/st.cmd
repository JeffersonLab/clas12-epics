#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("0","rich4")


## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

callbackSetQueueSize(5000)
scanOnceSetQueueSize(5000)

dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

dbLoadTemplate("db/jscalers_RICH_SSP.substitutions")

# these are just aliases from HW to DET:
dbLoadRecords("db/jscaler_RICH_Maps.db")

# averaging scalers over 8x8 PMTs:
dbLoadRecords("db/jscalers_RICH_sums.db")

# average temps over all tiles (just for alarm propogation):
dbLoadTemplate("db/jscalers_RICH_sums_tempvolt.substitutions")

# global alarm limit setters:
dbLoadTemplate("db/jscalers_puts_RICH.substitutions")

# make waveforms: 
dbLoadRecords("db/waveformApp.db","P=B_DET_RICH_SCALERS_,R=ROWS:,NELM=23, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/rows.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_RICH_SCALERS_,R=PMTS:,NELM=391,FTVL=FLOAT,PERIOD=5,FNAME=pvlists/pmts.txt")

dbLoadRecords("db/rich_maxTemp.db","P=B_DET_RICH_SSP,SUFF=:temp:fpga")
dbLoadTemplate("db/rich_maxTemp.substitutions")

dbLoadRecords("db/richIntlk.template","P=B_DET_RICH_INTLK,R=:temp:fpga:,TESTVAL=B_DET_RICH_SSP:temp:fpga:max,CTRL=B_DET_RICH_LVHV:OFF")

dbLoadRecords("db/jscalers_RICH_ColorScale.db")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

seq waveform, "P=B_DET_RICH_SCALERS_,R=ROWS:"
seq waveform, "P=B_DET_RICH_SCALERS_,R=PMTS:"

# load them once, then autosaving these to reduce ioc startup noise:
#< rich-setDesc.cmd

dbl > pv.list
