#!../../bin/linux-x86_64/monitor

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/monitor.dbd"
monitor_registerRecordDeviceDriver pdbbase

#dbLoadRecords("db/heartbeatCalc.db","P=B_HW_,R=CRIO_DEV_,DLY=60")
#dbLoadRecords("db/heartbeatCalc.db","P=B_HW_,R=CRIO_HTCC_,DLY=60")
#dbLoadRecords("db/heartbeatCalc.db","P=B_HW_,R=CRIO_SVT_,DLY=60")

dbLoadRecords("db/caenhv_FTOF_sums.db","SEC=1")
dbLoadRecords("db/caenhv_FTOF_sums.db","SEC=2")
dbLoadRecords("db/caenhv_FTOF_sums.db","SEC=3")
dbLoadRecords("db/caenhv_FTOF_sums.db","SEC=4")
dbLoadRecords("db/caenhv_FTOF_sums.db","SEC=5")
dbLoadRecords("db/caenhv_FTOF_sums.db","SEC=6")

dbLoadRecords("db/caenhv_ECAL_sums.db","SEC=1")
dbLoadRecords("db/caenhv_ECAL_sums.db","SEC=2")
dbLoadRecords("db/caenhv_ECAL_sums.db","SEC=3")
dbLoadRecords("db/caenhv_ECAL_sums.db","SEC=4")
dbLoadRecords("db/caenhv_ECAL_sums.db","SEC=5")
dbLoadRecords("db/caenhv_ECAL_sums.db","SEC=6")

dbLoadRecords("db/caenhv_PCAL_sums.db","SEC=1")
dbLoadRecords("db/caenhv_PCAL_sums.db","SEC=2")
dbLoadRecords("db/caenhv_PCAL_sums.db","SEC=3")
dbLoadRecords("db/caenhv_PCAL_sums.db","SEC=4")
dbLoadRecords("db/caenhv_PCAL_sums.db","SEC=5")
dbLoadRecords("db/caenhv_PCAL_sums.db","SEC=6")

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

cd ${TOP}/iocBoot/${IOC}

iocInit();


