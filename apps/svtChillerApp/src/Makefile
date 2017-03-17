TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# build an ioc application

PROD_IOC = svtChiller
#LIBRARY_IOC = svtChiller

DBD += svtChiller.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
svtChiller_SRCS += svtChiller_registerRecordDeviceDriver.cpp
svtChiller_SRCS_DEFAULT += svtChillerMain.cpp
svtChiller_SRCS_vxWorks += -nil-

#The following adds support from base/src/vxWorks
svtChiller_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

#add a definition for each support application used by this application
svtChiller_LIBS += stream
svtChiller_LIBS += asyn
svtChiller_LIBS += devIocStats 
svtChiller_LIBS += autosave
svtChiller_LIBS += caPutLog 
svtChiller_LIBS += autosave 
svtChiller_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

