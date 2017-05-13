TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#==================================================
# build a support library

LIBRARY_IOC_vxWorks += DVME628Dev

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxxRecord
# install DVME628Dev.dbd into <top>/dbd
DBD += DVME628Dev.dbd

# specify all source files to be compiled and added to the library
#DVME628Dev_SRCS += xxx
DVME628Dev_SRCS += devAoDVME628.c
DVME628Dev_SRCS += drvDVME628.c

#DVME628Dev_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================


include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

