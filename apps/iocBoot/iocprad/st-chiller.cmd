#!../../bin/linux-x86/c370

< envPaths

cd ${TOP}

dbLoadDatabase "dbd/c370.dbd"
c370_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("ETH","hallb-moxa8:4001",0,0,0)
#asynSetOption("ETH",0,"baud","19200")
#asynSetOption("ETH",0,"parity","none")
#asynSetOption("ETH",0,"bits","8")
#asynSetOption("ETH",0,"stop","2")

#asynSetTraceMask("ETH",-1,0x09)
#asynSetTraceIOMask("ETH",-1,0x02)

dbLoadRecords("db/asynRecord.db","PORT=ETH,ADDR=1,IMAX=2000,OMAX=2000,P=hycal:chiller:,R=asyn")

# modbusInterposeConfig(portName, linkType, timeoutMsec, writeDelayMsec)
#   linkType = 0/1/2 = TCPIP/RTU/ASCII
modbusInterposeConfig("ETH",1,1000,0)

#drvModbusAsynConfigure(
#  "portName", "tcpPortName", slaveAddress, modbusFunction,
#  modbusStartAddress, modbusLength, dataType, pollMsec,"plcType")

# read coil:
drvModbusAsynConfigure("CI", "ETH", 4, 1,   0,    1, 0, 2000, "DeltaT")

# write coil:
drvModbusAsynConfigure("CO", "ETH", 4, 5,   0,    1, 0, 2000, "DeltaT")

# read(-only) discrete inputs:
drvModbusAsynConfigure("DI", "ETH", 4, 2,   0, 1000, 0, 2000, "DeltaT")

# read input registers:
# 3 is the "read holding registers", but it "works" for index 9,
# acting chiller setpoint, which is labelled an input register by the manufacturer
drvModbusAsynConfigure("RI0","ETH", 4, 3,   0,  100, 0, 2000, "DeltaT")
drvModbusAsynConfigure("RI9","ETH", 4, 3, 900,  100, 0, 2000, "DeltaT")

# read holding registers:
drvModbusAsynConfigure("HI0","ETH", 4, 3,   0,    2, 0, 2000, "DeltaT")

# write holding registers:
drvModbusAsynConfigure("HO0","ETH", 4, 6,   0,    1, 0, 2000, "DeltaT")
drvModbusAsynConfigure("HO1","ETH", 4, 6,   1,    1, 0, 2000, "DeltaT")

# coils:
# These work in that writing one changes the readback of the other on its next polling:
dbLoadRecords("db/modbus-bi.db","P=hycal:chiller:,R=bms:onoff:rbk,PORT=CI,OFFSET=0")
dbLoadRecords("db/modbus-bo.db","P=hycal:chiller:,R=bms:onoff,    PORT=CO,OFFSET=0")

# holding registers:
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=units:rbk,    PORT=HI0,OFFSET=0")
dbLoadRecords("db/modbus-ao.db","P=hycal:chiller:,R=units:set,    PORT=HO0,OFFSET=0")

dbLoadRecords("db/modbus-ao.db","P=hycal:chiller:,R=bms:temp:set,     PORT=HO1,OFFSET=0")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=bms:temp:set:rbk, PORT=HI0,OFFSET=1")

# input registers:
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=temp:set:rbk, PORT=RI0,OFFSET=0")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=temp:act,     PORT=RI0,OFFSET=30")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=temp:out,     PORT=RI0,OFFSET=82")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=flow,         PORT=RI0,OFFSET=94")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=temp:dewpoint,PORT=RI9,OFFSET=12")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=temp:ambient, PORT=RI9,OFFSET=14")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=temp:in,      PORT=RI9,OFFSET=16")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=set:ctrl,     PORT=RI9,OFFSET=30")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=start:ctrl,   PORT=RI9,OFFSET=31")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=cool:demand,  PORT=RI9,OFFSET=10")
dbLoadRecords("db/modbus-ai.db","P=hycal:chiller:,R=tank:level,   PORT=RI9,OFFSET=26")

# discrete inputs:
dbLoadRecords("db/modbus-bi.db","P=hycal:chiller:,R=onoff, PORT=DI,OFFSET=80")
dbLoadRecords("db/modbus-bi.db","P=hycal:chiller:,R=pump,  PORT=DI,OFFSET=70")
dbLoadRecords("db/modbus-bi.db","P=hycal:chiller:,R=alarm, PORT=DI,OFFSET=3")
dbLoadRecords("db/modbus-bi.db","P=hycal:chiller:,R=bypass,PORT=DI,OFFSET=28")
dbLoadRecords("db/modbus-bi.db","P=hycal:chiller:,R=pump2, PORT=DI,OFFSET=910")

#dbLoadRecords("$(DEVIOCSTATS)/db/iocAdminSoft.db", "IOC=$(IOC)")
#dbLoadRecords("db/save_restoreStatus.db","P=${IOC}:")

cd ${TOP}/iocBoot/${IOC}

#< save_restore.cmd

#asSetFilename("../acf/cas.acf")

iocInit()

#caPutLogInit("clonioc1:7011")

#makeAutosaveFiles()
#create_monitor_set("info_positions.req","","")
#create_monitor_set("info_settings.req","","")

dbl > pv.list

