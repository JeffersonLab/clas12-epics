TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = mcc

# mcc.dbd will be created and installed
DBD += mcc.dbd
mcc_DBD += base.dbd
mcc_DBD += asSupport.dbd
mcc_DBD += devIocStats.dbd
mcc_DBD += caPutLog.dbd
mcc_DBD += calc.dbd
mcc_DBD += sCalcoutRecord.dbd

# mcc_registerRecordDeviceDriver.cpp derives from mcc.dbd
mcc_SRCS += mcc_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
mcc_SRCS_DEFAULT += mccMain.cpp
mcc_SRCS_vxWorks += -nil-

mcc_LIBS += calc
mcc_LIBS += autosave
mcc_LIBS += devIocStats
mcc_LIBS += caPutLog
mcc_LIBS += $(EPICS_BASE_IOC_LIBS)

# Finally link to the EPICS Base libraries
mcc_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

