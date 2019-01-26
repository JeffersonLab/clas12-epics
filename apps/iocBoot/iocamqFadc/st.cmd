#!../../bin/linux-x86_64/amq
< envPaths
cd ${TOP}
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.scalers.fadc")

dbLoadTemplate("db/amq-adc-ECAL.substitutions")
dbLoadTemplate("db/amq-adc-PCAL.substitutions")
dbLoadTemplate("db/amq-adc-FTOF.substitutions")
dbLoadTemplate("db/amq-adc-CTOF.substitutions")
dbLoadTemplate("db/amq-adc-HTCC.substitutions")
dbLoadTemplate("db/amq-adc-LTCC.substitutions")
dbLoadTemplate("db/amq-adc-CND.substitutions")

cd ${TOP}/iocBoot/${IOC}

dbLoadRecords("amq-adc-ECAL.alias")
dbLoadRecords("amq-adc-PCAL.alias")
dbLoadRecords("amq-adc-FTOF.alias")
dbLoadRecords("amq-adc-CTOF.alias")
dbLoadRecords("amq-adc-HTCC.alias")
dbLoadRecords("amq-adc-LTCC.alias")
dbLoadRecords("amq-adc-CND.alias")

iocInit

StartMQ()

dbl > pv.list

