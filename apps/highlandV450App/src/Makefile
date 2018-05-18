TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#==================================================
# build a support library

LIBRARY_IOC_vxWorks += V450

DBD += V450.dbd

# specify all source files to be compiled and added to the library
V450_SRCS += devAiV450.c
V450_SRCS += devLiV450.c
V450_SRCS += drvV450.c

V450_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================


include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

