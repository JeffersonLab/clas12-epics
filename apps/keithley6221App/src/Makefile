TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC support library

LIBRARY_IOC += keithley6221Support

keithley6221Support_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC = keithley6221
# keithley6221.dbd will be created and installed
DBD += keithley6221.dbd

# keithley6221.dbd will be made up from these files:
keithley6221_DBD += base.dbd
keithley6221_DBD += stream.dbd
keithley6221_DBD += drvAsynIPPort.dbd asyn.dbd
keithley6221_DBD += asSupport.dbd
keithley6221_DBD += devIocStats.dbd

# keithley6221_registerRecordDeviceDriver.cpp derives from keithley6221.dbd
keithley6221_SRCS += keithley6221_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
keithley6221_SRCS_DEFAULT += keithley6221Main.cpp
keithley6221_SRCS_vxWorks += -nil-

# Link in the code from the support library
keithley6221_LIBS += autosave
keithley6221_LIBS += stream
keithley6221_LIBS += devIocStats
keithley6221_LIBS += asyn
keithley6221_LIBS += seq pv

# Finally link to the EPICS Base libraries
keithley6221_LIBS += $(EPICS_BASE_IOC_LIBS)



#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

