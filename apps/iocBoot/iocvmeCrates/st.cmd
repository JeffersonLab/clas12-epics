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

cd "${TOP}"

dbLoadDatabase ("dbd/vmeCrates.dbd")
vmeCrates_registerRecordDeviceDriver(pdbbase)

#devSnmpSetParam(DebugLevel,10)
devSnmpSetParam(DebugLevel,0)

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", "IOC=$(IOC)")

epicsEnvSet("scan","10 second")


dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=ltcc0,IP=129.57.86.47")
dbLoadRecords("db/wienerW.db","HOST=ltcc0,IP=129.57.86.47")
dbLoadRecords("db/vmePedestals.db","HOST=ltcc0,IP=129.57.86.47,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=pcal0,IP=129.57.86.44")
dbLoadRecords("db/wienerW.db","HOST=pcal0,IP=129.57.86.44")
dbLoadRecords("db/vmePedestals.db","HOST=pcal0,IP=129.57.86.44,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=hps2,IP=129.57.69.40")
dbLoadRecords("db/wienerW.db","HOST=hps2,IP=129.57.69.40")
dbLoadRecords("db/vmePedestals.db","HOST=hps2,IP=129.57.69.40,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcecal1,IP=129.57.167.80")
dbLoadRecords("db/wienerW.db","HOST=adcecal1,IP=129.57.167.80")
dbLoadRecords("db/vmePedestals.db","HOST=adcecal1,IP=129.57.167.80,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=hps12,IP=129.57.167.20")
dbLoadRecords("db/wienerW.db","HOST=hps12,IP=129.57.167.20")
dbLoadRecords("db/vmePedestals.db","HOST=hps12,IP=129.57.167.20,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=hps1,IP=129.57.167.164")
dbLoadRecords("db/wienerW.db","HOST=hps1,IP=129.57.167.164")
dbLoadRecords("db/vmePedestals.db","HOST=hps1,IP=129.57.167.164,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=hps2,IP=129.57.167.165")
dbLoadRecords("db/wienerW.db","HOST=hps2,IP=129.57.167.165")
dbLoadRecords("db/vmePedestals.db","HOST=hps2,IP=129.57.167.165,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=dcrb1,IP=129.57.86.53")
dbLoadRecords("db/wienerW.db","HOST=dcrb1,IP=129.57.86.53")
dbLoadRecords("db/vmePedestals.db","HOST=dcrb1,IP=129.57.86.53,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcecal1,IP=129.57.167.52")
dbLoadRecords("db/wienerW.db","HOST=tdcecal1,IP=129.57.167.52")
dbLoadRecords("db/vmePedestals.db","HOST=tdcecal1,IP=129.57.167.52,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcpcal1,IP=129.57.167.54")
dbLoadRecords("db/wienerW.db","HOST=tdcpcal1,IP=129.57.167.54")
dbLoadRecords("db/vmePedestals.db","HOST=tdcpcal1,IP=129.57.167.54,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcftof1,IP=129.57.167.73")
dbLoadRecords("db/wienerW.db","HOST=tdcftof1,IP=129.57.167.73")
dbLoadRecords("db/vmePedestals.db","HOST=tdcftof1,IP=129.57.167.73,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcpcal1,IP=129.57.167.81")
dbLoadRecords("db/wienerW.db","HOST=adcpcal1,IP=129.57.167.81")
dbLoadRecords("db/vmePedestals.db","HOST=adcpcal1,IP=129.57.167.81,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcftof1,IP=129.57.167.156")
dbLoadRecords("db/wienerW.db","HOST=adcftof1,IP=129.57.167.156")
dbLoadRecords("db/vmePedestals.db","HOST=adcftof1,IP=129.57.167.156,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcecal1,IP=129.57.167.80")
dbLoadRecords("db/wienerW.db","HOST=adcecal1,IP=129.57.167.80")
dbLoadRecords("db/vmePedestals.db","HOST=adcecal1,IP=129.57.167.80,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcftof6,IP=129.57.167.157")
dbLoadRecords("db/wienerW.db","HOST=adcftof6,IP=129.57.167.157")
dbLoadRecords("db/vmePedestals.db","HOST=adcftof6,IP=129.57.167.157,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcftof6,IP=129.57.167.158")
dbLoadRecords("db/wienerW.db","HOST=tdcftof6,IP=129.57.167.158")
dbLoadRecords("db/vmePedestals.db","HOST=tdcftof6,IP=129.57.167.158,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcpcal6,IP=129.57.167.39")
dbLoadRecords("db/wienerW.db","HOST=adcpcal6,IP=129.57.167.39")
dbLoadRecords("db/vmePedestals.db","HOST=adcpcal6,IP=129.57.167.39,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcpcal6,IP=129.57.167.163")
dbLoadRecords("db/wienerW.db","HOST=tdcpcal6,IP=129.57.167.163")
dbLoadRecords("db/vmePedestals.db","HOST=tdcpcal6,IP=129.57.167.163,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcecal6,IP=129.57.167.38")
dbLoadRecords("db/wienerW.db","HOST=adcecal6,IP=129.57.167.38")
dbLoadRecords("db/vmePedestals.db","HOST=adcecal6,IP=129.57.167.38,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcecal6,IP=129.57.167.40")
dbLoadRecords("db/wienerW.db","HOST=tdcecal6,IP=129.57.167.40")
dbLoadRecords("db/vmePedestals.db","HOST=tdcecal6,IP=129.57.167.40,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcecal5,IP=129.57.167.169")
dbLoadRecords("db/wienerW.db","HOST=adcecal5,IP=129.57.167.169")
dbLoadRecords("db/vmePedestals.db","HOST=adcecal5,IP=129.57.167.169,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcecal5,IP=129.57.167.170")
dbLoadRecords("db/wienerW.db","HOST=tdcecal5,IP=129.57.167.170")
dbLoadRecords("db/vmePedestals.db","HOST=tdcecal5,IP=129.57.167.170,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcpcal5,IP=129.57.167.171")
dbLoadRecords("db/wienerW.db","HOST=adcpcal5,IP=129.57.167.171")
dbLoadRecords("db/vmePedestals.db","HOST=adcpcal5,IP=129.57.167.171,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcpcal5,IP=129.57.167.176")
dbLoadRecords("db/wienerW.db","HOST=tdcpcal5,IP=129.57.167.176")
dbLoadRecords("db/vmePedestals.db","HOST=tdcpcal5,IP=129.57.167.176,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcftof5,IP=129.57.167.177")
dbLoadRecords("db/wienerW.db","HOST=adcftof5,IP=129.57.167.177")
dbLoadRecords("db/vmePedestals.db","HOST=adcftof5,IP=129.57.167.177,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcftof5,IP=129.57.167.178")
dbLoadRecords("db/wienerW.db","HOST=tdcftof5,IP=129.57.167.178")
dbLoadRecords("db/vmePedestals.db","HOST=tdcftof5,IP=129.57.167.178,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcecal4,IP=129.57.167.189")
dbLoadRecords("db/wienerW.db","HOST=adcecal4,IP=129.57.167.189")
dbLoadRecords("db/vmePedestals.db","HOST=adcecal4,IP=129.57.167.189,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcecal4,IP=129.57.167.186")
dbLoadRecords("db/wienerW.db","HOST=tdcecal4,IP=129.57.167.186")
dbLoadRecords("db/vmePedestals.db","HOST=tdcecal4,IP=129.57.167.186,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcpcal4,IP=129.57.167.188")
dbLoadRecords("db/wienerW.db","HOST=adcpcal4,IP=129.57.167.188")
dbLoadRecords("db/vmePedestals.db","HOST=adcpcal4,IP=129.57.167.188,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcpcal4,IP=129.57.167.185")
dbLoadRecords("db/wienerW.db","HOST=tdcpcal4,IP=129.57.167.185")
dbLoadRecords("db/vmePedestals.db","HOST=tdcpcal4,IP=129.57.167.185,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcftof4,IP=129.57.167.187")
dbLoadRecords("db/wienerW.db","HOST=adcftof4,IP=129.57.167.187")
dbLoadRecords("db/vmePedestals.db","HOST=adcftof4,IP=129.57.167.187,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcftof4,IP=129.57.167.183")
dbLoadRecords("db/wienerW.db","HOST=tdcftof4,IP=129.57.167.183")
dbLoadRecords("db/vmePedestals.db","HOST=tdcftof4,IP=129.57.167.183,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcecal2,IP=129.57.167.212")
dbLoadRecords("db/wienerW.db","HOST=adcecal2,IP=129.57.167.212")
dbLoadRecords("db/vmePedestals.db","HOST=adcecal2,IP=129.57.167.212,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcecal2,IP=129.57.167.192")
dbLoadRecords("db/wienerW.db","HOST=tdcecal2,IP=129.57.167.192")
dbLoadRecords("db/vmePedestals.db","HOST=tdcecal2,IP=129.57.167.192,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcpcal2,IP=129.57.167.216")
dbLoadRecords("db/wienerW.db","HOST=adcpcal2,IP=129.57.167.216")
dbLoadRecords("db/vmePedestals.db","HOST=adcpcal2,IP=129.57.167.216,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcpcal2,IP=129.57.167.211")
dbLoadRecords("db/wienerW.db","HOST=tdcpcal2,IP=129.57.167.211")
dbLoadRecords("db/vmePedestals.db","HOST=tdcpcal2,IP=129.57.167.211,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcftof2,IP=129.57.167.251")
dbLoadRecords("db/wienerW.db","HOST=adcftof2,IP=129.57.167.251")
dbLoadRecords("db/vmePedestals.db","HOST=adcftof2,IP=129.57.167.251,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcftof2,IP=129.57.167.21")
dbLoadRecords("db/wienerW.db","HOST=tdcftof2,IP=129.57.167.21")
dbLoadRecords("db/vmePedestals.db","HOST=tdcftof2,IP=129.57.167.21,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcecal3,IP=129.57.167.32")
dbLoadRecords("db/wienerW.db","HOST=adcecal3,IP=129.57.167.32")
dbLoadRecords("db/vmePedestals.db","HOST=adcecal3,IP=129.57.167.32,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcecal3,IP=129.57.167.22")
dbLoadRecords("db/wienerW.db","HOST=tdcecal3,IP=129.57.167.22")
dbLoadRecords("db/vmePedestals.db","HOST=tdcecal3,IP=129.57.167.22,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcpcal3,IP=129.57.167.34")
dbLoadRecords("db/wienerW.db","HOST=adcpcal3,IP=129.57.167.34")
dbLoadRecords("db/vmePedestals.db","HOST=adcpcal3,IP=129.57.167.34,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcpcal3,IP=129.57.167.19")
dbLoadRecords("db/wienerW.db","HOST=tdcpcal3,IP=129.57.167.19")
dbLoadRecords("db/vmePedestals.db","HOST=tdcpcal3,IP=129.57.167.19,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcftof3,IP=129.57.167.37")
dbLoadRecords("db/wienerW.db","HOST=adcftof3,IP=129.57.167.37")
dbLoadRecords("db/vmePedestals.db","HOST=adcftof3,IP=129.57.167.37,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=tdcftof3,IP=129.57.167.27")
dbLoadRecords("db/wienerW.db","HOST=tdcftof3,IP=129.57.167.27")
dbLoadRecords("db/vmePedestals.db","HOST=tdcftof3,IP=129.57.167.27,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=hps11,IP=129.57.167.93")
dbLoadRecords("db/wienerW.db","HOST=hps11,IP=129.57.167.93")
dbLoadRecords("db/vmePedestals.db","HOST=hps11,IP=129.57.167.93,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=dcrb2,IP=129.57.86.67")
dbLoadRecords("db/wienerW.db","HOST=dcrb2,IP=129.57.86.67")
dbLoadRecords("db/vmePedestals.db","HOST=dcrb2,IP=129.57.86.67,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=ctof1,IP=129.57.86.79")
dbLoadRecords("db/wienerW.db","HOST=ctof1,IP=129.57.86.79")
dbLoadRecords("db/vmePedestals.db","HOST=ctof1,IP=129.57.86.79,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcft1,IP=129.57.86.102")
dbLoadRecords("db/wienerW.db","HOST=adcft1,IP=129.57.86.102")
dbLoadRecords("db/vmePedestals.db","HOST=adcft1,IP=129.57.86.102,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcft2,IP=129.57.86.103")
dbLoadRecords("db/wienerW.db","HOST=adcft2,IP=129.57.86.103")
dbLoadRecords("db/vmePedestals.db","HOST=adcft2,IP=129.57.86.103,VXS_FLAG=1")

dbLoadRecords("db/wienerR.db","SCAN=${scan},HOST=adcft3,IP=129.57.86.104")
dbLoadRecords("db/wienerW.db","HOST=adcft3,IP=129.57.86.104")
dbLoadRecords("db/vmePedestals.db","HOST=adcft3,IP=129.57.86.104,VXS_FLAG=1")

cd "${TOP}/iocBoot/${IOC}"
iocInit
