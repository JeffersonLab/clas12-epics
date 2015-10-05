TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#==================================================
# build a support library

# install XY240Support.dbd into <top>/dbd
DBD += XY240Support.dbd

# Build an IOC support library
LIBRARY_IOC_vxWorks += XY240Support

# specify all source files to be compiled and added to the library
XY240Support_SRCS += devBiXy240M.c
XY240Support_SRCS += devBoXy240M.c
XY240Support_SRCS += drvXy240M.c

XY240Support_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

