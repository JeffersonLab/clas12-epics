TOP=../..

include $(TOP)/configure/CONFIG

#CC=/apps/gcc/8.3.0/bin/gcc

#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC application
STATIC_BUILD=YES

PROD_Linux += iocscalers

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
iocscalers_LIBS += seq pv

iocscalers_LIBS += jscalers
iocscalers_LIBS += rol
iocscalers_LIBS += devIocStats
iocscalers_LIBS += autosave
iocscalers_LIBS += waveformApp
iocscalers_LIBS += $(EPICS_BASE_IOC_LIBS)

rol_DIR         += $(ROL_LIB)

#rol_DIR += $(CODA)/src/rol/Linux_x86_64/lib


#PROD_LIBS       += codautil
#codautil_DIR += $(CODA)/src/codautil/Linux_x86_64/lib 

PROD_LIBS       += mysql4.1.20
mysql4.1.20_DIR += $(MYSQL_LIB)
#mysql4.1.20_DIR = += /usr/clas12/release/1.3.2/coda/src/mysql4.1.20/Linux_x86_64/lib

#mysql4.1.20_DIR += /usr/clas12/release/1.3.2/coda/src/mysql4.1.20/Linux_x86_64/lib

#PROD_LIBS       += mysqlclient

#PROD_LIBS       += mysql
#mysqlclient_DIR += /usr/lib/mysql
#mysqlclient_DIR += /usr/lib64/mysql
#mysql_DIR = += /usr/clas12/release/1.3.2/coda/src/mysql4.1.20/Linux_x86_64/lib

USR_INCLUDES += $(ROL_INCLUDE)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
