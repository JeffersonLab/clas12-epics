#!../../bin/linux-x86_64/svtChiller

< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/svtChiller.dbd")
svtChiller_registerRecordDeviceDriver(pdbbase)

# For the Lauda ECO chiller (port L0 is hard-coded in svtChiller.db):
drvAsynIPPortConfigure("L0",svtchiller1.jlab.org:10001,0,0,0)

# For the Anova A40:
drvAsynIPPortConfigure("L1",hallb-moxa1.jlab.org:4005)

# For the Lauda ECO chiller:
#dbLoadRecords("db/svtChiller.db")

# For the Anova A40:
dbLoadRecords("db/anova.db","P=B_SVT_,R=CHILLER_,PORT=L1")


dbLoadRecords("db/iocAdminSoft.db", "IOC=${IOC}")
dbLoadRecords("db/save_restoreStatus.db", "P=${IOC}:")

cd "${TOP}/iocBoot/${IOC}"

# autosave setup
#< save_restore.cmd

iocInit

# Handle autosave 'commands' contained in loaded databases.
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=${IOC}:")
#create_monitor_set("info_settings.req", 30, "P=${IOC}:")

dbl > pv.list

