TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC += btaSupport

DBD += btaSupport.dbd

btaSupport_DBD += btaSNC.dbd

btaSupport_SRCS += bta.st
btaSupport_SRCS += bta_test.st

btaSupport_LIBS += seq pv
btaSupport_LIBS += $(EPICS_BASE_IOC_LIBS)


#=============================
# Build the IOC application

PROD_IOC = bta
# bta.dbd will be created and installed
DBD += bta.dbd

# bta.dbd will be made up from these files:
bta_DBD += btaSupport.dbd

# Build the main IOC entry point on workstation OSs.
bta_SRCS_DEFAULT += btaMain.cpp
bta_SRCS_vxWorks += bta_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
###bta_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
bta_LIBS += btaSupport
bta_LIBS += autosave
bta_LIBS += seq pv 

# Finally link to the EPICS Base libraries
bta_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

