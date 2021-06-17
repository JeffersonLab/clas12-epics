#!../../bin/linux-x86_64/amq

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/amqStringArray.db","P=qwerasdf,K=trig2vtp_VTPGT_TRIGGERBITS,N=100,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")

cd ${TOP}/iocBoot/${IOC}

#dbLoadRecords("stringy.db")

iocInit();

