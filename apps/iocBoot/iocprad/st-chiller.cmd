#!../../bin/linux-x86/c370

< envPaths

cd ${TOP}

dbLoadDatabase "dbd/c370.dbd"
c370_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("ETH1","hallb-moxa8:4001",0,0,0)
#asynSetTraceMask("ETH1",-1,0x09)
#asynSetTraceIOMask("ETH1",-1,0x02)

#dbLoadRecords("db/asynRecord.db","PORT=ETH1,ADDR=1,IMAX=2000,OMAX=2000,P=hycal:chiller:,R=asyn")

# modbusInterposeConfig(portName, linkType, timeoutMsec, writeDelayMsec)
#   linkType = 0/1/2 = TCPIP/RTU/ASCII
modbusInterposeConfig("ETH1",1,1000,0)

#drvModbusAsynConfigure(
#  "portName", "tcpPortName", slaveAddress, modbusFunction,
#  modbusStartAddress, modbusLength, dataType, pollMsec,"plcType")

drvModbusAsynConfigure("AIx000","ETH1", 4, 3, 0, 100, 0, 2000, "DeltaT")
drvModbusAsynConfigure("AIx900","ETH1", 4, 3, 900, 100, 0, 2000, "DeltaT")

drvModbusAsynConfigure("BIx000","ETH1", 4, 1, 0x0, 1000, 0, 2000, "DeltaT")

dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=temp:set:rbk, PORT=AIx000,OFFSET=0")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=temp:act,     PORT=AIx000,OFFSET=30")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=temp:out,     PORT=AIx000,OFFSET=82")

dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=dewpoint,     PORT=AIx900,OFFSET=12")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=ambient,      PORT=AIx900,OFFSET=14")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=temp:in,      PORT=AIx900,OFFSET=16")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=set:ctrl,     PORT=AIx900,OFFSET=30")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=start:ctrl,   PORT=AIx900,OFFSET=31")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=cool:demand,  PORT=AIx900,OFFSET=10")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=tank:level,   PORT=AIx900,OFFSET=26")

#dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", "IOC=$(IOC)")
#dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

#dbLoadTemplate("db/prad-chiller.substitutions")

cd ${TOP}/iocBoot/${IOC}

#< save_restore.cmd

#asSetFilename("../acf/cas.acf")

iocInit()

#caPutLogInit("clonioc1:7011")

#makeAutosaveFiles()
#create_monitor_set("info_positions.req","","")
#create_monitor_set("info_settings.req","","")

dbl > pv.list

