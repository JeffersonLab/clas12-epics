TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_vxWorks = classc6

# classc6.dbd will be created and installed
DBD += classc6.dbd

# classc6.dbd will include these files:
classc6_DBD += base.dbd
#classc6_DBD += xxxSupport.dbd
#classc6_DBD += dbSubExample.dbd
#classc6_DBD += classc6Hello.dbd
#classc6_DBD += initTrace.dbd

# classc6_registerRecordDeviceDriver.cpp derives from classc6.dbd
classc6_SRCS += classc6_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
classc6_SRCS_DEFAULT += classc6Main.cpp
classc6_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
classc6_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
#classc6_LIBS += classc6Support

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    # Build sncExample into classc6Support
#    sncExample_SNCFLAGS += +r
#    classc6_DBD += sncExample.dbd
#    classc6Support_SRCS += sncExample.stt
#    classc6Support_LIBS += seq pv
#    classc6_LIBS += seq pv

    # Build sncProgram as a standalone program
#    PROD_HOST += sncProgram
#    sncProgram_SNCFLAGS += +m
#    sncProgram_SRCS += sncProgram.st
#    sncProgram_LIBS += seq pv
#    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

# Finally link IOC to the EPICS Base libraries
classc6_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

