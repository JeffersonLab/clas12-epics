TOP=../..

include $(TOP)/configure/CONFIG

#CC=/apps/gcc/8.3.0/bin/gcc

#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC application
STATIC_BUILD=YES

# build both 32- and 64-bit:
PROD_Linux += iocscalers

# only build 64-bit:
#PROD_Linux-x86_64 += iocscalers

# <name>.dbd will be created from <name>Include.dbd
DBD += iocscalers.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
iocscalers_SRCS += iocscalers_registerRecordDeviceDriver.cpp
iocscalers_SRCS += devSCALERS.c
iocscalers_SRCS += jscalers_ioc.cpp

# Build the main IOC entry point on workstation OSs.
iocscalers_SRCS_DEFAULT += iocscalersMain.cpp
iocscalers_SRCS_vxWorks += -nil-

iocscalers_SRCS += jscalersF.st
iocscalers_SRCS += jscalersC.st

iocscalers_LIBS += jscalers
iocscalers_LIBS += rol
iocscalers_LIBS += seq pv
iocscalers_LIBS += asyn
iocscalers_LIBS += sscan
iocscalers_LIBS += stream
iocscalers_LIBS += waveformApp
iocscalers_LIBS += calc
iocscalers_LIBS += devIocStats
iocscalers_LIBS += autosave
iocscalers_LIBS += $(EPICS_BASE_IOC_LIBS)

rol_DIR         += $(ROL_LIB)

PROD_LIBS       += mysql4.1.20
mysql4.1.20_DIR += $(MYSQL_LIB)

USR_INCLUDES += $(ROL_INCLUDE)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
