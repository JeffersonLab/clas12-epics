#!../../bin/linux-x86/ioccaen

< envPaths
cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/ioccaen.dbd")
ioccaen_registerRecordDeviceDriver(pdbbase)

# call to run sy1527Init()
Init_CAEN()

# Start_CAEN - call to run sy1527Start(), sy1527GetMap(), sy1527PrintMap()

# hvecal1
Start_CAEN(4,  "129.57.167.53")

## Load record instances
dbLoadTemplate("db/ecal1.substitutions")
dbLoadTemplate("db/ltcc1.substitutions")

cd ${TOP}/iocBoot/${IOC}
iocInit()

