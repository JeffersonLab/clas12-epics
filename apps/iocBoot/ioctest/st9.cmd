#!../../bin/linux-x86_64/iocscalers
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/iocscalers.dbd")
iocscalers_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/waveformApp.db","P=B_DET_ECAL_,R=FADC_SEC1:,NELM=216,FTVL=FLOAT,PERIOD=2,FNAME=pvlists/ECAL_S1_FADC.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_ECAL_,R=DTRG_SEC1:,NELM=216,FTVL=FLOAT,PERIOD=2,FNAME=pvlists/ECAL_S1_TRG.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_ECAL_,R=DTDC_SEC1:,NELM=216,FTVL=FLOAT,PERIOD=2,FNAME=pvlists/ECAL_S1_TDC.txt")

dbLoadRecords("db/waveformApp.db","P=B_DET_PCAL_,R=FADC_SEC1:,NELM=192,FTVL=FLOAT,PERIOD=2,FNAME=pvlists/PCAL_S1_FADC.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_PCAL_,R=DTRG_SEC1:,NELM=192,FTVL=FLOAT,PERIOD=2,FNAME=pvlists/PCAL_S1_TRG.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_PCAL_,R=DTDC_SEC1:,NELM=192,FTVL=FLOAT,PERIOD=2,FNAME=pvlists/PCAL_S1_TDC.txt")

dbLoadRecords("db/waveformApp.db","P=B_DET_FTOF_,R=FADC_SEC1:,NELM=180,FTVL=FLOAT,PERIOD=2,FNAME=pvlists/FTOF_S1_FADC.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_FTOF_,R=DTRG_SEC1:,NELM=180,FTVL=FLOAT,PERIOD=2,FNAME=pvlists/FTOF_S1_TRG.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_FTOF_,R=DTDC_SEC1:,NELM=180,FTVL=FLOAT,PERIOD=2,FNAME=pvlists/FTOF_S1_TDC.txt")

dbLoadRecords("db/waveformApp.db","P=B_DET_LTCC_,R=FADC_SEC1:,NELM=180,FTVL=FLOAT,PERIOD=2,FNAME=pvlists/LTCC_S1_FADC.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_LTCC_,R=DTRG_SEC1:,NELM=180,FTVL=FLOAT,PERIOD=2,FNAME=pvlists/LTCC_S1_TRG.txt")
dbLoadRecords("db/waveformApp.db","P=B_DET_LTCC_,R=DTDC_SEC1:,NELM=180,FTVL=FLOAT,PERIOD=2,FNAME=pvlists/LTCC_S1_TDC.txt")

cd "${TOP}/iocBoot/${IOC}"
iocInit

seq waveform, "P=B_DET_ECAL_,R=FADC_SEC1:"
seq waveform, "P=B_DET_ECAL_,R=DTRG_SEC1:"
seq waveform, "P=B_DET_ECAL_,R=DTDC_SEC1:"

seq waveform, "P=B_DET_PCAL_,R=FADC_SEC1:"
seq waveform, "P=B_DET_PCAL_,R=DTRG_SEC1:"
seq waveform, "P=B_DET_PCAL_,R=DTDC_SEC1:"

seq waveform, "P=B_DET_FTOF_,R=FADC_SEC1:"
seq waveform, "P=B_DET_FTOF_,R=DTRG_SEC1:"
seq waveform, "P=B_DET_FTOF_,R=DTDC_SEC1:"

seq waveform, "P=B_DET_LTCC_,R=FADC_SEC1:"
seq waveform, "P=B_DET_LTCC_,R=DTRG_SEC1:"
seq waveform, "P=B_DET_LTCC_,R=DTDC_SEC1:"


