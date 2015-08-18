#!../../bin/linux-x86/ioccaen

< envPaths
cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/ioccaen.dbd")
ioccaen_registerRecordDeviceDriver(pdbbase)

# call to run sy1527Init()
Init_CAEN()

# Start_CAEN - call to run sy1527Start(), sy1527GetMap(), sy1527PrintMap()

# HVCTOF0
Start_CAEN(18,  "129.57.86.81")

## Load record instances
dbLoadTemplate("db/ctof.substitutions")

cd ${TOP}/iocBoot/${IOC}
iocInit()

