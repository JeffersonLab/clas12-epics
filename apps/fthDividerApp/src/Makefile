TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = fthDivider
# fthDivider.dbd will be created and installed
DBD += fthDivider.dbd

# fthDivider.dbd will be made up from these files:
fthDivider_DBD += base.dbd
fthDivider_DBD += devIocStats.dbd
fthDivider_DBD += asyn.dbd
fthDivider_DBD += calc.dbd
fthDivider_DBD += drvAsynIPPort.dbd
fthDivider_DBD += stream.dbd
fthDivider_DBD += system.dbd

# Include dbd files from all support applications:
#fthDivider_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#fthDivider_LIBS += xxx

# fthDivider_registerRecordDeviceDriver.cpp derives from fthDivider.dbd
fthDivider_SRCS += fthDivider_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
fthDivider_SRCS_DEFAULT += fthDividerMain.cpp
fthDivider_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#fthDivider_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
fthDivider_LIBS += devIocStats
fthDivider_LIBS += stream
fthDivider_LIBS += asyn
fthDivider_LIBS += calc
fthDivider_LIBS += autosave

# Finally link to the EPICS Base libraries
fthDivider_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

