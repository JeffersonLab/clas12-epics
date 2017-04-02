#!../../bin/linux-x86_64/svtCtrlApp

< envPaths

cd ${TOP}

dbLoadDatabase("dbd/svtCtrlApp.dbd")

svtCtrlApp_registerRecordDeviceDriver pdbbase

dbLoadTemplate("db/svtIntlk.substitutions")

dbLoadTemplate("db/svt-sums.substitutions")
dbLoadRecords("db/svt-sums-alarm.db")

dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")

cd "${TOP}/iocBoot/${IOC}"

iocInit

