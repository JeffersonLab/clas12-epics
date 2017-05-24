#!../../bin/linux-x86_64/testApp
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/testApp.dbd")
testApp_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/seq_test.db","R=1")
dbLoadRecords("db/seq_test.db","R=2")
dbLoadRecords("db/seq_test.db","R=3")
dbLoadRecords("db/seq_test.db","R=4")

dbLoadRecords("db/seq_test2.db")

cd "${TOP}/iocBoot/${IOC}"
iocInit

#seq seq_test, "R=1"
#seq seq_test, "R=2"
#seq seq_test, "R=3"
#seq seq_test, "R=4"

#seq seq_test2

seq seq_svtOnOff_1R, "R=4"

