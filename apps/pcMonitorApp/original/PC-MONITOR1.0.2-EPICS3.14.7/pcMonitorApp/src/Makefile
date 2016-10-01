TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#==================================================
# Build an IOC support library

#LIBRARY_IOC += xxxSupport

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxxRecord
# install devXxxSoft.dbd into <top>/dbd
#DBD += xxxSupport.dbd

# The following are compiled and added to the Support library
#xxxSupport_SRCS += xxxRecord.c
#xxxSupport_SRCS += devXxxSoft.c
#xxxSupport_SRCS += devSysMon.c

#xxxSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

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
pcMonitor_DBD += dbSubExample.dbd
pcMonitor_DBD += pcDB.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
pcMonitor_SRCS += pcMonitor_registerRecordDeviceDriver.cpp
pcMonitor_SRCS_DEFAULT += pcMonitorMain.cpp
pcMonitor_SRCS_vxWorks += -nil-

# Add locally compiled object code
pcMonitor_SRCS += dbSubExample.c
pcMonitor_SRCS += devSysMon.c
# The following adds support from base/src/vxWorks
OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

#pcMonitor_LIBS += xxxSupport

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file

ifneq ($(SNCSEQ),)
    # This builds sncExample as a component of pcMonitor
    pcMonitor_SNCFLAGS += +r
    pcMonitor_DBD += sncExample.dbd
    pcMonitor_SRCS += sncExample.stt
    pcMonitor_LIBS += seq pv

    # The following builds sncProgram as a standalone application
    PROD_HOST += sncProgram
    sncProgram_SNCFLAGS += +m
    sncProgram_SRCS += sncProgram.st
    sncProgram_LIBS += seq pv
    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

pcMonitor_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

