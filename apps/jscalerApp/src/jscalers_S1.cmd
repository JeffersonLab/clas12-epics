#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("0","ADCECAL1")
Start_SCALERS_CRATE("1","ADCPCAL1")
Start_SCALERS_CRATE("2","ADCFTOF1")
Start_SCALERS_CRATE("3","TDCECAL1")
Start_SCALERS_CRATE("4","TDCPCAL1")
Start_SCALERS_CRATE("5","TDCFTOF1")


## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")

dbLoadTemplate("db/jscalers_S1_ECAL_FADC.sub")
dbLoadTemplate("db/jscalers_S1_PCAL_FADC.sub")
dbLoadTemplate("db/jscalers_S1_FTOF_FADC.sub")
dbLoadTemplate("db/jscalers_S1_ECAL_DISC.sub")
dbLoadTemplate("db/jscalers_S1_PCAL_DISC.sub")
dbLoadTemplate("db/jscalers_S1_FTOF_DISC.sub")


cd ${TOP}/iocBoot/${IOC}

iocInit

