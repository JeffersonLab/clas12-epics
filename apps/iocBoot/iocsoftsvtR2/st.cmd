#!../../bin/linux-x86_64/svtCtrlApp

< envPaths

epicsEnvSet("MIBDIRS","${TOP}/iocBoot/iocsoftsvtRX:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")
epicsEnvSet("W","WIENER-CRATE-MIB::")

cd ${TOP}

dbLoadDatabase("dbd/svtCtrlApp.dbd")

svtCtrlApp_registerRecordDeviceDriver pdbbase

dbLoadTemplate("db/svtR2-mpv-iseg.substitutions")
dbLoadTemplate("db/svtR2-hfcb.substitutions")
dbLoadRecords("db/svtWienerCrate.db","HOST=vmetlsvt4")

dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

iocInit

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

seq &seq_crate4Off
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

< R2_LV_VD_ntrlk.init
epicsThreadSleep(5)
< R2_HV_setpt.init

dbl > pv.list

