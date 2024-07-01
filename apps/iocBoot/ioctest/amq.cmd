#!../../bin/linux-x86_64/amq

< envPaths

cd ${TOP}

dbLoadDatabase "dbd/amq.dbd"

amq_registerRecordDeviceDriver pdbbase

#ConnectMQ("tcp://clon00:61616","clasrun.clasprod.daq.HallB_DAQ")
ConnectMQ("tcp://clon00:61616","clasrun.clasprod.controls")

#ConnectMQ("tcp://clon00:1883?wireFormat=mqtt","clasrun/clasprod"

dbLoadRecords("db/amqFloatArray.db","P=b:yuk:a,K=FCL1Weather,N=2,TH=5,THH=10,HSV=MINOR,HHSV=MAJOR")

cd ${TOP}/iocBoot/${IOC}

iocInit

StartMQ()

