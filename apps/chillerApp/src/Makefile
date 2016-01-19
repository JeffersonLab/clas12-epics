TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Install xxxSupport.dbd into <top>/dbd
DBD += chillerSupport.dbd

chillerSupport_DBD += base.dbd
chillerSupport_DBD += stream.dbd
chillerSupport_DBD += asyn.dbd
chillerSupport_DBD += drvAsynIPPort.dbd

# Build an IOC support library
LIBRARY_IOC += chillerSupport

# Compile and add the code to the support library
#chillerSupport_SRCS += xxxRecord.c

chillerSupport_LIBS += stream
chillerSupport_LIBS += asyn
chillerSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC = chiller

# chiller.dbd will be created and installed
DBD += chiller.dbd

# chiller.dbd will include these files:
chiller_DBD += base.dbd
chiller_DBD += chillerSupport.dbd
chiller_DBD += asSupport.dbd
chiller_DBD += devIocStats.dbd

# chiller_registerRecordDeviceDriver.cpp derives from chiller.dbd
chiller_SRCS += chiller_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
chiller_SRCS_DEFAULT += chillerMain.cpp
chiller_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#chiller_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
#chiller_LIBS += chillerSupport
chiller_LIBS += stream
chiller_LIBS += autosave
chiller_LIBS += devIocStats
chiller_LIBS += asyn
chiller_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

