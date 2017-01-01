#!../../bin/linux-x86_64/sensorProbe

< envPaths

epicsEnvSet("MIBDIRS","$(DEVSNMP)/mibs:$(TOP)/mibs:/usr/share/snmp/mibs")
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

###
### We have occaisonal read errors (log below) which result in no further
### PV updates (.STATs stay stuck in READ forever).  Dividing records into
### different scan rates appears to alleviate this a bit, as does reducing
### number of records, but even with only one record problem still happens.
###
### *** devSnmp 129.57.160.153 transaction (GET) error = 2 ((noSuchName) There is no such variable name in this MIB.)
### *** devSnmp SPAGENT-MIB::sensorProbeTempDegree.0 (GET) error = 2 ((noSuchName) There is no such variable name in this MIB.)
### *** devSnmp SPAGENT-MIB::sensorProbeTempDegree.0 (GET) flagged bad, error = 2 ((noSuchName) There is no such variable name in this MIB.)
### 2016/12/31 18:02:10  devSnmp SPAGENT-MIB::sensorProbeTempDegree.0 data stale (20000 msec overdue for poll)
### 2016/12/31 18:02:14  devSnmp AI read error 'B_WEATHER_FC0_Temp' : oid has no valid reading
###
# devSnmpSetParam(parname,value)
#   DataStaleTimeoutMSec
#   MaxOidCompFailures
#   MaxTopPollWeight
#   DoNotPollWeight
#   ThreadSleepMSec
#   SessionTimeout
#   SessionRetries
#
# This didn't seem to help:
#devSnmpSetMaxOidsPerReq("${IP2}",1)
#
# and neither did these:
#devSnmpSetParam(ThreadSleepMSec,100)
#devSnmpSetParam(SessionTimeout,100000)
#devSnmpSetParam(SessionRetries,50)
#
### Did a shell script loop of snmpgets, and eventually hit this error
### below.  The following (10 seconds later) snmpget succeeded.  Since
### snmpgets recover, but devsnmp does not, either debug devsnmp module
### or write a one-off snmpget driver to fix this?
###
### Error in packet
### Reason: (noSuchName) There is no such variable name in this MIB.
### Failed object: SPAGENT-MIB::sensorProbeTempDegree.0
###

# Forward Carriage:
dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second, HOST=${IP2},P=B_WEATHER_FC,R=,C=0")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second, HOST=${IP2},P=B_WEATHER_FC,R=,C=1")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second, HOST=${IP2},P=B_WEATHER_FC,R=,C=2")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=10 second, HOST=${IP2},P=B_WEATHER_FC,R=,C=3")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP2},P=B_WEATHER_FC,R=,C=0")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP2},P=B_WEATHER_FC,R=,C=1")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP2},P=B_WEATHER_FC,R=,C=2")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP2},P=B_WEATHER_FC,R=,C=3")

# SpaceFrame North:
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=5 second, HOST=${IP1},P=B_WEATHER_SF_N,R=,C=0")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=5 second, HOST=${IP1},P=B_WEATHER_SF_N,R=,C=1")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=5 second, HOST=${IP1},P=B_WEATHER_SF_N,R=,C=2")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=5 second, HOST=${IP1},P=B_WEATHER_SF_N,R=,C=3")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP1},P=B_WEATHER_SF_N,R=,C=0")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP1},P=B_WEATHER_SF_N,R=,C=1")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP1},P=B_WEATHER_SF_N,R=,C=2")
#dbLoadRecords("db/sensorProbe_humidity.db",   "SCAN=10 second,HOST=${IP1},P=B_WEATHER_SF_N,R=,C=3")

# SpaceFrame South:
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=5 second, HOST=${IP3},P=B_WEATHER_SF_S,R=,C=0")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=5 second, HOST=${IP3},P=B_WEATHER_SF_S,R=,C=1")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=5 second, HOST=${IP3},P=B_WEATHER_SF_S,R=,C=2")
#dbLoadRecords("db/sensorProbe_temperature.db","SCAN=5 second, HOST=${IP3},P=B_WEATHER_SF_S,R=,C=3")
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

