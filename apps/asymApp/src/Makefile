TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

#LIBRARY_IOC_DEFAULT += -nil-
LIBRARY_IOC_vxWorks += asymSupport

# asymSupport will be created and installed
DBD += asymSupport.dbd

asymSupport_DBD += base.dbd
asymSupport_DBD += stdSupport.dbd
asymSupport_DBD += mcaSupport.dbd
asymSupport_DBD += SIS38XXSupport.dbd

ifneq ($(SNCSEQ),)
    asymSupport_DBD += asymSNC.dbd
    asymSupport_SRCS += asym.st
    asymSupport_LIBS += seq pv
endif

asymSupport_LIBS += mca
asymSupport_LIBS += std
asymSupport_LIBS += asyn
asymSupport_LIBS += SIS38XX
asymSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC_vxWorks = asym
# asym.dbd will be created and installed
DBD += asym.dbd

# asym.dbd will be made up from these files:
asym_DBD += base.dbd
asym_DBD += asymSupport.dbd

# Build the main IOC entry point on workstation OSs.
asym_SRCS_DEFAULT += asymMain.cpp
asym_SRCS_vxWorks += asym_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
asym_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
asym_LIBS += asymSupport 
asym_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

