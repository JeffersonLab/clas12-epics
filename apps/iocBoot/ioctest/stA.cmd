#!../../bin/linux-x86_64/testApp
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/testApp.dbd")
testApp_registerRecordDeviceDriver pdbbase

#dbLoadRecords("db/moeller_coincaccid_ratio.db")

#dbLoadRecords("db/timeDerivative.db","P=LL8210,R=:deriv,DT=10,SCALE=1000,EGU=g/s")

dbLoadTemplate("db/mcc_fsd.substitutions")

cd "${TOP}/iocBoot/${IOC}"

iocInit

