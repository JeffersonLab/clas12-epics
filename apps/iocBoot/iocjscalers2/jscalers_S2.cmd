#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("0","ADCECAL2")
Start_SCALERS_CRATE("1","ADCPCAL2")
Start_SCALERS_CRATE("2","ADCFTOF2")
Start_SCALERS_CRATE("3","TDCECAL2")
Start_SCALERS_CRATE("4","TDCPCAL2")
Start_SCALERS_CRATE("5","TDCFTOF2")


## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

callbackSetQueueSize(5000)
scanOnceSetQueueSize(5000)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

dbLoadTemplate("db/jscalers_S2_ECAL_FADC.substitutions")
dbLoadTemplate("db/jscalers_S2_PCAL_FADC.substitutions")
dbLoadTemplate("db/jscalers_S2_FTOF_FADC.substitutions")
dbLoadTemplate("db/jscalers_S2_LTCC_FADC.substitutions")
dbLoadTemplate("db/jscalers_S2_ECAL_DISC.substitutions")
dbLoadTemplate("db/jscalers_S2_PCAL_DISC.substitutions")
dbLoadTemplate("db/jscalers_S2_FTOF_DISC.substitutions")
dbLoadTemplate("db/jscalers_S2_LTCC_DISC.substitutions")

dbLoadRecords("db/jscalers_ECAL_sums.db","TYPE=FADC,SEC=2,CH=1")
dbLoadRecords("db/jscalers_ECAL_sums.db","TYPE=DISC,SEC=2,CH=3")
dbLoadRecords("db/jscalers_PCAL_sums.db","TYPE=FADC,SEC=2,CH=1")
dbLoadRecords("db/jscalers_PCAL_sums.db","TYPE=DISC,SEC=2,CH=3")
dbLoadRecords("db/jscalers_FTOF_sums.db","TYPE=FADC,SEC=2,CH=1")
dbLoadRecords("db/jscalers_FTOF_sums.db","TYPE=DISC,SEC=2,CH=3")
dbLoadRecords("db/jscalers_LTCC_sums.db","TYPE=FADC,SEC=2,CH=1")
dbLoadRecords("db/jscalers_LTCC_sums.db","TYPE=DISC,SEC=2,CH=3")

dbLoadTemplate("db/jscalers_TDCPCAL2_TRIG.substitutions")
dbLoadTemplate("db/jscalers_TDCFTOF2_TRIG.substitutions")

dbLoadRecords("db/jscalers_wf.db","S=2")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

seq seqJscalersF, "S=2"

dbl > pv.list
