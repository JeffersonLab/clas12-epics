#!../../bin/linux-x86/plc2epics
############################################################################
< envPaths
############################################################################
cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/plc2epics.dbd")
plc2epics_registerRecordDeviceDriver(pdbbase)

## Initialize EtherIP driver, define PLCs
## NOTE: if buffer limit is left at 500, read errors will occur.
EIP_buffer_limit(450)
drvEtherIP_init()
#drvEtherIP_define_PLC("PLC_CRYO",  "129.57.96.17", 0)
drvEtherIP_define_PLC("PLC_TORUS", "129.57.96.15", 0)

## Debugging [7-10]
#EIP_verbosity(7)

## Load record instances
#dbLoadTemplate("db/torus_import.substitutions")
dbLoadTemplate("db/torus_force_addons.substitutions")

cd ${TOP}/iocBoot/${IOC}

dbl > pv.list
iocInit
