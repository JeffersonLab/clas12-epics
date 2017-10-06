#!../../bin/linux-x86_64/monitor
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/monitor.dbd")
monitor_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/cRIO_heartbeat_bi.db","P=iocRollingAverages,R=:")

dbLoadRecords("db/rollingAverages.db","P=CPI0840")
dbLoadRecords("db/rollingAverages.db","P=LL8210")
dbLoadRecords("db/rollingAverages.db","P=B_TORUS:LHe:LL8120DP")
dbLoadRecords("db/rollingAverages.db","P=B_TORUS:LHe:LL8120SC")
dbLoadRecords("db/rollingAverages.db","P=B_SOL:LHe:LL8620DP")
dbLoadRecords("db/rollingAverages.db","P=B_SOL:LHe:LL8620SC")
dbLoadRecords("db/rollingAverages.db","P=B_SOL:LHe:LL8670DP")
dbLoadRecords("db/rollingAverages.db","P=B_SOL:LHe:LL8670SC")
dbLoadRecords("db/rollingAverages.db","P=B_SACLAYTGT:LT_CR")
dbLoadRecords("db/rollingAverages.db","P=B_SACLAYTGT:PT_2KH")
dbLoadRecords("db/rollingAverages.db","P=B_SACLAYTGT:TT_ET")
dbLoadRecords("db/rollingAverages.db","P=B_TORUS:LHe:FI8561")
dbLoadRecords("db/rollingAverages.db","P=B_SOL:MPS:I_ZFCT")
dbLoadRecords("db/rollingAverages.db","P=B_SOL:LHe:FI8621A_IN")
dbLoadRecords("db/rollingAverages.db","P=B_SOL:LHe:FI8621B_IN")
dbLoadRecords("db/rollingAverages.db","P=B_TORUS:MPS:I_ZFCT")
dbLoadRecords("db/rollingAverages.db","P=B_TORUS:LHe:FV8121A_IN")
dbLoadRecords("db/rollingAverages.db","P=B_TORUS:LHe:FV8121B_IN")

cd "${TOP}/iocBoot/${IOC}"

iocInit

