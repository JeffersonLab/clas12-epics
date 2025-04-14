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

dbLoadRecords("db/amq-alert-rate-aliases.db")
dbLoadRecords("db/amq-alert-err-aliases.db")

dbLoadTemplate("db/amq-adc-URWELL.substitutions")
dbLoadRecords("amq-adc-URWELL.alias")

cd ${TOP}/iocBoot/${IOC}

#< save_restore.cmd

iocInit

#Need this to start responding to messages after all records are defined
StartMQ()

dbpf("B_DAQ:EB6:stats:01.EGU","Hz")
dbpf("B_DAQ:EB6:stats:02.EGU","MB")
dbpf("B_DAQ:EB6:stats:03.EGU","MB/s")

dbpf("B_DAQ:STA:clondaq11:dataRate.DESC","clondaq11")
dbpf("B_DAQ:STA:clondaq12:dataRate.DESC","clondaq12")
dbpf("B_DAQ:STA:alert1:dataRate.DESC","alert1")
dbpf("B_DAQ:err:clondaq11.DESC","clondaq11")
dbpf("B_DAQ:err:clondaq12.DESC","clondaq12")
dbpf("B_DAQ:err:alert1.DESC","alert1")
dbpf("B_DAQ:ROCS_BUSY:mvt3.DESC","alert1")
dbpf("B_DAQ:ROCS_BUSY:clondaq11","clondaq11")
dbpf("B_DAQ:ROCS_BUSY:clondaq12","clondaq12")

seq waveform, "P=B_DAQ:,R=STA:dataRate:wf"

dbl > pv.list
