#!../../bin/linux-x86_64/amq
< envPaths
cd ${TOP}
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.daq.HallB_DAQ")

dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:PRAD:triggers,K=SSPPRAD_SLOT9_TRIGGERBITS,N=32,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:PRAD:prescales,K=SSPPRAD_SLOT9_PRESCALES,N=32,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")

cd ${TOP}/iocBoot/${IOC}

iocInit

StartMQ()

dbl > pv.list

