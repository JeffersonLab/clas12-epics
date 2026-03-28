#!../../bin/linux-x86_64/amq
< envPaths
cd ${TOP}
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.daq.HallB_DAQ")

dbLoadTemplate("db/amq-tagger.substitutions")
dbLoadRecords("db/amq-tagger-aliases.db")

dbLoadRecords("db/waveformApp.db","P=B_DET_TAGGER_TDC,R=:c:,NELM=20,FTVL=FLOAT,PERIOD=5,FNAME=wf.txt")

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")

cd ${TOP}/iocBoot/${IOC}

iocInit

StartMQ()

dbl > pv.list

seq waveform, "P=B_DET_TAGGER_TDC,R=:c:"

