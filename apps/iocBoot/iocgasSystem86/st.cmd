#!../../bin/linux-x86_64/cRio
############################################################################
< envPaths
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/cRio.dbd")
cRio_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadRecords("db/gas_cRIO_HTCC.db",    "P=B_DET_,R=HTCC_")
dbLoadRecords("db/gas_cRIO_SVT.db",     "P=B_DET_,R=SVT_")

cd "${TOP}/iocBoot/${IOC}"
iocInit

