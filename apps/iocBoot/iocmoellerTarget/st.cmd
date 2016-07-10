#!../../bin/linux-x86_64/moeller_target

< envPaths
cd ${TOP}

dbLoadDatabase "dbd/moeller_target.dbd"
moeller_target_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

dbLoadRecords "db/moeller_target_cmd.db")

cd ${TOP}/iocBoot/${IOC}

iocInit

seq moeller_target

