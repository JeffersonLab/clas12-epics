TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build an IOC support library
LIBRARY_IOC_vxWorks += dynabcSupport

# dynabc.dbd will be created and installed
DBD += dynabcSupport.dbd

# dynabcSupport.dbd will include these files:
dynabcSupport_DBD += base.dbd
dynabcSupport_DBD += dynabcSNC.dbd
dynabcSupport_DBD += XY240Support.dbd

dynabcSupport_SRCS += quad_current.st

dynabcSupport_LIBS += XY240Support
dynabcSupport_LIBS += seq pv
dynabcSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC_vxWorks = dynabc

# dynabc.dbd will be created and installed
DBD += dynabc.dbd

# dynabc.dbd will include these files:
dynabc_DBD += base.dbd
dynabc_DBD += dynabcSNC.dbd

# dynabc_registerRecordDeviceDriver.cpp derives from dynabc.dbd
dynabc_SRCS += dynabc_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
dynabc_SRCS_DEFAULT += dynabcMain.cpp
dynabc_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
dynabc_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
dynabc_LIBS += dynabcSupport

dynabc_DBD += dynabcSupport.dbd

dynabc_LIBS += XY240Support
dynabc_LIBS += seq pv
dynabc_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

