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
system 'nslookup lvatof | awk "/^Address: / {print\"epicsEnvSet(lvatof,\"\$2\")\"}" > ${TOP}/iocBoot/${IOC}/ip.cmd'
< ${TOP}/iocBoot/${IOC}/ip.cmd

# ATOF:
dbLoadTemplate("db/atof-hvlv.substitutions")
dbLoadTemplate("db/atof-seq.substitutions")
dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_ATOF")
dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_ATOF_HV")

# GAS:
dbLoadRecords("db/gas_cRIO_BONUS.db")
dbLoadRecords("db/gas_cRIO_AHDC.db")
dbLoadRecords("db/cRIO_heartbeat_bi.db","P=B_HW_,R=CRIO_BONUS_,DLY=60")
dbLoadRecords("db/gas_cRIO_ALERT_alias.db")

# Note, AHDC is sharing hardware with MVT, in separate IOCs:
# iocmvtlv, iocmmfeuMVT

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

iocInit

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

