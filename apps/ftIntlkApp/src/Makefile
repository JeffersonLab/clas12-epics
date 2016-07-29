TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================

#=============================
# Build the IOC application

PROD_IOC = ftIntlk
# ftIntlk.dbd will be created and installed
DBD += ftIntlk.dbd

# ftIntlk.dbd will be made up from these files:
ftIntlk_DBD += base.dbd
ftIntlk_DBD += devIocStats.dbd

# ftIntlk_registerRecordDeviceDriver.cpp derives from ftIntlk.dbd
ftIntlk_SRCS += ftIntlk_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
ftIntlk_SRCS_DEFAULT += ftIntlkMain.cpp
ftIntlk_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#ftIntlk_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
ftIntlk_LIBS += devIocStats

# Finally link to the EPICS Base libraries
ftIntlk_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

