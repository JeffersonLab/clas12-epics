#!../../bin/linux-x86_64/svtChiller

< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/svtChiller.dbd")
svtChiller_registerRecordDeviceDriver(pdbbase)

# Anova chiller:
# (when it's an Anova, we do some aliases to preserve rest of SVT controls system) 
drvAsynIPPortConfigure("L0",hallb-moxa1.jlab.org:4005)
dbLoadRecords("db/anova.db","P=B_SVT_,R=CHILLER_N2_,PORT=L0")
dbLoadRecords("db/svtChiller-anova2eco.db","P=B_SVT_CHILLER_N2"))

# Julabo chiller:
# (when it's a Julabo, we do some aliases to preserve rest of SVT controls system) 
#drvAsynIPPortConfigure("L2",hallb-moxa1.jlab.org:4007)
#dbLoadRecords("db/anova.db","P=B_SVT_,R=CHILLER_,PORT=L2")
#dbLoadRecords("db/svtChiller-anova2eco.db","P=B_SVT_CHILLER"))

# Lauda chiller:
drvAsynIPPortConfigure("L1",hallb-moxa1.jlab.org:4006)
dbLoadRecords("db/Lauda_ECO.db","P=B_SVT_CHILLER,PORT=L1")

# This is for the seqsvtChillerTemp sequencer:
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

