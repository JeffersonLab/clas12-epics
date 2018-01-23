#!../../bin/linux-x86_64/svtChiller

< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/svtChiller.dbd")
svtChiller_registerRecordDeviceDriver(pdbbase)


####################################
####################################
#
# This is the standard SVT chiller.
#
# These two chillers (Lauda/Anova) are "hotswappable" in terms
# of EPICS configuration, i.e. their records and all related things
# (e.g. interlocks, alarms, archiving).  This also means we can
# only run ONE of these TWO at a time.
#
# For the Lauda ECO (port L0 is hard-coded in svtChiller.db):
#drvAsynIPPortConfigure("L0",svtchiller1.jlab.org:10001,0,0,0)
#dbLoadRecords("db/svtChiller.db")
#
# For the Anova A40:
drvAsynIPPortConfigure("L1",hallb-moxa1.jlab.org:4005)
dbLoadRecords("db/anova.db","P=B_SVT_,R=CHILLER_,PORT=L1")
dbLoadRecords("db/svtChiller-anova2eco.db","P=B_SVT_CHILLER"))
#
####################################
####################################



####################################
####################################
#
# This is for the new N2 line added in January 2018.
#
# Currently uses the same Lauda ECO records, just suffixed by "N2"
# to differentiate.
#
# For the Lauda ECO (port L0 is hard-coded in svtChiller-N2.db):
drvAsynIPPortConfigure("L0",hallb-moxa1.jlab.org:4003)
dbLoadRecords("db/svtChiller-N2.db")
#
####################################
####################################

dbLoadRecords("db/svtChiller-autoSet.db")


dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

cd "${TOP}/iocBoot/${IOC}"

# autosave setup
< save_restore.cmd

asSetFilename("../acf/svt.acf")
asSetSubstitutions("P=B_,R=SVT_")

iocInit

caPutLogInit("clonioc1:7011")

# Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=${IOC}:")
create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbpf("${IOC}:SysReset.ASG","ALLWRITE")

seq seqsvtChillerTemp

dbl > pv.list

