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

# Determine IP address:
system 'nslookup lvatof | awk "/^Address: / {print\"epicsEnvSet(lvatof,\"\$2\")\"}" > ip.iocsh'
< ip.iocsh

# ATOF:
dbLoadTemplate("db/atof-hvlv.substitutions")
dbLoadTemplate("db/atof-seq.substitutions")
dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_ATOF")

# GAS:
#dbLoadRecords("db/gas_cRIO_ALERT_TGT.db")
dbLoadRecords("db/gas_cRIO_AHDC.db")
dbLoadRecords("db/cRIO_heartbeat.db","P=B_HW_,R=CRIO_ALERT_,DLY=60")

# Note, AHDC HV and LV are in separate IOCs (ioccaenhv_HVMVT and iocmvtlv)

# Standard IOC stuff:
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

iocInit

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

