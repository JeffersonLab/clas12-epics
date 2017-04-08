#!../../bin/linux-x86_64/testApp
< envPaths
cd ${TOP}
dbLoadDatabase("dbd/testApp.dbd")
testApp_registerRecordDeviceDriver pdbbase
dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")


# NELM has to be at least as large as #PVs in FNAME

dbLoadRecords("db/waveformApp.db","P=beam:,R=0:,NELM=4,   FTVL=FLOAT,PERIOD=5,FNAME=pvlists/BEAM.txt")

dbLoadRecords("db/waveformApp.db","P=iecal:,R=1:,NELM=216, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iECAL1.txt")
dbLoadRecords("db/waveformApp.db","P=iecal:,R=2:,NELM=216, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iECAL2.txt")
dbLoadRecords("db/waveformApp.db","P=iecal:,R=3:,NELM=216, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iECAL3.txt")
dbLoadRecords("db/waveformApp.db","P=iecal:,R=4:,NELM=216, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iECAL4.txt")
dbLoadRecords("db/waveformApp.db","P=iecal:,R=5:,NELM=216, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iECAL5.txt")
dbLoadRecords("db/waveformApp.db","P=iecal:,R=6:,NELM=216, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iECAL6.txt")

dbLoadRecords("db/waveformApp.db","P=ipcal:,R=1:,NELM=192, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iPCAL1.txt")
dbLoadRecords("db/waveformApp.db","P=ipcal:,R=2:,NELM=192, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iPCAL2.txt")
dbLoadRecords("db/waveformApp.db","P=ipcal:,R=3:,NELM=192, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iPCAL3.txt")
dbLoadRecords("db/waveformApp.db","P=ipcal:,R=4:,NELM=192, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iPCAL4.txt")
dbLoadRecords("db/waveformApp.db","P=ipcal:,R=5:,NELM=192, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iPCAL5.txt")
dbLoadRecords("db/waveformApp.db","P=ipcal:,R=6:,NELM=192, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iPCAL6.txt")

dbLoadRecords("db/waveformApp.db","P=iftof:,R=1:,NELM=180, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iFTOF1.txt")
dbLoadRecords("db/waveformApp.db","P=iftof:,R=2:,NELM=180, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iFTOF2.txt")
dbLoadRecords("db/waveformApp.db","P=iftof:,R=3:,NELM=180, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iFTOF3.txt")
dbLoadRecords("db/waveformApp.db","P=iftof:,R=4:,NELM=180, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iFTOF4.txt")
dbLoadRecords("db/waveformApp.db","P=iftof:,R=5:,NELM=180, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iFTOF5.txt")
dbLoadRecords("db/waveformApp.db","P=iftof:,R=6:,NELM=180, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iFTOF6.txt")

dbLoadRecords("db/waveformApp.db","P=idc:,R=1:,NELM=108, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iDC1.txt")
dbLoadRecords("db/waveformApp.db","P=idc:,R=2:,NELM=108, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iDC2.txt")
dbLoadRecords("db/waveformApp.db","P=idc:,R=3:,NELM=108, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iDC3.txt")
dbLoadRecords("db/waveformApp.db","P=idc:,R=4:,NELM=108, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iDC4.txt")
dbLoadRecords("db/waveformApp.db","P=idc:,R=5:,NELM=108, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iDC5.txt")
dbLoadRecords("db/waveformApp.db","P=idc:,R=6:,NELM=108, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iDC6.txt")

dbLoadRecords("db/waveformApp.db","P=vecal:,R=1:,NELM=216, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vECAL1.txt")
dbLoadRecords("db/waveformApp.db","P=vecal:,R=2:,NELM=216, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vECAL2.txt")
dbLoadRecords("db/waveformApp.db","P=vecal:,R=3:,NELM=216, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vECAL3.txt")
dbLoadRecords("db/waveformApp.db","P=vecal:,R=4:,NELM=216, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vECAL4.txt")
dbLoadRecords("db/waveformApp.db","P=vecal:,R=5:,NELM=216, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vECAL5.txt")
dbLoadRecords("db/waveformApp.db","P=vecal:,R=6:,NELM=216, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vECAL6.txt")

dbLoadRecords("db/waveformApp.db","P=vpcal:,R=1:,NELM=192, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vPCAL1.txt")
dbLoadRecords("db/waveformApp.db","P=vpcal:,R=2:,NELM=192, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vPCAL2.txt")
dbLoadRecords("db/waveformApp.db","P=vpcal:,R=3:,NELM=192, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vPCAL3.txt")
dbLoadRecords("db/waveformApp.db","P=vpcal:,R=4:,NELM=192, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vPCAL4.txt")
dbLoadRecords("db/waveformApp.db","P=vpcal:,R=5:,NELM=192, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vPCAL5.txt")
dbLoadRecords("db/waveformApp.db","P=vpcal:,R=6:,NELM=192, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vPCAL6.txt")

