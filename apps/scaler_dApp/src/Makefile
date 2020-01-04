TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC_vxWorks += scaler_dSupport

# scaler_dSupport.dbd will be created and installed
DBD += scaler_dSupport.dbd

# scaler_dSupport.dbd will be made up from these files:
scaler_dSupport_DBD += base.dbd
scaler_dSupport_DBD += asyn.dbd
scaler_dSupport_DBD += stdSupport.dbd
scaler_dSupport_DBD += calcSupport.dbd
scaler_dSupport_DBD += busySupport.dbd 
scaler_dSupport_DBD += sscanSupport.dbd 
scaler_dSupport_DBD += vmeVXSupport.dbd
scaler_dSupport_DBD += scaler_dSNC.dbd

scaler_dSupport_SRCS += scaler_d_restart.st

scaler_dSupport_LIBS += calc
scaler_dSupport_LIBS += busy
scaler_dSupport_LIBS += sscan
scaler_dSupport_LIBS += vme
scaler_dSupport_LIBS += std
scaler_dSupport_LIBS += asyn
scaler_dSupport_LIBS += seq pv

# Finally link to the EPICS Base libraries
scaler_dSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC_vxWorks = scaler_d
# scaler_d.dbd will be created and installed
DBD += scaler_d.dbd

# scaler_d.dbd will be made up from these files:
scaler_d_DBD += scaler_dSupport.dbd

# Build the main IOC entry point on workstation OSs.
scaler_d_SRCS_DEFAULT += scaler_dMain.cpp
scaler_d_SRCS_vxWorks += scaler_d_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
scaler_d_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
scaler_d_LIBS += scaler_dSupport
scaler_d_LIBS += calc
scaler_d_LIBS += busy
scaler_d_LIBS += sscan
scaler_d_LIBS += vme
scaler_d_LIBS += std
scaler_d_LIBS += asyn
scaler_d_LIBS += seq pv 

# Finally link to the EPICS Base libraries
scaler_d_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

