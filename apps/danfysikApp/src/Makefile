TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = danfysik

# danfysik.dbd will be created and installed
DBD += danfysik.dbd
danfysik_DBD += base.dbd
danfysik_DBD += stream.dbd
danfysik_DBD += drvAsynIPPort.dbd
danfysik_DBD += asyn.dbd
danfysik_DBD += asSupport.dbd
danfysik_DBD += devIocStats.dbd

# danfysik_registerRecordDeviceDriver.cpp derives from danfysik.dbd
danfysik_SRCS += danfysik_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
danfysik_SRCS_DEFAULT += danfysikMain.cpp
danfysik_SRCS_vxWorks += -nil-

danfysik_LIBS += seq pv
danfysik_LIBS += stream
danfysik_LIBS += asyn
danfysik_LIBS += autosave
danfysik_LIBS += devIocStats
danfysik_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
danfysik_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

