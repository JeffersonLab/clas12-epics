TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = monitor

# monitor.dbd will be created and installed
DBD += monitor.dbd
monitor_DBD += base.dbd
monitor_DBD += devIocStats.dbd
monitor_DBD += asSupport.dbd
monitor_DBD += caPutLog.dbd

# monitor_registerRecordDeviceDriver.cpp derives from monitor.dbd
monitor_SRCS += monitor_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
monitor_SRCS_DEFAULT += monitorMain.cpp
monitor_SRCS_vxWorks += -nil-

monitor_LIBS += autosave
monitor_LIBS += devIocStats
monitor_LIBS += caPutLog
monitor_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
monitor_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

