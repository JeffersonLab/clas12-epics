#!../../bin/linux-x86_64/monitor

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/monitor.dbd"
monitor_registerRecordDeviceDriver pdbbase

# increase from the defaults was necessary (although not tuned)
callbackSetQueueSize(10000)
scanOnceSetQueueSize(10000)

#dbLoadRecords("db/heartbeatCalc.db","P=B_HW_,R=CRIO_DEV_,DLY=60")
#dbLoadRecords("db/heartbeatCalc.db","P=B_HW_,R=CRIO_HTCC_,DLY=60")
#dbLoadRecords("db/heartbeatCalc.db","P=B_HW_,R=CRIO_SVT_,DLY=60")

dbLoadTemplate("db/caenhv_stat.substitutions")
dbLoadRecords("db/caenhv_stat.db","SEC=1")
dbLoadRecords("db/caenhv_stat.db","SEC=2")
dbLoadRecords("db/caenhv_stat.db","SEC=3")
dbLoadRecords("db/caenhv_stat.db","SEC=4")
dbLoadRecords("db/caenhv_stat.db","SEC=5")
dbLoadRecords("db/caenhv_stat.db","SEC=6")

dbLoadRecords("db/monitorApp_torus.db")

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

cd ${TOP}/iocBoot/${IOC}

iocInit();


