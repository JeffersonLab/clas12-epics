#!../../bin/linux-x86_64/bta

## You may have to change bta to something else
## everywhere it appears in this file

< envPaths
cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/bta.dbd"
bta_registerRecordDeviceDriver pdbbase

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", "IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:"

dbLoadRecords("db/bta_suppl.db","hall=B,ioc=classc6");

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

