TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC_vxWorks += scalerSupport

DBD += scalerSupport.dbd

scalerSupport_DBD += scalerSNC.dbd
scalerSupport_SRCS += scaler_restart.st

scalerSupport_LIBS += std
#scalerSupport_LIBS += busy
#scalerSupport_LIBS += calc
#scalerSupport_LIBS += sscan
scalerSupport_LIBS += vme
scalerSupport_LIBS += asyn
scalerSupport_LIBS += seq pv
scalerSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC_vxWorks = scaler
# scaler.dbd will be created and installed
DBD += scaler.dbd

scaler_DBD += base.dbd
scaler_DBD += scalerSupport.dbd

# Build the main IOC entry point on workstation OSs.
scaler_SRCS_DEFAULT += scalerMain.cpp
scaler_SRCS_vxWorks += scaler_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
scaler_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
scaler_LIBS += scalerSupport
scaler_LIBS += devIocStats autosave
scaler_LIBS += std
#scalerSupport_LIBS += busy
#scalerSupport_LIBS += calc
#scalerSupport_LIBS += sscan
scaler_LIBS += vme
scaler_LIBS += asyn
scaler_LIBS += seq pv
scaler_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

