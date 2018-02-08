#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/scaler-ped.db","P=fcup2_offset,VAL=scalerS2b,REF=IPM2C21A,MIN=0.1,N=10")
dbLoadRecords("db/scaler-ped.db","P=slm2_offset,VAL=scalerS15b,REF=IPM2C21A,MIN=0.1,N=10")

cd ${TOP}/iocBoot/${IOC}

iocInit();

