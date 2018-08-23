#!../../bin/linux-x86_64/mollerSetup

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mollerSetup.dbd"
mollerSetup_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/automoller.db","P=B_MOLLER:")
dbLoadRecords("db/automoller-sim.db","P=B_MOLLER:,S=SIM:")

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit();

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

seq automoller "P=B_MOLLER:"

