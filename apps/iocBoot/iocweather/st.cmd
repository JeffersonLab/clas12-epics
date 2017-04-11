#!../../bin/linux-x86_64/sensorProbe

< envPaths

#epicsEnvSet("MIBDIRS","$(DEVSNMP)/mibs:$(TOP)/mibs:/usr/share/snmp/mibs")
#epicsEnvSet("MIBDIRS","$(DEVSNMP)/mibs:/usr/share/snmp/mibs")
epicsEnvSet("MIBDIRS","$(TOP)/mibs:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")

# hallb-akcp123:
epicsEnvSet("AKCP1","129.57.160.80")
epicsEnvSet("AKCP2","129.57.160.153")
epicsEnvSet("AKCP3","129.57.160.154")

# to reduce record's INP length:
epicsEnvSet("MIB","SPAGENT-MIB::sensorProbe")

cd "${TOP}"

dbLoadDatabase ("dbd/sensorProbe.dbd")
sensorProbe_registerRecordDeviceDriver(pdbbase)

devSnmpSetParam(DebugLevel,99999)
#devSnmpSetParam(DebugLevel,0)

# AKCP SensorProbe requires SNMP version #1:
devSnmpSetSnmpVersion("${AKCP1}",SNMP_VERSION_1)
devSnmpSetSnmpVersion("${AKCP2}",SNMP_VERSION_1)
devSnmpSetSnmpVersion("${AKCP3}",SNMP_VERSION_1)

dbLoadTemplate("db/hallWeather.substitutions")
dbLoadRecords("db/weather_cRIO.db")

dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

iocInit
dbl > pv.list

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

