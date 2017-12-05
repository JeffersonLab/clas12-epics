#!../../bin/linux-x86_64/testApp
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/testApp.dbd")
testApp_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/hallb_ia.db")

cd "${TOP}/iocBoot/${IOC}"

iocInit


dbl > pv.list

