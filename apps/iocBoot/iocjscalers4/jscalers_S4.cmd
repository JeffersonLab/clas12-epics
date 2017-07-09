#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("0","ADCECAL4")
Start_SCALERS_CRATE("1","ADCPCAL4")
Start_SCALERS_CRATE("2","ADCFTOF4")
Start_SCALERS_CRATE("3","TDCECAL4")
Start_SCALERS_CRATE("4","TDCPCAL4")
Start_SCALERS_CRATE("5","TDCFTOF4")


## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

callbackSetQueueSize(5000)
scanOnceSetQueueSize(5000)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

dbLoadTemplate("db/jscalers_S4_ECAL_FADC.substitutions")
dbLoadTemplate("db/jscalers_S4_PCAL_FADC.substitutions")
dbLoadTemplate("db/jscalers_S4_FTOF_FADC.substitutions")
dbLoadTemplate("db/jscalers_S4_LTCC_FADC.substitutions")
dbLoadTemplate("db/jscalers_S4_ECAL_DISC.substitutions")
dbLoadTemplate("db/jscalers_S4_PCAL_DISC.substitutions")
dbLoadTemplate("db/jscalers_S4_FTOF_DISC.substitutions")
dbLoadTemplate("db/jscalers_S4_LTCC_DISC.substitutions")

dbLoadTemplate("db/jscalers_TDCFTOF4_RF.substitutions")
dbLoadTemplate("db/jscalers_TDCPCAL4_TRIG.substitutions")
dbLoadTemplate("db/jscalers_TDCFTOF4_TRIG.substitutions")

dbLoadRecords("db/jscalers_wf.db","S=4")
dbLoadTemplate("db/jscalers_wf_S4.substitutions")
dbLoadTemplate("db/jscalers_puts_S4.substitutions")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

seq seqJscalersF, "S=4"

dbl > pv.list

