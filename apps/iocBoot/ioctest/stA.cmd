#!../../bin/linux-x86_64/testApp
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/testApp.dbd")
testApp_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/moeller_coincaccid_ratio.db")

cd "${TOP}/iocBoot/${IOC}"

iocInit

