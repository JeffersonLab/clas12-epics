#!../../bin/linux-x86_64/wf2root
############################################################################
< envPaths
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/wf2root.dbd"(
wf2root_registerRecordDeviceDriver(pdbbase)

## Load record instances
dbLoadTemplate("iocBoot/${IOC}/wf2root.substitutions")

cd "${TOP}/iocBoot/${IOC}"
iocInit

#dbpf("B_TORUS:DAQ_REC:ctrl:daq.INPC", "torus")
#dbpf("B_TORUS:DAQ_REC:ctrl:file_limit", "500")
dbpf("B_TORUS:DAQ_REC:ctrl:daq_state", "0")

