TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# build an ioc application

#PROD_IOC = iocsoftsvtApps
LIBRARY_IOC_Linux = iocsoftsvtApps
# <name>.dbd will be created from <name>Include.dbd
DBD += iocsoftsvtApps.dbd


# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
iocsoftsvtApps_SRCS += iocsoftsvtApps_registerRecordDeviceDriver.cpp
iocsoftsvtApps_SRCS += modCntrl.st
iocsoftsvtApps_SRCS += seq_vmetlsvt1Off.st
iocsoftsvtApps_SRCS += seq_vmetlsvt2Off.st
iocsoftsvtApps_SRCS += seq_vmetlsvt3Off.st
iocsoftsvtApps_SRCS += seq_vmetlsvt4Off.st
iocsoftsvtApps_SRCS += seq_vmetlsvt5Off.st
iocsoftsvtApps_SRCS_DEFAULT += iocsoftsvtAppsMain.cpp
iocsoftsvtApps_SRCS_vxWorks += -nil-

#The following adds support from base/src/vxWorks
iocsoftsvtApps_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

#add a definition for each support application used by this application
iocsoftsvtApps_LIBS += devIocStats
iocsoftsvtApps_LIBS += devSnmp
iocsoftsvtApps_LIBS += caPutLog
iocsoftsvtApps_LIBS += seq pv
iocsoftsvtApps_LIBS += $(EPICS_BASE_IOC_LIBS)

#NOTES:
#      1)It is not possible to build sncExample both as a component of iocsoftsvtApps
#        and standalone. You must choose only one.
#      2)To build sncExample SNCSEQ must be defined in <top>/configure/RELEASE

#The following builds sncExample as a component of iocsoftsvtApps
#iocsoftsvtApps_SRCS += sncExample.stt

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

