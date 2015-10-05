TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_vxWorks = classc3

# classc3.dbd will be created and installed
DBD += classc3.dbd

# classc3.dbd will include these files:
classc3_DBD += base.dbd
classc3_DBD += XY560Support.dbd

# classc3_registerRecordDeviceDriver.cpp derives from classc3.dbd
classc3_SRCS += classc3_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
classc3_SRCS_DEFAULT += classc3Main.cpp
classc3_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
classc3_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
classc3_LIBS += XY560Support
# classc3_LIBS += seq pv
classc3_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

