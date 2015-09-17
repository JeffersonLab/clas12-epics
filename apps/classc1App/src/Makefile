TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_vxWorks = classc1

# classc1.dbd will be created and installed
DBD += classc1.dbd

# classc1.dbd will include these files:
classc1_DBD += base.dbd
#classc1_DBD += xxxSupport.dbd
#classc1_DBD += dbSubExample.dbd
#classc1_DBD += classc1Hello.dbd
#classc1_DBD += initTrace.dbd

# classc1_registerRecordDeviceDriver.cpp derives from classc1.dbd
classc1_SRCS += classc1_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
classc1_SRCS_DEFAULT += classc1Main.cpp
classc1_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
classc1_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
#classc1_LIBS += classc1Support

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    # Build sncExample into classc1Support
#    sncExample_SNCFLAGS += +r
#    classc1_DBD += sncExample.dbd
#    classc1Support_SRCS += sncExample.stt
#    classc1Support_LIBS += seq pv
#    classc1_LIBS += seq pv

    # Build sncProgram as a standalone program
#    PROD_HOST += sncProgram
#    sncProgram_SNCFLAGS += +m
#    sncProgram_SRCS += sncProgram.st
#    sncProgram_LIBS += seq pv
#    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

# Finally link IOC to the EPICS Base libraries
classc1_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

