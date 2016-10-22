#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("0","ADCECAL3")
Start_SCALERS_CRATE("1","ADCPCAL3")
Start_SCALERS_CRATE("2","ADCFTOF3")
Start_SCALERS_CRATE("3","TDCECAL3")
Start_SCALERS_CRATE("4","TDCPCAL3")
Start_SCALERS_CRATE("5","TDCFTOF3")


## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")

dbLoadTemplate("db/jscalers_S3_ECAL_FADC.sub")
dbLoadTemplate("db/jscalers_S3_LTCC_FADC.sub")
dbLoadTemplate("db/jscalers_S3_PCAL_FADC.sub")
dbLoadTemplate("db/jscalers_S3_FTOF_FADC.sub")
dbLoadTemplate("db/jscalers_S3_ECAL_DISC.sub")
dbLoadTemplate("db/jscalers_S3_LTCC_DISC.sub")
dbLoadTemplate("db/jscalers_S3_PCAL_DISC.sub")
dbLoadTemplate("db/jscalers_S3_FTOF_DISC.sub")


cd ${TOP}/iocBoot/${IOC}

iocInit

