TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# build an ioc application

#PROD_IOC = svtApp
LIBRARY_IOC_Linux = svtApp
# <name>.dbd will be created from <name>Include.dbd
DBD += svtApp.dbd


# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
svtApp_SRCS += svtApp_registerRecordDeviceDriver.cpp
svtApp_SRCS += modCntrl.st
svtApp_SRCS += seq_vmetlsvt1Off.st
svtApp_SRCS += seq_vmetlsvt2Off.st
svtApp_SRCS += seq_vmetlsvt3Off.st
svtApp_SRCS += seq_vmetlsvt4Off.st
svtApp_SRCS += seq_vmetlsvt5Off.st
svtApp_SRCS_DEFAULT += svtAppMain.cpp
svtApp_SRCS_vxWorks += -nil-

#The following adds support from base/src/vxWorks
svtApp_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

#add a definition for each support application used by this application
svtApp_LIBS += devIocStats
svtApp_LIBS += devSnmp
svtApp_LIBS += caPutLog
svtApp_LIBS += seq pv
svtApp_LIBS += $(EPICS_BASE_IOC_LIBS)

#NOTES:
#      1)It is not possible to build sncExample both as a component of svtApp
#        and standalone. You must choose only one.
#      2)To build sncExample SNCSEQ must be defined in <top>/configure/RELEASE

#The following builds sncExample as a component of svtApp
#svtApp_SRCS += sncExample.stt

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

