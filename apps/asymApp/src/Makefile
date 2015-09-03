TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

#LIBRARY_IOC_DEFAULT += -nil-
LIBRARY_IOC_vxWorks += asymSupport
# xxxRecord.h will be created from xxxRecord.dbd
##DBDINC += xxxRecord
# Install devXxxSoft.dbd into <top>/dbd
##DBD += xxxSupport.dbd
DBD += asymSupport.dbd
asymSupport_DBD += base.dbd
#asymSupport_DBD += asyn.dbd

asymSupport_DBD += stdSupport.dbd
#asymSupport_DBD += calcSupport.dbd
#asymSupport_DBD += busySupport.dbd 
#asymSupport_DBD += sscanSupport.dbd 
#asymSupport_DBD += asSupport.dbd
#asymSupport_DBD += std.dbd
asymSupport_DBD += mcaSupport.dbd
asymSupport_DBD += mcaSISSupport.dbd
#asymSupport_DBD += mcaCanberraSupport.dbd
#asymSupport_DBD += stdVXSupport.dbd

asymSupport_LIBS += $(EPICS_BASE_IOC_LIBS)


#=============================
# Build the IOC application

##PROD_IOC = asym
PROD_IOC_vxWorks = asym
# asym.dbd will be created and installed
DBD += asym.dbd

# asym.dbd will be made up from these files:
asym_DBD += asymSupport.dbd

# asym_registerRecordDeviceDriver.cpp derives from asym.dbd

# Build the main IOC entry point on workstation OSs.
asym_SRCS_DEFAULT += asymMain.cpp
#asym_SRCS_vxWorks += -nil-
asym_SRCS_vxWorks += asym_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
asym_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
asym_LIBS += asymSupport 
asym_LIBS += mca
#asym_LIBS += calc
#asym_LIBS += busy
#asym_LIBS += sscan
#asym_LIBS += autosave
asym_LIBS += std
#asym_LIBS += stream streamSynApps
asym_LIBS += asyn
asym_LIBS += seqDev seq pv

asym_LIBS += mcaSIS
asym_LIBS += mcaCanberra

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file

ifneq ($(SNCSEQ),)
    # Build sncExample into asymSupport
##    sncExample_SNCFLAGS += +r
##    asym_DBD += sncExample.dbd
##    asymSupport_SRCS += sncExample.stt

#    asym_SNCFLAGS += +r
    asymSupport_DBD += asymSNC.dbd
    asymSupport_SRCS += asym.st
    asym_SRCS += asym.st
    asymSupport_LIBS += seq pv

    # Build sncProgram as a standalone program
##    PROD_HOST += sncProgram
##    sncProgram_SNCFLAGS += +m
##    sncProgram_SRCS += sncProgram.st
##    sncProgram_LIBS += seq pv
##    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
#    asym_SRCS += asym.st
endif

# Finally link to the EPICS Base libraries
asym_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

