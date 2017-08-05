TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# build an ioc application


#PROD_IOC_Linux = waveformApp
LIBRARY_IOC = waveformApp

# <name>.dbd will be created from <name>Include.dbd
DBD += waveformApp.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
waveformApp_SRCS += waveformApp_registerRecordDeviceDriver.cpp
waveformApp_SRCS += waveform.st
#waveformApp_SRCS += waveformN.st
waveformApp_SRCS_vxWorks += -nil-

#The following adds support from base/src/vxWorks
waveformApp_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

#add a definition for each support application used by this application
waveformApp_LIBS += seq pv
waveformApp_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

