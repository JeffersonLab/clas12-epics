#!../../bin/linux-x86_64/amq

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.daq.HallB_DAQ")

dbLoadRecords("db/amqIntArray.db","P=B_DAQ:HEL:c,K=L3_HELICITY_SCALERS,N=66,TH=0,THH=120,HSV=NO_ALARM,HHSV=MAJOR")

dbLoadRecords("db/array-to-scalar-66.template","P=B_DAQ:HEL:,R=,S=,INP=B_DAQ:HEL:c,FTVL=LONG,FLNK=B_DAQ:HEL:flnk.PROC")

dbLoadTemplate("db/amq-helicity.substitutions")
dbLoadRecords("db/amq-helicity-flnk.db","P=B_DAQ:HEL:")

dbLoadRecords("db/timer.db","P=TGT:PT12:NMR,OUT=TGT:PT12:NMR_Time:1.PROC")
dbLoadRecords("db/nmr-heartbeat.db")

cd ${TOP}/iocBoot/${IOC}

iocInit();

StartMQ()

