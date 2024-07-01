#!../../bin/linux-x86_64/amq

< envPaths

cd ${TOP}

dbLoadDatabase "dbd/amq.dbd"

amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.daq.HallB_DAQ")

#dbLoadRecords("db/amqStringAlarm.db","P=B_DAQ:,R=ss,OK=Ok,N=10")
#dbLoadRecords("db/timer.db","P=B_DAQ:,R=ss,OUT=B_DAQ:ss:clear")
#dbLoadRecords("db/amqString.db","P=B_DAQ:,R=sss")

dbLoadTemplate("db/amqDaqErrorStrings.substitutions")

cd ${TOP}/iocBoot/${IOC}

iocInit

StartMQ()

