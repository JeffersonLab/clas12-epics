TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = sy2604

# sy2604.dbd will be created and installed
DBD += sy2604.dbd
sy2604_DBD += base.dbd
sy2604_DBD += stream.dbd
sy2604_DBD += drvAsynIPPort.dbd
sy2604_DBD += asyn.dbd
sy2604_DBD += devIocStats.dbd
sy2604_DBD += asSupport.dbd

# sy2604_registerRecordDeviceDriver.cpp derives from sy2604.dbd
sy2604_SRCS += sy2604_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
sy2604_SRCS_DEFAULT += sy2604Main.cpp
sy2604_SRCS_vxWorks += -nil-

sy2604_LIBS += stream
sy2604_LIBS += asyn
sy2604_LIBS += autosave
sy2604_LIBS += devIocStats
sy2604_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
sy2604_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

