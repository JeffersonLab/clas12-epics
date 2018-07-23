#!../../bin/linux-x86_64/rollAvg

< envPaths
cd ${TOP}
dbLoadDatabase("dbd/rollAvg.dbd")
rollAvg_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/cRIO_heartbeat_bi.db","P=iocrollAvgGet,R=:")
dbLoadRecords("db/cRIO_heartbeat_bi.db","P=iocrollAvgGet,R=:2h:")
dbLoadRecords("db/cRIO_heartbeat_bi.db","P=iocrollAvgGet,R=:8h:")
dbLoadRecords("db/cRIO_heartbeat_bi.db","P=iocrollAvgGet,R=:24h:")
dbLoadRecords("db/cRIO_heartbeat_bi.db","P=iocrollAvgGet,R=:1w:")

dbLoadRecords("db/rollingAverages-status.db")

dbLoadTemplate("db/rollingAverages.substitutions")

dbLoadRecords("db/timeDerivative.db","P=LL8210,R=,DT=10,SCALE=604,EGU=g/s")
dbLoadRecords("db/timeDerivative.db","P=CLL6763A,R=,DT=2,SCALE=12080,EGU=%/s")

# live average is over DT*N seconds
dbLoadRecords("db/liveRollAvg.db","I=LL8210:dxdt,P=LL8210:dxdt,N=18,EGU=g/s,SCAN=10")
dbLoadRecords("db/liveRollAvg.db","I=CLL6763A:dxdt,P=CLL6763A:dxdt,N=150,EGU=%/s,SCAN=2")

dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")
dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

