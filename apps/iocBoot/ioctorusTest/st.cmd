#!../../bin/linux-x86_64/plc2epics
############################################################################
< envPaths
epicsEnvSet("EPICS_CA_MAX_ARRAY_BYTES",1000000)
############################################################################
cd ${TOP}

## Register all support components
dbLoadDatabase("dbd/plc2epics.dbd")
plc2epics_registerRecordDeviceDriver(pdbbase)

## Initialize EtherIP driver, define PLCs
## NOTE: if buffer limit is left at 500, read errors will occur.
EIP_buffer_limit(450)
drvEtherIP_init()
#drvEtherIP_define_PLC("PLC_CRYO",  "129.57.96.17", 0)
#drvEtherIP_define_PLC("PLC_TORUS", "129.57.96.15", 0)

## Debugging [7-10]
#EIP_verbosity(7)

## Load record instances
dbLoadRecords("db/torus_wf_generic.db","P=B_TORUS:,R=WF1,NELM=1,PREC=2")
dbLoadRecords("db/torus_wf_generic.db","P=B_TORUS:,R=WF10,NELM=10,PREC=2")
dbLoadRecords("db/torus_wf_generic.db","P=B_TORUS:,R=WF100,NELM=100,PREC=2")
dbLoadRecords("db/torus_wf_generic.db","P=B_TORUS:,R=WF2000,NELM=2000,PREC=2")
dbLoadRecords("db/torus_wf_generic.db","P=B_TORUS:,R=WF5000,NELM=5000,PREC=2")

cd ${TOP}/iocBoot/${IOC}

dbl > pv.list
iocInit
