#!../../bin/linux-x86/c370

< envPaths

cd ${TOP}

dbLoadDatabase "dbd/c370.dbd"
c370_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("ETH1","hallb-moxa3:4001",0,0,1)
#asynSetTraceMask("ETH1",-1,0x09)
#asynSetTraceIOMask("ETH1",-1,0x02)

# modbusInterposeConfig(portName, linkType, timeoutMsec, writeDelayMsec)
#   linkType = 0/1/2 = TCPIP/RTU/ASCII
modbusInterposeConfig("ETH1",1,1000,0)

#drvModbusAsynConfigure(
#  "portName", "tcpPortName", slaveAddress, modbusFunction,
#  modbusStartAddress, modbusLength, dataType, pollMsec,"plcType")
# 32-bit integers (Function code = 3)


drvModbusAsynConfigure("C370x600", "ETH1", 1, 3, 0x600,  40, 0, 2000, "C370")
drvModbusAsynConfigure("C370x640", "ETH1", 1, 3, 0x640,   6, 0, 2000, "C370")
drvModbusAsynConfigure("C370x702", "ETH1", 1, 3, 0x702,   2, 0, 2000, "C370")
drvModbusAsynConfigure("C370x3800","ETH1", 1, 3, 0x3800, 20, 0, 2000, "C370")

dbLoadTemplate("db/saclayTarget.substitutions")

dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", "IOC=$(IOC)")
dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

cd ${TOP}/iocBoot/${IOC}

< save_restore.cmd

asSetFilename("../acf/cas.acf")

iocInit()

caPutLogInit("clonioc1:7011")

makeAutosaveFiles()
create_monitor_set("info_positions.req","","")
create_monitor_set("info_settings.req","","")

