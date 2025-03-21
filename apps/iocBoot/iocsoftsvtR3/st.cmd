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

dbLoadTemplate("db/svtR3-mpv-iseg.substitutions")
dbLoadTemplate("db/svtR3-hfcb.substitutions")
dbLoadRecords("db/svtWienerCrate.db","HOST=vmetlsvt3")

dbLoadRecords("db/seq_svtOnOff-1R.db","R=3")

dbLoadRecords("db/svt-averages-R3.db","SIDE=T")
dbLoadRecords("db/svt-averages-R3.db","SIDE=B")

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

seq &seq_crate3Off

seq seq_svtOnOff_1R, "R=3"

epicsThreadSleep(5)

seq &modCntrl,"MODULE=R3S1,HS=8,LS=1"
seq &modCntrl,"MODULE=R3S2,HS=8,LS=1"
seq &modCntrl,"MODULE=R3S3,HS=8,LS=2"
seq &modCntrl,"MODULE=R3S4,HS=8,LS=2"
seq &modCntrl,"MODULE=R3S5,HS=8,LS=3"
seq &modCntrl,"MODULE=R3S6,HS=8,LS=3"
seq &modCntrl,"MODULE=R3S7,HS=8,LS=4"
seq &modCntrl,"MODULE=R3S8,HS=8,LS=4"
seq &modCntrl,"MODULE=R3S9,HS=9,LS=5"
seq &modCntrl,"MODULE=R3S10,HS=9,LS=5"
seq &modCntrl,"MODULE=R3S11,HS=9,LS=6"
seq &modCntrl,"MODULE=R3S12,HS=9,LS=6"
seq &modCntrl,"MODULE=R3S13,HS=9,LS=7"
seq &modCntrl,"MODULE=R3S14,HS=9,LS=7"
seq &modCntrl,"MODULE=R3S15,HS=9,LS=8"
seq &modCntrl,"MODULE=R3S16,HS=9,LS=8"
seq &modCntrl,"MODULE=R3S17,HS=10,LS=9"
seq &modCntrl,"MODULE=R3S18,HS=10,LS=9"

#< R3_LV_VD_ntrlk.init
#epicsThreadSleep(5)

< R3_HV_setpt.init

dbpf("${IOC}:SysReset.ASG","ALLWRITE")

dbl > pv.list

