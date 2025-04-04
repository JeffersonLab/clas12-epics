#!../../bin/linux-x86_64/mmGas

# "mmGas" already includes the necessary dependencies, Modbus TCP/IP for Siemens S7

< envPaths
epicsEnvSet("IOC","iocplcTest")
cd "${TOP}"

dbLoadDatabase("dbd/mmGas.dbd")
mmGas_registerRecordDeviceDriver(pdbbase)

drvAsynIPPortConfigure("TCP505","129.57.160.84:505",0,0,1)
modbusInterposeConfig("TCP505",0,5000,0)

#asynSetTraceMask("TCP505",0,9)
#asynSetTraceIOMask("TCP505",0,4)

drvModbusAsynConfigure("R505", "TCP505", 0, 3,  0, 33, 0, 1000, "Siemens")
drvModbusAsynConfigure("W505", "TCP505", 0, 6,  32, 1, 0, 1000, "Siemens")
drvModbusAsynConfigure("W505A","TCP505", 0,16,  0, 33, 0, 0,    "Siemens")

dbLoadTemplate("${TOP}/iocBoot/${IOC}/bufferdewar.substitutions")

cd "${TOP}/iocBoot/${IOC}"

iocInit

