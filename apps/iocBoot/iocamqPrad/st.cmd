#!../../bin/linux-x86_64/amq
< envPaths
cd ${TOP}
dbLoadDatabase "dbd/amq.dbd"
amq_registerRecordDeviceDriver pdbbase

ConnectMQ("tcp://clon00:61616","clasrun.clasprod.scalers.fadc")

dbLoadTemplate("db/amq-hycal.substitutions")
dbLoadRecords("db/amq-hycal-aliases.db")

dbLoadRecords("db/waveformApp.db","P=B_HW_HYCAL_FADC,R=:c:,NELM=2016,FTVL=FLOAT,PERIOD=2,FNAME=hw-wf.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_HYCAL_FADC,R=:c:,NELM=1156,FTVL=FLOAT,PERIOD=2,FNAME=pb-wf.txt")

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db","IOC=$(IOC)")

cd ${TOP}/iocBoot/${IOC}

iocInit

StartMQ()

dbl > pv.list

seq waveform, "P=B_HW_HYCAL_FADC,R=:c:"
seq waveform, "P=B_DET_HYCAL_FADC,R=:c:"

