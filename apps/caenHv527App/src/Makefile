TOP=../..
include $(TOP)/configure/CONFIG

EPICS_BASE=/usr/clas12/R3.14.12.5/base_RHEL5
MODULES=$(EPICS_BASE)/../modules_RHEL5
SYNAPPS=$(EPICS_BASE)/../modules_RHEL5
EPICS_EXTENSIONS=$(EPICS_BASE)/../externsions_RHEL5
include $(MODULES)/configure/RELEASE
include $(SYNAPPS)/configure/RELEASE
COMMANDLINE_LIBRARY = READLINE_NCURSES

PROD_IOC_Linux = ioccaen527

#PROD_IOC_vxWorks = ioccaen527
#ioccaen527_SRCS_vxWorks += ioccaen527_registerRecordDeviceDriver.cpp
#ioccaen527_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

DBD += ioccaen527.dbd

ioccaen527_SRCS += ioccaen527_registerRecordDeviceDriver.cpp
ioccaen527_SRCS += bigsub.c
ioccaen527_SRCS += devCAEN.c
ioccaen527_SRCS += dchv_waveforms-S126.st
ioccaen527_SRCS += dchv_waveforms-S345.st
ioccaen527_SRCS_DEFAULT += ioccaen527Main.cpp
ioccaen527_SRCS_vxWorks += -nil-

USR_INCLUDES += -I$(TOP)/include

ioccaen527_LIBS += seq pv
ioccaen527_LIBS += sy527epics2
ioccaen527_LIBS += caenhvwrapper
ioccaen527_LIBS += hscaenet
ioccaen527_LIBS += devIocStats
ioccaen527_LIBS += caPutLog
ioccaen527_LIBS += autosave
ioccaen527_LIBS += $(EPICS_BASE_IOC_LIBS)

sy1527epics1_DIR  += $(TOP)/lib/$(T_A)
caenhvwrapper_DIR += $(CAENHVWRAPPER_LIB)
hscaenet_DIR      += $(HSCAENET_LIB)

ioccaen527_OBJS += $(CLAS)/coda/src/rol/Linux_i686_vme/obj/all_rocs.o
ioccaen527_LIBS += jvme
jvme_DIR += $(CLAS)/coda/src/rol/jvme

USR_CFLAGS += -DUSE_CAEN527

include $(TOP)/configure/RULES

