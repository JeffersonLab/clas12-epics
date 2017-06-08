#!../../bin/linux-x86_64/mmGas
############################################################################
< envPaths
############################################################################
cd "${TOP}"

## Register all support components
dbLoadDatabase("dbd/mmGas.dbd")
mmGas_registerRecordDeviceDriver(pdbbase)

## Configure modbus ports
#drvAsynIPPortConfigure("TCP502","129.57.86.110:502",0,0,1)
#drvAsynIPPortConfigure("TCP503","129.57.86.110:503",0,0,1)
#drvAsynIPPortConfigure("TCP504","129.57.86.110:504",0,0,1)
drvAsynIPPortConfigure("TCP505","129.57.86.110:505",0,0,1)

# modbusInterposeConfig(portName, linkType, timeoutMsec, writeDelayMsec)
#modbusInterposeConfig("TCP502",0,5000,0)
#modbusInterposeConfig("TCP503",0,5000,0)
#modbusInterposeConfig("TCP504",0,5000,0)
modbusInterposeConfig("TCP505",0,5000,0)

# Debugging...
#asynSetTraceMask("TCP505",0,9)
#asynSetTraceIOMask("TCP505",0,4)

#drvModbusAsynConfigure("portName", "tcpPortName", slaveAddress, modbusFunction,
#                       modbusStartAddress, modbusLength, dataType, pollMsec,
#                       "plcType")
# 32-bit integers (Function code = 3)
#drvModbusAsynConfigure("MM502", "TCP502", 0, 2, 0, 2,  0, 1000, "Siemens")
#drvModbusAsynConfigure("MM503", "TCP503", 0, 2, 0, 30, 0, 1000, "Siemens")
#drvModbusAsynConfigure("MM504", "TCP504", 0, 4, 0, 12, 7, 1000, "Siemens")
drvModbusAsynConfigure("R505", "TCP505", 0, 3, 0, 32, 0, 1000, "Siemens")
#drvModbusAsynConfigure("W505", "TCP505", 0, 16, 0, 100, 0, 1000, "Siemens")

## Load record instances
# dbLoadRecords("db/save_restoreStatus.db", "P=$(IOC):")
# dbLoadRecords("db/iocAdminSoft.db","P=$(IOC)")
dbLoadTemplate("db/mm_gas.substitutions")

cd "${TOP}/iocBoot/${IOC}"

## autosave setup
# < save_restore.cmd

dbl > pv.list
iocInit

#asynReport(5, "MM502")
#asynReport(5, "MM503")
#asynReport(5, "MM504")
#asynReport(5, "MM505")

## Handle autosave 'commands' contained in loaded databases.
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=:")
#create_monitor_set("info_settings.req", 30, "P=xxx:")

