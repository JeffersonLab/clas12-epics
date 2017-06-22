#!../../bin/linux-x86_64/plc2epics
############################################################################
< envPaths
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/plc2epics.dbd")
plc2epics_registerRecordDeviceDriver(pdbbase)

## Initialize EtherIP driver, define PLCs
## NOTE: if buffer limit is left at 500, read errors will occur.
EIP_buffer_limit(450)
drvEtherIP_init()
drvEtherIP_define_PLC("PLC_SOL",  "129.57.96.30", 0)

## Debugging [7-10]
#EIP_verbosity(7)

## Load record instances
dbLoadRecords("${DEVIOCSTATS}/db/iocAdminSoft.db","IOC=${IOC}")
dbLoadRecords("${AUTOSAVE}/asApp/Db/save_restoreStatus.db", "P=${IOC}:")
## PLC_SOL
dbLoadTemplate("db/solenoid_LHe.substitutions")
dbLoadRecords("db/solenoid_cryocon.db", "P=B_SOL:,R=PLC:,PLCID=PLC_SOL")

## CA Security
dbLoadRecords("db/cas.db", "P=B_SOL:,R=CRYO:,ASG=DEFAULT")
asSetFilename("${TOP}/iocBoot/acf/solenoid_cryo.acf")
asSetSubstitutions("P=B_SOL:,R=CRYO:")

cd ${TOP}/iocBoot/${IOC}

## autosave setup
< save_restore.cmd

dbl > pv.list
iocInit
caPutLogInit("clonioc1:7011")

## autosave startup
## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=xxx:")
create_monitor_set("info_settings.req", 30, "P=xxx:")

