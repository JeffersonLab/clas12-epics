TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC_Linux = ioccaen
# ecalHV.dbd will be created and installed
DBD += ioccaen.dbd

# <name>_registerRecordDeviceDriver.cpp will be created from <name>.dbd
ioccaen_SRCS += ioccaen_registerRecordDeviceDriver.cpp
ioccaen_SRCS += bigsub.c
ioccaen_SRCS += devCAEN.c
ioccaen_SRCS_DEFAULT += ioccaenMain.cpp
ioccaen_SRCS_vxWorks += -nil-

# CAEN_HV/include
USR_INCLUDES += -I$(TOP)/include

ioccaen_LIBS += calc
ioccaen_LIBS += sy1527epics1
ioccaen_LIBS += caenhvwrapper 
ioccaen_LIBS += hscaenet 
ioccaen_LIBS += devIocStats
ioccaen_LIBS += caPutLog
ioccaen_LIBS += autosave
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


#TARGETS += mkHVEpics ../HV_allnames.txt 

#===========================
include $(TOP)/configure/RULES

#----------------------------------------
#  ADD RULES AFTER THIS LINE

mkHVEpics:	mkHVEpics.C
	g++ -o $@ $^

../HV_allnames.txt:	mkHVEpics ../HVswaps.txt ../../Db/caenhv.db
	echo "Generating HV names, substitutions and iocs. See mkHVEpics.log and HV_allnames.txt"
#	./mkHVEpics crates > ../mkHVEpics.log 
#	./mkHVEpics groups >> ../mkHVEpics.log
#	./mkHVEpics all >> ../mkHVEpics.log
	./mkHVEpics crates
	./mkHVEpics groups
	./mkHVEpics all
