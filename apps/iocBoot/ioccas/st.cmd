#!../../bin/linux-x86_64/cas
#################################################
< envPaths
#################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/cas.dbd"
cas_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")

dbLoadRecords("db/accessControl.db")

cd "${TOP}/iocBoot/${IOC}"
asSetFilename("${TOP}/iocBoot/acf/caenhv.acf")

## autosave setup
< save_restore.cmd

dbl > pv.list
iocInit
caPutLogInit("clonioc1:7011")

create_monitor_set("cas_settings.req", 30, "P=B_,R=CAS:")

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

