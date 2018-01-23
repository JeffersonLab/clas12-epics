#!../../bin/linux-x86_64/svtChiller

< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/svtChiller.dbd")
svtChiller_registerRecordDeviceDriver(pdbbase)

####################################
# For the Anova A40:
drvAsynIPPortConfigure("L0",hallb-moxa1.jlab.org:4003)
dbLoadRecords("db/svtChiller-N2.db")
####################################

#dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
#dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

cd "${TOP}/iocBoot/${IOC}"

# autosave setup
#< save_restore.cmd

#asSetFilename("../acf/svt.acf")
#asSetSubstitutions("P=B_,R=SVT_")

iocInit

caPutLogInit("clonioc1:7011")

# Handle autosave 'commands' contained in loaded databases.
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=${IOC}:")
#create_monitor_set("info_settings.req", 30, "P=${IOC}:")

#dbpf("${IOC}:SysReset.ASG","ALLWRITE")

dbl > pv.list

