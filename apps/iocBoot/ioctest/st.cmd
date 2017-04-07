#!../../bin/linux-x86_64/waveformApp
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/waveformApp.dbd")
waveformApp_registerRecordDeviceDriver pdbbase
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")


# NELM just has to be at least as large as #PVs in FNAME
dbLoadRecords("db/waveformApp.db","P=a:,R=a:,NELM=4,PERIOD=5,FNAME=dog.txt")
dbLoadRecords("db/waveformApp.db","P=a:,R=b:,NELM=6,PERIOD=5,FNAME=dog2.txt")

cd "${TOP}/iocBoot/${IOC}"

iocInit

seq waveform, "P=a:,R=a:"
seq waveform, "P=a:,R=b:"

