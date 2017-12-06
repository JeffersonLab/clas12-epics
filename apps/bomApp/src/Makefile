TOP=../..

include $(TOP)/configure/CONFIG

#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC application
STATIC_BUILD=YES

PROD_Linux += iocbom

# <name>.dbd will be created from <name>Include.dbd
DBD += iocbom.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
iocbom_SRCS += iocbom_registerRecordDeviceDriver.cpp
iocbom_SRCS += devBOM.c
iocbom_SRCS += bom_ioc.cpp

# Build the main IOC entry point on workstation OSs.
iocbom_SRCS_DEFAULT += iocbomMain.cpp
iocbom_SRCS_vxWorks += -nil-

iocbom_LIBS += seq pv

iocbom_LIBS += bomDrv
iocbom_LIBS += rol
iocbom_LIBS += devIocStats
iocbom_LIBS += autosave
#iocbom_LIBS += waveformApp
iocbom_LIBS += $(EPICS_BASE_IOC_LIBS)

rol_DIR         += $(ROL_LIB)

PROD_LIBS       += mysql4.1.20
mysql4.1.20_DIR += $(MYSQL_LIB)

USR_INCLUDES += $(ROL_INCLUDE)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
