TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC = cagw

# cagw.dbd will be created and installed
DBD += cagw.dbd

# cagw.dbd will include these files:
cagw_DBD += base.dbd
cagw_DBD += devIocStats.dbd
cagw_DBD += asSupport.dbd

# cagw_registerRecordDeviceDriver.cpp derives from cagw.dbd
cagw_SRCS += cagw_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
cagw_SRCS_DEFAULT += cagwMain.cpp
cagw_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#cagw_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
cagw_LIBS += devIocStats
cagw_LIBS += autosave
cagw_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

