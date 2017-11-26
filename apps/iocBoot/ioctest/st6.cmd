#!../../bin/linux-x86_64/testApp
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/testApp.dbd")
testApp_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/scaler-ped.db","P=fcup_offset,VAL=scaler.S2,REF=IPM2C21A,MIN=0.1,N=10")

cd "${TOP}/iocBoot/${IOC}"

iocInit


dbl > pv.list

