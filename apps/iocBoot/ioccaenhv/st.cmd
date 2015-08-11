#!../../bin/linux-x86/ioccaen

< envPaths
cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/ioccaen.dbd")
ioccaen_registerRecordDeviceDriver(pdbbase)

# call to run sy1527Init()
Init_CAEN()

# Start_CAEN - call to run sy1527Start(), sy1527GetMap(), sy1527PrintMap()

# hvftof6
Start_CAEN(1,  "129.57.167.161")

# hvftof5 ###
Start_CAEN(2,  "129.57.167.162")

# hvftof4
Start_CAEN(3,  "129.57.167.79")

# hvecal1
Start_CAEN(4,  "129.57.167.53")

# hvftof1
Start_CAEN(5,  "129.57.167.78")

# hvftof2 ###
Start_CAEN(6,  "129.57.167.47")

# hvftof3
Start_CAEN(7,  "129.57.167.46")

# hvecal5
Start_CAEN(8,  "129.57.167.55")

# hvecal6
Start_CAEN(9,  "129.57.167.56")

# hvecal2
Start_CAEN(10, "129.57.167.191")

# hvecal3
Start_CAEN(11, "129.57.167.51")

# hvltcc0
Start_CAEN(12, "129.57.86.36")

# hvecal4
Start_CAEN(13, "129.57.167.190")

# HVCTOF0
Start_CAEN(18,  "129.57.86.81")


## Load record instances
dbLoadTemplate("db/hv.substitutions")
dbLoadTemplate("db/ecal.substitutions")
dbLoadTemplate("db/ctof.substitutions")

cd ${TOP}/iocBoot/${IOC}
iocInit()

