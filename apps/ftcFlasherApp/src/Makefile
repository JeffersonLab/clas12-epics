TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================

#=============================
# Build the IOC application

PROD_IOC = ftcFlasher
# ftcFlasher.dbd will be created and installed
DBD += ftcFlasher.dbd

# ftcFlasher.dbd will be made up from these files:
ftcFlasher_DBD += base.dbd
ftcFlasher_DBD += devIocStats.dbd
ftcFlasher_DBD += asyn.dbd
ftcFlasher_DBD += drvAsynIPPort.dbd
ftcFlasher_DBD += stream.dbd
ftcFlasher_DBD += system.dbd

# ftcFlasher_registerRecordDeviceDriver.cpp derives from ftcFlasher.dbd
ftcFlasher_SRCS += ftcFlasher_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
ftcFlasher_SRCS_DEFAULT += ftcFlasherMain.cpp
ftcFlasher_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#ftcFlasher_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
ftcFlasher_LIBS += devIocStats
ftcFlasher_LIBS += stream
ftcFlasher_LIBS += asyn

# Finally link to the EPICS Base libraries
ftcFlasher_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

