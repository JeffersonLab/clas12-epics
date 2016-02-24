TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_Linux = sensorProbe

# sensorProbe.dbd will be created and installed
DBD += sensorProbe.dbd

# sensorProbe.dbd will include these files:
sensorProbe_DBD += base.dbd
sensorProbe_DBD += devSnmp.dbd 
sensorProbe_DBD += asSupport.dbd
sensorProbe_DBD += devIocStats.dbd

# sensorProbe_registerRecordDeviceDriver.cpp derives from sensorProbe.dbd
sensorProbe_SRCS += sensorProbe_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
sensorProbe_SRCS_DEFAULT += sensorProbeMain.cpp
sensorProbe_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#sensorProbe_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
sensorProbe_LIBS += devSnmp
sensorProbe_LIBS += autosave
sensorProbe_LIBS += devIocStats

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
sensorProbe_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

