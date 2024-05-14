#!../../bin/linux-x86_64/amq

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.daq.HallB_DAQ")

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")

dbLoadTemplate("db/amqRocsRate.substitutions")
dbLoadRecords("db/amqRocsRate-sums.db","P=B_DAQ:STA")
dbLoadRecords("db/waveformApp.db","P=B_DAQ:STA:dataRate:wf,R=,NELM=72,FTVL=FLOAT,PERIOD=1,FNAME=portnames-rates.txt")

dbLoadTemplate("db/amqLatency.substitutions")

dbLoadTemplate("db/amqDaq.substitutions")
dbLoadRecords("db/amqDaq-aliases.db")

dbLoadTemplate("db/amqDaqErrorStrings.substitutions")
dbLoadRecords("db/amqDaqErrorStrings-alarm.db")

cd ${TOP}/iocBoot/${IOC}

#< save_restore.cmd

iocInit

#Need this to start responding to messages after all records are defined
StartMQ()

dbpf("B_DAQ:EB6:stats:01.EGU","Hz")
dbpf("B_DAQ:EB6:stats:02.EGU","MB")
dbpf("B_DAQ:EB6:stats:03.EGU","MB/s")

seq waveform, "P=B_DAQ:,R=STA:dataRate:wf"

dbl > pv.list
