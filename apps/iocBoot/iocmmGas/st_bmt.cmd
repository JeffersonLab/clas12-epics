#!../../bin/linux-x86_64/mmGas
############################################################################
< envPaths
epicsEnvSet("IOC","iocmmGasBMT")
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/mmGas.dbd")
mmGas_registerRecordDeviceDriver(pdbbase)

## Configure modbus ports
drvAsynIPPortConfigure("TCP505","129.57.160.181:505",0,0,1)

# modbusInterposeConfig(portName, linkType, timeoutMsec, writeDelayMsec)
modbusInterposeConfig("TCP505",0,5000,0)

# Debugging...
#asynSetTraceMask("TCP505",0,9)
#asynSetTraceIOMask("TCP505",0,4)

#drvModbusAsynConfigure("portName", "tcpPortName", slaveAddress, modbusFunction,
#                       modbusStartAddress, modbusLength, dataType, pollMsec,
#                       "plcType")
# 32-bit integers (Function code = 3)
drvModbusAsynConfigure("R505", "TCP505", 0, 3,  0, 33, 0, 1000, "Siemens")
drvModbusAsynConfigure("W505", "TCP505", 0, 6,  32, 1, 0, 1000, "Siemens")
drvModbusAsynConfigure("W505A","TCP505", 0,16,  0, 33, 0, 0,    "Siemens")

## Load record instances
 dbLoadRecords("db/save_restoreStatus.db", "P=$(IOC):")
dbLoadRecords("db/iocAdminSoft.db","IOC=$(IOC)")
dbLoadTemplate("db/mmgas_bmt.substitutions")

dbLoadRecords("db/mvt_gasOnOff.db")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
< save_restore.cmd

dbl > pv_bmt.list
iocInit

## Handle autosave 'commands' contained in loaded databases.
makeAutosaveFiles()
create_monitor_set("info_positions.req", 5, "P=:")
create_monitor_set("info_settings.req", 30, "P=xxx:")

