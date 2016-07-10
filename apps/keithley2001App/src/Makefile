TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = keithley2001

# keithley2001.dbd will be created and installed
DBD += keithley2001.dbd
keithley2001_DBD += base.dbd
keithley2001_DBD += stream.dbd
keithley2001_DBD += drvAsynIPPort.dbd
keithley2001_DBD += asyn.dbd
keithley2001_DBD += asSupport.dbd
keithley2001_DBD += devIocStats.dbd
keithley2001_DBD += keithley2001SNC.dbd

# keithley2001_registerRecordDeviceDriver.cpp derives from keithley2001.dbd
keithley2001_SRCS += keithley2001_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
keithley2001_SRCS_DEFAULT += keithley2001Main.cpp
keithley2001_SRCS_vxWorks += -nil-

keithley2001_SRCS += moellermeter.st

keithley2001_LIBS += seq pv
keithley2001_LIBS += stream
keithley2001_LIBS += asyn
keithley2001_LIBS += autosave
keithley2001_LIBS += devIocStats
keithley2001_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
keithley2001_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

