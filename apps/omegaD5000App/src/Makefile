TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC += tempSensSupport

tempSensSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC = tempSens
# tempSens.dbd will be created and installed
DBD += tempSens.dbd

# tempSens.dbd will be made up from these files:
tempSens_DBD += base.dbd
tempSens_DBD += asyn.dbd
tempSens_DBD += drvAsynIPPort.dbd
tempSens_DBD += stream.dbd
tempSens_DBD += asSupport.dbd
tempSens_DBD += devIocStats.dbd

# tempSens_registerRecordDeviceDriver.cpp derives from tempSens.dbd
tempSens_SRCS += tempSens_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
tempSens_SRCS_DEFAULT += tempSensMain.cpp
tempSens_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#tempSens_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

tempSens_LIBS += autosave
tempSens_LIBS += devIocStats
tempSens_LIBS += stream streamSynApps
tempSens_LIBS += asyn
tempSens_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

