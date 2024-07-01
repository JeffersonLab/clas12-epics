#!../../bin/linux-x86_64/amq

< envPaths

cd ${TOP}

dbLoadDatabase "dbd/amq.dbd"

amq_registerRecordDeviceDriver pdbbase

cd ${TOP}/iocBoot/${IOC}

dbLoadRecords("rich-recovery.db")

iocInit

StartMQ()

