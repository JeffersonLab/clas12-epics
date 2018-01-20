#!../../bin/linux-x86_64/ftIntlk

< envPaths

cd "${TOP}"

dbLoadDatabase "dbd/ftIntlk.dbd"
ftIntlk_registerRecordDeviceDriver pdbbase

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", "IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:"

dbLoadTemplate("db/mmIntlk.substitutions")
dbLoadRecords("db/mmIntlkSums.db")

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

# these don't fit the template, due to solenoid polarity:
epicsThreadSleep(2)
dbpf("B_DET_BMT_INTLK_Solenoid:first_check.CALC", "(C<=ABS(A)||ABS(A)<B)&(D#1)?1:0")
dbpf("B_DET_BMT_INTLK_Solenoid:second_check.CALC","(C<=ABS(A)||ABS(A)<B)&(D#1)?1:0")
dbpf("B_DET_FMT_INTLK_Solenoid:first_check.CALC", "(C<=ABS(A)||ABS(A)<B)&(D#1)?1:0")
dbpf("B_DET_FMT_INTLK_Solenoid:second_check.CALC","(C<=ABS(A)||ABS(A)<B)&(D#1)?1:0")
dbpf("B_DET_FTT_INTLK_Solenoid:first_check.CALC", "(C<=ABS(A)||ABS(A)<B)&(D#1)?1:0")
dbpf("B_DET_FTT_INTLK_Solenoid:second_check.CALC","(C<=ABS(A)||ABS(A)<B)&(D#1)?1:0")

