TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = A6551

# A6551.dbd will be created and installed
DBD += A6551.dbd
A6551_DBD += base.dbd
A6551_DBD += stream.dbd
A6551_DBD += drvAsynIPPort.dbd
A6551_DBD += asyn.dbd
A6551_DBD += asSupport.dbd
A6551_DBD += devIocStats.dbd

# A6551_registerRecordDeviceDriver.cpp derives from A6551.dbd
A6551_SRCS += A6551_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
A6551_SRCS_DEFAULT += A6551Main.cpp
A6551_SRCS_vxWorks += -nil-

A6551_LIBS += stream
A6551_LIBS += asyn
A6551_LIBS += autosave
A6551_LIBS += devIocStats
A6551_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
A6551_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

