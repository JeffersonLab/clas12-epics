TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC_Linux = dcPower

# dcPower.dbd will be created and installed
DBD += dcPower.dbd
dcPower_DBD += base.dbd
dcPower_DBD += stream.dbd
dcPower_DBD += drvAsynIPPort.dbd
dcPower_DBD += asyn.dbd
dcPower_DBD += asSupport.dbd
dcPower_DBD += devIocStats.dbd

# dcPower_registerRecordDeviceDriver.cpp derives from dcPower.dbd
dcPower_SRCS += dcPower_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
dcPower_SRCS_DEFAULT += dcPowerMain.cpp
dcPower_SRCS_vxWorks += -nil-

dcPower_LIBS += seq pv
dcPower_LIBS += stream
dcPower_LIBS += asyn
dcPower_LIBS += autosave
dcPower_LIBS += devIocStats
dcPower_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
dcPower_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

