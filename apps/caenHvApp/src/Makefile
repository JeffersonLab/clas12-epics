TOP=../..

include $(TOP)/configure/CONFIG

#=============================

PROD_IOC_Linux = ioccaen
DBD += ioccaen.dbd

ioccaen_SRCS += ioccaen_registerRecordDeviceDriver.cpp
ioccaen_SRCS += bigsub.c
ioccaen_SRCS += devCAEN.c
ioccaen_SRCS += dchv_waveforms.st
ioccaen_SRCS += dchv_waveforms-S126.st
ioccaen_SRCS += dchv_waveforms-S345.st
ioccaen_SRCS_DEFAULT += ioccaenMain.cpp
ioccaen_SRCS_vxWorks += -nil-

USR_INCLUDES += -I$(TOP)/include

ioccaen_LIBS += calc
ioccaen_LIBS += sy1527epics1
ioccaen_LIBS += caenhvwrapper 
ioccaen_LIBS += hscaenet 
ioccaen_LIBS += devIocStats
ioccaen_LIBS += caPutLog
ioccaen_LIBS += autosave
ioccaen_LIBS += seq
ioccaen_LIBS += waveformApp
ioccaen_LIBS += $(EPICS_BASE_IOC_LIBS)

sy1527epics1_DIR  += $(TOP)/lib/$(T_A)
caenhvwrapper_DIR += $(CAENHVWRAPPER_LIB)
hscaenet_DIR      += $(HSCAENET_LIB)

#===========================

ioccaen_LIBS += smi
ioccaen_LIBS += smiui
ioccaen_LIBS += dim

smi_DIR   += $(SMIXX_LIB)
smiui_DIR += $(SMIXX_LIB)
dim_DIR   += $(DIM_LIB)

USR_INCLUDES += $(SMIXX_INCLUDE)
USR_INCLUDES += $(DIM_INCLUDE)

#===========================
include $(TOP)/configure/RULES

