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

# The original BMT gas PLC:
#drvAsynIPPortConfigure("TCP505","129.57.160.181:505",0,0,1)

# The weather PLC:
drvAsynIPPortConfigure("TCP508","129.57.160.224:508",0,0,1)

# The FMT gas PLC, not used during BONUS when Saclay swapped PLCs:
# (But I put it here just to not have 2 IOCs polling the same PLC, see st_fmt.cmd)
drvAsynIPPortConfigure("TCP505","129.57.160.183:506",0,0,1)

# modbusInterposeConfig(portName, linkType, timeoutMsec, writeDelayMsec)
modbusInterposeConfig("TCP505",0,5000,0)
modbusInterposeConfig("TCP508",0,5000,0)

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

drvModbusAsynConfigure("R508", "TCP508", 0, 3,  0, 51, 0, 1000, "Siemens")
drvModbusAsynConfigure("W508A","TCP508", 0,16, 44, 6,  0, 0,    "Siemens")
drvModbusAsynConfigure("W508B","TCP508", 0, 6, 50, 1,  0, 1000, "Siemens")

## Load record instances
dbLoadRecords("db/save_restoreStatus.db", "P=$(IOC):")
dbLoadRecords("db/iocAdminSoft.db","IOC=$(IOC)")
dbLoadTemplate("db/mmgas_bmt.substitutions")

dbLoadTemplate("db/mmgas_weather.substitutions")
dbLoadRecords("db/mmgas_weather_aliases.db")
dbLoadRecords("db/mmgas_weather_avg.db")

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

