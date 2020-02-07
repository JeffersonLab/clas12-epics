#!../../bin/linux-x86_64/mpodLv

< envPaths

epicsEnvSet("MIBDIRS","${TOP}/iocBoot/iocsoftsvtRX:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")
epicsEnvSet("W","WIENER-CRATE-MIB::")

cd "${TOP}"

## Register all support components
#dbLoadDatabase("dbd/cRio.dbd")
#cRio_registerRecordDeviceDriver(pdbbase)
dbLoadDatabase("dbd/mpodLv.dbd")
mpodLv_registerRecordDeviceDriver(pdbbase)

#devSnmpSetParam(DebugLevel,10)

## IOC records:
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")

## cRIO heartbeat alarms:
dbLoadRecords("db/cRIO_heartbeat_bi.db","P=B_HW_,R=CRIO_BONUS_")

## BONUS Gas:
dbLoadRecords("db/gas_cRIO_BONUS.db")

## BONUS HV:
dbLoadTemplate("db/bonus-hv.substitutions")
dbLoadRecords("db/bonus-hv-watchdog.db","VMON=outputMeasSenseV")

# BONUS Interlocks:
dbLoadTemplate("db/gas_cRIO_BONUS_intlk.substitutions")
dbLoadRecords("db/gas_cRIO_BONUS_intlk.db")

## waveform test for Brian:
dbLoadRecords("db/criowf.db")

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

seq bonus_hv_watchdog

