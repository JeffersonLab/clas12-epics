#!../../bin/linux-x86_64/mollerSetup

< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/mollerSetup.dbd"
mollerSetup_registerRecordDeviceDriver pdbbase

dbLoadRecords("db/automoller.db","P=B_MOLLER:")
dbLoadRecords("db/automoller-sim.db","P=B_MOLLER:,S=SIM:")

cd ${TOP}/iocBoot/${IOC}

iocInit();

seq automoller "P=B_MOLLER:,S=SIM:"

