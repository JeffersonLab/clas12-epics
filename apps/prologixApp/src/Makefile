TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC_Linux += prologixSupport

DBD += prologixSupport.dbd

prologixSupport_DBD += base.dbd
prologixSupport_DBD += asyn.dbd
prologixSupport_DBD += drvAsynIPPort.dbd
prologixSupport_DBD += stream.dbd

prologixSupport_LIBS += stream
prologixSupport_LIBS += asyn
prologixSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC_Linux = prologix
# prologix.dbd will be created and installed
DBD += prologix.dbd

# prologix.dbd will be made up from these files:
prologix_DBD += prologixSupport.dbd
prologix_DBD += asSupport.dbd
prologix_DBD += devIocStats.dbd

# prologix_registerRecordDeviceDriver.cpp derives from prologix.dbd
prologix_SRCS += prologix_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
prologix_SRCS_DEFAULT += prologixMain.cpp
prologix_SRCS_vxWorks += -nil-

#prologix_LIBS += prologixSupport
prologix_LIBS += autosave
prologix_LIBS += devIocStats
prologix_LIBS += stream
prologix_LIBS += asyn
prologix_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
