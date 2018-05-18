#!../../bin/linux-x86_64/iocbom
< envPaths
cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/iocbom.dbd")
iocbom_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

#dbLoadTemplate("db/bom_channels.substitutions")
dbLoadTemplate("db/bom_channels_sim.substitutions")
dbLoadRecords("db/bom_channels_sum.db")
dbLoadRecords("db/bom_calc.db")

cd ${TOP}/iocBoot/${IOC}

#< save_restore.cmd

iocInit

#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=${IOC}:")
#create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

