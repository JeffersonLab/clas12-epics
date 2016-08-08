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

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")

dbLoadTemplate("db/jscalers_S4_ECAL_FADC.sub")
dbLoadTemplate("db/jscalers_S4_PCAL_FADC.sub")
dbLoadTemplate("db/jscalers_S4_FTOF_FADC.sub")
dbLoadTemplate("db/jscalers_S4_ECAL_DISC.sub")
dbLoadTemplate("db/jscalers_S4_PCAL_DISC.sub")
dbLoadTemplate("db/jscalers_S4_FTOF_DISC.sub")


cd ${TOP}/iocBoot/${IOC}

iocInit

