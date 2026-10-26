TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC application

PROD_IOC_Linux = siemens
# siemens.dbd will be created and installed
DBD += siemens.dbd

# siemens.dbd will be made up from these files:
siemens_DBD += base.dbd
siemens_DBD += s7nodave.dbd
siemens_DBD += calcSupport.dbd
siemens_DBD += busySupport.dbd
siemens_DBD += sscanSupport.dbd
siemens_DBD += calc.dbd
siemens_DBD += aCalcoutRecord.dbd
siemens_DBD += sCalcoutRecord.dbd
siemens_DBD += asSupport.dbd
siemens_DBD += asyn.dbd
siemens_DBD += std.dbd
siemens_DBD += devIocStats.dbd 
siemens_DBD += caPutLog.dbd

# siemens_registerRecordDeviceDriver.cpp derives from siemens.dbd
siemens_SRCS += siemens_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
siemens_SRCS_DEFAULT += siemensMain.cpp

# Link in the code from the support library
siemens_LIBS += s7nodave
siemens_LIBS += calc
siemens_LIBS += busy
siemens_LIBS += sscan
siemens_LIBS += autosave
siemens_LIBS += std
siemens_LIBS += caPutLog
siemens_LIBS += asyn
siemens_LIBS += devIocStats
siemens_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

