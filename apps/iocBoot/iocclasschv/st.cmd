cd "$IOC_root_classchv"

< cdCommands
< ../network-NAB
< ../nfsCommands

cd topbin
ld < classchv.munch
cd top

putenv("EPICS_CA_AUTO_ADDR_LIST = NO")
putenv("EPICS_CA_ADDR_LIST = 129.57.163.255")

## Register all support components
dbLoadDatabase("dbd/classchv.dbd")
classchv_registerRecordDeviceDriver(pdbbase)

dbLoadRecords("${DEVIOCSTATS}/db/iocAdminVxWorks.db","IOC=iocclasschv")

dbLoadRecords("db/save_restoreStatus.db", "P=iocclasschv:")

cd startup

## autosave setup
#< save_restore.cmd

iocInit

## Handle autosave 'commands' contained in loaded databases.
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=iocclasschv:")
#create_monitor_set("info_settings.req", 30, "P=iocclasschv:")

#dbl > pv.list

