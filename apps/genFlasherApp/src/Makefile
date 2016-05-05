TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = genFlasher
# genFlasher.dbd will be created and installed
DBD += genFlasher.dbd

# genFlasher.dbd will be made up from these files:
genFlasher_DBD += base.dbd
genFlasher_DBD += devIocStats.dbd
genFlasher_DBD += asyn.dbd
genFlasher_DBD += drvAsynIPPort.dbd
genFlasher_DBD += stream.dbd
genFlasher_DBD += system.dbd

# Include dbd files from all support applications:
#genFlasher_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#genFlasher_LIBS += xxx

# genFlasher_registerRecordDeviceDriver.cpp derives from genFlasher.dbd
genFlasher_SRCS += genFlasher_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
genFlasher_SRCS_DEFAULT += genFlasherMain.cpp
genFlasher_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#genFlasher_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Link in the code from the support library
genFlasher_LIBS += devIocStats
genFlasher_LIBS += stream
genFlasher_LIBS += asyn

# Finally link to the EPICS Base libraries
genFlasher_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

