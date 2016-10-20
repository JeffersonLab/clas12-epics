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
dbLoadTemplate("db/jscalers_S1_LTCC_FADC.sub")
dbLoadTemplate("db/jscalers_S1_ECAL_DISC.sub")
dbLoadTemplate("db/jscalers_S1_PCAL_DISC.sub")
dbLoadTemplate("db/jscalers_S1_FTOF_DISC.sub")
dbLoadTemplate("db/jscalers_S1_LTCC_DISC.sub")

dbLoadRecords("db/jscalers_ECAL_sums.db","TYPE=FADC,SEC=1,CH=1")
dbLoadRecords("db/jscalers_ECAL_sums.db","TYPE=DISC,SEC=1,CH=3")
dbLoadRecords("db/jscalers_PCAL_sums.db","TYPE=FADC,SEC=1,CH=1")
dbLoadRecords("db/jscalers_PCAL_sums.db","TYPE=DISC,SEC=1,CH=3")
dbLoadRecords("db/jscalers_FTOF_sums.db","TYPE=FADC,SEC=1,CH=1")
dbLoadRecords("db/jscalers_FTOF_sums.db","TYPE=DISC,SEC=1,CH=3")

dbLoadTemplate("db/jscalers_TDCPCAL1_TRIG.sub")
dbLoadTemplate("db/jscalers_TDCFTOF1_TRIG.sub")

cd ${TOP}/iocBoot/${IOC}

iocInit

dbl > pv.list
