TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_Linux = mmGas

# mmGas.dbd will include these files:
DBD += mmGas.dbd

mmGas_DBD += base.dbd
mmGas_DBD += modbusSupport.dbd
mmGas_DBD += asSupport.dbd
mmGas_DBD += devIocStats.dbd
mmGas_DBD += drvAsynIPPort.dbd asyn.dbd
mmGas_DBD += caPutLog.dbd

# mmGas_registerRecordDeviceDriver.cpp derives from mmGas.dbd
mmGas_SRCS += mmGas_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
mmGas_SRCS_DEFAULT += mmGasMain.cpp
mmGas_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#mmGas_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
mmGas_LIBS += modbus
mmGas_LIBS += autosave
mmGas_LIBS += caPutLog
mmGas_LIBS += devIocStats
mmGas_LIBS += asyn
mmGas_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

