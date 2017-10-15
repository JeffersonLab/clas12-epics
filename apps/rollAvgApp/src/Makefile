TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = rollAvg

# rollAvg.dbd will be created and installed
DBD += rollAvg.dbd
rollAvg_DBD += base.dbd
rollAvg_DBD += devIocStats.dbd
rollAvg_DBD += asSupport.dbd
rollAvg_DBD += caPutLog.dbd

# rollAvg_registerRecordDeviceDriver.cpp derives from rollAvg.dbd
rollAvg_SRCS += rollAvg_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
rollAvg_SRCS_DEFAULT += rollAvgMain.cpp
rollAvg_SRCS_vxWorks += -nil-

rollAvg_LIBS += autosave
rollAvg_LIBS += devIocStats
rollAvg_LIBS += caPutLog
rollAvg_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
rollAvg_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

