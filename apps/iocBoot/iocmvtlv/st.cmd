#!../../bin/linux-x86_64/mpodLv

< envPaths

< lvCrateAddresses.env

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
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

devSnmpSetParam(DebugLevel,10)

#MpodStatusParserDebug=1

dbLoadTemplate("db/mvtlv.substitutions")

#dbLoadRecords("db/mmfeusums.db","SUFFIX=Current_A")
#dbLoadRecords("db/mmfeusums.db","XTmpV6")
#dbLoadRecords("db/mmfeusums.db","MTmpInt")
#dbLoadRecords("db/mmfeusums.db","TmpSdX")
#dbLoadRecords("db/mmfeusums.db","TmpSdA")

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

asSetFilename("../acf/cas.acf")

iocInit

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

