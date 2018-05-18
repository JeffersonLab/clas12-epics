#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadTemplate("db/hallb_ia.substitutions")
dbLoadRecords("db/hallb_ia.db")

cd ${TOP}/iocBoot/${IOC}

iocInit();

epicsThreadSleep(2)
dbpf "B_IA_C1068_QDAC07:init.PROC", "1"
dbpf "B_IA_C1068_QDAC08:init.PROC", "1"
dbpf "B_IA_C1068_QDAC09:init.PROC", "1"
dbpf "B_IA_C1068_QDAC10:init.PROC", "1"

