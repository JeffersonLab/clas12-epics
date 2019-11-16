#!../../bin/linux-x86_64/mpodLv

< envPaths

epicsEnvSet("EPICS_CA_ADDR_LIST", "129.57.163.255")
epicsEnvSet("EPICS_CAS_BEACON_ADDR_LIST", "129.57.163.255")
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES","10000000")

epicsEnvSet("MIBDIRS","${TOP}/iocBoot/iocsoftsvtRX:/usr/share/snmp/mibs")
epicsEnvSet("MIBS","ALL")
epicsEnvSet("W","WIENER-CRATE-MIB::")

cd "${TOP}"

## Register all support components
#dbLoadDatabase("dbd/cRio.dbd")
#cRio_registerRecordDeviceDriver(pdbbase)
dbLoadDatabase("dbd/mpodLv.dbd")
mpodLv_registerRecordDeviceDriver(pdbbase)

#devSnmpSetParam(DebugLevel,10)

## IOC records:
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")

## cRIO heartbeat alarms:
dbLoadRecords("db/cRIO_heartbeat.db",   "P=B_HW_, R=CRIO_DEV_,  DLY=60")

## Gas systems:
#dbLoadRecords("db/gas_cRIO_HTCC.db",    "P=B_DET_, R=HTCC_GAS_")
#dbLoadRecords("db/gas_cRIO_SVT.db",     "P=B_DET_, R=SVT_GAS_")

## BONUS Gas:
dbLoadRecords("db/gas_cRIO_BONUS.db")

## BONUS HV:
dbLoadRecords("db/mpod-crate.db","HOST=hbmpod5")
dbLoadRecords("db/iseg-module.db","HOST=129.57.86.179,HOSTNAME=hbmpod5,MX=1")
dbLoadRecords("db/iseg-module.db","HOST=129.57.86.179,HOSTNAME=hbmpod5,MX=2")
dbLoadRecords("db/iseg-channel.db","HVHOST=129.57.86.179,HV=B_BONUS_HV_Sl0_Ch0,HVCH=1")
dbLoadRecords("db/iseg-channel.db","HVHOST=129.57.86.179,HV=B_BONUS_HV_Sl0_Ch1,HVCH=2")
dbLoadRecords("db/iseg-channel.db","HVHOST=129.57.86.179,HV=B_BONUS_HV_Sl0_Ch2,HVCH=3")
dbLoadRecords("db/iseg-channel.db","HVHOST=129.57.86.179,HV=B_BONUS_HV_Sl0_Ch3,HVCH=4")
dbLoadRecords("db/iseg-channel.db","HVHOST=129.57.86.179,HV=B_BONUS_HV_Sl0_Ch4,HVCH=5")
dbLoadRecords("db/iseg-channel.db","HVHOST=129.57.86.179,HV=B_BONUS_HV_Sl0_Ch5,HVCH=6")
dbLoadRecords("db/iseg-channel.db","HVHOST=129.57.86.179,HV=B_BONUS_HV_Sl0_Ch6,HVCH=7")
dbLoadRecords("db/iseg-channel.db","HVHOST=129.57.86.179,HV=B_BONUS_HV_Sl0_Ch7,HVCH=8")
dbLoadRecords("db/iseg-channel.db","HVHOST=129.57.86.179,HV=B_BONUS_HV_Sl1_Ch0,HVCH=101")
dbLoadRecords("db/iseg-channel.db","HVHOST=129.57.86.179,HV=B_BONUS_HV_Sl1_Ch1,HVCH=102")
dbLoadRecords("db/iseg-channel.db","HVHOST=129.57.86.179,HV=B_BONUS_HV_Sl1_Ch2,HVCH=103")
dbLoadRecords("db/iseg-channel.db","HVHOST=129.57.86.179,HV=B_BONUS_HV_Sl1_Ch3,HVCH=104")

## waveform test for Brian:
dbLoadRecords("db/criowf.db")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

iocInit

## export pv list
dbl > pv.list

## autosave startup
## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=xxx:")
create_monitor_set("info_settings.req", 30, "P=xxx:")
