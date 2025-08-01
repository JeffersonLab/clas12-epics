#!../../bin/linux-x86_64/amq

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.daq.HallB_DAQ")

#The RAWMESG key means don't parse for JSON, but writes the whole message into
#a waveform PV up to NELM characters. TYPE must be CHAR.
#Eg. dbLoadRecords("db/amqStringArray.db","P=B,K=RAWMSG,N=200")

#Now PVs pulling from json objects
#There are 4 types:
#1 Int
#2 Double
#3 Array of Ints
#4 Array of Doubles
#5 String

#Types 1 and 2 for into aiRecords
#Types 3,4,5 go into waveformRecords (with FTVL=DBR_LONG, DBR_DOUBLE, DBR_CHAR respectively) 

#The required macros are:
#P = Prefix
#K = json key
#N = No of elements in the array, if required

#dbLoadRecords("db/amqStringArray.db","P=B_DAQ:RAWMSG,K=RAWMSG,N=1000,TH=0,THH=0,HSV=NO_ALARM,HHSV=NO_ALARM")
#dbLoadRecords("db/amqInt.db","P=B_DAQ:LiveTime,K=LiveTime,TH=10,THH=20,HSV=MINOR,HHSV=MAJOR")
#dbLoadRecords("db/amqDouble.db","P=B_DAQ:EventRate,K=EventRate,TH=10,THH=20,HSV=MINOR,HHSV=MAJOR")
#dbLoadRecords("db/amqIntArray.db","P=B_DAQ:TestScalers,K=TestScalers,N=20,TH=10,THH=20,HSV=MINOR,HHSV=MAJOR")
#dbLoadRecords("db/amqFloatArray.db","P=B_DAQ:TestVals,K=TestVals,N=20,TH=5,THH=10,HSV=MINOR,HHSV=MAJOR")
#dbLoadRecords("db/amqStringArray.db","P=B_DAQ:NameAddress,K=NameAddress,N=100,TH=0,THH=0,HSV=NO_ALARM,HHSV=NO_ALARM")
#dbLoadRecords("db/amqHistogram.db","P=B_DAQ:TestHist,K=TestHist,N=100,NE=101,TH=10,THH=20,HSV=MINOR,HHSV=MAJOR")
#dbLoadRecords("db/amqIntArray.db","P=B_DAQ:FTScalers,K=FTScalers,N=100,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")

############################################################################################################
############################################################################################################

dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:trig2vtp_VTPGT_TRIGGERBITS,K=trig2vtp_VTPGT_TRIGGERBITS,N=32,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")

dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:adcecal1vtp_VTPECS_CLUSTERS,K=adcecal1vtp_VTPECS_CLUSTERS,N=4,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:adcecal2vtp_VTPECS_CLUSTERS,K=adcecal2vtp_VTPECS_CLUSTERS,N=4,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:adcecal3vtp_VTPECS_CLUSTERS,K=adcecal3vtp_VTPECS_CLUSTERS,N=4,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:adcecal4vtp_VTPECS_CLUSTERS,K=adcecal4vtp_VTPECS_CLUSTERS,N=4,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:adcecal5vtp_VTPECS_CLUSTERS,K=adcecal5vtp_VTPECS_CLUSTERS,N=4,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:adcecal6vtp_VTPECS_CLUSTERS,K=adcecal6vtp_VTPECS_CLUSTERS,N=4,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:adcpcal1vtp_VTPPCS_CLUSTERS,K=adcpcal1vtp_VTPPCS_CLUSTERS,N=4,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:adcpcal2vtp_VTPPCS_CLUSTERS,K=adcpcal2vtp_VTPPCS_CLUSTERS,N=4,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:adcpcal3vtp_VTPPCS_CLUSTERS,K=adcpcal3vtp_VTPPCS_CLUSTERS,N=4,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:adcpcal4vtp_VTPPCS_CLUSTERS,K=adcpcal4vtp_VTPPCS_CLUSTERS,N=4,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:adcpcal5vtp_VTPPCS_CLUSTERS,K=adcpcal5vtp_VTPPCS_CLUSTERS,N=4,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:adcpcal6vtp_VTPPCS_CLUSTERS,K=adcpcal6vtp_VTPPCS_CLUSTERS,N=4,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")

