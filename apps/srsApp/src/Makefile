TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# build an ioc application

PROD_IOC_Linux = srsApp
#LIBRARY_IOC = srsApp

DBD += srsApp.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
srsApp_SRCS += srsApp_registerRecordDeviceDriver.cpp
srsApp_SRCS_DEFAULT += srsAppMain.cpp
srsApp_SRCS_vxWorks += -nil-

srsApp_SRCS += srs.st

#The following adds support from base/src/vxWorks
srsApp_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

#add a definition for each support application used by this application
srsApp_LIBS += stream
srsApp_LIBS += asyn
srsApp_LIBS += devIocStats 
srsApp_LIBS += autosave
srsApp_LIBS += caPutLog 
srsApp_LIBS += autosave 
srsApp_LIBS += calc
srsApp_LIBS += seq
srsApp_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

