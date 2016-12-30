#!../../bin/linux-x86_64/sensorProbe

< envPaths

epicsEnvSet("MIBDIRS","$(DEVSNMP)/mibs:$(TOP)/mibs:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")

# hallb-akcp123:
epicsEnvSet("IP1","129.57.160.80")
epicsEnvSet("IP2","129.57.160.153")
epicsEnvSet("IP3","129.57.160.154")

# to reduce record INP length:
epicsEnvSet("SPM","SPAGENT-MIB::sensorProbe")

cd "${TOP}"

dbLoadDatabase ("dbd/sensorProbe.dbd")
sensorProbe_registerRecordDeviceDriver(pdbbase)

# AKCP SensorProbe requires SNMP version #1:
devSnmpSetSnmpVersion("${IP1}",SNMP_VERSION_1)
devSnmpSetSnmpVersion("${IP2}",SNMP_VERSION_1)
devSnmpSetSnmpVersion("${IP3}",SNMP_VERSION_1)

devSnmpSetParam(DebugLevel,10)
#devSnmpSetParam(DebugLevel,0)

dbLoadRecords("db/sensorProbe_temperature.db","HOST=${IP2},SPM=${SPM},P=B_WEATHER_FC:,R=,CHAN=0")
dbLoadRecords("db/sensorProbe_temperature.db","HOST=${IP2},SPM=${SPM},P=B_WEATHER_FC:,R=,CHAN=1")
dbLoadRecords("db/sensorProbe_temperature.db","HOST=${IP2},SPM=${SPM},P=B_WEATHER_FC:,R=,CHAN=2")
dbLoadRecords("db/sensorProbe_temperature.db","HOST=${IP2},SPM=${SPM},P=B_WEATHER_FC:,R=,CHAN=3")

dbLoadRecords("db/sensorProbe_humidity.db","HOST=${IP2},SPM=${SPM},P=B_WEATHER_FC:,R=,CHAN=0")
dbLoadRecords("db/sensorProbe_humidity.db","HOST=${IP2},SPM=${SPM},P=B_WEATHER_FC:,R=,CHAN=1")
dbLoadRecords("db/sensorProbe_humidity.db","HOST=${IP2},SPM=${SPM},P=B_WEATHER_FC:,R=,CHAN=2")
dbLoadRecords("db/sensorProbe_humidity.db","HOST=${IP2},SPM=${SPM},P=B_WEATHER_FC:,R=,CHAN=3")

#dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", "IOC=$(IOC)")

cd "${TOP}/iocBoot/${IOC}"
iocInit

