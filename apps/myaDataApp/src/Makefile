TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC application

PROD_IOC_Linux = myaData
# myaData.dbd will be created and installed
DBD += myaData.dbd

# myaData.dbd will be made up from these files:
myaData_DBD += base.dbd
myaData_DBD += asSupport.dbd
myaData_DBD += devIocStats.dbd

# myaData_registerRecordDeviceDriver.cpp derives from myaData.dbd
myaData_SRCS += myaData_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
myaData_SRCS_DEFAULT += myaDataMain.cpp

# Link in the code from the support library
myaData_LIBS += autosave
myaData_LIBS += devIocStats

# Finally link to the EPICS Base libraries
myaData_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

