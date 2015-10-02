TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build an IOC support library
LIBRARY_IOC_vxWorks += kepcoSupport

DBD += kepcoSupport.dbd
kepcoSupport_DBD += base.dbd
kepcoSupport_DBD += DVME628Support.dbd
kepcoSupport_DBD += kepcoSNC.dbd

kepcoSupport_SRCS += kepco_seq.st

kepcoSupport_LIBS += seq pv
kepcoSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC_vxWorks = kepco

# kepco.dbd will be created and installed
DBD += kepco.dbd

# kepco.dbd will include these files:
kepco_DBD += kepcoSupport.dbd

# kepco_registerRecordDeviceDriver.cpp derives from kepco.dbd
kepco_SRCS += kepco_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
kepco_SRCS_DEFAULT += kepcoMain.cpp
kepco_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
kepco_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
kepco_LIBS += DVME628Support
kepco_LIBS += kepcoSupport
kepco_LIBS += seq pv
kepco_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

