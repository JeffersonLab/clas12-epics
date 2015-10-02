TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Install dbd into <top>/dbd
DBD += DVME628Support.dbd

# Build an IOC support library
LIBRARY_IOC_vxWorks += DVME628Support

# Compile and add the code to the support library
DVME628Support_SRCS += devAoDVME628.c
DVME628Support_SRCS += drvDVME628.c

DVME628Support_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC_vxWorks = DVME628

# DVME628.dbd will be created and installed
DBD += DVME628.dbd

# DVME628.dbd will include these files:
DVME628_DBD += base.dbd
DVME628_DBD += DVME628Support.dbd

# DVME628_registerRecordDeviceDriver.cpp derives from DVME628.dbd
DVME628_SRCS += DVME628_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
DVME628_SRCS_DEFAULT += DVME628Main.cpp
DVME628_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
DVME628_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
DVME628_LIBS += DVME628Support
DVME628_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

