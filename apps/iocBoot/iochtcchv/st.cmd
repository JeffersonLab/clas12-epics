#!../../bin/linux-x86_64/mpodLv

< envPaths

epicsEnvSet("MIBDIRS","${TOP}/iocBoot/iocsoftsvtRX:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")
epicsEnvSet("W","WIENER-CRATE-MIB::")

cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/mpodLv.dbd")
mpodLv_registerRecordDeviceDriver(pdbbase)

#devSnmpSetParam(DebugLevel,10000)
#MpodStatusParserDebug=1000

## IOC records:
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")

dbLoadTemplate("db/htcc-iseg.substitutions")

dbLoadTemplate("db/htccOnOff.substitutions")
dbLoadRecords("db/iseg_HTCC_isOnOffComm.db","SEC=1")
dbLoadRecords("db/iseg_HTCC_isOnOffComm.db","SEC=2")
dbLoadRecords("db/iseg_HTCC_isOnOffComm.db","SEC=3")
dbLoadRecords("db/iseg_HTCC_isOnOffComm.db","SEC=4")
dbLoadRecords("db/iseg_HTCC_isOnOffComm.db","SEC=5")
dbLoadRecords("db/iseg_HTCC_isOnOffComm.db","SEC=6")
dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_HTCC_HV_SEC1")
dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_HTCC_HV_SEC2")
dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_HTCC_HV_SEC3")
dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_HTCC_HV_SEC4")
dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_HTCC_HV_SEC5")
dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_HTCC_HV_SEC6")
dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_HTCC_HV")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

iocInit

## export pv list
dbl > pv.list

## autosave startup
## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=xxx:")
create_monitor_set("info_settings.req", 30, "P=xxx:")

