#!../../bin/linux-x86_64/svtCtrl

< envPaths

epicsEnvSet("MIBDIRS","$(DEVSNMP)/mibs:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")

cd ${TOP}

dbLoadDatabase("dbd/svtCtrl.dbd")

svtCtrl_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/svtR4-mpv-iseg.substitutions")
dbLoadRecords("db/svtR4-hfcb.substitutions")
dbLoadRecords("db/svtWienerCrate.db","HOST=vmetlsvt2")
dbLoadRecords("db/svtWienerCrate.db","HOST=vmetlsvt5")

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

seq &seq_crate2Off
seq &seq_crate5Off
epicsThreadSleep(5)

seq &modCntrl,"MODULE=R4S1,HS=8,LS=1"
seq &modCntrl,"MODULE=R4S2,HS=8,LS=1"
seq &modCntrl,"MODULE=R4S3,HS=8,LS=2"
seq &modCntrl,"MODULE=R4S4,HS=8,LS=2"
seq &modCntrl,"MODULE=R4S5,HS=8,LS=3"
seq &modCntrl,"MODULE=R4S6,HS=8,LS=3"
seq &modCntrl,"MODULE=R4S7,HS=8,LS=4"
seq &modCntrl,"MODULE=R4S8,HS=8,LS=4"
seq &modCntrl,"MODULE=R4S9,HS=9,LS=5"
seq &modCntrl,"MODULE=R4S10,HS=9,LS=5"
seq &modCntrl,"MODULE=R4S11,HS=9,LS=6"
seq &modCntrl,"MODULE=R4S12,HS=9,LS=6"
seq &modCntrl,"MODULE=R4S13,HS=9,LS=1"
seq &modCntrl,"MODULE=R4S14,HS=9,LS=1"
seq &modCntrl,"MODULE=R4S15,HS=9,LS=2"
seq &modCntrl,"MODULE=R4S16,HS=9,LS=2"
seq &modCntrl,"MODULE=R4S17,HS=10,LS=3"
seq &modCntrl,"MODULE=R4S18,HS=10,LS=3"
seq &modCntrl,"MODULE=R4S19,HS=10,LS=4"
seq &modCntrl,"MODULE=R4S20,HS=10,LS=4"
seq &modCntrl,"MODULE=R4S21,HS=10,LS=5"
seq &modCntrl,"MODULE=R4S22,HS=10,LS=5"
seq &modCntrl,"MODULE=R4S23,HS=10,LS=6"
seq &modCntrl,"MODULE=R4S24,HS=10,LS=7"

#< R4_LV_VD_ntrlk.init
#epicsThreadSleep(5)
#< R4_HV_setpt.init

dbl > pv.list

