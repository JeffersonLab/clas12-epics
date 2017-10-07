#!../../bin/linux-x86_64/monitor
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/monitor.dbd")
monitor_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/cRIO_heartbeat_bi.db","P=iocRollAvg,R=:")

dbLoadTemplate("db/rollingAverages.substitutions")

cd "${TOP}/iocBoot/${IOC}"

iocInit

