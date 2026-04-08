#!../../bin/linux-x86_64/amq
< envPaths
cd ${TOP}
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.daq.HallB_DAQ")

dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ_PRAD:triggers,K=SSPPRAD_SLOT9_TRIGGERBITS,N=32,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ_PRAD:prescales,K=SSPPRAD_SLOT9_PRESCALES,N=32,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/array-to-scalar-8.template","INP=B_DAQ_PRAD:triggers,P=B_DAQ_PRAD:,R=trigger:,S=")
dbLoadRecords("db/array-to-scalar-9.template","INP=B_DAQ_PRAD:prescales,P=B_DAQ_PRAD:,R=prescale:,S=")

dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ_PRAD:trig0tsfp:triggers,K=TRIG0_TSFPSLOT21,N=32")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ_PRAD:trig0tsfp:prescales,K=TRIG0_TSFPPRESCALESSLOT21,N=32")
dbLoadRecords("db/array-to-scalar-32.template","P=B_DAQ_PRAD:trig0tsfp:trigger:,R=,S=,INP=B_DAQ_PRAD:trig0tsfp:triggers,FTVL=FLOAT")
dbLoadRecords("db/array-to-scalar-32.template","P=B_DAQ_PRAD:trig0tsfp:prescale:,R=,S=,INP=B_DAQ_PRAD:trig0tsfp:prescales,FTVL=FLOAT")

dbLoadRecords("db/amq-trigger-names.template","INP=SSPPRAD_SLOT9_TRIGGERBIT,BIT=00,P=B_DAQ_PRAD:trigger:")
dbLoadRecords("db/amq-trigger-names.template","INP=SSPPRAD_SLOT9_TRIGGERBIT,BIT=01,P=B_DAQ_PRAD:trigger:")
dbLoadRecords("db/amq-trigger-names.template","INP=SSPPRAD_SLOT9_TRIGGERBIT,BIT=02,P=B_DAQ_PRAD:trigger:")
dbLoadRecords("db/amq-trigger-names.template","INP=SSPPRAD_SLOT9_TRIGGERBIT,BIT=03,P=B_DAQ_PRAD:trigger:")
dbLoadRecords("db/amq-trigger-names.template","INP=SSPPRAD_SLOT9_TRIGGERBIT,BIT=04,P=B_DAQ_PRAD:trigger:")
dbLoadRecords("db/amq-trigger-names.template","INP=SSPPRAD_SLOT9_TRIGGERBIT,BIT=05,P=B_DAQ_PRAD:trigger:")
dbLoadRecords("db/amq-trigger-names.template","INP=SSPPRAD_SLOT9_TRIGGERBIT,BIT=06,P=B_DAQ_PRAD:trigger:")
dbLoadRecords("db/amq-trigger-names.template","INP=SSPPRAD_SLOT9_TRIGGERBIT,BIT=07,P=B_DAQ_PRAD:trigger:")

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")

dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:prescaled:00,RATE=B_DAQ_PRAD:trigger:00,PRESCALE=B_DAQ_PRAD:prescale:00")
dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:prescaled:01,RATE=B_DAQ_PRAD:trigger:01,PRESCALE=B_DAQ_PRAD:prescale:01")
dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:prescaled:02,RATE=B_DAQ_PRAD:trigger:02,PRESCALE=B_DAQ_PRAD:prescale:02")
dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:prescaled:03,RATE=B_DAQ_PRAD:trigger:03,PRESCALE=B_DAQ_PRAD:prescale:03")
dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:prescaled:04,RATE=B_DAQ_PRAD:trigger:04,PRESCALE=B_DAQ_PRAD:prescale:04")
dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:prescaled:05,RATE=B_DAQ_PRAD:trigger:05,PRESCALE=B_DAQ_PRAD:prescale:05")
dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:prescaled:06,RATE=B_DAQ_PRAD:trigger:06,PRESCALE=B_DAQ_PRAD:prescale:06")
dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:prescaled:07,RATE=B_DAQ_PRAD:trigger:07,PRESCALE=B_DAQ_PRAD:prescale:07")

dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:trig0tsfp:prescaled:23,RATE=B_DAQ_PRAD:trig0tsfp:trigger:23,PRESCALE=B_DAQ_PRAD:trig0tsfp:prescale:23,EQN=A/B")
dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:trig0tsfp:prescaled:24,RATE=B_DAQ_PRAD:trig0tsfp:trigger:24,PRESCALE=B_DAQ_PRAD:trig0tsfp:prescale:24,EQN=A/B")
dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:trig0tsfp:prescaled:25,RATE=B_DAQ_PRAD:trig0tsfp:trigger:25,PRESCALE=B_DAQ_PRAD:trig0tsfp:prescale:25,EQN=A/B")
dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:trig0tsfp:prescaled:26,RATE=B_DAQ_PRAD:trig0tsfp:trigger:26,PRESCALE=B_DAQ_PRAD:trig0tsfp:prescale:26,EQN=A/B")
dbLoadRecords("db/prescaler.db","P=B_DAQ_PRAD:trig0tsfp:prescaled:27,RATE=B_DAQ_PRAD:trig0tsfp:trigger:27,PRESCALE=B_DAQ_PRAD:trig0tsfp:prescale:27,EQN=A/B")

cd ${TOP}/iocBoot/${IOC}

iocInit

StartMQ()

dbl > pv.list

dbpf("B_DAQ_PRAD:trig0tsfp:trigger:23.DESC","Fadc OR")
dbpf("B_DAQ_PRAD:trig0tsfp:trigger:24.DESC","LMS")
dbpf("B_DAQ_PRAD:trig0tsfp:trigger:25.DESC","Alpha")
dbpf("B_DAQ_PRAD:trig0tsfp:trigger:26.DESC","FC")
dbpf("B_DAQ_PRAD:trig0tsfp:trigger:27.DESC","Master OR")
