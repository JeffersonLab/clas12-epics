#!../../bin/linux-x86_64/mcc

< envPaths
epicsEnvSet("EPICS_CA_ADDR_LIST","129.57.255.12 129.57.163.255")

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mcc.dbd"
mcc_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")
dbLoadRecords("db/iocAdminSoft.db","IOC=${IOC}")

dbLoadRecords("db/mcc_vacuum.db")
dbLoadRecords("db/mcc_bpm.db")
dbLoadRecords("db/mcc_cryo.db")
dbLoadRecords("db/mcc_tagger.db")
dbLoadRecords("db/mcc_fsd.db")
dbLoadRecords("db/mcc_fsd_alarm.db")

dbLoadRecords("db/hall_target.db","P=HLB:TARGET:")

dbLoadTemplate("db/alarm_bpm.substitutions")

# these must be run as user=clasioc and host=clonioc#:
dbLoadTemplate("db/hallb_ia.substitutions")

dbLoadRecords("db/mcc_fsdGlobal.db","P=B_FSD")

dbLoadRecords("db/bta_suppl.db","hall=B,ioc=classc6");

dbLoadRecords("db/alarm-on-change.db","INP=IGL1I00OD16_16,P=B_HWP:")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

iocInit();

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

