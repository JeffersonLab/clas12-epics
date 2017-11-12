#!../../bin/linux-x86_64/monitor

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/monitor.dbd"
monitor_registerRecordDeviceDriver pdbbase

# increase from the defaults was necessary (although not tuned)
callbackSetQueueSize(10000)
scanOnceSetQueueSize(10000)

dbLoadRecords("db/camera_crosshair.db","P=B_HW_CAMS_cctv6")
dbLoadRecords("db/heartbeatCalc.db","P=B_HW_CAMS_cctv6,R=:")

# remove this from iocmonitor after ioctorusForce is restarted:
dbLoadRecords("db/torus_fieldAverage.db")

dbLoadRecords("db/collimator_alarm.db")

dbLoadRecords("db/htcc-gas-calc.db")

# cross-IOC hv stuff:
dbLoadRecords("db/HVDC_VSCAN.db")
dbLoadTemplate("db/ltccOnOff.substitutions")
dbLoadTemplate("db/pcalOnOff.substitutions")
dbLoadTemplate("db/ecalOnOff.substitutions")
dbLoadTemplate("db/ftofOnOff.substitutions")
dbLoadTemplate("db/hvOnOff.substitutions")
dbLoadRecords("db/ltccOnOff.db","ONOFF=ON")
dbLoadRecords("db/ltccOnOff.db","ONOFF=OFF")

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit();

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

