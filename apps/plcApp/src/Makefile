TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC application

PROD_IOC_Linux = plc2epics
# plc2epics.dbd will be created and installed
DBD += plc2epics.dbd

# plc2epics.dbd will be made up from these files:
plc2epics_DBD += base.dbd
plc2epics_DBD += ether_ip.dbd
plc2epics_DBD += calcSupport.dbd
plc2epics_DBD += busySupport.dbd
plc2epics_DBD += sscanSupport.dbd
plc2epics_DBD += asSupport.dbd
plc2epics_DBD += asyn.dbd
plc2epics_DBD += std.dbd
plc2epics_DBD += devIocStats.dbd 


# plc2epics_registerRecordDeviceDriver.cpp derives from plc2epics.dbd
plc2epics_SRCS += plc2epics_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
plc2epics_SRCS_DEFAULT += plc2epicsMain.cpp

# Link in the code from the support library
plc2epics_LIBS += ether_ip 
plc2epics_LIBS += calc
plc2epics_LIBS += busy
plc2epics_LIBS += sscan
plc2epics_LIBS += autosave
plc2epics_LIBS += std
plc2epics_LIBS += asyn
plc2epics_LIBS += devIocStats

ifneq ($(SNCSEQ),)
    plc2epics_DBD  += snc4plc.dbd
    plc2epics_SRCS += sncSmallTest.st
    plc2epics_LIBS += seq pv
endif

plc2epics_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

