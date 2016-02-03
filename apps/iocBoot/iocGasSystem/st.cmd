#!../../bin/linux-x86_64/cRio

## You may have to change bom to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/cRio.dbd")
cRio_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadTemplate("db/userHost.substitutions")
dbLoadRecords("db/cRioTest.db", "P=B_SVT_,R=N2_")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncExample, "user=wmooreHost"
