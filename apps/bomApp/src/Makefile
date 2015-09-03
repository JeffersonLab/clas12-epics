TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

##LIBRARY_IOC += bomSupport

LIBRARY_IOC_vxWorks += bomSupport

# xxxRecord.h will be created from xxxRecord.dbd
##DBDINC += xxxRecord
# Install devXxxSoft.dbd into <top>/dbd
##DBD += xxxSupport.dbd
DBD += bomSupport.dbd
bomSupport_DBD += base.dbd
bomSupport_DBD += asyn.dbd
bomSupport_DBD += stdSupport.dbd
#bomSupport_DBD += calcSupport.dbd
#bomSupport_DBD += busySupport.dbd 
#bomSupport_DBD += sscanSupport.dbd 
bomSupport_DBD += asSupport.dbd
bomSupport_DBD += mcaSupport.dbd
bomSupport_DBD += mcaSISSupport.dbd
#bomSupport_DBD += mcaCanberraSupport.dbd
#bomSupport_DBD += stdVXSupport.dbd
bomSupport_DBD += histogramRecord.dbd
bomSupport_DBD += sub_funcs.dbd

#bomSupport_DBD += devSequencer.dbd

# Compile and add the code to the support library
##bomSupport_SRCS += xxxRecord.c
##bomSupport_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application.
##bomSupport_SRCS += dbSubExample.c
##bomSupport_SRCS += bomHello.c
##bomSupport_SRCS += initTrace.c

bomSupport_SRCS += sub_funcs.c

bomSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

##PROD_IOC = bom
PROD_IOC_vxWorks = bom
# bom.dbd will be created and installed
DBD += bom.dbd

# bom.dbd will be made up from these files:
##bom_DBD += base.dbd
##bom_DBD += xxxSupport.dbd
##bom_DBD += dbSubExample.dbd
##bom_DBD += bomHello.dbd
##bom_DBD += initTrace.dbd
bom_DBD += bomSupport.dbd

# bom_registerRecordDeviceDriver.cpp derives from bom.dbd
##bom_SRCS += bom_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
bom_SRCS_DEFAULT += bomMain.cpp
bom_SRCS_vxWorks += -nil-
bom_SRCS_vxWorks += bom_registerRecordDeviceDriver.cpp

# Add support from base/src/vxWorks if needed
bom_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
bom_LIBS += bomSupport

bom_LIBS += asyn
bom_LIBS += mca
#bom_LIBS += calc
#bom_LIBS += busy
#bom_LIBS += sscan
bom_LIBS += autosave
#bom_LIBS += vme
bom_LIBS += std

bom_LIBS += asyn
bom_LIBS += seq pv 

bom_LIBS += mcaSIS
#bom_LIBS += mcaCanberra

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file

ifneq ($(SNCSEQ),)
    # Build sncExample into bomSupport
##    sncExample_SNCFLAGS += +r
##    bom_DBD += sncExample.dbd
##    bomSupport_SRCS += sncExample.stt
##    bomSupport_LIBS += seq pv
##    bom_LIBS += seq pv

    # Build sncProgram as a standalone program
##    PROD_HOST += sncProgram
##    sncProgram_SNCFLAGS += +m
##    sncProgram_SRCS += sncProgram.st
##    sncProgram_LIBS += seq pv
##    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)

      bomSupport_LIBS += seq pv

endif

# Finally link to the EPICS Base libraries
bom_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

