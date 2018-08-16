#!../../bin/linux-x86_64/ftIntlk

< envPaths

cd "${TOP}"

dbLoadDatabase "dbd/ftIntlk.dbd"
ftIntlk_registerRecordDeviceDriver pdbbase

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", "IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:"

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

dbLoadRecords("db/ftcfthOnOff.db")
dbLoadTemplate("db/ftIntlk.substitutions")
dbLoadRecords("db/ftIntlkSums.db")

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")


dbpf("B_DET_FTC_SOFTINTLK_TEMP1:bypass",1)
dbpf("B_DET_FTC_SOFTINTLK_TEMP2:bypass",1)
dbpf("B_DET_FTC_SOFTINTLK_TEMP3:bypass",1)
dbpf("B_DET_FTC_SOFTINTLK_TEMP4:bypass",1)
dbpf("B_DET_FTC_SOFTINTLK_TEMP5:bypass",1)
dbpf("B_DET_FTC_SOFTINTLK_TEMP6:bypass",1)
dbpf("B_DET_FTC_SOFTINTLK_HUMID1:bypass",1)
dbpf("B_DET_FTC_SOFTINTLK_HUMID2:bypass",1)
dbpf("B_DET_FTH_SOFTINTLK_TEMP1:bypass",1)
dbpf("B_DET_FTH_SOFTINTLK_TEMP2:bypass",1)
dbpf("B_DET_FTC_SOFTINTLK_FLOW:bypass",1)
dbpf("B_DET_FTC_SOFTINTLK_CHILLER:temp:bypass",1)
dbpf("B_DET_FTC_SOFTINTLK_CHILLER:bath_level:bypass",1)
dbpf("B_DET_FTC_SOFTINTLK_CHILLER:pressure:bypass",1)

