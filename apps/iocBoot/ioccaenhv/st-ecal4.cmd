#!../../bin/linux-x86/ioccaen

< envPaths
cd ${TOP}
epicsEnvSet("IOC","iochvecal4")

## Register all support components
dbLoadDatabase("dbd/ioccaen.dbd")
ioccaen_registerRecordDeviceDriver(pdbbase)

# call to run sy1527Init()
Init_CAEN()

# Start_CAEN - call to run sy1527Start(), sy1527GetMap(), sy1527PrintMap()

# hvecal4
Start_CAEN(13, "129.57.167.190")


## Load record instances
dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")
dbLoadTemplate("db/ecal4.substitutions")
dbLoadTemplate("db/ltcc4.substitutions")

cd ${TOP}/iocBoot/${IOC}

asSetFileName("caenhv.acf")

iocInit()

caPutLogInit("clonioc2:7011")

