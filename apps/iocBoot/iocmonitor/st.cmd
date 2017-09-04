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

dbLoadTemplate("db/caenhv_stat-DC.substitutions")

dbLoadRecords("db/monitorApp_torus.db")

dbLoadRecords("db/camera_crosshair.db","P=B_HW_CAMS_cctv6")
dbLoadRecords("db/heartbeatCalc.db","P=B_HW_CAMS_cctv6,R=:")

dbLoadRecords("db/HVDC_VSCAN.db")

dbLoadRecords("db/collimator_alarm.db")

dbLoadRecords("db/htcc-gas-calc.db")

dbLoadTemplate("db/ltccOnOff.substitutions")
dbLoadTemplate("db/htccOnOff.substitutions")
dbLoadTemplate("db/pcalOnOff.substitutions")
dbLoadTemplate("db/ecalOnOff.substitutions")
dbLoadTemplate("db/ftofOnOff.substitutions")
dbLoadTemplate("db/hvOnOff.substitutions")

dbLoadTemplate("db/ctofcndOnOff.substitutions")

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit();

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

