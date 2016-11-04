TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = codaDaq

# codaDaq.dbd will be created and installed
DBD += codaDaq.dbd
codaDaq_DBD += base.dbd
codaDaq_DBD += devIocStats.dbd

# codaDaq_registerRecordDeviceDriver.cpp derives from codaDaq.dbd
codaDaq_SRCS += codaDaq_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
codaDaq_SRCS_DEFAULT += codaDaqMain.cpp
codaDaq_SRCS_vxWorks += -nil-

codaDaq_LIBS += devIocStats
codaDaq_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
codaDaq_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

