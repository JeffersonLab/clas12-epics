#!../../bin/linux-x86/ioccaen

< envPaths
cd ${TOP}
epicsEnvSet("IOC","iochvecal3")

## Register all support components
dbLoadDatabase("dbd/ioccaen.dbd")
ioccaen_registerRecordDeviceDriver(pdbbase)

# call to run sy1527Init()
Init_CAEN()

# Start_CAEN - call to run sy1527Start(), sy1527GetMap(), sy1527PrintMap()

# hvecal3
Start_CAEN(11, "129.57.167.51")


## Load record instances
dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")
dbLoadTemplate("db/ecal3.substitutions")
dbLoadTemplate("db/ltcc3.substitutions")

cd ${TOP}/iocBoot/${IOC}

asSetFileName("caenhv.acf")

iocInit()

caPutLogInit("clonioc2:7011")

