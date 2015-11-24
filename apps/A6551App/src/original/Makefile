TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# xxxRecord.h will be created from xxxRecord.dbd
DBDINC += xxxRecord

# Install xxxSupport.dbd into <top>/dbd
DBD += xxxSupport.dbd

# Build an IOC support library
LIBRARY_IOC += A6551Support

# Compile and add the code to the support library
A6551Support_SRCS += xxxRecord.c
A6551Support_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application.
# This is required for Windows DLL builds.
A6551Support_SRCS += dbSubExample.c
A6551Support_SRCS += A6551Hello.c
A6551Support_SRCS += initTrace.c

A6551Support_LIBS += $(EPICS_BASE_IOC_LIBS)

# Build the IOC application
PROD_IOC = A6551

# A6551.dbd will be created and installed
DBD += A6551.dbd

# A6551.dbd will include these files:
A6551_DBD += base.dbd
A6551_DBD += xxxSupport.dbd
A6551_DBD += dbSubExample.dbd
A6551_DBD += A6551Hello.dbd
A6551_DBD += initTrace.dbd

# A6551_registerRecordDeviceDriver.cpp derives from A6551.dbd
A6551_SRCS += A6551_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
A6551_SRCS_DEFAULT += A6551Main.cpp
A6551_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#A6551_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
A6551_LIBS += A6551Support

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    # Build sncExample into A6551Support
    sncExample_SNCFLAGS += +r
    A6551_DBD += sncExample.dbd
    A6551Support_SRCS += sncExample.stt
    A6551Support_LIBS += seq pv
    A6551_LIBS += seq pv

    # Build sncProgram as a standalone program
    PROD_HOST += sncProgram
    sncProgram_SNCFLAGS += +m
    sncProgram_SRCS += sncProgram.st
    sncProgram_LIBS += seq pv
    sncProgram_LIBS += $(EPICS_BASE_HOST_LIBS)
endif

# Finally link IOC to the EPICS Base libraries
A6551_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

