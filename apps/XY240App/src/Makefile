TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#==================================================
# build a support library

# Build an IOC support library
LIBRARY_IOC_vxWorks += XY240Support

# install XY240Support.dbd into <top>/dbd
DBD += XY240Support.dbd

XY240Support_DBD += base.dbd
XY240Support_DBD += vmeRecord.dbd
XY240Support_DBD += XY240.dbd

# specify all source files to be compiled and added to the library
XY240Support_SRCS += devBiXy240M.c
XY240Support_SRCS += devBoXy240M.c
XY240Support_SRCS += drvXy240M.c

XY240Support_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

