#!../../bin/linux-x86_64/svtCtrlApp

< envPaths

epicsEnvSet("MIBDIRS","${TOP}/iocBoot/iocsoftsvtRX:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")
epicsEnvSet("W","WIENER-CRATE-MIB::")

< svtVmeCrateAddresses.env

cd ${TOP}

dbLoadDatabase("dbd/svtCtrlApp.dbd")

svtCtrlApp_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

dbLoadTemplate("db/svtR1-mpv-iseg.substitutions")
dbLoadTemplate("db/svtR1-hfcb.substitutions")
dbLoadRecords("db/svtWienerCrate.db","HOST=vmetlsvt1")
dbLoadRecords("db/svtCrateAlarm.db")
dbLoadRecords("db/svtWatchdog.db")

dbLoadRecords("db/svtWienerCrate2.db","HOST=svtvme1")

dbLoadRecords("db/seq_svtOnOff-1R.db","R=1")
dbLoadRecords("db/seq_svtOnOff-All.db")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

asSetFilename("../acf/cas.acf")

iocInit

caPutLogInit("clonioc1:7011")

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

seq &seq_crate1Off

seq seq_svtOnOff_1R, "R=1"
seq seq_svtOnOff_All

epicsThreadSleep(5)

seq &modCntrl,"MODULE=R1S1,HS=7,LS=1"
seq &modCntrl,"MODULE=R1S2,HS=7,LS=1"
seq &modCntrl,"MODULE=R1S3,HS=7,LS=2"
seq &modCntrl,"MODULE=R1S4,HS=7,LS=2"
seq &modCntrl,"MODULE=R1S5,HS=7,LS=3"
seq &modCntrl,"MODULE=R1S6,HS=7,LS=3"
seq &modCntrl,"MODULE=R1S7,HS=7,LS=4"
seq &modCntrl,"MODULE=R1S8,HS=7,LS=4"
seq &modCntrl,"MODULE=R1S9,HS=8,LS=5"
seq &modCntrl,"MODULE=R1S10,HS=8,LS=5"

#< R1_LV_VD_ntrlk.init
epicsThreadSleep(5)
< R1_HV_setpt.init

dbl > pv.list

