TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#==================================================
# build a support library

LIBRARY_IOC_vxWorks += XY560Support

# install XY560Support.dbd into <top>/dbd
DBD += XY560Support.dbd

# specify all source files to be compiled and added to the library
XY560Support_SRCS += devAiXy560.c
XY560Support_SRCS += drvXy560.c

XY560Support_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

