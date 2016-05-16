TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE


USR_INCLUDES += -I$(shell $(ROOT_CONFIG) --incdir)

EPICS_HOST_ARCH=linux-x86_64

#=============================
# Build the IOC application

PROD_IOC_Linux = wf2root
# wf2root.dbd will be created and installed
DBD += wf2root.dbd

# wf2root.dbd will be made up from these files:
wf2root_DBD += base.dbd
wf2root_DBD += asSupport.dbd
wf2root_DBD += devIocStats.dbd
wf2root_DBD += wf2rootSub.dbd

# wf2root_registerRecordDeviceDriver.cpp derives from wf2root.dbd
wf2root_SRCS += wf2root_registerRecordDeviceDriver.cpp

wf2root_SRCS += wf2rootSub.c
wf2root_SRCS += wf2rootManager.cpp

# Build the main IOC entry point on workstation OSs.
wf2root_SRCS_DEFAULT += wf2rootMain.cpp
wf2root_SRCS_vxWorks += -nil-


# Link in the code from the support library
wf2root_LIBS += autosave
wf2root_LIBS += devIocStats

wf2root_LDFLAGS += $(shell $(ROOT_CONFIG) --cflags)
wf2root_LDFLAGS += $(shell $(ROOT_CONFIG) --libs)

# Finally link to the EPICS Base libraries
wf2root_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
