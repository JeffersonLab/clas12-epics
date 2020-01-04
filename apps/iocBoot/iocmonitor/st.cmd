#!../../bin/linux-x86_64/monitor

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/monitor.dbd"
monitor_registerRecordDeviceDriver pdbbase

# increase from the defaults was necessary (although not tuned)
callbackSetQueueSize(10000)
scanOnceSetQueueSize(10000)

# move these to classc1:
dbLoadRecords("db/collimator_alarm.db")
dbLoadRecords("db/beamCurrentRatios.db")

# move this to iocsoftsvtIntlk:
dbLoadRecords("db/svt-sums-global.db")

# cross-IOC hv stuff:
dbLoadRecords("db/HVDC_VSCAN.db")
dbLoadTemplate("db/ltccOnOff.substitutions")
dbLoadTemplate("db/pcalOnOff.substitutions")
dbLoadTemplate("db/ecalOnOff.substitutions")
dbLoadTemplate("db/ftofOnOff.substitutions")
dbLoadTemplate("db/hvOnOff.substitutions")
dbLoadRecords("db/ltccOnOff.db","ONOFF=ON")
dbLoadRecords("db/ltccOnOff.db","ONOFF=OFF")
dbLoadRecords("db/caenhv_DC_onoff.db")
dbLoadTemplate("db/dcOnOff.substitutions")

dbLoadRecords("db/misc-crate-alive.db","P=B_HW_camac1")

dbLoadTemplate("db/bonner-spheres.substitutions")

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit();

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

