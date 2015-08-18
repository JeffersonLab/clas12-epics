TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = cas

# cas.dbd will be created and installed
DBD += cas.dbd

# cas.dbd will include these files:
cas_DBD += base.dbd
cas_DBD += asSupport.dbd
cas_DBD += devIocStats.dbd

# cas_registerRecordDeviceDriver.cpp derives from cas.dbd
cas_SRCS += cas_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
cas_SRCS_DEFAULT += casMain.cpp
cas_SRCS_vxWorks += -nil-

# Link in the support libraries
cas_LIBS += autosave devIocStats
cas_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

