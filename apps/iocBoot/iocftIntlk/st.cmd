#!../../bin/linux-x86_64/ftIntlk

< envPaths

cd "${TOP}"

dbLoadDatabase "dbd/ftIntlk.dbd"
ftIntlk_registerRecordDeviceDriver pdbbase

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", "IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:"

#dbLoadRecords("db/ftcIntlk_test.db")

#dbLoadRecords("db/ftcIntlk_hvQ.db","P=B_DET_FTC_HV_Q1")
#dbLoadRecords("db/ftcIntlk_hvQ.db","P=B_DET_FTC_HV_Q2")
#dbLoadRecords("db/ftcIntlk_hvQ.db","P=B_DET_FTC_HV_Q3")
#dbLoadRecords("db/ftcIntlk_hvQ.db","P=B_DET_FTC_HV_Q4")
#dbLoadRecords("db/ftcIntlk_lv2Q.db","P=B_DET_FTC_INTLK_Q1Q4")
#dbLoadRecords("db/ftcIntlk_lv2Q.db","P=B_DET_FTC_INTLK_Q2Q3")

dbLoadRecords("db/ftcIntlk_hvQ.db","P=B_DET_FTC_,Q=1")
dbLoadRecords("db/ftcIntlk_hvQ.db","P=B_DET_FTC_,Q=2")
dbLoadRecords("db/ftcIntlk_hvQ.db","P=B_DET_FTC_,Q=3")
dbLoadRecords("db/ftcIntlk_hvQ.db","P=B_DET_FTC_,Q=4")
dbLoadRecords("db/ftcIntlk_lv2Q.db","P=B_DET_FTC_,Q1=1,Q2=4")
dbLoadRecords("db/ftcIntlk_lv2Q.db","P=B_DET_FTC_,Q1=2,Q2=3")

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

