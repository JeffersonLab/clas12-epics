TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build an IOC support library
LIBRARY_IOC_Linux += mollerSetupSupport
DBD += mollerSetupSupport.dbd

mollerSetupSupport_DBD += mollerSetupSNC.dbd

# Compile and add the code to the support library
mollerSetupSupport_SRCS += makeLogEntry.c
mollerSetupSupport_SRCS += quadCurrent.c
mollerSetupSupport_SRCS += automoller.st

mollerSetupSupport_LIBS += seq pv
mollerSetupSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

PROD_IOC_Linux = mollerSetup

# mollerSetup.dbd will be created and installed
DBD += mollerSetup.dbd

# mollerSetup.dbd will include these files:
mollerSetup_DBD += base.dbd
mollerSetup_DBD += devIocStats.dbd
mollerSetup_DBD += asSupport.dbd
mollerSetup_DBD += mollerSetupSupport.dbd
mollerSetup_DBD += calc.dbd

# mollerSetup_registerRecordDeviceDriver.cpp derives from mollerSetup.dbd
mollerSetup_SRCS += mollerSetup_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
mollerSetup_SRCS_DEFAULT += mollerSetupMain.cpp

# Link in the code from our support library
mollerSetup_LIBS += mollerSetupSupport
mollerSetup_LIBS += seq pv
mollerSetup_LIBS += calc
mollerSetup_LIBS += autosave
mollerSetup_LIBS += devIocStats
mollerSetup_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

