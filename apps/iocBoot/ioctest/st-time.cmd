#!../../bin/linux-x86_64/amq

< envPaths

cd ${TOP}

dbLoadDatabase "dbd/amq.dbd"

amq_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/clock-human.db","P=B_RICH,R=:recovery:,CLOCK=B_RICH:recovery:clock")

cd ${TOP}/iocBoot/${IOC}

#dbLoadRecords("amqDaqErrorStrings-alarm.db")

iocInit

StartMQ()

