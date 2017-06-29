#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("0","ADCCTOF1")
#Start_SCALERS_CRATE("1","ADCFT1")
#Start_SCALERS_CRATE("2","ADCFT2")

## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")

dbLoadTemplate("db/jscalers_CTOF_FADC.substitutions")
dbLoadTemplate("db/jscalers_HTCC_FADC.substitutions")

#dbLoadTemplate("db/jscalers_FTC_FADC.substitutions")

dbLoadRecords("db/jscalers_wfC.db")
dbLoadRecords("db/jscalers_wf_averagesC.db")


cd ${TOP}/iocBoot/${IOC}

iocInit

seq seqJscalersC

dbl > pv.list

