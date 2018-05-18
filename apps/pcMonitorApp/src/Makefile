TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#==================================================
# Build an IOC support library


#=============================
# build an ioc application

PROD_HOST = pcMonitor
#PROD_IOC is used to complie things for all architectures
#PROD_IOC = pcMonitor
# pcMonitor.dbd will be created and installed
#pcMonitor_DBD += pcMonitor.dbd

# pcMonitor.dbd will be made up from these files:
DBD += pcMonitor.dbd
pcMonitor_DBD += base.dbd
#pcMonitor_DBD += xxxSupport.dbd
pcMonitor_DBD += pcDB.dbd
pcMonitor_DBD += asSupport.dbd
pcMonitor_DBD += devIocStats.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
pcMonitor_SRCS += pcMonitor_registerRecordDeviceDriver.cpp
pcMonitor_SRCS_DEFAULT += pcMonitorMain.cpp
pcMonitor_SRCS_vxWorks += -nil-

# Add locally compiled object code
pcMonitor_SRCS += devSysMon.c

pcMonitor_LIBS += autosave
pcMonitor_LIBS += devIocStats
pcMonitor_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

