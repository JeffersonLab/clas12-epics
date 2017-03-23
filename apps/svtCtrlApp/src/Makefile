TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# build an ioc application

PROD_IOC_Linux = svtCtrlApp
#LIBRARY_IOC_Linux = svtCtrlApp
# <name>.dbd will be created from <name>Include.dbd
DBD += svtCtrlApp.dbd


# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
svtCtrlApp_SRCS += svtCtrlApp_registerRecordDeviceDriver.cpp
svtCtrlApp_SRCS += modCntrl.st
svtCtrlApp_SRCS += seq_vmetlsvt1Off.st
svtCtrlApp_SRCS += seq_vmetlsvt2Off.st
svtCtrlApp_SRCS += seq_vmetlsvt3Off.st
svtCtrlApp_SRCS += seq_vmetlsvt4Off.st
svtCtrlApp_SRCS += seq_vmetlsvt5Off.st
svtCtrlApp_SRCS += seq_v450waveform.st
svtCtrlApp_SRCS += seq_mpodwaveform.st
svtCtrlApp_SRCS_DEFAULT += svtCtrlAppMain.cpp
svtCtrlApp_SRCS_vxWorks += -nil-

#The following adds support from base/src/vxWorks
svtCtrlApp_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

#add a definition for each support application used by this application
svtCtrlApp_LIBS += devIocStats
svtCtrlApp_LIBS += devSnmp
svtCtrlApp_LIBS += caPutLog
svtCtrlApp_LIBS += seq pv
svtCtrlApp_LIBS += autosave
svtCtrlApp_LIBS += $(EPICS_BASE_IOC_LIBS)

#NOTES:
#      1)It is not possible to build sncExample both as a component of svtCtrlApp
#        and standalone. You must choose only one.
#      2)To build sncExample SNCSEQ must be defined in <top>/configure/RELEASE

#The following builds sncExample as a component of svtCtrlApp
#svtCtrlApp_SRCS += sncExample.stt

#The following builds sncExample as a standalone application
#PROD_HOST += sncExample
#sncExample_SNCFLAGS += +m
#sncExample_SRCS += sncExample.stt
#sncExample_LIBS += seq pv
#sncExample_LIBS += $(EPICS_BASE_HOST_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

