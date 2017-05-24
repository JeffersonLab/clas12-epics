TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# build an ioc application

PROD_IOC_Linux = testApp

# <name>.dbd will be created from <name>Include.dbd
DBD += testApp.dbd

testApp_DBD += waveformApp.dbd
testApp_DBD += devIocStats.dbd
testApp_DBD += asSupport.dbd 
testApp_DBD += caPutLog.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
testApp_SRCS += testApp_registerRecordDeviceDriver.cpp
testApp_SRCS += seq_test.st 
testApp_SRCS += seq_test2.st 
testApp_SRCS += seq_svtOnOff-1R.st 
testApp_SRCS_DEFAULT += testAppMain.cpp
testApp_SRCS_vxWorks += -nil-

#The following adds support from base/src/vxWorks
testApp_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

#add a definition for each support application used by this application
testApp_LIBS += $(EPICS_BASE_IOC_LIBS)
testApp_LIBS += waveformApp
testApp_LIBS += devIocStats
testApp_LIBS += autosave
testApp_LIBS += caPutLog
testApp_LIBS += seq pv

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

