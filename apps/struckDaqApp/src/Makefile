TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC_vxWorks += struckDaqSupport

DBD += struckDaqSupport.dbd
struckDaqSupport_DBD += base.dbd
struckDaqSupport_DBD += asyn.dbd

struckDaqSupport_DBD += stdSupport.dbd
struckDaqSupport_DBD += calcSupport.dbd
struckDaqSupport_DBD += busySupport.dbd 
struckDaqSupport_DBD += sscanSupport.dbd 
#struckDaqSupport_DBD += asSupport.dbd
struckDaqSupport_DBD += std.dbd

struckDaqSupport_DBD += mcaSupport.dbd
struckDaqSupport_DBD += SIS38XXSupport.dbd

struckDaqSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC_vxWorks = struckDaq
# struckDaq.dbd will be created and installed
DBD += struckDaq.dbd

# struckDaq.dbd will be made up from these files:
struckDaq_DBD += struckDaqSupport.dbd
#struckDaq_DBD += devIocStats.dbd

# Build the main IOC entry point on workstation OSs.
struckDaq_SRCS_DEFAULT += struckDaqMain.cpp
struckDaq_SRCS_vxWorks += struckDaq_registerRecordDeviceDriver.cpp
struckDaq_SRCS += testLoop.c

# Add support from base/src/vxWorks if needed
struckDaq_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
struckDaq_LIBS += struckDaqSupport 
struckDaq_LIBS += SIS38XX mca
struckDaq_LIBS += calc
struckDaq_LIBS += busy
struckDaq_LIBS += sscan
#struckDaq_LIBS += devIocStats
#struckDaq_LIBS += autosave
struckDaq_LIBS += std
struckDaq_LIBS += asyn

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file

ifneq ($(SNCSEQ),)
      struckDaqSupport_DBD += struckDaqSNC.dbd
      struckDaqSupport_SRCS += struckDaq.st
      struckDaq_SRCS += struckDaq.st
      struckDaq_LIBS += seq pv
endif

# Finally link to the EPICS Base libraries
struckDaq_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

