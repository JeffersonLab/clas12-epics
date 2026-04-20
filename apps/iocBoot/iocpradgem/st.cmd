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

dbLoadTemplate("db/prad-gems.substitutions")

dbLoadRecords("db/prad-gems-seq.db","M=0,L=0,S=OFF,VAL=0")
dbLoadRecords("db/prad-gems-seq.db","M=0,L=1,S=OFF,VAL=0")
dbLoadRecords("db/prad-gems-seq.db","M=1,L=0,S=OFF,VAL=0")
dbLoadRecords("db/prad-gems-seq.db","M=1,L=1,S=OFF,VAL=0")
dbLoadRecords("db/prad-gems-seq.db","M=0,L=0,S=ON,VAL=1")
dbLoadRecords("db/prad-gems-seq.db","M=0,L=1,S=ON,VAL=1")
dbLoadRecords("db/prad-gems-seq.db","M=1,L=0,S=ON,VAL=1")
dbLoadRecords("db/prad-gems-seq.db","M=1,L=1,S=ON,VAL=1")

dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_PRADGEM_HV")
dbLoadRecords("db/caenhv_genericStat.db","P=B_DET_PRADGEM_LV")

dbLoadTemplate("db/prad-gems-intlk.substitutions")

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

iocInit

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

