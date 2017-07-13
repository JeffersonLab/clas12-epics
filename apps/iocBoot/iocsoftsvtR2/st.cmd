#!../../bin/linux-x86_64/svtCtrlApp

< envPaths

epicsEnvSet("EPICS_CA_ADDR_LIST","129.57.163.255")

epicsEnvSet("MIBDIRS","${TOP}/iocBoot/iocsoftsvtRX:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")
epicsEnvSet("W","WIENER-CRATE-MIB::")

< svtVmeCrateAddresses.env

cd ${TOP}

dbLoadDatabase("dbd/svtCtrlApp.dbd")

svtCtrlApp_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

dbLoadTemplate("db/svtR2-mpv-iseg.substitutions")
dbLoadTemplate("db/svtR2-hfcb.substitutions")
dbLoadRecords("db/svtWienerCrate.db","HOST=vmetlsvt4")

dbLoadRecords("db/svtV450waveform.db")
dbLoadRecords("db/svtmpodwaveform.db")

dbLoadRecords("db/waveformApp.db","P=B_SVT_LV_D_,R=V:,NELM=132,FTVL=FLOAT,PERIOD=5,FNAME=svtLV-V-D.txt")
dbLoadRecords("db/waveformApp.db","P=B_SVT_LV_D_,R=I:,NELM=132,FTVL=FLOAT,PERIOD=5,FNAME=svtLV-I-D.txt")
dbLoadRecords("db/waveformApp.db","P=B_SVT_LV_A_,R=V:,NELM=132,FTVL=FLOAT,PERIOD=5,FNAME=svtLV-V-A.txt")
dbLoadRecords("db/waveformApp.db","P=B_SVT_LV_A_,R=I:,NELM=132,FTVL=FLOAT,PERIOD=5,FNAME=svtLV-I-A.txt")

dbLoadRecords("db/seq_svtOnOff-1R.db","R=2")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

asSetFilename("../acf/svt.acf")
asSetSubstitutions("P=B_,R=SVT_")

iocInit

caPutLogInit("clonioc1:7011")

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

seq &seq_crate4Off

seq seq_svtOnOff_1R, "R=2"

epicsThreadSleep(5)

seq &modCntrl,"MODULE=R2S1,HS=9,LS=1"
seq &modCntrl,"MODULE=R2S2,HS=9,LS=1"
seq &modCntrl,"MODULE=R2S3,HS=9,LS=2"
seq &modCntrl,"MODULE=R2S4,HS=9,LS=2"
seq &modCntrl,"MODULE=R2S5,HS=9,LS=3"
seq &modCntrl,"MODULE=R2S6,HS=9,LS=3"
seq &modCntrl,"MODULE=R2S7,HS=9,LS=4"
seq &modCntrl,"MODULE=R2S8,HS=9,LS=4"
seq &modCntrl,"MODULE=R2S9,HS=10,LS=5"
seq &modCntrl,"MODULE=R2S10,HS=10,LS=5"
seq &modCntrl,"MODULE=R2S11,HS=10,LS=6"
seq &modCntrl,"MODULE=R2S12,HS=10,LS=6"
seq &modCntrl,"MODULE=R2S13,HS=10,LS=7"
seq &modCntrl,"MODULE=R2S14,HS=10,LS=7"

seq &seq_v450waveform
seq &seq_mpodwaveform

seq waveform, "P=B_SVT_LV_D_,R=V:"
seq waveform, "P=B_SVT_LV_D_,R=I:"
seq waveform, "P=B_SVT_LV_A_,R=V:"
seq waveform, "P=B_SVT_LV_A_,R=I:"

#< R2_LV_VD_ntrlk.init

epicsThreadSleep(5)

< R2_HV_setpt.init

dbl > pv.list

