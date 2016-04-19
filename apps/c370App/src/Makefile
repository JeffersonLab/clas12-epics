TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = c370
# c370.dbd will be created and installed
DBD += c370.dbd

# c370.dbd will be made up from these files:
c370_DBD += base.dbd
c370_DBD += drvAsynIPPort.dbd
c370_DBD += modbusSupport.dbd
c370_DBD += asSupport.dbd
c370_DBD += devIocStats.dbd
c370_DBD += asyn.dbd

# Add all the support libraries needed by this IOC
c370_LIBS += autosave
c370_LIBS += devIocStats
c370_LIBS += modbus
c370_LIBS += asyn

# c370_registerRecordDeviceDriver.cpp derives from c370.dbd
c370_SRCS += c370_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
c370_SRCS_DEFAULT += c370Main.cpp
c370_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#c370_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
c370_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE




