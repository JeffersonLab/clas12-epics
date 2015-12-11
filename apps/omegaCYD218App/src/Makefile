TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

DBD += OmegaCYD218Support.dbd

OmegaCYD218Support_DBD += base.dbd
OmegaCYD218Support_DBD += stream.dbd
OmegaCYD218Support_DBD += asyn.dbd
OmegaCYD218Support_DBD += drvAsynIPPort.dbd

# Build an IOC support library
#LIBRARY_IOC += OmegaCYD218Support

# Compile and add the code to the support library
#OmegaCYD218Support_SRCS += xxxRecord.c

#OmegaCYD218Support_LIBS += stream
#OmegaCYD218Support_LIBS += asyn
#OmegaCYD218Support_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC = OmegaCYD218

# OmegaCYD218.dbd will be created and installed
DBD += OmegaCYD218.dbd

# OmegaCYD218.dbd will include these files:
OmegaCYD218_DBD += base.dbd
OmegaCYD218_DBD += OmegaCYD218Support.dbd
OmegaCYD218_DBD += asSupport.dbd
OmegaCYD218_DBD += devIocStats.dbd

# OmegaCYD218_registerRecordDeviceDriver.cpp derives from OmegaCYD218.dbd
OmegaCYD218_SRCS += OmegaCYD218_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
OmegaCYD218_SRCS_DEFAULT += OmegaCYD218Main.cpp
OmegaCYD218_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#OmegaCYD218_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
OmegaCYD218_LIBS += autosave
OmegaCYD218_LIBS += devIocStats
OmegaCYD218_LIBS += stream
OmegaCYD218_LIBS += asyn
OmegaCYD218_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

