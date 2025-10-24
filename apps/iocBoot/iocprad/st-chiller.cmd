#!../../bin/linux-x86/c370

< envPaths

cd ${TOP}

dbLoadDatabase "dbd/c370.dbd"
c370_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("ETH1","hallb-moxa8:4001",0,0,1)
#asynSetTraceMask("ETH1",-1,0x09)
#asynSetTraceIOMask("ETH1",-1,0x02)

# modbusInterposeConfig(portName, linkType, timeoutMsec, writeDelayMsec)
#   linkType = 0/1/2 = TCPIP/RTU/ASCII
modbusInterposeConfig("ETH1",1,1000,0)

#drvModbusAsynConfigure(
#  "portName", "tcpPortName", slaveAddress, modbusFunction,
#  modbusStartAddress, modbusLength, dataType, pollMsec,"plcType")

# 32-bit floats:
#drvModbusAsynConfigure("C370x0600","ETH1", 4, 3, 0x0600, 40, 0, 2000, "C370")

# bits:
drvModbusAsynConfigure("C370x1880","ETH1", 4, 1, 0x0, 128, 0, 2000, "C370")

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

dbl > pv.list

