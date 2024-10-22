#!../../bin/linux-x86_64/mpodLv

< envPaths

< lvCrateAddresses.env

epicsEnvSet("MIBDIRS","$(DEVSNMP)/mibs:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")

# just to decrease string size in record definitions:
epicsEnvSet("MIB","WIENER-CRATE-MIB::")
epicsEnvSet("W","WIENER-CRATE-MIB::")
epicsEnvSet("WO","WIENER-CRATE-MIB::output")

cd "${TOP}"

dbLoadDatabase "dbd/mpodLv.dbd"
mpodLv_registerRecordDeviceDriver pdbbase

dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

#devSnmpSetParam(DebugLevel,10)
#MpodStatusParserDebug=1

dbLoadTemplate("db/atof-hvlv.substitutions")
dbLoadRecords("db/atof-hvlv-seq.db","S=ON,VAL=1")
dbLoadRecords("db/atof-hvlv-seq.db","S=OFF,VAL=0")
dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_ATOF_HV")

dbLoadTemplate("db/mmtb-lv.substitutions")
#dbLoadTemplate("db/ahdc-lv.substitutions")
#dbLoadTemplate("db/ahdc-intlk.substitutions")

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

iocInit

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

