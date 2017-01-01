#!../../bin/linux-x86_64/sensorProbe

< envPaths

#epicsEnvSet("MIBDIRS","$(DEVSNMP)/mibs:$(TOP)/mibs:/usr/share/snmp/mibs")
epicsEnvSet("MIBDIRS","$(DEVSNMP)/mibs:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")

# hallb-akcp123:
epicsEnvSet("IP1","129.57.160.80")
epicsEnvSet("IP2","129.57.160.153")
epicsEnvSet("IP3","129.57.160.154")

# to reduce record's INP length:
epicsEnvSet("MIB","SPAGENT-MIB::sensorProbe")

cd "${TOP}"

dbLoadDatabase ("dbd/sensorProbe.dbd")
sensorProbe_registerRecordDeviceDriver(pdbbase)

devSnmpSetParam(DebugLevel,99999)
#devSnmpSetParam(DebugLevel,0)

# AKCP SensorProbe requires SNMP version #1:
devSnmpSetSnmpVersion("${IP1}",SNMP_VERSION_1)
devSnmpSetSnmpVersion("${IP2}",SNMP_VERSION_1)
devSnmpSetSnmpVersion("${IP3}",SNMP_VERSION_1)

# Forward Carriage:
dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second,HOST=${IP2},P=B_WEATHER_FC,R=,C=0")
dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second,HOST=${IP2},P=B_WEATHER_FC,R=,C=1")
dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second,HOST=${IP2},P=B_WEATHER_FC,R=,C=2")
dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second,HOST=${IP2},P=B_WEATHER_FC,R=,C=3")
dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP2},P=B_WEATHER_FC,R=,C=0")
dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP2},P=B_WEATHER_FC,R=,C=1")
dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP2},P=B_WEATHER_FC,R=,C=2")
dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP2},P=B_WEATHER_FC,R=,C=3")

# SpaceFrame North:
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second,HOST=${IP1},P=B_WEATHER_SF_N,R=,C=0")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second,HOST=${IP1},P=B_WEATHER_SF_N,R=,C=1")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second,HOST=${IP1},P=B_WEATHER_SF_N,R=,C=2")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second,HOST=${IP1},P=B_WEATHER_SF_N,R=,C=3")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP1},P=B_WEATHER_SF_N,R=,C=0")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP1},P=B_WEATHER_SF_N,R=,C=1")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP1},P=B_WEATHER_SF_N,R=,C=2")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP1},P=B_WEATHER_SF_N,R=,C=3")

# SpaceFrame South:
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second,HOST=${IP3},P=B_WEATHER_SF_S,R=,C=0")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second,HOST=${IP3},P=B_WEATHER_SF_S,R=,C=1")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second,HOST=${IP3},P=B_WEATHER_SF_S,R=,C=2")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second,HOST=${IP3},P=B_WEATHER_SF_S,R=,C=3")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP3},P=B_WEATHER_SF_S,R=,C=0")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP3},P=B_WEATHER_SF_S,R=,C=1")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP3},P=B_WEATHER_SF_S,R=,C=2")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP3},P=B_WEATHER_SF_S,R=,C=3")



dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

