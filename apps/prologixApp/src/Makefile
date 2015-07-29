TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC += prologixSupport

prologixSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC = prologix
# prologix.dbd will be created and installed
DBD += prologix.dbd

# prologix.dbd will be made up from these files:
prologix_DBD += base.dbd
prologix_DBD += drvAsynIPPort.dbd
prologix_DBD += stream.dbd
prologix_DBD += asSupport.dbd
prologix_DBD += devIocStats.dbd

# prologix_registerRecordDeviceDriver.cpp derives from prologix.dbd
prologix_SRCS += prologix_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
prologix_SRCS_DEFAULT += prologixMain.cpp
prologix_SRCS_vxWorks += -nil-

prologix_LIBS += autosave
prologix_LIBS += stream
prologix_LIBS += devIocStats
prologix_LIBS += asyn

# Finally link to the EPICS Base libraries
prologix_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
