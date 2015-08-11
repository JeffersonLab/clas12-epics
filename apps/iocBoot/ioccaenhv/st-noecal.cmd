#!../../bin/linux-x86/ioccaen

< envPaths
cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/ioccaen.dbd")
ioccaen_registerRecordDeviceDriver(pdbbase)

# call to run sy1527Init()
Init_CAEN()

# Start_CAEN - call to run sy1527Start(), sy1527GetMap(), sy1527PrintMap()

# hvftof1
Start_CAEN(5,  "129.57.167.78")

# hvftof2 ###
Start_CAEN(6,  "129.57.167.47")

# hvftof3
Start_CAEN(7,  "129.57.167.46")

# hvftof4
Start_CAEN(3,  "129.57.167.79")

# hvftof5 ###
Start_CAEN(2,  "129.57.167.162")

# hvftof6
Start_CAEN(1,  "129.57.167.161")



# hvltcc0
Start_CAEN(12, "129.57.86.36")

# HVCTOF0
Start_CAEN(18,  "129.57.86.81")


## Load record instances

dbLoadTemplate("db/hv.substitutions")
dbLoadTemplate("db/ctof.substitutions")

cd ${TOP}/iocBoot/${IOC}
iocInit()

