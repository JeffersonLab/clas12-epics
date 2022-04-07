TOP=../..

include $(TOP)/configure/CONFIG

STATIC_BUILD=YES

PROD_IOC_Linux += ioccamac
PROD_Linux += cnd-cfd-thresh
DBD += ioccamac.dbd

ioccamac_DBD += base.dbd
ioccamac_DBD += asSupport.dbd
ioccamac_DBD += devIocStats.dbd

ioccamac_SRCS += ioccamac_registerRecordDeviceDriver.cpp
ioccamac_SRCS += c111cLib.c

cnd-cfd-thresh_SRCS += c111cLib.c
cnd-cfd-thresh_SRCS += cnd-cfd-thresh.c

#ioccamac_SRCS += c111c_read.c
#ioccamac_SRCS += c111c_test.c

ioccamac_SRCS_DEFAULT += ioccamacMain.cpp
ioccamac_SRCS_vxWorks += -nil-

ioccamac_LIBS += seq pv
ioccamac_LIBS += devIocStats
ioccamac_LIBS += autosave
ioccamac_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES

