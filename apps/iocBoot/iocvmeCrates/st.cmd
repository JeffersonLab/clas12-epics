#!../../bin/linux-x86_64/vmeCrates

< envPaths

#
epicsEnvSet("MIBDIRS","$(DEVSNMP)/mibs:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")


# just to decrease string size in record:
epicsEnvSet("MIB","WIENER-CRATE-MIB::")
epicsEnvSet("WO", "WIENER-CRATE-MIB::output")
epicsEnvSet("WOM","WIENER-CRATE-MIB::outputMeasurement")
epicsEnvSet("WS", "WIENER-CRATE-MIB::sensor")
epicsEnvSet("WF", "WIENER-CRATE-MIB::fan")

# hostname-ipaddr mapping, used in vmeCrates.substitutions:
< vmeCratesAddresses.env

cd "${TOP}"

dbLoadDatabase ("dbd/vmeCrates.dbd")
vmeCrates_registerRecordDeviceDriver(pdbbase)

#devSnmpSetParam(DebugLevel,10)
devSnmpSetParam(DebugLevel,0)

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", "IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

#epicsEnvSet("scan","10 second")

dbLoadTemplate("db/vmeCrates.substitutions")

#epicsEnvSet("MIBDIRS","${TOP}/iocBoot/iocsoftsvtRX:/usr/share/snmp/mibs")
#epicsEnvSet("W","WIENER-CRATE-MIB::")
#dbLoadRecords("db/svtWienerCrate2.db","HOST=svtvme1")

cd "${TOP}/iocBoot/${IOC}"

< save_restore.cmd

asSetFilename("../acf/cas.acf")

iocInit

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

