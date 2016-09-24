#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("0","CTOF1")


## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")

dbLoadTemplate("db/jscalers_CTOF_FADC.sub")

dbLoadRecords("db/jscalers_CTOF_FADC_sums.db","SIDE=U")
dbLoadRecords("db/jscalers_CTOF_FADC_sums.db","SIDE=D")

cd ${TOP}/iocBoot/${IOC}

iocInit

