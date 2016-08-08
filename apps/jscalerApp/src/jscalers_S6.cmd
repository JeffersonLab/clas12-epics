#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("0","ADCECAL6")
Start_SCALERS_CRATE("1","ADCPCAL6")
Start_SCALERS_CRATE("2","ADCFTOF6")
Start_SCALERS_CRATE("3","TDCECAL6")
Start_SCALERS_CRATE("4","TDCPCAL6")
Start_SCALERS_CRATE("5","TDCFTOF6")


## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")

dbLoadTemplate("db/jscalers_S6_ECAL_FADC.sub")
dbLoadTemplate("db/jscalers_S6_PCAL_FADC.sub")
dbLoadTemplate("db/jscalers_S6_FTOF_FADC.sub")
dbLoadTemplate("db/jscalers_S6_ECAL_DISC.sub")
dbLoadTemplate("db/jscalers_S6_PCAL_DISC.sub")
dbLoadTemplate("db/jscalers_S6_FTOF_DISC.sub")


cd ${TOP}/iocBoot/${IOC}

iocInit

