TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC_vxWorks += scaler_eSupport

# scaler_eSupport.dbd will be created and installed
DBD += scaler_eSupport.dbd

# scaler_eSupport.dbd will be made up from these files:
scaler_eSupport_DBD += base.dbd
scaler_eSupport_DBD += asyn.dbd
scaler_eSupport_DBD += stdSupport.dbd
scaler_eSupport_DBD += calcSupport.dbd
scaler_eSupport_DBD += busySupport.dbd 
scaler_eSupport_DBD += sscanSupport.dbd 
scaler_eSupport_DBD += vmeVXSupport.dbd
scaler_eSupport_DBD += scaler_eSNC.dbd

scaler_eSupport_SRCS += scaler_e_restart.st

scaler_eSupport_LIBS += calc
scaler_eSupport_LIBS += busy
scaler_eSupport_LIBS += sscan
scaler_eSupport_LIBS += vme
scaler_eSupport_LIBS += std
scaler_eSupport_LIBS += asyn
scaler_eSupport_LIBS += seq pv

# Finally link to the EPICS Base libraries
scaler_eSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC_vxWorks = scaler_e
# scaler_e.dbd will be created and installed
DBD += scaler_e.dbd

# scaler_e.dbd will be made up from these files:
scaler_e_DBD += scaler_eSupport.dbd

# Build the main IOC entry point on workstation OSs.
scaler_e_SRCS_DEFAULT += scaler_eMain.cpp
scaler_e_SRCS_vxWorks += scaler_e_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
scaler_e_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
scaler_e_LIBS += scaler_eSupport
scaler_e_LIBS += calc
scaler_e_LIBS += busy
scaler_e_LIBS += sscan
scaler_e_LIBS += vme
scaler_e_LIBS += std
scaler_e_LIBS += asyn
scaler_e_LIBS += seq pv 

# Finally link to the EPICS Base libraries
scaler_e_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

