#!../../bin/linux-x86_64/amq
< envPaths
cd ${TOP}
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.daq.HallB_DAQ")

dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ_PRAD:triggers,K=SSPPRAD_SLOT9_TRIGGERBITS,N=32,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ_PRAD:prescales,K=SSPPRAD_SLOT9_PRESCALES,N=32,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")

dbLoadRecords("db/array-to-scalar-8.template","INP=B_DAQ_PRAD:triggers,P=B_DAQ_PRAD:,R=trigger:,S=")
dbLoadRecords("db/array-to-scalar-9.template","INP=B_DAQ_PRAD:triggers,P=B_DAQ_PRAD:,R=prescale:,S=")

dbLoadTemplate("db/amq-prad-trigger.substitutions")

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")

cd ${TOP}/iocBoot/${IOC}

iocInit

StartMQ()

dbl > pv.list

