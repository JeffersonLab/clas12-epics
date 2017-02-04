TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = bta

# bta.dbd will be created and installed
DBD += bta.dbd
bta_DBD += base.dbd
bta_DBD += devIocStats.dbd
bta_DBD += asSupport.dbd

# bta_registerRecordDeviceDriver.cpp derives from bta.dbd
bta_SRCS += bta_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
bta_SRCS_DEFAULT += btaMain.cpp
bta_SRCS_vxWorks += -nil-

bta_LIBS += autosave
bta_LIBS += devIocStats
bta_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
bta_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

