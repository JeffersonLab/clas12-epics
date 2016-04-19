#!../../bin/linux-x86/c370

< envPaths
cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/c370.dbd"
c370_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("ETH1","hallb-moxa3:4001",0,0,1)

# modbusInterposeConfig(portName, linkType, timeoutMsec, writeDelayMsec)
modbusInterposeConfig("ETH1",0,5000,0)

# Debugging...
#asynSetTraceMask("ETH1",0,9)
#asynSetTraceIOMask("ETH1",0,2)

#drvModbusAsynConfigure(
#  "portName", "tcpPortName", slaveAddress, modbusFunction,
#  modbusStartAddress, modbusLength, dataType, pollMsec,"plcType")

# 32-bit integers (Function code = 3)

drvModbusAsynConfigure("C370",  "ETH1", 1, 3, 3800,  20, 0, 1000, "C370")
#drvModbusAsynConfigure("C370",  "ETH1", 1, 3, 3300,  20, 0, 1000, "C370")
#drvModbusAsynConfigure("C370",  "ETH1", 1, 3, 4300,  20, 0, 1000, "C370")

#drvModbusAsynConfigure("C370",  "ETH1", 1, 3, 3800,  40, 0, 1000, "C370")
#drvModbusAsynConfigure("C370",  "ETH1", 1, 3, 3300,  40, 0, 1000, "C370")
#drvModbusAsynConfigure("C370",  "ETH1", 1, 3, 4300,  40, 0, 1000, "C370")

#drvModbusAsynConfigure("DS_360_IN",  "ETH1", 1, 3, 360,  9, 0, 1000, "WATLOW")


# Load IOC status records
#dbLoadRecords("db/iocAdminSoft.db","IOC=BCALCHIL")

# Load record instances
#dbLoadRecords("db/save_restoreStatus.db", "P=BCALCHIL:")

dbLoadTemplate("db/saclayTarget.substitutions")


cd ${TOP}/iocBoot/${IOC}

#  autosave setup
#< save_restore.cmd

#dbl > bcal_pv.list
iocInit

# autosave startup
#create_monitor_set("watlow_settings.req", 30, "P=BCAL:,R=CHILL:")

# Handle autosave 'commands' contained in loaded databases.
#makeAutosaveFiles()
#create_monitor_set("info_positions.req", 5, "P=xxx:")
#create_monitor_set("info_settings.req", 30, "P=xxx:")

