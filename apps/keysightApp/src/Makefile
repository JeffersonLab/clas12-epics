TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = keysight

# keysight.dbd will be created and installed
DBD += keysight.dbd
keysight_DBD += base.dbd
keysight_DBD += stream.dbd
keysight_DBD += drvAsynIPPort.dbd
keysight_DBD += asyn.dbd
keysight_DBD += asSupport.dbd
keysight_DBD += devIocStats.dbd
keysight_DBD += calc.dbd
keysight_DBD += sCalcoutRecord.dbd

# keysight_registerRecordDeviceDriver.cpp derives from keysight.dbd
keysight_SRCS += keysight_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
keysight_SRCS_DEFAULT += keysightMain.cpp
keysight_SRCS_vxWorks += -nil-

keysight_LIBS += seq pv
keysight_LIBS += calc
keysight_LIBS += stream
keysight_LIBS += asyn
keysight_LIBS += autosave
keysight_LIBS += devIocStats
keysight_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
keysight_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

