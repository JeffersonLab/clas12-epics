TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Build the IOC application
PROD_IOC_vxWorks = classc4

# classc4.dbd will be created and installed
DBD += classc4.dbd

# classc4.dbd will include these files:
classc4_DBD += base.dbd
classc4_DBD += scalerSupport.dbd
classc4_DBD += sixty_hzSupport.dbd

# classc4_registerRecordDeviceDriver.cpp derives from classc4.dbd
classc4_SRCS += classc4_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
classc4_SRCS_DEFAULT += classc4Main.cpp
classc4_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
classc4_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from our support library
classc4_LIBS += scalerSupport
classc4_LIBS += sixty_hzSupport

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    # Build sncExample into classc4Support
#    sncExample_SNCFLAGS += +r
#    classc4_DBD += sncExample.dbd
#    classc4Support_SRCS += sncExample.stt
#    classc4Support_LIBS += seq pv
#    classc4_LIBS += seq pv

endif

# Finally link IOC to the EPICS Base libraries
classc4_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

