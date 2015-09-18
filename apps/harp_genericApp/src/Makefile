TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC_vxWorks += harp_genericSupport

DBD += harp_genericSupport.dbd

harp_genericSupport_DBD += base.dbd
harp_genericSupport_DBD += motorRecord.dbd
harp_genericSupport_DBD += devOms.dbd
harp_genericSupport_DBD += harp_genericSNC.dbd

harp_genericSupport_SRCS += harp_scan_generic.st
harp_genericSupport_SRCS += reset_motor.st

harp_genericSupport_LIBS += oms
harp_genericSupport_LIBS += motor
harp_genericSupport_LIBS += seq pv
harp_genericSupport_LIBS += $(EPICS_BASE_IOC_LIBS)


#=============================
# Build the IOC application

PROD_IOC_vxWorks = harp_generic
# harp_generic.dbd will be created and installed
DBD += harp_generic.dbd

# harp_generic.dbd will be made up from these files:
harp_generic_DBD += harp_genericSupport.dbd

# harp_generic_registerRecordDeviceDriver.cpp derives from harp_generic.dbd

# Build the main IOC entry point on workstation OSs.
harp_generic_SRCS_DEFAULT += harp_genericMain.cpp
harp_generic_SRCS_vxWorks += harp_generic_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
harp_generic_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
harp_generic_LIBS += harp_genericSupport
harp_generic_LIBS += oms
harp_generic_LIBS += motor
harp_generic_LIBS += seq pv 
harp_generic_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

