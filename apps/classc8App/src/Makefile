TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_vxWorks = classc8

# classc8.dbd will be created and installed
DBD += classc8.dbd

# classc8.dbd will include these files:
classc8_DBD += base.dbd
#classc8_DBD += xxxSupport.dbd
#classc8_DBD += dbSubExample.dbd
#classc8_DBD += classc8Hello.dbd
#classc8_DBD += initTrace.dbd

# classc8_registerRecordDeviceDriver.cpp derives from classc8.dbd
classc8_SRCS += classc8_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
classc8_SRCS_DEFAULT += classc8Main.cpp
classc8_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
classc8_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
#classc8_LIBS += classc8Support

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    # Build sncExample into classc8Support
#    sncExample_SNCFLAGS += +r
#    classc8_DBD += sncExample.dbd
#    classc8Support_SRCS += sncExample.stt
#    classc8Support_LIBS += seq pv
#    classc8_LIBS += seq pv

    # Build sncProgram as a standalone program
#    PROD_HOST += sncProgram
#    sncProgram_SNCFLAGS += +m
#    sncProgram_SRCS += sncProgram.st
#    sncProgram_LIBS += seq pv
#    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

# Finally link IOC to the EPICS Base libraries
classc8_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

