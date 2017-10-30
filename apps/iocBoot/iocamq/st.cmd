#!../../bin/linux-x86_64/amq

cd "../.."

## Register all support components
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clondb3:61616","HallB_TALK")
#ConnectMQ("tcp://127.0.0.1:61616","HallB_DAQ")

## Load record instances

#The RAWMESG key means don't parse for JSON, but writes the whole message into
#a waveform PV up to NELM characters. TYPE must be CHAR.
dbLoadRecords("db/amqStringArray.db","P=B_MSG_DAQ_MSGSTRING,K=RAWMSG,N=200")

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
#N = No of elements in the arrayy

#Ints
dbLoadRecords("db/amqInt.db","P=B_MSG_DAQ_EventRate,K=EventRate")

#Doubles
dbLoadRecords("db/amqDouble.db","P=B_MSG_DAQ_LiveTime,K=LiveTime")

#Int Arrays
dbLoadRecords("db/amqIntArray.db","P=B_MSG_DAQ_TestScalers,K=TestScalers,N=20")

#Double Arrays
dbLoadRecords("db/amqDoubleArray.db","P=B_MSG_DAQ_TestVals,K=TestVals,N=10")

#Strings
dbLoadRecords("db/amqStringArray.db","P=B_MSG_DAQ_NameAddress,K=NameAddress,N=200")

#Need this to start responding to messages after all records are defined
#StartMQ()

#cd ${TOP}/iocBoot/${IOC}
iocInit

#Need this to start responding to messages after all records are defined
StartMQ()