# stage 2 trigger:
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:SSPGT_Slot3_TriggerBits,K=SSPGT_Slot3_TriggerBits,N=8,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:SSPGT_Slot4_TriggerBits,K=SSPGT_Slot4_TriggerBits,N=8,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:SSPGT_Slot5_TriggerBits,K=SSPGT_Slot5_TriggerBits,N=8,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:SSPGT_Slot6_TriggerBits,K=SSPGT_Slot6_TriggerBits,N=8,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:SSPGT_Slot7_TriggerBits,K=SSPGT_Slot7_TriggerBits,N=8,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:SSPGT_Slot8_TriggerBits,K=SSPGT_Slot8_TriggerBits,N=8,TH=0,THH=30,HSV=NO_ALARM,HHSV=MAJOR")
dbLoadRecords("db/amqTrigBit-alias.db")

dbLoadRecords("db/amqDouble.db","P=B_DAQ:adccnd1vtp_VTPCND_CLUSTERS,K=adccnd1vtp_VTPCND_CLUSTERS,TH=10,THH=20,HSV=MINOR,HHSV=MAJOR")
dbLoadRecords("db/amqDouble.db","P=B_DAQ:adcctof1vtp_VTPCTOF_CLUSTERS,K=adcctof1vtp_VTPCTOF_CLUSTERS,TH=10,THH=20,HSV=MINOR,HHSV=MAJOR")
dbLoadRecords("db/amqDouble.db","P=B_DAQ:adcctof1vtp_VTPHTCC_CLUSTERS,K=adcctof1vtp_VTPHTCC_CLUSTERS,TH=10,THH=20,HSV=MINOR,HHSV=MAJOR")

dbLoadTemplate("db/amqTriggerBits.substitutions")
dbLoadRecords("db/waveformApp.db","P=B_DAQ:,R=trig2vtp_VTPGT_TRIGGERBITS_P,NELM=32,FTVL=DOUBLE,PERIOD=1,FNAME=trigBitsWaveform.txt")

dbLoadRecords("db/amqTrigBit-alarms.db")
dbLoadRecords("db/amqTrigBit-alarms-set.db")

dbLoadRecords("db/amqTrigBit-sums.db")

dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:SSPGTC_FTCLUSTER_RATE,K=SSPGTC_FTCLUSTER_RATE,N=2,TH=10,THH=20,HSV=MINOR,HHSV=MAJOR")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:SSPGTC_TRIGGERBIT_RATE,K=SSPGTC_TRIGGERBIT_RATE,N=4,TH=10,THH=20,HSV=MINOR,HHSV=MAJOR")
dbLoadRecords("db/amqSplitFT.db")

dbLoadRecords("db/amqFloatArray.db","P=B_DAQ:ROCS_BUSY,K=ROCS_BUSY,N=72,TH=30,THH=60,HSV=MINOR,HHSV=MAJOR")
dbLoadRecords("db/amqRocsBusy.db")

dbLoadRecords("db/stage2bits-wf.db")

dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:TSFP:TriggerBits,K=TRIG1_TSFPSLOT21,N=32,TH=0,THH=30,HSV=NO_ALARM,HHSV=NO_ALARM")
dbLoadRecords("db/amqDoubleArray.db","P=B_DAQ:TSGTP:TriggerBits,K=TRIG1_TSGTPSLOT21,N=32,TH=0,THH=30,HSV=NO_ALARM,HHSV=NO_ALARM")

dbLoadRecords("db/daq2epics-alias.db")

dbLoadRecords("db/amqRocBusy-alarm.db","ROC=mmft1,HIHI=50")

dbLoadTemplate("db/amqTriggerNames.substitutions")
dbLoadTemplate("db/amqTriggerFlags.substitutions")

dbLoadRecords("db/amq-alert-busy-aliases.db")

dbLoadRecords("db/amq-prescaler.db")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

#Need this to start responding to messages after all records are defined
StartMQ()

seq waveform, "P=B_DAQ:,R=trig2vtp_VTPGT_TRIGGERBITS_P"
seq stage2bits
seq sums

seq trigbitclean "INP=B_DAQ:TSGTP:rates:raw, OUT=B_DAQ:TSGTP:rates, PRE=B_DAQ:TSGTP:prescales")
seq trigbitclean "INP=B_DAQ:TSFP:rates:raw,  OUT=B_DAQ:TSFP:rates,  PRE=B_DAQ:TSFP:prescales")

dbpf("B_DAQ:ROCS_BUSY:clondaq11.DESC","clondaq11")
dbpf("B_DAQ:ROCS_BUSY:alert1.DESC","alert1")

dbl > pv.list
