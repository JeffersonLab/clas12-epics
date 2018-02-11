#!../../bin/linux-x86_64/mcc

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/scaler-ped.db","OUT=fcup2_offset,P=fcup2_offset,RAW=scalerS2b, REF=myIPM2C21A,REFMAX=0.1,RAWMAX=500,N=10")
dbLoadRecords("db/scaler-ped.db","OUT=slm2_offset, P=slm2_offset, RAW=scalerS15b,REF=myIPM2C21A,REFMAX=0.1,RAWMAX=500,N=10")

cd ${TOP}/iocBoot/${IOC}

iocInit();

