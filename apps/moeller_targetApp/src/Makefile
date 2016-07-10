TOP=../..

include $(TOP)/configure/CONFIG

# Build the IOC application
PROD_IOC = moeller_target
#PROD_IOC_LINUX = moeller_target
#PROD_IOC_Linux = moeller_target

# moeller_target.dbd will be created and installed
DBD += moeller_target.dbd

moeller_target_DBD += asSupport.dbd
moeller_target_DBD += devIocStats.dbd

# moeller_target_registerRecordDeviceDriver.cpp derives from moeller_target.dbd
moeller_target_SRCS += moeller_target_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
moeller_target_SRCS_DEFAULT += moeller_targetMain.cpp
moeller_target_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#moeller_target_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

moeller_target_SRCS += moeller_target.st
moeller_target_LIBS += seq pv
moeller_target_LIBS += autosave
moeller_target_LIBS += devIocStats
moeller_target_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES

