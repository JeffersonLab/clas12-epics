#!../../bin/linux-x86_64/svtChiller

< envPaths
epicsEnvSet("STREAM_PROTOCOL_PATH","${TOP}/proto")

cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/svtChiller.dbd")
svtChiller_registerRecordDeviceDriver(pdbbase)

# Julabo chiller:
# (when it's a Julabo, we do some aliases to preserve rest of SVT controls system) 
drvAsynIPPortConfigure("L2",hallb-moxa1.jlab.org:4007)
dbLoadRecords("db/julabo-FP51-SL.db","P=B_SVT_,R=JULABO_,PORT=L2")
#dbLoadRecords("db/svtChiller-anova2eco.db","P=B_SVT_JULABO"))

cd "${TOP}/iocBoot/${IOC}"

iocInit


