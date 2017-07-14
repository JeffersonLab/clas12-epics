#!../../bin/linux-x86_64/svtCtrlApp

< envPaths

cd ${TOP}

dbLoadDatabase("dbd/svtCtrlApp.dbd")

svtCtrlApp_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

dbLoadTemplate("db/svtIntlk.substitutions")

dbLoadTemplate("db/svt-sums.substitutions")
dbLoadRecords("db/svt-sums-alarm.db")

dbLoadRecords("db/svtIntlkSummary.db")

dbLoadRecords("db/svt-sums-inhibits.db")

dbLoadRecords("db/cas.db","P=B_,R=SVT_") 

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

asSetFilename("../acf/svt.acf")
asSetSubstitutions("P=B_,R=SVT_")

iocInit

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbpf("${IOC}:SysReset.ASG","ALLWRITE")

