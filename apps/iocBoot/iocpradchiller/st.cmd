#!../../bin/linux-x86/modbus

< envPaths

cd ${TOP}

dbLoadDatabase "dbd/modbus.dbd"
modbus_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("ETH","hallb-moxa8:4001",0,0,0)

#asynSetTraceMask("ETH",-1,0x09)
#asynSetTraceIOMask("ETH",-1,0x02)

dbLoadRecords("db/asynRecord.db","PORT=ETH,ADDR=1,IMAX=2000,OMAX=2000,P=hycal:chiller:,R=asyn")

# modbusInterposeConfig(portName, linkType, timeoutMsec, writeDelayMsec)
#   linkType = 0/1/2 = TCPIP/RTU/ASCII
modbusInterposeConfig("ETH",1,1000,0)

#drvModbusAsynConfigure("portName", "tcpPortName", slaveAddress, modbusFunction,
#  modbusStartAddress, modbusLength, dataType, pollMsec,"plcType")

# define mappings between modbus functions and memory ranges:
drvModbusAsynConfigure("CI", "ETH", 4, 1,   0,    1, 0, 2000, "DeltaT")  # read coil
drvModbusAsynConfigure("CO", "ETH", 4, 5,   0,    1, 0, 2000, "DeltaT")  # write coil
drvModbusAsynConfigure("HI0","ETH", 4, 3,   0,    2, 0, 2000, "DeltaT")  # read holding registers
drvModbusAsynConfigure("HO0","ETH", 4, 6,   0,    1, 0, 2000, "DeltaT")  # write holding registers
drvModbusAsynConfigure("HO1","ETH", 4, 6,   1,    1, 0, 2000, "DeltaT")  # write holding registers
drvModbusAsynConfigure("DI", "ETH", 4, 2,   0, 1000, 0, 2000, "DeltaT")  # read discrete inputs
drvModbusAsynConfigure("RI0","ETH", 4, 4,   0,  100, 0, 2000, "DeltaT")  # read input registers
drvModbusAsynConfigure("RI9","ETH", 4, 4, 900,  100, 0, 2000, "DeltaT")  # read input registers
drvModbusAsynConfigure("RI5","ETH", 4, 4, 500,  100, 0, 2000, "DeltaT")  # read input registers

# coils:
dbLoadRecords("db/modbus-bi.db","PORT=CI,OFFSET=0,R=bms:onoff:rbk,P=hycal:chiller:")
dbLoadRecords("db/modbus-bo.db","PORT=CO,OFFSET=0,R=bms:onoff,    P=hycal:chiller:")

# holding registers:
dbLoadRecords("db/modbus-ao.db","PORT=HO1,OFFSET=0,R=bms:temp:set,    EGU=F,P=hycal:chiller:")
dbLoadRecords("db/modbus-ai.db","PORT=HI0,OFFSET=1,R=bms:temp:set:rbk,EGU=F,P=hycal:chiller:")

# input registers:
dbLoadRecords("db/modbus-ai.db","PORT=RI0,OFFSET=0, R=temp:set:rbk, EGU=F,  P=hycal:chiller:")
dbLoadRecords("db/modbus-ai.db","PORT=RI0,OFFSET=30,R=temp:act,     EGU=F,  P=hycal:chiller:")
dbLoadRecords("db/modbus-ai.db","PORT=RI0,OFFSET=82,R=temp:out,     EGU=F,  P=hycal:chiller:")
dbLoadRecords("db/modbus-ai.db","PORT=RI0,OFFSET=94,R=flow,         EGU=lpm,P=hycal:chiller:")
dbLoadRecords("db/modbus-ai.db","PORT=RI9,OFFSET=12,R=temp:dewpoint,EGU=F,  P=hycal:chiller:")
dbLoadRecords("db/modbus-ai.db","PORT=RI9,OFFSET=14,R=temp:ambient, EGU=C,  P=hycal:chiller:")
dbLoadRecords("db/modbus-ai.db","PORT=RI9,OFFSET=16,R=temp:in,      EGU=F,  P=hycal:chiller:")
dbLoadRecords("db/modbus-ai.db","PORT=RI9,OFFSET=10,R=cool:demand,  EGU=%,  P=hycal:chiller:")
dbLoadRecords("db/modbus-ai.db","PORT=RI9,OFFSET=26,R=tank:level,   EGU=%,  P=hycal:chiller:")

# discrete inputs:
dbLoadRecords("db/modbus-bi.db","PORT=DI,OFFSET=80,R=onoff, P=hycal:chiller:")
dbLoadRecords("db/modbus-bi.db","PORT=DI,OFFSET=70,R=pump,  P=hycal:chiller:")
dbLoadRecords("db/modbus-bi.db","PORT=DI,OFFSET=28,R=bypass,P=hycal:chiller:")
dbLoadRecords("db/modbus-bi.db","PORT=DI,OFFSET=3, R=alarm,ZNAM=Ok,ONAM=Alarm,P=hycal:chiller:")

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

