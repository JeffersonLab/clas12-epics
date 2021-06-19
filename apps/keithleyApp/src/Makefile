TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC_Linux = keithley

# keithley.dbd will be created and installed
DBD += keithley.dbd
keithley_DBD += base.dbd
keithley_DBD += stream.dbd
keithley_DBD += drvAsynIPPort.dbd
keithley_DBD += asyn.dbd
keithley_DBD += asSupport.dbd
keithley_DBD += devIocStats.dbd
keithley_DBD += keithleySNC.dbd

# keithley_registerRecordDeviceDriver.cpp derives from keithley.dbd
keithley_SRCS += keithley_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
keithley_SRCS_DEFAULT += keithleyMain.cpp
keithley_SRCS_vxWorks += -nil-

keithley_SRCS += moellermeter.st

keithley_LIBS += seq pv
keithley_LIBS += stream
keithley_LIBS += asyn
keithley_LIBS += autosave
keithley_LIBS += devIocStats
keithley_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
keithley_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

