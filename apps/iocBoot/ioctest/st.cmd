#!../../bin/linux-x86_64/testApp
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/testApp.dbd")
testApp_registerRecordDeviceDriver pdbbase
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")


# NELM has to be at least as large as #PVs in FNAME
dbLoadRecords("db/waveformApp.db","P=a:,R=a:,NELM=4,  FTVL=FLOAT,PERIOD=5,FNAME=pvScalers.txt")
dbLoadRecords("db/waveformApp.db","P=a:,R=b:,NELM=216,FTVL=FLOAT,PERIOD=5,FNAME=pvCurrents.txt")

cd "${TOP}/iocBoot/${IOC}"

iocInit

seq waveform, "P=a:,R=a:"
seq waveform, "P=a:,R=b:"

