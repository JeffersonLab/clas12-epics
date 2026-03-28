#!../../bin/linux-x86_64/mpodLv

< envPaths

epicsEnvSet("MIBDIRS","$(DEVSNMP)/mibs:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")

# just to decrease string size in SNMP record definitions:
epicsEnvSet("MIB","WIENER-CRATE-MIB::")
epicsEnvSet("W","WIENER-CRATE-MIB::")
epicsEnvSet("WO","WIENER-CRATE-MIB::output")

cd "${TOP}"

dbLoadDatabase "dbd/mpodLv.dbd"
mpodLv_registerRecordDeviceDriver pdbbase

#devSnmpSetParam(DebugLevel,10)
#MpodStatusParserDebug=1

# Standard IOC stuff:
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

# Determine IP address:
system 'nslookup lvpradgem0 | awk "/^Address: / {print\"epicsEnvSet(lvpradgem0,\"\$2\")\"}" > ${TOP}/iocBoot/${IOC}/ip.cmd'

< ${TOP}/iocBoot/${IOC}/ip.cmd

dbLoadTemplate("db/pradgems-lv.substitutions")

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

iocInit

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

