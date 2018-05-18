TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE
#
PROD_IOC = richsim

# richsim.dbd will be created and installed
DBD += richsim.dbd

# richsim.dbd will include these files:
richsim_DBD += base.dbd
richsim_DBD += asSupport.dbd
richsim_DBD += devIocStats.dbd
richsim_DBD += caPutLog.dbd
richsim_DBD += richalarm.dbd

# richsim_registerRecordDeviceDriver.cpp derives from richsim.dbd
richsim_SRCS += richalarm.c
richsim_SRCS += richsim_registerRecordDeviceDriver.cpp
# Build the main IOC entry point where needed
richsim_SRCS_DEFAULT += richsimMain.cpp
richsim_SRCS_vxWorks += -nil-

# Link in the support libraries
richsim_LIBS += autosave devIocStats
richsim_LIBS += autosave
richsim_LIBS += caPutLog
richsim_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE
