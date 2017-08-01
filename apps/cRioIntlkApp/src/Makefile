TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================

#=============================
# Build the IOC application

PROD_IOC = cRioIntlk
# cRioIntlk.dbd will be created and installed
DBD += cRioIntlk.dbd

# cRioIntlk.dbd will be made up from these files:
cRioIntlk_DBD += base.dbd
cRioIntlk_DBD += asSupport.dbd
cRioIntlk_DBD += devIocStats.dbd

# cRioIntlk_registerRecordDeviceDriver.cpp derives from cRioIntlk.dbd
cRioIntlk_SRCS += cRioIntlk_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
cRioIntlk_SRCS_DEFAULT += cRioIntlkMain.cpp
cRioIntlk_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#cRioIntlk_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
cRioIntlk_LIBS += devIocStats
cRioIntlk_LIBS += autosave

# Finally link to the EPICS Base libraries
cRioIntlk_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

