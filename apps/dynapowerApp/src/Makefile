TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC_Linux = dynapower

# dynapower.dbd will be created and installed
DBD += dynapower.dbd
dynapower_DBD += base.dbd
dynapower_DBD += stream.dbd
dynapower_DBD += drvAsynIPPort.dbd
dynapower_DBD += asyn.dbd
dynapower_DBD += asSupport.dbd
dynapower_DBD += devIocStats.dbd

# dynapower_registerRecordDeviceDriver.cpp derives from dynapower.dbd
dynapower_SRCS += dynapower_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
dynapower_SRCS_DEFAULT += dynapowerMain.cpp
dynapower_SRCS_vxWorks += -nil-

dynapower_LIBS += seq pv
dynapower_LIBS += stream
dynapower_LIBS += asyn
dynapower_LIBS += autosave
dynapower_LIBS += devIocStats
dynapower_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
dynapower_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

