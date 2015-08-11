#!../../bin/linux-x86/ioccaen

< envPaths
cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/ioccaen.dbd")
ioccaen_registerRecordDeviceDriver(pdbbase)

# call to run sy1527Init()
Init_CAEN()

# Start_CAEN - call to run sy1527Start(), sy1527GetMap(), sy1527PrintMap()


# hvltcc0
Start_CAEN(12, "129.57.86.36")


## Load record instances
dbLoadTemplate("db/ltcc0.substitutions")

cd ${TOP}/iocBoot/${IOC}
iocInit()

