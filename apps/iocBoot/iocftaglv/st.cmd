#!../../bin/linux-x86_64/mpodLv

< envPaths

#
epicsEnvSet("MIBDIRS","$(DEVSNMP)/mibs:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")

# just to decrease string size in record:
epicsEnvSet("MIB","WIENER_CRATE-MIB::")
epicsEnvSet("WO","WIENER-CRATE-MIB::output")

cd "${TOP}"

dbLoadDatabase "dbd/mpodLv.dbd"
mpodLv_registerRecordDeviceDriver pdbbase

dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")

devSnmpSetParam(DebugLevel,10)

#MpodStatusParserDebug=1

dbLoadTemplate("db/ftcallv.substitutions")
dbLoadTemplate("db/fthodlv.substitutions")
dbLoadTemplate("db/fttrklv.substitutions")

cd "${TOP}/iocBoot/${IOC}"


dbl > pv.list

iocInit

