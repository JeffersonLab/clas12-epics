TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_vxWorks = taggerTemp

# taggerTemp.dbd will be created and installed
DBD += taggerTemp.dbd

# taggerTemp.dbd will include these files:
taggerTemp_DBD += base.dbd
taggerTemp_DBD += XY560Support.dbd

# taggerTemp_registerRecordDeviceDriver.cpp derives from taggerTemp.dbd
taggerTemp_SRCS += taggerTemp_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
taggerTemp_SRCS_DEFAULT += taggerTempMain.cpp
taggerTemp_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
taggerTemp_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
taggerTemp_LIBS += XY560Support
taggerTemp_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

