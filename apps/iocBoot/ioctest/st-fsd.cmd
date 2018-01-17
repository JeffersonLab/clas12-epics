#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/mcc_fsd_bits.template","P=B_FSD_2H001:,R=MASK,I=ISD2H001HALOMASKr,ZSV=NO_ALARM,OSV=MAJOR")
dbLoadRecords("db/mcc_fsd_bits.template","P=B_FSD_2H001:,R=TRIP,I=ISD2H001HALOTESTr,ZSV=NO_ALARM,OSV=MAJOR")
dbLoadRecords("db/mcc_fsd_aliases.db")

cd ${TOP}/iocBoot/${IOC}

iocInit();

