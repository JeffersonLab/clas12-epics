#!../../bin/linux-x86_64/svtCtrlApp

< envPaths

cd ${TOP}

dbLoadDatabase("dbd/svtCtrlApp.dbd")

svtCtrlApp_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

#dbLoadTemplate("db/V450-160subnet.substitutions")

dbLoadTemplate("db/svtIntlk.substitutions")

dbLoadTemplate("db/svt-sums.substitutions")
dbLoadRecords("db/svt-sums-alarm.db")

dbLoadRecords("db/svtIntlkSummary.db")

dbLoadRecords("db/svt-sums-inhibits.db")

dbLoadRecords("db/seq_svtOnOff-All.db")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
#< save_restore.cmd

iocInit

#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=${IOC}:")
#create_monitor_set("info_settings.req", 30, "P=${IOC}:")