dbLoadRecords("db/waveformApp.db","P=vftof:,R=1:,NELM=180, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vFTOF1.txt")
dbLoadRecords("db/waveformApp.db","P=vftof:,R=2:,NELM=180, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vFTOF2.txt")
dbLoadRecords("db/waveformApp.db","P=vftof:,R=3:,NELM=180, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vFTOF3.txt")
dbLoadRecords("db/waveformApp.db","P=vftof:,R=4:,NELM=180, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vFTOF4.txt")
dbLoadRecords("db/waveformApp.db","P=vftof:,R=5:,NELM=180, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vFTOF5.txt")
dbLoadRecords("db/waveformApp.db","P=vftof:,R=6:,NELM=180, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vFTOF6.txt")

dbLoadRecords("db/waveformApp.db","P=vdc:,R=1:,NELM=108, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vDC1.txt")
dbLoadRecords("db/waveformApp.db","P=vdc:,R=2:,NELM=108, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vDC2.txt")
dbLoadRecords("db/waveformApp.db","P=vdc:,R=3:,NELM=108, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vDC3.txt")
dbLoadRecords("db/waveformApp.db","P=vdc:,R=4:,NELM=108, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vDC4.txt")
dbLoadRecords("db/waveformApp.db","P=vdc:,R=5:,NELM=108, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vDC5.txt")
dbLoadRecords("db/waveformApp.db","P=vdc:,R=6:,NELM=108, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vDC6.txt")

dbLoadRecords("db/waveformApp.db","P=imisc:,R=0:,NELM=4176, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/iMISC.txt")
dbLoadRecords("db/waveformApp.db","P=vmisc:,R=0:,NELM=4176, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/vMISC.txt")

dbLoadRecords("db/waveformApp.db","P=all:,R=0:,NELM=20884, FTVL=FLOAT,PERIOD=5,FNAME=pvlists/ALL.txt")

cd "${TOP}/iocBoot/${IOC}"

iocInit

seq waveform, "P=beam:,R=0:"

seq waveform, "P=iecal:,R=1:"
seq waveform, "P=iecal:,R=2:"
seq waveform, "P=iecal:,R=3:"
seq waveform, "P=iecal:,R=4:"
seq waveform, "P=iecal:,R=5:"
seq waveform, "P=iecal:,R=6:"

seq waveform, "P=ipcal:,R=1:"
seq waveform, "P=ipcal:,R=2:"
seq waveform, "P=ipcal:,R=3:"
seq waveform, "P=ipcal:,R=4:"
seq waveform, "P=ipcal:,R=5:"
seq waveform, "P=ipcal:,R=6:"

seq waveform, "P=iftof:,R=1:"
seq waveform, "P=iftof:,R=2:"
seq waveform, "P=iftof:,R=3:"
seq waveform, "P=iftof:,R=4:"
seq waveform, "P=iftof:,R=5:"
seq waveform, "P=iftof:,R=6:"

seq waveform, "P=idc:,R=1:"
seq waveform, "P=idc:,R=2:"
seq waveform, "P=idc:,R=3:"
seq waveform, "P=idc:,R=4:"
seq waveform, "P=idc:,R=5:"
seq waveform, "P=idc:,R=6:"

seq waveform, "P=vecal:,R=1:"
seq waveform, "P=vecal:,R=2:"
seq waveform, "P=vecal:,R=3:"
seq waveform, "P=vecal:,R=4:"
seq waveform, "P=vecal:,R=5:"
seq waveform, "P=vecal:,R=6:"

seq waveform, "P=vpcal:,R=1:"
seq waveform, "P=vpcal:,R=2:"
seq waveform, "P=vpcal:,R=3:"
seq waveform, "P=vpcal:,R=4:"
seq waveform, "P=vpcal:,R=5:"
seq waveform, "P=vpcal:,R=6:"

seq waveform, "P=vftof:,R=1:"
seq waveform, "P=vftof:,R=2:"
seq waveform, "P=vftof:,R=3:"
seq waveform, "P=vftof:,R=4:"
seq waveform, "P=vftof:,R=5:"
seq waveform, "P=vftof:,R=6:"

seq waveform, "P=vdc:,R=1:"
seq waveform, "P=vdc:,R=2:"
seq waveform, "P=vdc:,R=3:"
seq waveform, "P=vdc:,R=4:"
seq waveform, "P=vdc:,R=5:"
seq waveform, "P=vdc:,R=6:"

seq waveform, "P=imisc:,R=0:"
seq waveform, "P=vmisc:,R=0:"

seq waveform, "P=all:,R=0:"

dbl > pv.list

