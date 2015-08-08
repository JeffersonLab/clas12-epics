TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#=============================
# Build the IOC application

PROD_IOC_Linux = ioccaen
# <name>.dbd will be created from <name>Include.dbd
DBD += ioccaen.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
ioccaen_SRCS += ioccaen_registerRecordDeviceDriver.cpp

ioccaen_SRCS += bigsub.c
ioccaen_SRCS += sub.c
ioccaen_SRCS += devCAEN.c
ioccaen_SRCS_DEFAULT += ioccaenMain.cpp
ioccaen_SRCS_vxWorks += -nil-

ioccaen_LIBS += sy1527epics
ioccaen_LIBS += caenhvwrapper 
ioccaen_LIBS += hscaenet 
ioccaen_LIBS += smi
ioccaen_LIBS += smiui
ioccaen_LIBS += dim
ioccaen_LIBS += $(EPICS_BASE_IOC_LIBS)

sy1527epics_DIR += $(TOP)/lib/$(T_A)
caenhvwrapper_DIR += $(CAENHVWRAPPER_LIB)
hscaenet_DIR      += $(HSCAENET_LIB)
smi_DIR   += $(SMIXX_LIB)
smiui_DIR += $(SMIXX_LIB)
dim_DIR   += $(DIM_LIB)

USR_INCLUDES += $(SMIXX_INCLUDE)
USR_INCLUDES += $(DIM_INCLUDE)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

