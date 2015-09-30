#!../../bin/linux-x86_64/cas

< envPaths
cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/cas.dbd"
cas_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords "db/cas.db", "P=B_,R=CAS:"

cd "${TOP}/iocBoot/${IOC}"
asSetFilename("${TOP}/iocBoot/acf/cas.acf")

## autosave setup
# < save_restore.cmd

iocInit
caPutLogInit "clonioc2:7011"

create_monitor_set("cas_settings.req", 30, "P=B_,R=CAS:")

## Handle autosave 'commands' contained in loaded databases.
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=B_,R=CAS:")
#create_monitor_set("info_settings.req", 30, "P=B_,R=CAS:")

