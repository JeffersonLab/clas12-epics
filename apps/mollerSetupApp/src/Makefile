TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build an IOC support library
LIBRARY_IOC_vxWorks += mollerSetupSupport
DBD += mollerSetupSupport.dbd

mollerSetupSupport_DBD += mollerSetupSNC.dbd

# Compile and add the code to the support library
mollerSetupSupport_SRCS += moller_oplog_remote.c
mollerSetupSupport_SRCS += moller_setup.st

mollerSetupSupport_LIBS += seq pv
mollerSetupSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC_vxWorks = mollerSetup

# mollerSetup.dbd will be created and installed
DBD += mollerSetup.dbd

# mollerSetup.dbd will include these files:
mollerSetup_DBD += base.dbd
mollerSetup_DBD += mollerSetupSupport.dbd

# mollerSetup_registerRecordDeviceDriver.cpp derives from mollerSetup.dbd
mollerSetup_SRCS += mollerSetup_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
mollerSetup_SRCS_DEFAULT += mollerSetupMain.cpp
mollerSetup_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#mollerSetup_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
mollerSetup_LIBS += mollerSetupSupport
mollerSetup_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

