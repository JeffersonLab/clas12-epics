TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC_vxWorks += frwd_scalerSupport

# frwd_scalerSupport.dbd will be created and installed
DBD += frwd_scalerSupport.dbd

# frwd_scalerSupport.dbd will be made up from these files:
frwd_scalerSupport_DBD += base.dbd
frwd_scalerSupport_DBD += asyn.dbd
frwd_scalerSupport_DBD += stdSupport.dbd
frwd_scalerSupport_DBD += calcSupport.dbd
frwd_scalerSupport_DBD += busySupport.dbd 
frwd_scalerSupport_DBD += sscanSupport.dbd 
frwd_scalerSupport_DBD += vmeVXSupport.dbd
frwd_scalerSupport_DBD += frwd_scalerSNC.dbd

frwd_scalerSupport_SRCS += frwd_scaler_restart.st

frwd_scalerSupport_LIBS += calc
frwd_scalerSupport_LIBS += busy
frwd_scalerSupport_LIBS += sscan
frwd_scalerSupport_LIBS += vme
frwd_scalerSupport_LIBS += std
frwd_scalerSupport_LIBS += asyn
frwd_scalerSupport_LIBS += seq pv

# Finally link to the EPICS Base libraries
frwd_scalerSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC_vxWorks = frwd_scaler
# frwd_scaler.dbd will be created and installed
DBD += frwd_scaler.dbd

# frwd_scaler.dbd will be made up from these files:
frwd_scaler_DBD += frwd_scalerSupport.dbd

# Build the main IOC entry point on workstation OSs.
frwd_scaler_SRCS_DEFAULT += frwd_scalerMain.cpp
frwd_scaler_SRCS_vxWorks += frwd_scaler_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
frwd_scaler_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
frwd_scaler_LIBS += frwd_scalerSupport
frwd_scaler_LIBS += calc
frwd_scaler_LIBS += busy
frwd_scaler_LIBS += sscan
frwd_scaler_LIBS += vme
frwd_scaler_LIBS += std
frwd_scaler_LIBS += asyn
frwd_scaler_LIBS += seq pv 

# Finally link to the EPICS Base libraries
frwd_scaler_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

