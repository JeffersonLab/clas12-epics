#!../../bin/linux-x86_64/dchvWaveform

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/dchvWaveform.dbd"
dchvWaveform_registerRecordDeviceDriver pdbbase

# increase from the defaults was necessary (although not tuned)
callbackSetQueueSize(10000)
scanOnceSetQueueSize(10000)

dbLoadRecords("db/dchvWaveformsGlobal.db")
dbLoadTemplate("db/dchvWaveforms.substitutions")

cd ${TOP}/iocBoot/${IOC}

iocInit();

seq seqDCHVwaveforms


