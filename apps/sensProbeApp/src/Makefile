TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_Linux = sensProbe

# sensProbe.dbd will be created and installed
DBD += sensProbe.dbd

# sensProbe.dbd will include these files:
sensProbe_DBD += base.dbd
sensProbe_DBD += devSnmp.dbd 
sensProbe_DBD += asSupport.dbd
sensProbe_DBD += devIocStats.dbd

# sensProbe_registerRecordDeviceDriver.cpp derives from sensProbe.dbd
sensProbe_SRCS += sensProbe_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
sensProbe_SRCS_DEFAULT += sensProbeMain.cpp
sensProbe_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#sensProbe_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
sensProbe_LIBS += devSnmp
sensProbe_LIBS += autosave
sensProbe_LIBS += devIocStats

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    # Build sncExample into sensProbeSupport
    #sncExample_SNCFLAGS += +r
    #sensProbe_DBD += sncExample.dbd
    #sensProbeSupport_SRCS += sncExample.stt
    #sensProbeSupport_LIBS += seq pv
    #sensProbe_LIBS += seq pv

    # Build sncProgram as a standalone program
    #PROD_HOST += sncProgram
    #sncProgram_SNCFLAGS += +m
    #sncProgram_SRCS += sncProgram.st
    #sncProgram_LIBS += seq pv
    #sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

# Finally link IOC to the EPICS Base libraries
sensProbe_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

