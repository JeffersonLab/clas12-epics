#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("0","ADCECAL5")
Start_SCALERS_CRATE("1","ADCPCAL5")
Start_SCALERS_CRATE("2","ADCFTOF5")
Start_SCALERS_CRATE("3","TDCECAL5")
Start_SCALERS_CRATE("4","TDCPCAL5")
Start_SCALERS_CRATE("5","TDCFTOF5")


## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")

dbLoadTemplate("db/jscalers_S5_ECAL_FADC.sub")
dbLoadTemplate("db/jscalers_S5_LTCC_FADC.sub")
dbLoadTemplate("db/jscalers_S5_PCAL_FADC.sub")
dbLoadTemplate("db/jscalers_S5_FTOF_FADC.sub")
dbLoadTemplate("db/jscalers_S5_ECAL_DISC.sub")
dbLoadTemplate("db/jscalers_S5_LTCC_DISC.sub")
dbLoadTemplate("db/jscalers_S5_PCAL_DISC.sub")
dbLoadTemplate("db/jscalers_S5_FTOF_DISC.sub")


cd ${TOP}/iocBoot/${IOC}

iocInit

