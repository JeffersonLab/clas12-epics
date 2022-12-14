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

