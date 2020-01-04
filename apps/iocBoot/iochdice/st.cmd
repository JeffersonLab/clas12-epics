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
drvEtherIP_define_PLC("PLC_HDICE", "129.57.86.23", 0)

## Debugging [7-10]
#EIP_verbosity(7)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/hdice_solenoid.db")
dbLoadRecords("db/hdice_solenoid_breakout.db")

cd ${TOP}/iocBoot/${IOC}

iocInit

dbl > pv.list

