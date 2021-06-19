TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC_Linux = agilent

# agilent.dbd will be created and installed
DBD += agilent.dbd
agilent_DBD += base.dbd
agilent_DBD += stream.dbd
agilent_DBD += drvAsynIPPort.dbd
agilent_DBD += asyn.dbd
agilent_DBD += asSupport.dbd
agilent_DBD += devIocStats.dbd
agilent_DBD += caPutLog.dbd

# agilent_registerRecordDeviceDriver.cpp derives from agilent.dbd
agilent_SRCS += agilent_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
agilent_SRCS_DEFAULT += agilentMain.cpp
agilent_SRCS_vxWorks += -nil-

agilent_LIBS += stream
agilent_LIBS += asyn
agilent_LIBS += autosave
agilent_LIBS += devIocStats
agilent_LIBS += caPutLog
agilent_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
agilent_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

