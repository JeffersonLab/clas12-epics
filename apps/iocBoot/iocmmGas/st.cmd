#!../../bin/linux-x86_64/mmGas
############################################################################
< envPaths
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/mmGas.dbd")
mmGas_registerRecordDeviceDriver(pdbbase)

## Configure modbus ports
drvAsynIPPortConfigure("TCP502","129.57.86.151:502",0,0,1)
#drvAsynIPPortConfigure("TCP503","129.57.86.151:503",0,0,1)
#drvAsynIPPortConfigure("TCP504","129.57.86.151:504",0,0,1)

# modbusInterposeConfig(portName, linkType, timeoutMsec, writeDelayMsec)
modbusInterposeConfig("TCP502",0,5000,0)
#modbusInterposeConfig("TCP503",0,5000,0)
#modbusInterposeConfig("TCP504",0,5000,0)

# Debugging...
#asynSetTraceMask("TCP502",0,9)
#asynSetTraceIOMask("TCP502",0,2)

#drvModbusAsynConfigure("portName", "tcpPortName", slaveAddress, modbusFunction,
#                       modbusStartAddress, modbusLength, dataType, pollMsec,
#                       "plcType")
# 32-bit integers (Function code = 3)
drvModbusAsynConfigure("MM502", "TCP502", 1, 1, 0, 16, 0, 1000, "Siemens")
#drvModbusAsynConfigure("MM503", "TCP503", 1, 1, 0, 16, 0, 1000, "Siemens")
#drvModbusAsynConfigure("MM504", "TCP504", 1, 4, 0,  5, 0, 1000, "Siemens")

## Load record instances
# dbLoadRecords("db/save_restoreStatus.db", "P=$(IOC):")
# dbLoadRecords("db/iocAdminSoft.db","P=$(IOC)")
dbLoadTemplate("db/mm_gas.substitutions")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
# < save_restore.cmd

dbl > pv.list
iocInit

## Handle autosave 'commands' contained in loaded databases.
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=:")
#create_monitor_set("info_settings.req", 30, "P=xxx:")
