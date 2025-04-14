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

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbLoadRecords("amq-adc-ECAL.alias")
dbLoadRecords("amq-adc-PCAL.alias")
dbLoadRecords("amq-adc-FTOF.alias")
dbLoadRecords("amq-adc-CTOF.alias")
dbLoadRecords("amq-adc-HTCC.alias")
dbLoadRecords("amq-adc-LTCC.alias")
dbLoadRecords("amq-adc-CND.alias")

StartMQ()

dbl > pv.list

