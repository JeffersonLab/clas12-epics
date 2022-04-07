TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# build an ioc application

LIBRARY_IOC_vxWorks += brm13

# <name>.dbd will be created from <name>Include.dbd
DBD += brm13.dbd

brm13_SRCS += raster2021.st
brm13_SRCS += fr_xscalewf.st

brm13_SRCS += devLobrm13.c
brm13_SRCS += devLibrm13.c
brm13_SRCS += devWfbrm13.c
brm13_SRCS += drvbrm13.c

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
brm13_SRCS += brm13_registerRecordDeviceDriver.cpp
brm13_SRCS_DEFAULT += brm13Main.cpp
brm13_SRCS_vxWorks += -nil-

brm13_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

#add a definition for each support application used by this application
brm13_LIBS += $(EPICS_BASE_IOC_LIBS)
brm13_LIBS += seq pv

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

