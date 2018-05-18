#!../../bin/linux-x86_64/testApp
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/testApp.dbd")
testApp_registerRecordDeviceDriver pdbbase

epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","10000000")

# NELM has to be at least as large as #PVs in FNAME

dbLoadRecords("db/waveformApp.db","P=beam:,R=0:,NELM=4,   FTVL=FLOAT,PERIOD=5,FNAME=pvlists/wfN.txt")


cd "${TOP}/iocBoot/${IOC}"

iocInit

seq waveformN, "P=beam:,R=0:"


dbl > pv.list

