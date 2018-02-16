TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_vxWorks = classchv

# classchv.dbd will be created and installed
DBD += classchv.dbd

# classchv.dbd will include these files:
classchv_DBD += base.dbd
classchv_DBD += devIocStats.dbd
classchv_DBD += asSupport.dbd
classchv_DBD += XY240Support.dbd

# classchv_registerRecordDeviceDriver.cpp derives from classchv.dbd
classchv_SRCS += classchv_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
classchv_SRCS_DEFAULT += classchvMain.cpp
classchv_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#classchv_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
classchv_LIBS += devIocStats
classchv_LIBS += autosave
classchv_LIBS += XY240Support
classchv_LIBS += vme
classchv_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

