#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}

Init_SCALERS()

Start_SCALERS_CRATE("0","LTCC0")


## Register all support components
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")

dbLoadTemplate("db/jscalers_HTCC_FADC.substitutions")

dbLoadRecords("db/jscalers_HTCC_sums.db","SEC=1,TYPE=FADC")
dbLoadRecords("db/jscalers_HTCC_sums.db","SEC=2,TYPE=FADC")
dbLoadRecords("db/jscalers_HTCC_sums.db","SEC=3,TYPE=FADC")
dbLoadRecords("db/jscalers_HTCC_sums.db","SEC=4,TYPE=FADC")
dbLoadRecords("db/jscalers_HTCC_sums.db","SEC=5,TYPE=FADC")
dbLoadRecords("db/jscalers_HTCC_sums.db","SEC=6,TYPE=FADC")

cd ${TOP}/iocBoot/${IOC}

iocInit

