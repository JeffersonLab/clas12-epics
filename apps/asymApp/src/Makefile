TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC_vxWorks += asymSupport

DBD += asymSupport.dbd

asymSupport_DBD += base.dbd
asymSupport_DBD += asyn.dbd
asymSupport_DBD += stdSupport.dbd
asymSupport_DBD += asSupport.dbd
asymSupport_DBD += mcaSupport.dbd
asymSupport_DBD += SIS38XXSupport.dbd

asymSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC_vxWorks = asym

DBD += asym.dbd

asym_DBD += asymSupport.dbd

# Build the main IOC entry point on workstation OSs.
asym_SRCS_DEFAULT += asymMain.cpp
asym_SRCS_vxWorks += asym_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
asym_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
asym_LIBS += asymSupport 
asym_LIBS += SIS38XX mca
asym_LIBS += autosave
asym_LIBS += std
asym_LIBS += asyn
asym_LIBS += seq pv

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    asymSupport_DBD += asymSNC.dbd
    asymSupport_SRCS += asym.st
    asym_SRCS += asym.st
    asymSupport_SRCS += SIS38XX_SNL_asym.st
    asym_SRCS += SIS38XX_SNL_asym.st
    asymSupport_LIBS += seq pv
endif

# Finally link to the EPICS Base libraries
asym_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

