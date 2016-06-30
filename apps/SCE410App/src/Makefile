TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Install SCE410Support.dbd into <top>/dbd
DBD += SCE410Support.dbd

SCE410Support_DBD += base.dbd
SCE410Support_DBD += stream.dbd
SCE410Support_DBD += asyn.dbd
SCE410Support_DBD += drvAsynIPPort.dbd

# Build an IOC support library
LIBRARY_IOC += SCE410Support

SCE410Support_LIBS += stream
SCE410Support_LIBS += asyn
SCE410Support_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC = SCE410

# SCE410.dbd will be created and installed
DBD += SCE410.dbd

# SCE410.dbd will include these files:
SCE410_DBD += base.dbd
SCE410_DBD += SCE410Support.dbd
SCE410_DBD += asSupport.dbd
SCE410_DBD += devIocStats.dbd

# SCE410_registerRecordDeviceDriver.cpp derives from SCE410.dbd
SCE410_SRCS += SCE410_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
SCE410_SRCS_DEFAULT += sce410Main.cpp
SCE410_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#SCE410_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
SCE410_LIBS += stream
SCE410_LIBS += autosave
SCE410_LIBS += devIocStats
SCE410_LIBS += asyn
SCE410_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

